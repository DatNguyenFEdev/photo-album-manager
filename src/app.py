import uuid
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from src.storage.store import (
    load_all_albums, load_album, save_album, delete_album,
    save_photo, load_photos, delete_photo, get_photo_path,
)
from src.lib.image import make_thumbnail
from src.types import AlbumData

app = FastAPI(title="Photo Album Manager")

templates = Jinja2Templates(directory="src/templates")
app.mount("/static", StaticFiles(directory="src/static"), name="static")
app.mount("/data/photos", StaticFiles(directory="data/photos"), name="photos")


def _group_albums_by_date(albums: list[AlbumData]) -> list[dict]:
    groups: dict[str, list[AlbumData]] = {}
    for album in albums:
        parts = album.date.split("-")
        prefix = f"{parts[0]}-{parts[1]}"
        if prefix not in groups:
            month_names = [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December",
            ]
            month_idx = int(parts[1]) - 1
            label = f"{month_names[month_idx]} {parts[0]}"
            groups[prefix] = []
        groups[prefix].append(album)

    sorted_prefixes = sorted(groups.keys(), reverse=True)
    result = []
    for prefix in sorted_prefixes:
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December",
        ]
        parts = prefix.split("-")
        label = f"{month_names[int(parts[1]) - 1]} {parts[0]}"
        result.append({
            "label": label,
            "date_prefix": prefix,
            "albums": groups[prefix],
        })
    return result


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    albums = load_all_albums()
    date_groups = _group_albums_by_date(albums)
    return templates.TemplateResponse(
        request,
        "index.html",
        {"request": request, "date_groups": date_groups},
    )


@app.get("/album/{album_id}", response_class=HTMLResponse)
async def album_detail(request: Request, album_id: str):
    album = load_album(album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    photos = load_photos(album_id)
    return templates.TemplateResponse(
        request,
        "album.html",
        {"request": request, "album": album, "photos": photos},
    )


@app.post("/api/albums")
async def api_create_album(title: str = Form(...), date: str = Form(...)):
    album_id = str(uuid.uuid4())[:8]
    albums = load_all_albums()
    max_order = max((a.display_order for a in albums), default=0)
    album = AlbumData(
        id=album_id,
        title=title,
        date=date,
        display_order=max_order + 1,
        created_at=datetime.now().isoformat(),
    )
    save_album(album)
    return {"id": album_id, "title": title, "date": date}


@app.post("/api/albums/reorder")
async def api_reorder_albums(album_id: str = Form(...), new_order: int = Form(...)):
    album = load_album(album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    album.display_order = new_order
    save_album(album)
    return {"status": "ok"}


@app.post("/api/albums/{album_id}/photos")
async def api_upload_photo(album_id: str, file: UploadFile = File(...)):
    album = load_album(album_id)
    if not album:
        raise HTTPException(status_code=404, detail="Album not found")
    photo_id = str(uuid.uuid4())[:8]
    ext = Path(file.filename).suffix if file.filename else ".jpg"
    contents = await file.read()
    photo = save_photo(album_id, photo_id, contents, ext)
    photo_path = get_photo_path(album_id, photo_id)
    if photo_path:
        make_thumbnail(photo_path)
    return {"id": photo.id, "filename": photo.filename}


@app.delete("/api/albums/{album_id}/photos/{photo_id}")
async def api_delete_photo(album_id: str, photo_id: str):
    delete_photo(album_id, photo_id)
    return {"status": "ok"}


@app.delete("/api/albums/{album_id}")
async def api_delete_album(album_id: str):
    delete_album(album_id)
    return {"status": "ok"}
