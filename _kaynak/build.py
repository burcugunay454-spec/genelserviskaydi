# -*- coding: utf-8 -*-
"""Genel Servis Kaydı — tek sayfa site üretici.
Çalıştır:  python -I -X utf8 _kaynak/build.py
Fotoğraflar: _kaynak/gorsel/ içine GORSEL-PROMPTLARI.md'deki adlarla (jpg/png/webp) koyun; build webp'ye çevirir.
Ayarlar ve metinler: _kaynak/icerik.py"""
import json, os, sys
from html import escape as e
from urllib.parse import quote

KAYNAK = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(KAYNAK)
sys.path.insert(0, KAYNAK)
import icerik as C  # noqa: E402

rakam = "".join(c for c in C.TEL if c.isdigit())
TEL_E164 = ("+90" + rakam[-10:]) if len(rakam) >= 10 else ""
TEL_GOSTER = C.TEL or "0 (5XX) XXX XX XX"
TEL_HREF = f"tel:{TEL_E164}" if TEL_E164 else "#kayit"
wr = "".join(c for c in (C.WHATSAPP or C.TEL) if c.isdigit())
WA_NO = ("90" + wr[-10:]) if len(wr) >= 10 else ""
YAYINDA = bool(TEL_E164 and C.ALAN)
URL = C.ALAN.rstrip("/") + "/"


def wa(metin):
    return f"https://wa.me/{WA_NO}?text={quote(metin)}" if WA_NO else "#kayit"


P = {
    "tel": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "buzdolabi": '<rect x="5" y="2" width="14" height="20" rx="2.5"/><path d="M5 9.5h14M8.5 5v2M8.5 12.5v3.5"/>',
    "camasir": '<rect x="3.5" y="2" width="17" height="20" rx="2.5"/><circle cx="12" cy="13.5" r="5"/><path d="M7 5.5h.01M10 5.5h.01"/>',
    "bulasik": '<rect x="4" y="2" width="16" height="20" rx="2.5"/><path d="M4 7h16M7.5 4.5h.01M8 11h8M8 14.5h8M8 18h8"/>',
    "firin": '<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 8h18M6.5 5.5h.01M10 5.5h.01M7 11.5h10v6H7z"/>',
    "kombi": '<rect x="5" y="2" width="14" height="15" rx="2.5"/><path d="M9 21v-4M15 21v-4M12 5.5c-1.6 2-2.2 3.2-2.2 4.2a2.2 2.2 0 0 0 4.4 0c0-1-.6-2.2-2.2-4.2z"/>',
    "klima": '<rect x="2" y="4" width="20" height="8.5" rx="2.5"/><path d="M6 9.5h12M7 16c0 1.5-1 2-1 3.5M12 16v4M17 16c0 1.5 1 2 1 3.5"/>',
    "anahtar": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "onay": '<path d="M20 6 9 17l-5-5"/>',
    "bagimsiz": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "ucret": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
    "parca": '<path d="M12 2 3 7v10l9 5 9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
    "belge": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    "saat": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "konum": '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "ok": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}
WA_YOL = '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.6.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/>'


def ik(ad):
    if ad == "wa":
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{WA_YOL}</svg>'
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[ad]}</svg>'


GORSEL = {}


def gorselleri_hazirla():
    kaynak = os.path.join(KAYNAK, "gorsel")
    hazir = {}
    if not os.path.isdir(kaynak):
        return hazir
    try:
        from PIL import Image
    except ImportError:
        print("UYARI: Pillow yok, görseller atlandı")
        return hazir
    os.makedirs(os.path.join(KOK, "img"), exist_ok=True)
    for dosya in sorted(os.listdir(kaynak)):
        ad, uz = os.path.splitext(dosya)
        if uz.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            continue
        im = Image.open(os.path.join(kaynak, dosya)).convert("RGB")
        genislikler = [800, 1400] if ad in ("hero", "og-kapak", "kurumsal") else [480, 800]
        boy = []
        for g in genislikler:
            g2 = min(g, im.width)
            h2 = round(im.height * g2 / im.width)
            hedef = os.path.join(KOK, "img", f"{ad}-{g}.webp")
            if not os.path.exists(hedef) or os.path.getmtime(hedef) < os.path.getmtime(os.path.join(kaynak, dosya)):
                im.resize((g2, h2), Image.LANCZOS).save(hedef, "WEBP", quality=80, method=6)
            boy.append((g, g2, h2))
        hazir[ad] = boy
    return hazir


def resim(ad, alt, sizes, oncelik=False):
    if ad not in GORSEL:
        return ""
    boy = GORSEL[ad]
    srcset = ", ".join(f"img/{ad}-{g}.webp {g2}w" for g, g2, _ in boy)
    _, w0, h0 = boy[0]
    yuk = 'fetchpriority="high"' if oncelik else 'loading="lazy" decoding="async"'
    return f'<img src="img/{ad}-{boy[0][0]}.webp" srcset="{srcset}" sizes="{sizes}" width="{w0}" height="{h0}" alt="{e(alt)}" {yuk}>'


