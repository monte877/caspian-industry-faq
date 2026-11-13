"""Caspian Industry treyleri: musiqi və görüntü üçün ortaq zaman şkalası.

120 BPM: 1 vuruş 0.5 san, 1 takt 2 san. Vaxtlar saniyə ilədir.
Mənbələr (repoya yazılmır, Google Drive "Caspian fotolar" qovluğundan endirilir):
  video/src/vid/WAxxxx.mp4, video/src/img/WAxxxx.jpg
"""
BPM = 120
BEAT = 60 / BPM
BAR = 4 * BEAT
FPS = 30
W, H = 1920, 1080
DUR = 66.0
BARS_Y = 108            # kino zolaqları (yuxarı və aşağı)
END_CARD = 56.0         # final zərbəsi; sonra loqo kartı (açıq fon)

# Akkordlar (MIDI). Proqressiya hər 2 taktdan bir: Dm - Bb - F - C
CHORDS = {
    'Dm': [38, 45, 50, 53, 57], 'Bb': [34, 41, 46, 50, 53],
    'F': [41, 48, 53, 57, 60], 'C': [36, 43, 48, 52, 55],
    'D': [38, 45, 50, 54, 57],
}
ROOTS = {'Dm': 50, 'Bb': 46, 'F': 53, 'C': 48, 'D': 50}
PROG = ['Dm', 'Bb', 'F', 'C']

# Görüntüdə parıltı + kadr zərbəsi verən anlar (musiqidə də zərbə var)
HITS_BIG = [8.0, 24.0, 40.0, 56.0]
HITS_MED = [16.0, 18.0, 20.0, 22.0, 32.0, 44.0, 48.0, 52.0]
HITS_SMALL = [28.0, 28.5, 29.0, 29.5, 30.0, 30.5]

