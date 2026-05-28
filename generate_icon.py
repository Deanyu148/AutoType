"""Generate an icon for AutoType and write it as .ico + PNG preview"""
from PIL import Image, ImageDraw, ImageFont
import math, os, sys

OUT_ICO = os.path.join(os.path.dirname(__file__), "AutoType.ico")
OUT_PNG = os.path.join(os.path.dirname(__file__), "icon_preview.png")
PRIMARY = (124, 58, 237)
PRIMARY_DARK = (90, 30, 190)
BG_DARK = (26, 27, 38)
BG_MID = (36, 37, 58)
WHITE = (255, 255, 255)
ACCENT = (167, 139, 250)
SIZES = [16, 24, 32, 48, 64, 128, 256]


def _find_font_path(name: str, bold: bool = True) -> str | None:
    base = os.environ.get("WINDIR", "C:/Windows")
    fonts_dir = os.path.join(base, "Fonts")
    candidates = [
        os.path.join(fonts_dir, "seguiemj.ttf"),   # Segoe UI Emoji (has good rendering)
        os.path.join(fonts_dir, "segoeuib.ttf"),    # Segoe UI Bold
        os.path.join(fonts_dir, "segoeui.ttf"),     # Segoe UI
        os.path.join(fonts_dir, "seguisb.ttf"),     # Segoe UI Semibold
        os.path.join(fonts_dir, "arialbd.ttf"),     # Arial Bold
        os.path.join(fonts_dir, "arial.ttf"),       # Arial
        os.path.join(fonts_dir, "consola.ttf"),     # Consolas
        os.path.join(fonts_dir, "consolab.ttf"),    # Consolas Bold
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None


def draw_icon(size: int) -> Image.Image:
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if size <= 24:
        # Small sizes: simpler design, bolder shapes
        pad = 1
        r = size * 0.2
        draw.rounded_rectangle(
            [pad, pad, size - pad, size - pad],
            radius=int(r), fill=BG_DARK
        )
        # Simplified: just a bold "A"
        try:
            font = ImageFont.truetype(_find_font_path("Arial", bold=True), int(size * 0.55))
        except Exception:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0, 0), "A", font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        tx = (size - tw) / 2 - bbox[0]
        ty = (size - th) / 2 - bbox[1]
        draw.text((tx, ty), "A", fill=PRIMARY, font=font)
        return img

    # Medium+ sizes: full design
    margin = max(2, int(size * 0.07))
    r = int(size * 0.20)

    # Shadow (subtle offset)
    shadow_off = max(1, int(size * 0.015))
    draw.rounded_rectangle(
        [margin + shadow_off, margin + shadow_off,
         size - margin + shadow_off, size - margin + shadow_off],
        radius=r, fill=(0, 0, 0, 60)
    )

    # Main background card
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=r, fill=BG_DARK
    )

    # Inner subtle border
    inner = int(size * 0.035)
    draw.rounded_rectangle(
        [margin + inner, margin + inner,
         size - margin - inner, size - margin - inner],
        radius=max(1, int(r * 0.7)),
        outline=PRIMARY, width=max(1, int(size * 0.025))
    )

    # Draw "A" character
    font_path = _find_font_path("Segoe UI", bold=True)
    font_size = int(size * 0.42)
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception:
        font = ImageFont.load_default()

    char = "A"
    bbox = draw.textbbox((0, 0), char, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (size - tw) / 2 - bbox[0]
    ty = (size - th) / 2 - bbox[1]
    # Nudge "A" slightly up to leave room for cursor line below
    ty -= size * 0.04

    draw.text((tx, ty), char, fill=WHITE, font=font)

    # Blinking cursor line below the A
    cursor_h = max(2, int(size * 0.045))
    cursor_w = tw * 0.55
    cursor_x = tx + (tw - cursor_w) / 2
    cursor_y = ty + th + size * 0.04
    draw.rounded_rectangle(
        [cursor_x, cursor_y, cursor_x + cursor_w, cursor_y + cursor_h],
        radius=cursor_h // 2,
        fill=PRIMARY
    )

    return img


def main():
    icons = []
    for s in SIZES:
        img = draw_icon(s)
        icons.append(img)

    # Save .ico with all sizes
    icons[0].save(
        OUT_ICO, format="ICO",
        sizes=[(s, s) for s in SIZES],
        append_images=icons[1:],
    )
    size_kb = os.path.getsize(OUT_ICO) / 1024
    print(f"ICO saved: {OUT_ICO}  ({size_kb:.1f} KB)")

    # Save 256px PNG preview
    icons[-1].save(OUT_PNG, format="PNG")
    print(f"PNG saved: {OUT_PNG}  ({icons[-1].size})")


if __name__ == "__main__":
    main()