def yer_tutucu(ikon, yazi):
    return f'<div class="yt">{ik(ikon)}<span>{e(yazi)}</span></div>'


def bas(baslik, aciklama, yol, robots, ek=""):
    url = URL + yol
    gtm = ""
    if C.GTM:
        gtm = ("<script>(function(w,d,id){w.dataLayer=w.dataLayer||[];var y=0;function f(){if(y)return;y=1;"
               "w.dataLayer.push({'gtm.start':Date.now(),event:'gtm.js'});var j=d.createElement('script');j.async=1;"
               "j.src='https://www.googletagmanager.com/gtm.js?id='+id;d.head.appendChild(j)}w.__gtmY=f;"
               "if(/[?&](gclid|gbraid|wbraid)=/.test(location.search)){f();return}"
               "['pointerdown','keydown','touchstart','scroll'].forEach(function(e){w.addEventListener(e,f,{once:true,passive:true})});"
               "w.addEventListener('load',function(){setTimeout(f,3500)})})(window,document,'" + C.GTM + "');</script>")
    og_resim = f'<meta property="og:image" content="{URL}img/og-kapak-1400.webp">' if "og-kapak" in GORSEL else ""
    font = "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=Lexend:wght@500;600;700&display=swap"
    return f'''<!doctype html>
<html lang="tr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{gtm}
<title>{e(baslik)}</title>
<meta name="description" content="{e(aciklama)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0c3b2e">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="{e(C.FIRMA)}">
<meta property="og:title" content="{e(baslik)}"><meta property="og:description" content="{e(aciklama)}"><meta property="og:url" content="{url}">{og_resim}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{font}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{font}"></noscript>
<style>{open(os.path.join(KAYNAK, "stil.css"), encoding="utf-8").read()}</style>
{ek}
</head><body>'''


def ust(ana=True):
    on = "" if ana else "./"
    return f'''<div class="bilgi"><div class="kap"><span>{ik("saat")}{e(C.SAAT)}</span><span>{ik("belge")}Servis kaydı: <a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="bilgi">{e(TEL_GOSTER)}</a></span></div></div>
<header class="ust"><div class="kap">
<a class="logo" href="{'#ust' if ana else './'}" aria-label="{e(C.FIRMA)} ana sayfa"><span class="logo-isaret">{ik("belge")}</span><span class="logo-ad">Genel<b>Servis Kaydı</b></span></a>
<button class="menu-ac" type="button" aria-label="Menüyü aç" aria-expanded="false" aria-controls="menu">{ik("menu")}</button>
<nav class="menu" id="menu" aria-label="Ana menü">
<a href="{on}#kurumsal">Kurumsal</a><a href="{on}#hizmetler">Hizmetler</a><a href="{on}#surec">Servis Kaydı</a><a href="{on}#rehber">Arıza Rehberi</a><a href="{on}#sss">SSS</a><a href="{on}#iletisim">İletişim</a>
<a class="btn btn-ara btn-kucuk" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="menu">{ik("tel")}<span>Hemen Ara</span></a>
</nav></div></header>'''


TUZAK = '''<!-- BOT-TUZAK (gerçek ziyaretçi görmez; dokunan cihaz işaretlenir, dönüşüm göndermez) -->
<div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden">
<a href="tel:+900000000000" data-cf-trap="1" tabindex="-1" rel="nofollow" onclick="return __cfTrap(event)">Hemen Ara</a>
<a href="https://wa.me/900000000000" data-cf-trap="1" tabindex="-1" rel="nofollow" onclick="return __cfTrap(event)">WhatsApp Servis</a>
<a href="tuzak/" data-cf-trap="1" tabindex="-1" rel="nofollow" onclick="return __cfTrap(event)">Servis kaydı</a>
</div>'''