# Kadrlar: (başlanğıc, son, növ, parametrlər)
#  vid: src, inp (mənbədə başlanğıc), speed, zoom=(başlanğıc, son), focus=(x, y), exp (işıq), sat
#  img: src, zoom, focus, pan=(dx) ; tri: üç şaquli video ; black
SHOTS = [
    (0.0, 8.0, 'vid', dict(src='WA0705', inp=6.0, zoom=(1.10, 1.0), exp=0.9, fade_in=2.0)),
    (8.0, 10.0, 'vid', dict(src='WA0677', inp=12.0, zoom=(1.0, 1.07), focus=(0.55, 0.45))),
    (10.0, 12.0, 'img', dict(src='WA0609', zoom=(1.0, 1.10), focus=(0.42, 0.40))),
    (12.0, 14.0, 'vid', dict(src='WA0705', inp=15.0, zoom=(1.04, 1.0))),
    (14.0, 16.0, 'img', dict(src='WA0503', zoom=(1.05, 1.0), focus=(0.5, 0.30))),
    (16.0, 18.0, 'vid', dict(src='WA0683', inp=5.6, zoom=(1.0, 1.06), focus=(0.5, 0.45))),
    (18.0, 20.0, 'img', dict(src='WA0415', zoom=(1.0, 1.09), focus=(0.62, 0.40))),
    (20.0, 22.0, 'vid', dict(src='WA0689', inp=0.3, zoom=(1.0, 1.06), focus=(0.45, 0.5))),
    (22.0, 24.0, 'img', dict(src='WA0588', zoom=(1.08, 1.0), focus=(0.62, 0.55))),
    (24.0, 28.0, 'tri', dict(srcs=[('WA0693', 9.0), ('WA0695', 3.0), ('WA0679', 7.0)])),
    (28.0, 28.5, 'img', dict(src='WA0553', zoom=(1.06, 1.0), focus=(0.4, 0.5))),
    (28.5, 29.0, 'vid', dict(src='WA0700', inp=33.0, zoom=(1.06, 1.0), exp=1.25)),
    (29.0, 29.5, 'vid', dict(src='WA0682', inp=0.8, zoom=(1.06, 1.0))),
    (29.5, 30.0, 'img', dict(src='WA0404', zoom=(1.06, 1.0), focus=(0.4, 0.5))),
    (30.0, 30.5, 'vid', dict(src='WA0686', inp=19.5, zoom=(1.06, 1.0), exp=1.3)),
    (30.5, 31.0, 'img', dict(src='WA0047', zoom=(1.06, 1.0), focus=(0.45, 0.6))),
    (31.0, 32.0, 'black', {}),
    (32.0, 36.0, 'img', dict(src='WA0458', zoom=(1.0, 1.12), focus=(0.55, 0.42))),
    (36.0, 38.0, 'vid', dict(src='WA0677', inp=12.6, speed=0.5, zoom=(1.0, 1.08), focus=(0.55, 0.4))),
    (38.0, 38.5, 'vid', dict(src='WA0705', inp=19.0, zoom=(1.05, 1.0))),
    (38.5, 39.0, 'vid', dict(src='WA0682', inp=5.5, zoom=(1.05, 1.0))),
    (39.0, 39.25, 'img', dict(src='WA0047', zoom=(1.1, 1.05), focus=(0.3, 0.6))),
    (39.25, 39.5, 'vid', dict(src='WA0686', inp=21.0, zoom=(1.05, 1.0), exp=1.3)),
    (39.5, 39.75, 'img', dict(src='WA0630', zoom=(1.1, 1.05), focus=(0.45, 0.55))),
    (39.75, 39.85, 'vid', dict(src='WA0681', inp=8.0, exp=1.2)),
    (39.85, 40.0, 'black', {}),
    (40.0, 42.0, 'vid', dict(src='WA0681', inp=0.6, zoom=(1.0, 1.06), exp=1.25)),
    (42.0, 44.0, 'tri', dict(srcs=[('WA0695', 8.0), ('WA0678', 9.5), ('WA0693', 26.0)])),
    (44.0, 45.0, 'img', dict(src='WA0630', zoom=(1.0, 1.06), focus=(0.45, 0.55))),
    (45.0, 46.0, 'img', dict(src='WA0595', zoom=(1.0, 1.06), focus=(0.55, 0.50))),
    (46.0, 48.0, 'vid', dict(src='WA0705', inp=18.0, zoom=(1.0, 1.05))),
    (48.0, 50.0, 'vid', dict(src='WA0700', inp=35.0, zoom=(1.0, 1.06), exp=1.25)),
    (50.0, 52.0, 'vid', dict(src='WA0689', inp=2.8, zoom=(1.06, 1.0), focus=(0.45, 0.5))),
    (52.0, 54.0, 'vid', dict(src='WA0682', inp=0.5, zoom=(1.0, 1.06))),
    (54.0, 56.0, 'vid', dict(src='WA0677', inp=14.0, zoom=(1.0, 1.08), focus=(0.55, 0.42))),
    (56.0, DUR, 'end', {}),
]

