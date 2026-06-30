import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Optional

from src.types import AlbumData, PhotoData

DATA_ROOT = Path("data")
ALBUMS_DIR = DATA_ROOT / "albums"
PHOTOS_DIR = DATA_ROOT / "photos"


def _ensure_dirs():
    ALBUMS_DIR.mkdir(parents=True, exist_ok=True)
    PHOTOS_DIR.mkdir(parents=True, exist_ok=True)


def _album_path(album_id: str) -> Path:
    return ALBUMS_DIR / f"{album_id}.json"


def _photo_file_path(album_id: str, photo_id: str, ext: str) -> Path:
    album_photos_dir = PHOTOS_DIR / album_id
    album_photos_dir.mkdir(parents=True, exist_ok=True)
    return album_photos_dir / f"{photo_id}{ext}"


def _album_ids() -> list[str]:
    _ensure_dirs()
    return sorted(
        f.stem for f in ALBUMS_DIR.iterdir() if f.suffix == ".json"
    )


def load_all_albums() -> list[AlbumData]:
    albums = []
    for aid in _album_ids():
        album = load_album(aid)
        if album:
            albums.append(album)
    albums.sort(key=lambda a: (a.date, a.display_order), reverse=True)
    return albums


def load_album(album_id: str) -> Optional[AlbumData]:
    path = _album_path(album_id)
    if not path.exists():
        return None
    with open(path) as f:
        data = json.load(f)
    return AlbumData(**data)


def save_album(album: AlbumData):
    _ensure_dirs()
    with open(_album_path(album.id), "w") as f:
        json.dump({
            "id": album.id,
            "title": album.title,
            "date": album.date,
            "display_order": album.display_order,
            "created_at": album.created_at,
        }, f, indent=2)


def delete_album(album_id: str):
    path = _album_path(album_id)
    if path.exists():
        path.unlink()
    album_photos_dir = PHOTOS_DIR / album_id
    if album_photos_dir.exists():
        shutil.rmtree(album_photos_dir)


def save_photo(album_id: str, photo_id: str, file_bytes: bytes, ext: str) -> PhotoData:
    _ensure_dirs()
    dest = _photo_file_path(album_id, photo_id, ext)
    dest.write_bytes(file_bytes)
    return PhotoData(
        id=photo_id,
        album_id=album_id,
        filename=dest.name,
        original_name=dest.name,
        added_at=datetime.now().isoformat(),
    )


def load_photos(album_id: str) -> list[PhotoData]:
    album_photos_dir = PHOTOS_DIR / album_id
    if not album_photos_dir.exists():
        return []
    photos = []
    for f in sorted(album_photos_dir.iterdir()):
        if f.is_file():
            photos.append(PhotoData(
                id=f.stem,
                album_id=album_id,
                filename=f.name,
                original_name=f.name,
                added_at=datetime.fromtimestamp(f.stat().st_mtime).isoformat(),
            ))
    return photos


def delete_photo(album_id: str, photo_id: str):
    album_photos_dir = PHOTOS_DIR / album_id
    for f in album_photos_dir.iterdir():
        if f.stem == photo_id:
            f.unlink()
            return


def get_photo_path(album_id: str, photo_id: str) -> Optional[Path]:
    album_photos_dir = PHOTOS_DIR / album_id
    if not album_photos_dir.exists():
        return None
    for f in album_photos_dir.iterdir():
        if f.stem == photo_id:
            return f
    return None