def alt():
    li = [f'<li>{ik("tel")}<a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="alt">{e(TEL_GOSTER)}</a></li>']
    if WA_NO:
        li.append(f'<li>{ik("wa")}<a href="{wa("Merhaba, servis kaydı oluşturmak istiyorum.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="alt">WhatsApp</a></li>')
    if C.EPOSTA:
        li.append(f'<li>{ik("belge")}<a href="mailto:{e(C.EPOSTA)}">{e(C.EPOSTA)}</a></li>')
    if C.ADRES:
        li.append(f'<li>{ik("konum")}{e(C.ADRES)}</li>')
    li.append(f'<li>{ik("saat")}{e(C.SAAT)}</li>')
    unvan = f" ({e(C.UNVAN)})" if C.UNVAN else ""
    hizmet = "".join(f'<li><a href="./#hizmetler">{e(b)} servisi</a></li>' for _, b, _, _ in C.CIHAZLAR)
    return f'''<footer><div class="kap alt-izgara">
<div><a class="logo logo-acik" href="./"><span class="logo-isaret">{ik("belge")}</span><span class="logo-ad">Genel<b>Servis Kaydı</b></span></a>
<p>Beyaz eşya, kombi ve klima için servis kaydı, adreste arıza tespiti, onarım ve bakım.</p></div>
<div><h3>Hizmetler</h3><ul>{hizmet}</ul></div>
<div><h3>İletişim</h3><ul class="ik-liste">{"".join(li)}</ul></div>
<div><h3>Kurumsal</h3><ul><li><a href="./#kurumsal">Kurumsal yapı</a></li><li><a href="./#surec">Servis kaydı süreci</a></li><li><a href="hakkimizda.html">Hakkımızda</a></li><li><a href="iletisim.html">İletişim</a></li><li><a href="./#sss">Sık sorulanlar</a></li><li><a href="hizmet-kosullari.html">Hizmet koşulları</a></li><li><a href="gizlilik.html">Gizlilik ve KVKK</a></li><li><a href="cerez-politikasi.html">Çerez politikası</a></li></ul></div>
<p class="yasal">{e(C.FIRMA)}{unvan} bağımsız bir özel teknik servistir; hiçbir üretici markanın yetkili servisi, bayisi veya müşteri hizmetleri hattı değildir.
Marka garantisi kapsamındaki cihazlarınız için üreticinin yetkili servisine başvurabilirsiniz. © <span id="yil">2026</span> {e(C.FIRMA)}</p>
</div>
<div class="serit" role="note"><b>Bağımsız özel servis</b> Hiçbir markanın yetkili servisi değildir.</div></footer>'''


def yapiskan():
    w = (f'<a class="btn btn-wa" href="{wa("Merhaba, servis kaydı oluşturmak istiyorum.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="mobil">{ik("wa")}<span>WhatsApp</span></a>'
         if WA_NO else f'<a class="btn btn-wa" href="#kayit">{ik("wa")}<span>WhatsApp</span></a>')
    return f'<div class="yapiskan"><a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="mobil">{ik("tel")}<span>Hemen Ara</span></a>{w}</div>'


def js():
    return "<script>" + open(os.path.join(KAYNAK, "site.js"), encoding="utf-8").read() + "</script>"


def form():
    secenek = "".join(f"<option>{e(b)}</option>" for _, b, _, _ in C.CIHAZLAR)
    return f'''<form class="kayit-form" id="servis-formu" data-wa="{WA_NO}" novalidate>
<div class="kf-bas"><span class="kf-ikon">{ik("belge")}</span><div><h2 id="h-kayit">Servis kaydı oluşturun</h2><p>Mesajınız WhatsApp'ta hazır açılır.</p></div></div>
<div class="kf-izgara">
<div><label for="f-ad">Adınız</label><input id="f-ad" name="ad" autocomplete="name" required></div>
<div><label for="f-cihaz">Cihaz</label><select id="f-cihaz" name="cihaz" required><option value="">Seçin</option>{secenek}<option>Diğer</option></select></div>
<div class="tam"><label for="f-ariza">Arıza (kısaca)</label><input id="f-ariza" name="ariza" placeholder="Örn. su boşaltmıyor, hata kodu var"></div>
<div class="tam"><label for="f-semt">Semt / mahalle</label><input id="f-semt" name="semt" autocomplete="address-level3"></div>
</div>
<div class="bal" aria-hidden="true"><label for="f-web">Web siteniz</label><input id="f-web" name="web_sitesi" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-wa" type="submit">{ik("wa")}<span>Kaydı WhatsApp ile Gönder</span></button>
<p class="kvkk">Göndererek <a href="gizlilik.html">Gizlilik ve KVKK metnini</a> okuduğunuzu kabul edersiniz.</p>
</form>'''