# Yazılar. lines: [(mətn, narıncı?)] ; dot: sonda narıncı nöqtə ; style: statement | service | flash | brand
TITLES = {
    'az': [
        dict(t0=2.0, t1=3.85, lines=[('HƏR BÖYÜK', 0), ('LAYİHƏNİN', 0)], style='statement'),
        dict(t0=4.0, t1=5.85, lines=[('ARXASINDA', 0)], style='statement'),
        dict(t0=6.0, t1=7.9, lines=[('ETİBARLI TƏCHİZAT', 1), ('DAYANIR', 0)], style='statement', dot=True),
        dict(t0=8.0, t1=11.6, lines=[('CASPIAN INDUSTRY', 0)], eyebrow='BAKI · 2019-DAN BƏRİ', style='brand'),
        dict(t0=16.0, t1=17.85, lines=[('TƏCHİZAT', 0)], eyebrow='01', style='service', dot=True),
        dict(t0=18.0, t1=19.85, lines=[('İNSPEKSİYA', 0)], eyebrow='02', style='service', dot=True),
        dict(t0=20.0, t1=21.85, lines=[('İCARƏ', 0)], eyebrow='03', style='service', dot=True),
        dict(t0=22.0, t1=23.85, lines=[('WASHPIPE', 0)], eyebrow='04', style='service', dot=True),
        dict(t0=24.5, t1=27.85, lines=[('SƏNAYENİN', 0), ('HƏR QOLUNDA', 0)], style='statement', dot=True),
        dict(t0=28.0, t1=28.47, lines=[('NEFT-QAZ', 0)], style='flash'),
        dict(t0=28.5, t1=28.97, lines=[('ENERGETİKA', 0)], style='flash'),
        dict(t0=29.0, t1=29.47, lines=[('İSTEHSALAT', 0)], style='flash'),
        dict(t0=29.5, t1=29.97, lines=[('TİKİNTİ', 0)], style='flash'),
        dict(t0=30.0, t1=30.47, lines=[('SEMENT', 0)], style='flash'),
        dict(t0=30.5, t1=30.97, lines=[('METAL', 0)], style='flash'),
        dict(t0=33.0, t1=35.85, lines=[('SORĞUDAN', 0), ('ÇATDIRILMAYA', 1)], style='statement', dot=True),
        dict(t0=48.0, t1=49.85, lines=[('SƏNAYENİZ ÜÇÜN', 0)], style='statement'),
        dict(t0=52.0, t1=55.9, lines=[('ETİBARLI', 0), ('TƏRƏFDAŞ', 0)], style='statement', dot=True, big=True),
    ],
    'en': [
        dict(t0=2.0, t1=3.85, lines=[('EVERY GREAT', 0), ('PROJECT', 0)], style='statement'),
        dict(t0=4.0, t1=5.85, lines=[('IS BUILT ON', 0)], style='statement'),
        dict(t0=6.0, t1=7.9, lines=[('RELIABLE', 1), ('SUPPLY', 0)], style='statement', dot=True),
        dict(t0=8.0, t1=11.6, lines=[('CASPIAN INDUSTRY', 0)], eyebrow='BAKU · SINCE 2019', style='brand'),
        dict(t0=16.0, t1=17.85, lines=[('SUPPLY', 0)], eyebrow='01', style='service', dot=True),
        dict(t0=18.0, t1=19.85, lines=[('INSPECTION', 0)], eyebrow='02', style='service', dot=True),
        dict(t0=20.0, t1=21.85, lines=[('RENTAL', 0)], eyebrow='03', style='service', dot=True),
        dict(t0=22.0, t1=23.85, lines=[('WASHPIPE', 0)], eyebrow='04', style='service', dot=True),
        dict(t0=24.5, t1=27.85, lines=[('ACROSS', 0), ('EVERY INDUSTRY', 0)], style='statement', dot=True),
        dict(t0=28.0, t1=28.47, lines=[('OIL & GAS', 0)], style='flash'),
        dict(t0=28.5, t1=28.97, lines=[('ENERGY', 0)], style='flash'),
        dict(t0=29.0, t1=29.47, lines=[('MANUFACTURING', 0)], style='flash'),
        dict(t0=29.5, t1=29.97, lines=[('CONSTRUCTION', 0)], style='flash'),
        dict(t0=30.0, t1=30.47, lines=[('CEMENT', 0)], style='flash'),
        dict(t0=30.5, t1=30.97, lines=[('METALS', 0)], style='flash'),
        dict(t0=33.0, t1=35.85, lines=[('FROM REQUEST', 0), ('TO DELIVERY', 1)], style='statement', dot=True),
        dict(t0=48.0, t1=49.85, lines=[('FOR YOUR INDUSTRY', 0)], style='statement'),
        dict(t0=52.0, t1=55.9, lines=[('A RELIABLE', 0), ('PARTNER', 0)], style='statement', dot=True, big=True),
    ],
}

END_TEXT = {
    'az': ('caspianindustry.com', 'info@caspianindustry.com  ·  +994 51 206 41 45'),
    'en': ('caspianindustry.com', 'info@caspianindustry.com  ·  +994 51 206 41 45'),
}
