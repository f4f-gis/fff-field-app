"""Generate placeholder FfF icon assets (text 'FfF' as vector paths) in QField's formats.

Outputs (into OUT dir):
  fff_logo.svg                                   in-app logo (APP_ICON_PATH root)
  drawable/fff_logo_vector.xml                   splash screen vector
  drawable/launcher_fff_logo.xml                 adaptive icon
  drawable/launcher_fff_logo_background.xml
  drawable/launcher_fff_logo_foreground.xml
  drawable/launcher_fff_logo_monochrome.xml
  preview.png (via ImageMagick, for checking)
"""
import os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

OUT = sys.argv[1]
TEXT = "FfF"
GREEN = "#1B5E20"   # deep field green (placeholder; replace with FfF's brand colour)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

font = TTFont(FONT)
gs = font.getGlyphSet()
cmap = font.getBestCmap()
hmtx = font["hmtx"]

def text_path(box_x, box_y, box_w, box_h):
    """Path data for TEXT fitted & centred inside the box (y down)."""
    # measure in font units
    x = 0; glyphs = []
    for ch in TEXT:
        g = cmap[ord(ch)]
        glyphs.append((g, x)); x += hmtx[g][0]
    bp = BoundsPen(gs)
    for g, gx in glyphs:
        gs[g].draw(TransformPen(bp, (1, 0, 0, 1, gx, 0)))
    xmin, ymin, xmax, ymax = bp.bounds
    w, h = xmax - xmin, ymax - ymin
    s = min(box_w / w, box_h / h)
    ox = box_x + (box_w - w * s) / 2 - xmin * s
    oy = box_y + (box_h - h * s) / 2 + ymax * s   # flip y
    pen = SVGPathPen(gs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip("."))
    for g, gx in glyphs:
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, ox + gx * s, oy)))
    return pen.getCommands()

os.makedirs(os.path.join(OUT, "drawable"), exist_ok=True)
w = lambda p, t: open(os.path.join(OUT, p), "w").write(t)

# 512x512 logo: green rounded square + white text
p512 = text_path(86, 166, 340, 180)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512">
  <!-- Placeholder FfF app logo. Replace with the official FfF logo before release. -->
  <rect x="16" y="16" width="480" height="480" rx="96" ry="96" fill="{GREEN}"/>
  <path fill="#FFFFFF" d="{p512}"/>
</svg>
'''
w("fff_logo.svg", svg)

rr = "M112,16h288a96,96 0 0 1 96,96v288a96,96 0 0 1 -96,96h-288a96,96 0 0 1 -96,-96v-288a96,96 0 0 1 96,-96z"
w("drawable/fff_logo_vector.xml", f'''<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="512dp" android:height="512dp"
    android:viewportWidth="512" android:viewportHeight="512">
    <path android:fillColor="{GREEN}" android:pathData="{rr}" />
    <path android:fillColor="#FFFFFF" android:pathData="{p512}" />
</vector>
''')

# adaptive icon 108x108; keep content inside the 66dp safe circle (21..87)
p108 = text_path(28, 40, 52, 28)
w("drawable/launcher_fff_logo.xml", '''<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@drawable/launcher_fff_logo_background" />
    <foreground android:drawable="@drawable/launcher_fff_logo_foreground" />
    <monochrome android:drawable="@drawable/launcher_fff_logo_monochrome"/>
</adaptive-icon>
''')
w("drawable/launcher_fff_logo_background.xml", f'''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="{GREEN}" android:pathData="M0,0h108v108h-108z" />
</vector>
''')
for name in ("foreground", "monochrome"):
    w(f"drawable/launcher_fff_logo_{name}.xml", f'''<?xml version="1.0" encoding="utf-8"?>
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp" android:height="108dp"
    android:viewportWidth="108" android:viewportHeight="108">
    <path android:fillColor="#FFFFFF" android:pathData="{p108}" />
</vector>
''')
print("ok")