def ana_sayfa():
    sema = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": C.FIRMA, "url": URL, "inLanguage": "tr-TR"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in C.SSS]},
        {"@context": "https://schema.org", "@type": "Service", "serviceType": "Beyaz eşya, kombi ve klima teknik servisi",
         "provider": {"@type": "Organization", "name": C.FIRMA, "url": URL},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servis hizmetleri",
                             "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"{b} servisi"}} for _, b, _, _ in C.CIHAZLAR]}},
    ]
    if YAYINDA:
        isletme = {"@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "name": C.FIRMA, "url": URL,
                   "telephone": TEL_E164, "description": C.DESC}
        if C.UNVAN:
            isletme["legalName"] = C.UNVAN
        if C.ADRES:
            isletme["address"] = {"@type": "PostalAddress", "streetAddress": C.ADRES, "addressCountry": "TR"}
        if "hero" in GORSEL:
            isletme["image"] = URL + "img/hero-1400.webp"
        sema.insert(0, isletme)
    ek = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in sema)
    if "hero" in GORSEL:
        ek += '<link rel="preload" as="image" href="img/hero-800.webp" imagesrcset="img/hero-800.webp 800w, img/hero-1400.webp 1400w" imagesizes="100vw" fetchpriority="high">'
    robots = "index,follow,max-image-preview:large" if YAYINDA else "noindex,nofollow"

    ara = f'<a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="hero">{ik("tel")}<span>Hemen Ara</span></a>'
    hero_gorsel = resim("hero", "Teknisyen evde bulaşık makinesini onarırken, anne ve kızı mutfakta izliyor", "100vw", oncelik=True)
    kurumsal_gorsel = resim("kurumsal", "Servis kayıt biriminde talep kaydeden çalışan", "(max-width:900px) 92vw, 520px") or yer_tutucu("belge", "Servis kayıt birimi")

    yapi = "".join(f'<li><span class="y-no">{i:02d}</span><div><h3>{ik(k)}{e(b)}</h3><p>{e(m)}</p></div></li>' for i, (k, b, m) in enumerate(C.YAPI, 1))
    hizmet = "".join(
        f'<article class="hizmet"><div class="h-foto">{resim(g, b + " onarımı yapan teknisyen", "(max-width:640px) 92vw, (max-width:1020px) 46vw, 360px") or yer_tutucu(k, b)}'
        f'<span class="h-ikon">{ik(k)}</span></div>'
        f'<div class="h-ic"><h3>{e(b)} Servisi</h3><p>{e(m)}</p>'
        + (f'<a href="{wa("Merhaba, " + b.lower() + " için servis kaydı oluşturmak istiyorum.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="hizmet">Servis kaydı oluştur {ik("ok")}</a>' if WA_NO else f'<a href="#kayit">Servis kaydı oluştur {ik("ok")}</a>')
        + '</div></article>' for k, b, m, g in C.CIHAZLAR)
    adim = "".join(f'<li><span class="a-no">{i}</span><h3>{e(b)}</h3><p>{e(m)}</p></li>' for i, (b, m) in enumerate(C.ADIMLAR, 1))
    ilke = "".join(f'<div class="ilke">{ik(k)}<div><h3>{e(b)}</h3><p>{e(m)}</p></div></div>' for k, b, m in C.ILKELER)
    rehber = "".join(f'<details><summary>{e(b)}</summary><p>{e(m)}</p></details>' for b, m in C.BELIRTILER)
    sss = "".join(f'<details><summary>{e(s)}</summary><p>{e(c)}</p></details>' for s, c in C.SSS)
    firma_satir = [("Firma", e(C.FIRMA))]
    if C.UNVAN:
        firma_satir.append(("Ünvan", e(C.UNVAN)))
    firma_satir += [("Telefon", f'<a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="firma">{e(TEL_GOSTER)}</a>'), ("Çalışma", e(C.SAAT))]
    if C.ADRES:
        firma_satir.append(("Adres", e(C.ADRES)))
    firma_satir.append(("Statü", "Bağımsız özel teknik servis"))
    firma = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in firma_satir)
    wa_btn = (f'<a class="btn btn-wa" href="{wa("Merhaba, servis kaydı oluşturmak istiyorum.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="iletisim">{ik("wa")}<span>WhatsApp</span></a>'
              if WA_NO else f'<a class="btn btn-wa" href="#kayit">{ik("wa")}<span>WhatsApp</span></a>')

    return bas(C.TITLE, C.DESC, "", robots, ek) + ust() + f'''
<main id="ust">
<!-- 1 · GİRİŞ + SERVİS KAYDI -->
<section class="hero{' foto' if hero_gorsel else ''}" aria-labelledby="h1">
<div class="hero-arka">{hero_gorsel}</div>
<div class="kap hero-izgara">
<div class="hero-ic">
<span class="etiket">Bağımsız özel teknik servis</span>
<h1 id="h1">Beyaz eşya, kombi ve klima için <span>servis kaydı</span></h1>
<p class="giris">Kaydınızı oluşturun; teknisyen randevu saatinde adresinize gelsin, arızayı tespit etsin ve ücreti işlemden önce söylesin.</p>
<ul class="hero-liste"><li>{ik("onay")}Adreste arıza tespiti</li><li>{ik("onay")}Ücretlendirme işlemden önce</li><li>{ik("onay")}Hafta sonu da randevu</li></ul>
<div class="hero-tel"><span class="ht-ikon">{ik("tel")}</span><span><small>Servis kayıt hattı</small><a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="hero-numara">{e(TEL_GOSTER)}</a></span></div>
</div>
<div class="hero-form" id="kayit" aria-labelledby="h-kayit">{form()}</div>
</div></section>

<!-- 2 · KURUMSAL YAPI -->
<section class="bolum" id="kurumsal" aria-labelledby="h-kur"><div class="kap kurumsal">
<div class="kur-gorsel">{kurumsal_gorsel}<div class="kur-rozet">{ik("bagimsiz")}<span><b>Kayıtlı süreç</b>Her talep kayıtla başlar, kayıtla kapanır</span></div></div>
<div>
<span class="etiket koyu">Kurumsal yapımız</span>
<h2 id="h-kur">Her servis talebi kayıtlı ve planlı ilerler</h2>
<p class="bas-p">Talebiniz kayıt biriminden teknik ekibe, oradan kontrol ve kapanışa kadar tek bir kayıt üzerinden takip edilir.</p>
<ol class="yapi">{yapi}</ol>
</div>
</div></section>

<!-- 3 · HİZMETLER -->
<section class="bolum acik" id="hizmetler" aria-labelledby="h-hiz"><div class="kap">
<div class="bas"><span class="etiket koyu">Hizmetlerimiz</span><h2 id="h-hiz">Servis verdiğimiz cihazlar</h2><p>Arıza, bakım ve onarım için tek kayıt.</p></div>
<div class="hizmetler">{hizmet}</div>
</div></section>

<!-- 4 · SERVİS KAYDI SÜRECİ -->
<section class="bolum yesil" id="surec" aria-labelledby="h-sur"><div class="kap">
<div class="bas"><span class="etiket">Servis kaydı süreci</span><h2 id="h-sur">Dört adımda servis</h2><p>Arızayı ve ücreti öğrenmeden hiçbir işlem yapılmaz.</p></div>
<ol class="adimlar">{adim}</ol>
<div class="ilkeler">{ilke}</div>
</div></section>

<!-- 5 · ARIZA REHBERİ -->
<section class="bolum" id="rehber" aria-labelledby="h-reh"><div class="kap iki-kolon">
<div class="bas"><span class="etiket koyu">Arıza rehberi</span><h2 id="h-reh">Kayıt oluşturmadan önce kontrol edin</h2>
<p>Sık görülen belirtiler ve güvenle yapabileceğiniz ilk kontroller.</p>
<p class="uyari-kutu"><b>Güvenlik:</b> Gaz kokusu alırsanız elektrik düğmelerini kullanmayın, ortamı havalandırın ve doğal gaz acil hattı 187'yi arayın.</p></div>
<div class="akordeon">{rehber}</div>
</div></section>

<!-- 6 · SSS -->
<section class="bolum acik" id="sss" aria-labelledby="h-sss"><div class="kap iki-kolon">
<div class="bas"><span class="etiket koyu">Sık sorulan sorular</span><h2 id="h-sss">Merak edilenler</h2><p>Aradığınız cevap yoksa servis kayıt hattını arayın.</p></div>
<div class="akordeon">{sss}</div>
</div></section>

<!-- 7 · İLETİŞİM -->
<section class="bolum" id="iletisim" aria-labelledby="h-ilt"><div class="kap">
<div class="iletisim-kutu">
<div class="ik-sol"><span class="etiket">İletişim</span><h2 id="h-ilt">Servis kaydınızı şimdi oluşturun</h2>
<p>Telefonla arayın ya da WhatsApp'tan cihazınızı ve arızayı yazın.</p>
<div class="dugmeler">{ara.replace('data-konum="hero"', 'data-konum="iletisim"')}{wa_btn}</div></div>
<div class="firma"><h3>Firma bilgileri</h3><dl>{firma}</dl></div>
</div>
</div></section>
</main>
''' + alt() + TUZAK + yapiskan() + js() + "\n</body></html>\n"


