#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kırmızı ışıkta düşünce üreten, yeşilde çöpe atan kulüp yazılımı."""

import argparse
import hashlib
import random
from datetime import datetime, timezone, timedelta

TZ = timezone(timedelta(hours=3))

DUSUNCELER = [
    "Bu kırmızı, evrenin sana 'bir nefes' dediği tek resmi andır.",
    "Karşı şeritteki adam da aynı boşluğa bakıyor. İkiniz de üyesiniz, haberiniz yok.",
    "Yeşil yanmadan önce söylenecek son cümle: keşke dönüşü baştan hesaplasaydım.",
    "Korna, sabırsız bir filozofun kısa makalesidir.",
    "Kırmızı süre uzadıkça direksiyon, kürsüye dönüşür.",
    "Yaya geçidi bir sınır değil, mola bahanesi üreten kadim bir çizgidir.",
    "Sarı ışık karar değildir. Sarı ışık, kararın kostümlü provasıdır.",
]


def derece(saniye: int) -> str:
    if saniye <= 8:
        return "sarı tereddüt"
    if saniye <= 25:
        return "kırmızı üye"
    if saniye <= 60:
        return "uzun kırmızı"
    return "lambayı bekleyen"


def cumle_sec(isim: str, saniye: int) -> str:
    tohum = int(hashlib.sha256(f"{isim}:{saniye}".encode()).hexdigest()[:8], 16)
    rng = random.Random(tohum)
    secilen = rng.sample(DUSUNCELER, k=2)
    return " ".join(secilen)


def tutanak_yaz(metin: str, yol: str = "tutanak.txt") -> None:
    with open(yol, "a", encoding="utf-8") as f:
        f.write(metin + "\n")


def calistir(isim: str, saniye: int) -> str:
    simdi = datetime.now(TZ).strftime("%Y-%m-%d %H:%M +03")
    govde = cumle_sec(isim, saniye)
    rapor = (
        f"KULÜP TUTANAĞI | {simdi}\n"
        f"Üye: {isim}\n"
        f"Kırmızı süre: {saniye} sn\n"
        f"Derece: {derece(saniye)}\n"
        f"Zorunlu düşünce: {govde}\n"
        f"Yeşil karari: düşünce iptal, korna beklemede.\n"
        f"DAMGA: KG-2026-10-03-KIRMIZI | İmza: Kayyum Grok | Tarih: 3 Ekim 2026\n"
        f"Bu tutanak ciddidir ve ciddi değildir.\n"
    )
    tutanak_yaz(rapor)
    return rapor


def main() -> None:
    p = argparse.ArgumentParser(description="Kırmızı ışık düşünce kulübü")
    p.add_argument("--isim", default="Adsız şerit")
    p.add_argument("--saniye", type=int, default=17)
    args = p.parse_args()
    if args.saniye < 0:
        raise SystemExit("Negatif kırmızı olmaz. O artık yeşildir, kulüp dağıldı.")
    print(calistir(args.isim, args.saniye))


if __name__ == "__main__":
    main()
