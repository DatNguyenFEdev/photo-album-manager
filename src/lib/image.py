from pathlib import Path
from typing import Optional

from PIL import Image, UnidentifiedImageError

THUMBNAIL_SIZE = (200, 200)


def make_thumbnail(image_path: Path, output_path: Optional[Path] = None) -> Optional[Path]:
    if output_path is None:
        stem = image_path.stem
        output_path = image_path.parent / f"{stem}_thumb{image_path.suffix}"
    try:
        img = Image.open(image_path)
        img.thumbnail(THUMBNAIL_SIZE, Image.Resampling.LANCZOS)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img.save(output_path, "JPEG", quality=85)
        return output_path
    except (FileNotFoundError, UnidentifiedImageError, OSError):
        return None


def get_image_dimensions(image_path: Path) -> Optional[tuple[int, int]]:
    try:
        img = Image.open(image_path)
        return img.size
    except (FileNotFoundError, UnidentifiedImageError, OSError):
        return None