def gizlilik():
    kim = e(C.FIRMA) + (f" ({e(C.UNVAN)})" if C.UNVAN else "")
    return bas(f"Gizlilik ve KVKK Aydınlatma Metni | {C.FIRMA}", "Kişisel verilerin işlenmesi, çerezler ve haklarınız hakkında bilgilendirme.",
               "gizlilik.html", "index,follow" if YAYINDA else "noindex,nofollow") + ust(False) + f'''
<main class="kap dar"><article class="metin">
<h1>Gizlilik ve KVKK Aydınlatma Metni</h1>
<p>Bu metin, 6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında veri sorumlusu sıfatıyla {kim} tarafından hazırlanmıştır.</p>
<h2>Hangi verileri işliyoruz?</h2>
<p>Telefon, WhatsApp veya servis kayıt formu ile ilettiğiniz ad, telefon numarası, adres/semt ve cihaz-arıza bilgileri.</p>
<h2>Hangi amaçla?</h2>
<p>Servis kaydınızı oluşturmak, randevu planlamak, adreste hizmet vermek ve yapılan işleme ilişkin kayıt tutmak. Verileriniz pazarlama amacıyla üçüncü kişilere satılmaz veya kiralanmaz.</p>
<h2>Hukuki sebep</h2>
<p>Bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması ve kanunlarda öngörülen kayıt yükümlülükleri (KVKK md. 5/2-a, c, ç).</p>
<h2>Aktarım</h2>
<p>Form gönderdiğinizde mesajınız sizin cihazınızda WhatsApp uygulamasında açılır; gönderim WhatsApp hizmet şartlarına tabidir. Sitede ziyaret ve reklam ölçümü için Google araçları (Google Tag Manager, Google Analytics, Google Ads) ve sahte tıklama önleme amacıyla güvenlik araçları kullanılabilir; bu araçlar çerez ve benzeri teknolojilerle cihaz bilgisi toplayabilir.</p>
<h2>Haklarınız</h2>
<p>KVKK md. 11 uyarınca verilerinizin işlenip işlenmediğini öğrenme, düzeltilmesini veya silinmesini isteme ve itiraz etme haklarına sahipsiniz. Başvurularınızı {e(TEL_GOSTER)} numarasından{(" veya " + e(C.EPOSTA) + " adresinden") if C.EPOSTA else ""} iletebilirsiniz.</p>
<h2>Bağımsız servis bilgilendirmesi</h2>
<p>{e(C.FIRMA)} bağımsız bir özel teknik servistir; hiçbir üretici markanın yetkili servisi, bayisi veya müşteri hizmetleri hattı değildir.</p>
<p><a class="btn btn-cizgi btn-kucuk" href="./">← Ana sayfaya dön</a></p>
</article></main>''' + alt() + yapiskan() + js() + "\n</body></html>\n"


