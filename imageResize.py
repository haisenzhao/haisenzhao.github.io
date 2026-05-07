from pathlib import Path

from PIL import Image, ImageOps


input_dir = Path("images")
target_long_side = 1000
image_exts = {".jpg", ".jpeg", ".png", ".bmp", ".tif", ".tiff", ".webp"}


for img_path in input_dir.iterdir():
    if not img_path.is_file() or img_path.suffix.lower() not in image_exts:
        continue

    with Image.open(img_path) as img:
        img = ImageOps.exif_transpose(img)
        width, height = img.size
        long_side = max(width, height)

        if long_side == target_long_side:
            print(f"Keep: {img_path.name} ({width}x{height})")
            continue

        scale = target_long_side / long_side
        new_width = round(width * scale)
        new_height = round(height * scale)
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_img.save(img_path)

        print(f"Resized: {img_path.name} {width}x{height} -> {new_width}x{new_height}")
