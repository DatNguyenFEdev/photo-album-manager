from dataclasses import dataclass, field


@dataclass
class AlbumData:
    id: str
    title: str
    date: str  # YYYY-MM-DD format
    display_order: int
    created_at: str


@dataclass
class PhotoData:
    id: str
    album_id: str
    filename: str
    original_name: str
    added_at: str


@dataclass
class DateGroup:
    label: str  # e.g. "June 2026"
    date_prefix: str  # e.g. "2026-06"
    albums: list[AlbumData] = field(default_factory=list)
