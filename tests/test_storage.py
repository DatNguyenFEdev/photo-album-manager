import json
import tempfile
from pathlib import Path

from src.types import AlbumData, PhotoData


def test_album_data_creation():
    album = AlbumData(id="test1", title="Test Album", date="2026-06-01", display_order=1, created_at="2026-06-30T00:00:00")
    assert album.id == "test1"
    assert album.title == "Test Album"
    assert album.date == "2026-06-01"


def test_photo_data_creation():
    photo = PhotoData(id="p1", album_id="test1", filename="photo.jpg", original_name="photo.jpg", added_at="2026-06-30T00:00:00")
    assert photo.id == "p1"
    assert photo.album_id == "test1"
    assert photo.filename == "photo.jpg"
