#!/usr/bin/env python3
"""Render ONDRINE — The Wave That Never Breaks (1024x1024 travel poster).

Reference study (dev leaderboard, 2026-11-21 ~15:26 WIB, 2,494 entries):
  #1 SUVENNE 0.876 — giant sundial over a Mediterranean plaza, name cast
     as a huge shadow on the paving, cafe people, bougainvillea, gold light.
  #2 SOLMERE 0.846 — a hotel inside a giant hourglass, name on its rim,
     sunset sea, bathers in a thermal pool, lantern-lit pier.
  #3 MARELUNE 0.841 — a stone moon-arch framing the full moon, hillside
     town lights, couple on a terrace, moon path on the water.
Winning pattern: ONE impossible landmark, huge and central; golden-hour
light against blue-teal sea; people visibly enjoying a stay; the place
name set INTO the picture with intent; cream frame. This poster follows
the pattern with a landmark none of the top 10 uses: a colossal wave
frozen mid-crash, its lip curled over the promenade, the sun shining
through the barrel. Flat vector style with soft gradients (small PNG).
"""
import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W = H = 1024
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

CREAM = (250, 240, 214)
INK = (38, 42, 66)
SAND = (238, 205, 150)
SAND_D = (214, 170, 110)
WHITE = (250, 248, 240)
TERRA = (198, 96, 58)
ROSE = (214, 74, 110)


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vgrad(size, top, bottom):
    img = Image.new("RGB", size)
    px = img.load()
    for y in range(size[1]):
        c = lerp(top, bottom, y / max(1, size[1] - 1))
        for x in range(size[0]):
            px[x, y] = c
    return img