YASAL = [("hakkimizda.html", "Hakkımızda"), ("iletisim.html", "İletişim"), ("hizmet-kosullari.html", "Hizmet Koşulları"),
         ("gizlilik.html", "Gizlilik ve KVKK"), ("cerez-politikasi.html", "Çerez Politikası")]


def sayfa(yol, baslik, aciklama, govde):
    return bas(f"{baslik} | {C.FIRMA}", aciklama, yol, "index,follow" if YAYINDA else "noindex,nofollow") + ust(False) + f"""
<main class="kap dar"><article class="metin">
<h1>{e(baslik)}</h1>
{govde}
<p><a class="btn btn-cizgi btn-kucuk" href="./">← Ana sayfaya dön</a></p>
</article></main>""" + alt() + yapiskan() + js() + "\n</body></html>\n"


def kim():
    return e(C.FIRMA) + (f" ({e(C.UNVAN)})" if C.UNVAN else "")


def hakkimizda():
    yapi = "".join(f"<li><b>{e(b)}:</b> {e(m)}</li>" for _, b, m in C.YAPI)
    cihaz = ", ".join(b.lower() for _, b, _, _ in C.CIHAZLAR)
    ilke = "".join(f"<h2>{e(b)}</h2><p>{e(m)}</p>" for _, b, m in C.ILKELER)
    return sayfa("hakkimizda.html", "Hakkımızda", "Genel Servis Kaydı kimdir, nasıl çalışır: bağımsız özel teknik servis, kayıtlı ve şeffaf servis süreci.", f"""
<p>{kim()}, beyaz eşya, kombi ve klima için adreste arıza tespiti, onarım ve bakım hizmeti veren <b>bağımsız bir özel teknik servistir</b>.
Hiçbir üretici markanın yetkili servisi, bayisi veya müşteri hizmetleri hattı değildir; sitemizde marka adı veya logosu kullanılmaz.</p>
<h2>Hangi cihazlara bakıyoruz?</h2><p>{e(cihaz)}.</p>
<h2>Servis kaydı nasıl işler?</h2><ul>{yapi}</ul>
{ilke}
<h2>Garanti kapsamındaki cihazlar</h2><p>Cihazınız üretici garantisi kapsamındaysa, garantinin geçerliliğini korumak için önce üreticinin yetkili servisine başvurmanızı öneririz.</p>""")


