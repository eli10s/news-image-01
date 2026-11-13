#!/usr/bin/env python3
"""Draw the news-image-01 front page: THE WORLD TODAY, Friday 13 November 2026.

Procedural PIL drawing, no network, no randomness. Every word is set in
DejaVu fonts so the text is crisp and spelled exactly. Deterministic:
running it twice writes byte-identical entry.png.
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 232)
INK = (24, 24, 28)
NAVY = (16, 32, 66)
GOLD = (212, 175, 55)
RED = (158, 28, 32)
BLUE = (24, 84, 160)
MUTE = (90, 88, 80)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap using the font's real metrics."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


def headline(draw, x, y, text, fnt, color, max_w, leading):
    return para(draw, x, y, text, fnt, color, max_w, leading)


def kicker(draw, x, y, text, color):
    f = font(SANS_B, 19)
    draw.text((x, y), text, font=f, fill=color)
    return y + 26


def rule(draw, x0, x1, y, color=INK, w=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=w)


# ---------------------------------------------------------------- illustrations
def draw_senate(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(38, 56, 92))
    # back wall band
    d.rectangle([x, y, x + w, y + 12], fill=(28, 42, 72))
    # green AI chip badge, top left
    d.rounded_rectangle([x + 14, y + 12, x + 66, y + 64], radius=4, fill=(16, 140, 90))
    d.text((x + 26, y + 24), "AI", font=font(SANS_B, 24), fill=(255, 255, 255))
    # two witness chairs
    desk_top = y + h - 38
    for cx in (x + 62, x + w - 128):
        d.rectangle([cx, desk_top - 56, cx + 66, desk_top], fill=(96, 96, 104))
        d.rectangle([cx, desk_top - 56, cx + 66, desk_top - 40], fill=(120, 120, 128))
    # microphone between them
    d.line([(x + w // 2, desk_top - 30), (x + w // 2, desk_top)], fill=(220, 220, 220), width=3)
    d.ellipse([x + w // 2 - 9, desk_top - 48, x + w // 2 + 9, desk_top - 30], fill=(230, 230, 230))
    # hearing desk
    d.rectangle([x + 10, desk_top, x + w - 10, y + h - 8], fill=(122, 78, 38))
    d.rectangle([x + 10, desk_top, x + w - 10, desk_top + 8], fill=(146, 96, 50))
    # name plate on the desk front
    d.rectangle([x + w // 2 - 52, desk_top + 8, x + w // 2 + 52, y + h - 10], fill=(247, 243, 232))
    d.text((x + w // 2 - 38, desk_top + 9), "SENATE", font=font(SANS_B, 15), fill=INK)


def draw_talks(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 230, 244))
    # round table
    d.ellipse([x + 22, y + h - 58, x + w - 22, y + h - 8], fill=(146, 96, 50))
    d.ellipse([x + 22, y + h - 66, x + w - 22, y + h - 30], fill=(168, 116, 64))
    # three small flags on poles above the table
    flags = [
        ((52, 110, 190), (250, 210, 30)),   # Ukraine: blue over yellow
        ((178, 34, 52), (255, 255, 255)),   # USA: red stripes (simplified)
        ((30, 60, 150), (250, 210, 30)),    # EU: blue with gold
    ]
    fx = [x + 26, x + w // 2 - 28, x + w - 82]
    for (c1, c2), px in zip(flags, fx):
        d.line([(px + 28, y + 12), (px + 28, y + 62)], fill=(80, 80, 80), width=3)
        d.rectangle([px, y + 12, px + 56, y + 36], fill=c1)
        d.rectangle([px, y + 36, px + 56, y + 60], fill=c2)
        if c1 == (178, 34, 52):
            for sy in range(y + 16, y + 58, 8):
                d.line([(px, sy), (px + 56, sy)], fill=(255, 255, 255), width=2)
        if c1 == (30, 60, 150):
            for dx, dy in [(14, 6), (28, 2), (42, 6), (14, 16), (42, 16)]:
                d.ellipse([px + dx, y + 12 + dy, px + dx + 5, y + 17 + dy], fill=GOLD)


def draw_warship(d, x, y, w, h):
    import math
    d.rectangle([x, y, x + w, y + h], fill=(168, 186, 205))
    sea_top = y + h - 30
    # sea
    d.rectangle([x, sea_top, x + w, y + h], fill=(38, 84, 128))
    for wx in range(x + 8, x + w - 10, 34):
        d.arc([wx, sea_top + 6, wx + 26, sea_top + 22], 180, 360, fill=(220, 235, 245), width=3)
    # hull
    d.polygon([(x + 18, sea_top), (x + w - 18, sea_top),
               (x + w - 34, sea_top + 18), (x + 34, sea_top + 18)], fill=(74, 78, 84))
    # superstructure + mast
    sh = max(18, h - 58)
    d.rectangle([x + w // 2 - 46, sea_top - sh, x + w // 2 + 40, sea_top], fill=(96, 100, 106))
    d.rectangle([x + w // 2 - 30, sea_top - sh - 12, x + w // 2 + 24, sea_top - sh], fill=(74, 78, 84))
    d.line([(x + w // 2, sea_top - sh - 12), (x + w // 2, sea_top - sh - 22)], fill=(60, 60, 60), width=3)
    # drone + explosion burst at the bow
    bx, by = x + 58, sea_top - 22
    d.ellipse([x + 22, y + 12, x + 34, y + 24], fill=(30, 30, 30))
    d.line([(x + 28, y + 18), (bx - 12, by - 6)], fill=(30, 30, 30), width=2)
    for ang, ln in [(0, 24), (45, 18), (90, 22), (135, 16), (180, 20), (225, 16), (270, 22), (315, 18)]:
        r = math.radians(ang)
        d.line([(bx + 11 * math.cos(r), by + 11 * math.sin(r)),
                (bx + ln * math.cos(r), by + ln * math.sin(r))],
               fill=(240, 120, 20), width=4)
    d.ellipse([bx - 12, by - 12, bx + 12, by + 12], fill=(250, 170, 40))


def draw_gulf(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(238, 214, 160))
    # desert ground
    d.rectangle([x, y + h - 22, x + w, y + h], fill=(196, 158, 96))
    # sun
    d.ellipse([x + w - 56, y + 8, x + w - 16, y + 48], fill=(245, 180, 60))
    # radar dome, radius fits the panel height
    r = min(52, (h - 22) // 2)
    cx = x + w // 2
    base = y + h - 22
    d.pieslice([cx - r, base - 2 * r, cx + r, base], 180, 360, fill=(245, 245, 240))
    d.rectangle([cx - r, base - 6, cx + r, base], fill=(210, 210, 205))
    # antenna + missile streak
    d.line([(cx, base - 2 * r + 6), (cx, y + 8)], fill=(90, 90, 90), width=3)
    d.ellipse([cx - 5, y + 4, cx + 5, y + 14], fill=(200, 40, 40))
    d.line([(x + 20, y + h - 26), (x + 84, y + h - 62)], fill=(220, 60, 30), width=5)
    d.polygon([(x + 84, y + h - 62), (x + 68, y + h - 62), (x + 78, y + h - 46)], fill=(240, 120, 20))


def draw_outage(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(208, 224, 240))
    # cloud
    d.ellipse([x + w // 2 - 70, y + 8, x + w // 2 - 6, y + 56], fill=(255, 255, 255))
    d.ellipse([x + w // 2 - 30, y - 6, x + w // 2 + 44, y + 52], fill=(255, 255, 255))
    d.ellipse([x + w // 2 + 6, y + 14, x + w // 2 + 72, y + 58], fill=(255, 255, 255))
    d.rectangle([x + w // 2 - 58, y + 34, x + w // 2 + 60, y + 58], fill=(255, 255, 255))
    # down arrow, left
    d.line([(x + 30, y + 22), (x + 30, y + 62)], fill=(24, 84, 160), width=6)
    d.polygon([(x + 16, y + 52), (x + 44, y + 52), (x + 30, y + 74)], fill=(24, 84, 160))
    # red X in a circle, right
    d.ellipse([x + w - 66, y + 18, x + w - 18, y + 66], fill=(178, 28, 32))
    d.line([(x + w - 56, y + 28), (x + w - 28, y + 56)], fill=(255, 255, 255), width=6)
    d.line([(x + w - 28, y + 28), (x + w - 56, y + 56)], fill=(255, 255, 255), width=6)


def draw_hack(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(32, 32, 44))
    # laptop
    d.rectangle([x + w // 2 - 92, y + 14, x + w // 2 + 92, y + h - 34], fill=(16, 60, 110))
    d.rectangle([x + w // 2 - 84, y + 22, x + w // 2 + 84, y + h - 42], fill=(20, 90, 150))
    # masked face on screen: grey head, black mask band, white eyes
    d.ellipse([x + w // 2 - 34, y + 26, x + w // 2 + 34, y + 78], fill=(200, 200, 205))
    d.rectangle([x + w // 2 - 34, y + 42, x + w // 2 + 34, y + 62], fill=(20, 20, 24))
    d.ellipse([x + w // 2 - 22, y + 48, x + w // 2 - 8, y + 56], fill=(255, 255, 255))
    d.ellipse([x + w // 2 + 8, y + 48, x + w // 2 + 22, y + 56], fill=(255, 255, 255))
    # laptop base
    d.rectangle([x + w // 2 - 108, y + h - 34, x + w // 2 + 108, y + h - 22], fill=(90, 90, 96))
    # gold coins spilling out
    for cx, cy in [(x + 22, y + h - 34), (x + 44, y + h - 22), (x + w - 44, y + h - 30),
                   (x + w - 22, y + h - 20), (x + w // 2 + 118, y + h - 40)]:
        d.ellipse([cx - 11, cy - 11, cx + 11, cy + 11], fill=(240, 190, 60))
        d.text((cx - 5, cy - 9), "$", font=font(SANS_B, 14), fill=(120, 80, 0))


# ---------------------------------------------------------------- page
def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 24  # margin

    # ---- masthead
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((W // 2, 14), "THE WORLD TODAY", font=font(SERIF_B, 62),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 82), "FRIDAY, 13 NOVEMBER 2026", font=font(SANS_B, 25),
           fill=GOLD, anchor="ma")
    d.rectangle([0, 118, W, 122], fill=GOLD)

    # ---- lead story
    y = 136
    y = kicker(d, M, y, "TOP STORY  \u2022  WASHINGTON", RED)
    y = headline(d, M, y, "NVIDIA CHIEF QUITS; SENATE SUMMONS HUANG AND LUTNICK",
                 font(SERIF_B, 38), INK, W - 2 * M, 46)
    y += 6
    draw_senate(d, M, y, 336, 148)
    para(d, M + 356, y + 4,
         "Jensen Huang resigned as Nvidia chief executive amid an inquiry into a "
         "suspected Chinese spy link. The Senate Banking Committee called Huang "
         "and Commerce Secretary Howard Lutnick to testify on AI chip exports "
         "to China.",
         font(SERIF, 23), INK, W - M - (M + 356), 31)
    y += 148 + 12
    rule(d, M, W - M, y)

    # ---- middle row: three stories, measured heights
    y += 12
    col_w = (W - 2 * M - 2 * 16) // 3
    stories = [
        ("UKRAINE  \u2022  DIPLOMACY", BLUE, "EUROPE WINS A SEAT AT THE PEACE TALKS",
         "US envoys Witkoff and Kushner met Putin in Moscow, then Zelensky near "
         "Dublin. Europe will join the next round; the war's largest prisoner "
         "swap is planned.", draw_talks),
        ("UKRAINE  \u2022  THE WAR AT SEA", BLUE, "DRONE HITS RUSSIAN WARSHIP OFF FINLAND",
         "Ukraine says its drones struck the corvette Naro-Fominsk near Ust-Luga. "
         "Finland confirmed it detected the strike in the Gulf of Finland.", draw_warship),
        ("THE GULF", RED, "IRAN SAYS IT STRUCK A US RADAR SITE IN BAHRAIN",
         "Tehran's Guards claim the attack as tankers are hit in the Strait of "
         "Hormuz. Trump says the US needs no deal with Iran.", draw_gulf),
    ]
    row_top = y
    row_end = y
    for i, (kick, kc, head, body, art) in enumerate(stories):
        x = M + i * (col_w + 16)
        art(d, x, y, col_w, 84)
        yy = y + 84 + 8
        yy = kicker(d, x, yy, kick, kc)
        yy = headline(d, x, yy, head, font(SANS_B, 22), INK, col_w, 26)
        yy = para(d, x, yy + 4, body, font(SERIF, 18), INK, col_w, 23)
        row_end = max(row_end, yy)
    y = row_end + 12
    rule(d, M, W - M, y)

    # ---- bottom row: two stories, thumbnail on the left, text on the right
    y += 12
    col2_w = (W - 2 * M - 16) // 2
    stories2 = [
        ("TECHNOLOGY", BLUE, "MICROSOFT 365 OUTAGE HITS 74 COUNTRIES",
         "Outlook, Teams and Copilot stayed down for a second day, disrupting "
         "hospitals, police and businesses around the world.", draw_outage),
        ("CYBERCRIME", RED, "FBI: N. KOREA HACKERS STOLE $400M IN FAKE VIDEO CALLS",
         "The FBI says North Korean hackers used fake video calls to steal $400m "
         "in crypto \u2014 and seized $1.2bn stolen from Binance.", draw_hack),
    ]
    for i, (kick, kc, head, body, art) in enumerate(stories2):
        x = M + i * (col2_w + 16)
        art(d, x, y, 160, 160)
        tx = x + 160 + 14
        tw = col2_w - 160 - 14
        yy = y + 2
        yy = kicker(d, tx, yy, kick, kc)
        yy = headline(d, tx, yy, head, font(SANS_B, 20), INK, tw, 24)
        para(d, tx, yy + 4, body, font(SERIF, 17), INK, tw, 22)
    y += 160 + 12
    print("content ends at y =", y, "(ticker starts at 950)")

    # ---- ticker strip
    d.rectangle([0, 950, W, H], fill=NAVY)
    d.text((M, 960), "ALSO TODAY:", font=font(SANS_B, 19), fill=GOLD)
    para(d, M + 150, 961,
         "US reports a record 483,200 deportations in 2026  \u2022  Harry Kane's 126th "
         "cap as England beat Croatia  \u2022  Israeli strike kills six at a Gaza "
         "hospital  \u2022  Kansas governor's race won by Democrat Cindy Holscher",
         font(SANS, 16), (235, 235, 235), W - M - (M + 150), 22)

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    build()
