"""
Run this once to copy all pool project images into the Portfolio folder.
Double-click it or run: python setup_images.py
"""
import shutil, os, sys
from pathlib import Path

HERE = Path(__file__).parent
RENDU = Path(r"D:\ALBA projects\10- Piscine d'un quartier\RENDU")

if not RENDU.exists():
    print("ERROR: Could not find the ALBA projects folder at:")
    print(f"  {RENDU}")
    input("Press Enter to exit.")
    sys.exit(1)

copies = {
    "pool_render.jpg":  RENDU / "untitled.19566.jpg",
    "pool_states.jpg":  RENDU / "untitled.19ù65.jpg",
    "pool_move_1.jpg":  RENDU / "move 1.jpg",
    "pool_move_2.jpg":  RENDU / "move 2.jpg",
    "pool_move_3.jpg":  RENDU / "move 3.jpg",
    "pool_move_4.jpg":  RENDU / "move 4.jpg",
    "pool_move_5.jpg":  RENDU / "move 5.jpg",
    "pool_move_6.jpg":  RENDU / "move 6.jpg",
}

print("Copying images...")
for dest_name, src in copies.items():
    dest = HERE / dest_name
    if src.exists():
        shutil.copy2(src, dest)
        print(f"  ✓ {dest_name}")
    else:
        print(f"  ✗ Not found: {src}")

# Convert PDFs using Pillow + pdf2image if available
try:
    from pdf2image import convert_from_path

    print("\nConverting PDFs...")

    # Roof sequence
    pages = convert_from_path(RENDU / "FINAL RENDU STRUCTURE- STORY BOARD.pdf", dpi=150)
    pages[0].save(HERE / "pool_roof_seq.jpg", "JPEG", quality=80)
    print("  ✓ pool_roof_seq.jpg")

    # Ventilation (split top/bottom)
    pages = convert_from_path(RENDU / "FINAL RENDU STRUCTURE-D.pdf", dpi=150)
    img = pages[0]
    w, h = img.size
    img.crop((0, 0, w, h//2)).save(HERE / "pool_vent_top.jpg", "JPEG", quality=80)
    img.crop((0, h//2, w, h)).save(HERE / "pool_vent_bottom.jpg", "JPEG", quality=80)
    print("  ✓ pool_vent_top.jpg + pool_vent_bottom.jpg")

    # Section
    pages = convert_from_path(RENDU / "FINAL RENDU STRUCTURE-DETAILS.pdf", dpi=150)
    pages[0].save(HERE / "pool_section.jpg", "JPEG", quality=82)
    print("  ✓ pool_section.jpg")

except ImportError:
    print("\n  pdf2image not installed — copying PDFs directly instead.")
    print("  (The browser will display them as embedded PDFs)\n")
    shutil.copy2(RENDU / "FINAL RENDU STRUCTURE- STORY BOARD.pdf", HERE / "pool_roof_seq.pdf")
    shutil.copy2(RENDU / "FINAL RENDU STRUCTURE-D.pdf",            HERE / "pool_vent.pdf")
    shutil.copy2(RENDU / "FINAL RENDU STRUCTURE-DETAILS.pdf",      HERE / "pool_section.pdf")
    print("  ✓ PDFs copied. Install pdf2image for better quality:")
    print("    pip install pdf2image")

print("\nAll done! Open index.html in your browser.")
input("Press Enter to exit.")