def iletisim():
    satir = [f'<li><b>Telefon:</b> <a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="iletisim-sayfa">{e(TEL_GOSTER)}</a></li>']
    if WA_NO:
        satir.append(f'<li><b>WhatsApp:</b> <a href="{wa("Merhaba, servis kaydı oluşturmak istiyorum.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="iletisim-sayfa">Mesaj gönderin</a></li>')
    if C.EPOSTA:
        satir.append(f'<li><b>E-posta:</b> <a href="mailto:{e(C.EPOSTA)}">{e(C.EPOSTA)}</a></li>')
    if C.UNVAN:
        satir.append(f"<li><b>Ticari unvan:</b> {e(C.UNVAN)}</li>")
    if C.ADRES:
        satir.append(f"<li><b>Adres:</b> {e(C.ADRES)}</li>")
    satir.append(f"<li><b>Çalışma:</b> {e(C.SAAT)}</li>")
    return sayfa("iletisim.html", "İletişim", "Servis kaydı oluşturmak için telefon, WhatsApp ve form ile bize ulaşın.", f"""
<p>Servis kaydı oluşturmak, randevu almak veya mevcut kaydınız hakkında bilgi almak için aşağıdaki kanallardan bize ulaşabilirsiniz.</p>
<ul>{"".join(satir)}</ul>
<h2>Servis kayıt formu</h2><p>Ana sayfadaki <a href="./#kayit">servis kayıt formunu</a> doldurduğunuzda mesajınız WhatsApp'ta hazır açılır; siz yalnızca gönderirsiniz.</p>
<h2>Bilgilendirme</h2><p>{e(C.FIRMA)} bağımsız bir özel teknik servistir; hiçbir markanın yetkili servisi veya müşteri hizmetleri hattı değildir.</p>""")


def hizmet_kosullari():
    return sayfa("hizmet-kosullari.html", "Hizmet Koşulları", "Servis kaydı, ücretlendirme, onay, parça ve iptal koşulları.", f"""
<p>Bu koşullar, {kim()} tarafından verilen servis hizmetleri ve bu internet sitesinin kullanımı için geçerlidir.</p>
<h2>1. Hizmetin niteliği</h2><p>{e(C.FIRMA)} bağımsız bir özel teknik servistir. Hiçbir üretici markanın yetkili servisi değildir; verilen hizmet üretici garantisi yerine geçmez.</p>
<h2>2. Servis kaydı ve randevu</h2><p>Kayıt telefon, WhatsApp veya form ile oluşturulur. Randevu günü ve saati sizinle birlikte belirlenir. Randevuyu değiştirmek veya iptal etmek için bize aynı kanallardan ulaşabilirsiniz.</p>
<h2>3. Arıza tespiti ve ücret</h2><p>Teknisyen cihazı adreste inceler, arızayı ve yapılacak işlemi açıklar. Ücret işlemden önce bildirilir. <b>Onayınız olmadan işlem yapılmaz.</b> İşlemi kabul etmemeniz durumunda uygulanacak bir tespit ücreti varsa bu, randevu sırasında önceden size söylenir.</p>
<h2>4. Parça</h2><p>Değişmesi gereken parça ve nedeni size açıklanır. Çıkan parça isterseniz size bırakılır.</p>
<h2>5. Belge</h2><p>Yapılan işlem ve ödenen ücret için isteğinize göre yazılı servis formu düzenlenir.</p>
<h2>6. Sitedeki bilgiler</h2><p>Arıza rehberindeki bilgiler genel bilgilendirme amaçlıdır; elektrik, gaz ve su tesisatına ilişkin işlemleri kendiniz yapmayın, cihazın kullanım kılavuzuna uyun.</p>
<h2>7. Kişisel veriler</h2><p>Kişisel verileriniz <a href="gizlilik.html">Gizlilik ve KVKK Aydınlatma Metni</a> kapsamında işlenir.</p>""")


def cerez():
    return sayfa("cerez-politikasi.html", "Çerez Politikası", "Sitede kullanılan çerezler ve tercihlerinizi nasıl yönetebileceğiniz.", f"""
<p>Bu sayfa, {kim()} internet sitesinde kullanılan çerezler (cookies) ve benzeri teknolojiler hakkında bilgi verir.</p>
<h2>Çerez nedir?</h2><p>Çerezler, siteyi ziyaret ettiğinizde tarayıcınıza kaydedilen küçük metin dosyalarıdır.</p>
<h2>Hangi çerezler kullanılabilir?</h2>
<ul><li><b>Zorunlu:</b> Sitenin çalışması ve sahte tıklamaların önlenmesi için tarayıcı hafızasına küçük kayıtlar yazılabilir.</li>
<li><b>Ölçüm ve reklam:</b> Ziyaret istatistikleri ve reklam performansının ölçülmesi için Google Analytics, Google Tag Manager ve Google Ads gibi araçlar kullanılabilir. Bu araçlar anonim cihaz ve ziyaret bilgisi toplayabilir.</li></ul>
<h2>Tercihlerinizi yönetme</h2><p>Tarayıcınızın ayarlarından çerezleri silebilir veya engelleyebilirsiniz. Google reklam kişiselleştirmesini <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Reklam Ayarları</a> sayfasından yönetebilirsiniz.</p>
<h2>Kişisel veriler</h2><p>Ayrıntılar için <a href="gizlilik.html">Gizlilik ve KVKK Aydınlatma Metni</a>'ni inceleyebilirsiniz.</p>""")