def spaced(draw, cx, y, text, font, fill, tracking):
    widths = [draw.textlength(ch, font=font) for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = cx - total / 2
    for ch, w in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += w + tracking


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img, "RGBA")

    # ---- sky: soft blue warming to peach at the horizon ----
    sky = vgrad((W, 640), (122, 168, 205), (250, 178, 128))
    img.paste(sky, (0, 0))

    # ---- sun, open sky between the name and the wave crest ----
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    for r, a in ((150, 26), (105, 42), (72, 70)):
        gd.ellipse((170 - r, 370 - r, 170 + r, 370 + r), fill=(255, 214, 140, a))
    img = Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB")
    d = ImageDraw.Draw(img, "RGBA")
    d.ellipse((124, 324, 216, 416), fill=(255, 226, 158))
    d.ellipse((134, 334, 206, 406), fill=(255, 240, 196))

    # ---- sea: teal gradient + sparkle ----
    sea = vgrad((W, 220), (34, 140, 152), (18, 96, 116))
    img.paste(sea, (0, 560))
    d = ImageDraw.Draw(img, "RGBA")
    for (x, y, r) in ((760, 600, 5), (820, 640, 4), (900, 600, 6), (960, 660, 4),
                      (720, 700, 5), (860, 720, 4), (980, 730, 5), (800, 680, 3)):
        d.ellipse((x - r, y - r // 2, x + r, y + r // 2), fill=(255, 240, 200, 120))
    for y in range(580, 780, 26):
        for x0 in range(660, W, 90):
            d.arc((x0, y, x0 + 70, y + 14), 200, 340, fill=(255, 255, 255, 46), width=3)

    # ---- cliff town, right: white cubes, terracotta roofs ----
    d.polygon([(700, 560), (1024, 560), (1024, 330), (950, 330), (920, 370),
               (830, 360), (800, 410), (730, 430), (700, 480)], fill=(232, 222, 200))
    houses = [(770, 430, 80, 62), (870, 390, 90, 72), (950, 430, 74, 56)]
    for x, y, w, h in houses:
        d.rectangle((x, y, x + w, y + h), fill=WHITE)
        d.polygon([(x - 6, y), (x + w // 2, y - 24), (x + w + 6, y)], fill=TERRA)
        for wx in range(x + 12, x + w - 8, 22):
            d.rectangle((wx, y + 14, wx + 10, y + 28), fill=(58, 74, 96))
        d.rectangle((x + w // 2 - 6, y + h - 24, x + w // 2 + 6, y + h), fill=(90, 70, 60))
    # small bougainvillea tufts at roof edges + dark shrubs (small!)
    for cx, cy, r, col in ((766, 428, 11, ROSE), (962, 424, 10, ROSE),
                           (876, 386, 9, ROSE), (1010, 470, 11, ROSE),
                           (806, 492, 10, (52, 110, 70)), (922, 492, 9, (52, 110, 70))):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col + (235,))

    # ---- THE WAVE: colossal curl frozen over the promenade ----
    # face: steep rise on the left, crest rolling right, lip hooking down
    face = [(40, 780), (58, 640), (110, 520), (200, 450), (330, 415),
            (470, 410), (560, 440), (620, 470), (642, 520), (600, 548),
            (520, 522), (430, 542), (350, 582), (300, 652), (282, 722),
            (268, 780)]
    wave = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wave)
    wd.polygon(face, fill=(30, 152, 166, 245))
    # barrel depth: dark crescent under the lip
    wd.polygon([(380, 590), (450, 552), (520, 534), (580, 552), (545, 615),
                (455, 650), (385, 668)], fill=(12, 88, 112, 175))
    # crest foam along the top edge + spray above the lip
    for cx, cy, r in ((200, 450, 15), (330, 415, 18), (470, 410, 16),
                      (560, 440, 14), (620, 470, 12), (110, 520, 12)):
        wd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255, 225))
    for cx, cy, r in ((660, 480, 7), (680, 510, 5), (650, 440, 6), (600, 420, 5)):
        wd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255, 200))
    # light through the barrel: soft gold wash inside the curl
    wd.polygon([(360, 600), (440, 556), (520, 534), (560, 600),
                (460, 650), (370, 660)], fill=(255, 222, 150, 60))
    wave = wave.filter(ImageFilter.GaussianBlur(1.0))
    img = Image.alpha_composite(img.convert("RGBA"), wave).convert("RGB")
    d = ImageDraw.Draw(img, "RGBA")

    # ---- promenade: sand band + balustrade + people ----
    d.polygon([(0, 780), (W, 780), (W, 1024), (0, 1024)], fill=SAND)
    d.polygon([(0, 780), (W, 780), (W, 800), (0, 800)], fill=SAND_D)
    d.rectangle((0, 752, W, 782), fill=(244, 238, 224))
    for x in range(14, W, 34):
        d.rectangle((x, 758, x + 12, 782), fill=(244, 238, 224))

    def person(x, y, s, shirt, hat=None):
        d.ellipse((x - 26 * s, y - 4 * s, x + 26 * s, y + 4 * s), fill=(190, 150, 100, 120))
        d.ellipse((x - 7 * s, y - 34 * s, x + 7 * s, y - 20 * s), fill=(52, 44, 40))
        d.polygon([(x - 9 * s, y - 20 * s), (x + 9 * s, y - 20 * s),
                   (x + 7 * s, y + 2 * s), (x - 7 * s, y + 2 * s)], fill=shirt)
        d.line((x - 4 * s, y + 2 * s, x - 5 * s, y + 20 * s), fill=(52, 44, 40),
               width=max(2, int(4 * s)))
        d.line((x + 4 * s, y + 2 * s, x + 5 * s, y + 20 * s), fill=(52, 44, 40),
               width=max(2, int(4 * s)))
        if hat:
            d.ellipse((x - 13 * s, y - 38 * s, x + 13 * s, y - 30 * s), fill=hat)

    person(270, 985, 2.2, (198, 96, 58), hat=(238, 214, 160))
    person(350, 992, 2.2, (250, 248, 240))
    person(700, 980, 2.0, (214, 74, 110), hat=(238, 214, 160))
    person(775, 990, 1.9, (38, 90, 120))
    # cafe table with two glasses under the wave
    d.ellipse((505, 935, 625, 952), fill=(250, 248, 240))
    d.rectangle((560, 952, 570, 1000), fill=(90, 70, 60))
    d.polygon([(535, 908), (557, 908), (552, 935), (540, 935)], fill=(255, 226, 158))
    d.polygon([(580, 908), (602, 908), (597, 935), (585, 935)], fill=(255, 226, 158))
    # string lights from cliff to wave lip
    for i in range(1, 10):
        t = i / 10
        x = 700 + (330 - 700) * t
        y = 470 + (560 - 470) * t + 26 * math.sin(math.pi * t)
        d.ellipse((x - 4, y - 4, x + 4, y + 4), fill=(255, 214, 130))
    d.line((700, 470, 330, 560), fill=(60, 50, 44), width=2)

    # ---- gulls ----
    for cx, cy, s in ((560, 250, 16), (620, 210, 12), (500, 300, 10), (760, 180, 11)):
        d.arc((cx - s, cy - s // 2, cx, cy + s // 2), 200, 340, fill=INK, width=3)
        d.arc((cx, cy - s // 2, cx + s, cy + s // 2), 200, 340, fill=INK, width=3)

    # ---- typography: name set INTO the sky, eyebrow above it ----
    f_big = ImageFont.truetype(SERIF, 168)
    f_eye = ImageFont.truetype(SANB, 34)
    f_sub = ImageFont.truetype(SANS, 30)
    spaced(d, W // 2, 92, "THE WAVE THAT NEVER BREAKS", f_eye, (255, 244, 214), 10)
    # (no side rules: the eyebrow spans nearly the full width)
    name = "ONDRINE"
    tw = d.textlength(name, font=f_big)
    x0 = (W - tw) / 2
    d.text((x0 + 5, 137), name, font=f_big, fill=(46, 52, 78, 200))
    d.text((x0, 132), name, font=f_big, fill=(255, 246, 224))
    d.line((x0 + 40, 318, x0 + tw - 40, 318), fill=(255, 214, 140), width=4)
    spaced(d, W // 2, 336, "WHERE THE SEA STANDS STILL", f_sub, (255, 244, 214), 6)

    # ---- cream frame ----
    d.rectangle((0, 0, W - 1, H - 1), outline=CREAM, width=26)
    d.rectangle((26, 26, W - 27, H - 27), outline=(38, 42, 66, 90), width=2)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