def llms(tam=False):
    cihaz = "\n".join(f"- {b}: {m}" for _, b, m, _ in C.CIHAZLAR)
    sayfalar = "\n".join(f"- [{b}]({URL}{y})" for y, b in YASAL)
    tel = C.TEL or "(telefon numarası yakında eklenecek)"
    t = f"""# {C.FIRMA}

> {C.FIRMA}, beyaz eşya (buzdolabı, çamaşır makinesi, bulaşık makinesi, fırın ve ocak), kombi ve klima için servis kaydı alan, adreste arıza tespiti, onarım ve bakım yapan bağımsız bir özel teknik servistir. Hiçbir üretici markanın yetkili servisi, bayisi veya müşteri hizmetleri hattı değildir.

## İletişim
- Telefon: {tel}
- Servis kayıt formu: {URL}#kayit (mesaj WhatsApp'ta hazır açılır)
- Çalışma: {C.SAAT}

## Hizmetler
{cihaz}

## Çalışma ilkeleri
- Ücret, arıza tespitinden sonra ve işlemden önce bildirilir; onay olmadan işlem yapılmaz.
- Değişen parça açıklanır, çıkan parça istenirse müşteriye bırakılır.
- İstenirse yazılı servis formu düzenlenir.
- Garanti kapsamındaki cihazlar için üreticinin yetkili servisine başvurulması önerilir.

## Sayfalar
- [Ana sayfa]({URL})
{sayfalar}
"""
    if tam:
        t += "\n## Sık sorulan sorular\n" + "\n".join(f"### {s}\n{c}\n" for s, c in C.SSS)
        t += "\n## Arıza rehberi\n" + "\n".join(f"### {s}\n{c}\n" for s, c in C.BELIRTILER)
        t += "\n## Servis süreci\n" + "\n".join(f"{i}. {b}: {m}" for i, (b, m) in enumerate(C.ADIMLAR, 1)) + "\n"
    return t


AI_BOTLAR = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot",
             "Perplexity-User", "Google-Extended", "Applebot-Extended", "Bingbot", "CCBot", "meta-externalagent"]


def bulunamadi():
    return bas(f"Sayfa bulunamadı | {C.FIRMA}", "Aradığınız sayfa bulunamadı.", "404.html", "noindex") + ust(False) + f'''
<main class="kap dar"><article class="metin" style="text-align:center">
<h1>Sayfa bulunamadı</h1><p>Aradığınız sayfa taşınmış veya kaldırılmış olabilir.</p>
<div class="dugmeler" style="justify-content:center"><a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="404">{ik("tel")}<span>Hemen Ara</span></a><a class="btn btn-cizgi" href="./">Ana sayfa</a></div>
</article></main>''' + alt() + yapiskan() + js() + "\n</body></html>\n"


def yaz(ad, metin):
    yol = os.path.join(KOK, ad)
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, "w", encoding="utf-8", newline="\n") as f:
        f.write(metin)


def main():
    GORSEL.update(gorselleri_hazirla())
    yaz("index.html", ana_sayfa())
    yaz("gizlilik.html", gizlilik())
    yaz("hakkimizda.html", hakkimizda())
    yaz("iletisim.html", iletisim())
    yaz("hizmet-kosullari.html", hizmet_kosullari())
    yaz("cerez-politikasi.html", cerez())
    yaz("llms.txt", llms())
    yaz("llms-full.txt", llms(True))
    yaz("404.html", bulunamadi())
    yaz("tuzak/index.html", '<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><title>Servis kaydı</title>'
        '<script>try{localStorage.setItem("cf_trap","1")}catch(e){}</script><p>Kayıt bulunamadı.</p>\n')
    yaz("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0c3b2e"/>'
        '<path d="M19 6h-8a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V10z" fill="none" stroke="#e0b13a" stroke-width="2.2" stroke-linejoin="round"/>'
        '<path d="M12.5 16.5l2.5 2.5 4.5-5" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>\n')
    yaz("robots.txt", "User-agent: *\nDisallow: /tuzak/\nAllow: /\n\n# Yapay zeka arama ve asistan botları: erişim serbest (tuzak hariç)\n"
        + "".join(f"User-agent: {b}\n" for b in AI_BOTLAR) + "Disallow: /tuzak/\nAllow: /\n" + f"\nSitemap: {URL}sitemap.xml\n")
    yaz("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + "".join(f"<url><loc>{URL}{y}</loc></url>" for y in ["", *[y for y, _ in YASAL]]) + "</urlset>\n")
    yaz("CNAME", C.ALAN.split("//")[-1].strip("/") + "\n")
    yaz(".nojekyll", "")
    print("Sayfalar yazıldı | görsel:", ", ".join(sorted(GORSEL)) or "yok", "|",
          "YAYINA HAZIR (index)" if YAYINDA else "TELEFON BEKLENIYOR - noindex")


if __name__ == "__main__":
    main()
