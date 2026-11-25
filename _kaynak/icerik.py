# -*- coding: utf-8 -*-
"""Genel Servis Kaydı — tüm ayarlar ve metinler.
Kurallar (Google Ads "kabul edilemez iş uygulamaları" / yanıltıcı beyan):
  * Hiçbir marka adı ve logosu yazılmaz/gösterilmez; "yetkili", "resmi", "orijinal" denmez.
  * "Bağımsız özel servis, hiçbir markanın yetkili servisi değildir" açıklaması sayfanın en altında görünür.
  * Doğrulanmamış iddia (yıl, garanti süresi, dakika, fiyat, yorum, puan, ekip sayısı) yazılmaz.
  * Ücret işlem öncesi bildirilir; onay olmadan işlem yapılmaz.
"""

# ---------------- AYARLAR (yalnız burayı doldurun) ----------------
FIRMA = "Genel Servis Kaydı"
ALAN = "https://genelserviskaydi.net.tr"
TEL = ""            # örn. "0532 123 45 67" — boşken site noindex ve yer tutucu numara
WHATSAPP = ""       # boşsa TEL kullanılır
UNVAN = ""          # resmi ticari unvan (varsa; Ads doğrulaması için önerilir)
ADRES = ""          # açık adres (varsa)
SAAT = "Hafta içi ve hafta sonu, randevu ile"
EPOSTA = ""
GTM = ""            # örn. "GTM-XXXXXXX"
# ------------------------------------------------------------------

TITLE = "Beyaz Eşya, Kombi ve Klima Servis Kaydı | " + FIRMA
DESC = ("Buzdolabı, çamaşır makinesi, bulaşık makinesi, fırın, kombi ve klima için servis kaydı oluşturun. "
        "Adreste arıza tespiti, ücret işlemden önce, onayınız olmadan işlem yok. Bağımsız özel teknik servis.")

# hizmetler (ikon, başlık, metin, görsel dosya adı)
CIHAZLAR = [
    ("buzdolabi", "Buzdolabı", "Soğutma kaybı, karlanma, su sızıntısı, fan ve termostat arızaları.", "buzdolabi"),
    ("camasir", "Çamaşır Makinesi", "Su boşaltmama, sıkmama, kapak kilidi, titreşim ve hata uyarıları.", "camasir"),
    ("bulasik", "Bulaşık Makinesi", "Temiz yıkamama, su almama, kurutmama ve pompa arızaları.", "bulasik"),
    ("firin", "Fırın ve Ocak", "Isınmama, rezistans, termostat, fan ve ocak gözü arızaları.", "firin"),
    ("kombi", "Kombi", "Sıcak su sorunu, basınç düşmesi, arıza kodları ve periyodik bakım.", "kombi"),
    ("klima", "Klima", "Soğutmama, su damlatma, koku, ses ve mevsimlik bakım.", "klima"),
]

# kurumsal yapı: bir servis kaydının geçtiği birimler
YAPI = [
    ("belge", "Kayıt birimi", "Telefon, WhatsApp veya form ile gelen her talep cihaz, arıza ve adres bilgisiyle kayda alınır."),
    ("saat", "Planlama", "Kayıt, size uygun gün ve saate göre teknik ekibin programına yerleştirilir."),
    ("anahtar", "Teknik ekip", "Teknisyen adreste cihazı inceler, arızayı ve yapılacak işlemi açıklar."),
    ("onay", "Kontrol ve kapanış", "Onarım sonrası cihaz yanınızda test edilir; kayıt yapılan işlem ve ücretle kapatılır."),
]

# servis kaydı adımları
ADIMLAR = [
    ("Kaydınızı oluşturun", "Arayın, WhatsApp'tan yazın ya da formu doldurun."),
    ("Randevu belirlenir", "Uygun gün ve saat sizinle birlikte planlanır."),
    ("Adreste tespit ve ücret", "Arıza açıklanır, ücret işlemden önce söylenir."),
    ("Onarım ve test", "Onayınızla onarılır, çalışır halde teslim edilir."),
]

# taahhütler (şeffaflık; politika uyumu)
ILKELER = [
    ("bagimsiz", "Bağımsız özel servis", "Hiçbir üretici markanın yetkili servisi, bayisi veya çağrı merkezi değiliz. Garanti kapsamındaki cihazlar için üreticinin yetkili servisine başvurmanızı öneririz."),
    ("ucret", "Ücretlendirme", "Arıza tespitinden sonra ücret açıkça bildirilir. Onayınız olmadan işlem yapılmaz."),
    ("parca", "Parça bilgisi", "Değişecek parçanın ne olduğunu ve neden değiştiğini anlatırız; çıkan parça isterseniz size bırakılır."),
    ("belge", "Yazılı kayıt", "Yapılan işlem ve ödenen ücret için isteğinize göre yazılı servis formu düzenlenir."),
]

# arıza rehberi
BELIRTILER = [
    ("Buzdolabı soğutmuyor", "Kapağın tam kapandığını ve arkada hava boşluğu olduğunu kontrol edin. Düzelmezse kapağı az açın ve servis kaydı oluşturun."),
    ("Çamaşır makinesi su boşaltmıyor", "Programı durdurun, kapağı zorlamayın. Pompa filtresi tıkanmış olabilir; emin değilseniz müdahale etmeyin."),
    ("Bulaşık makinesi temiz yıkamıyor", "Alt filtreyi ve pervane deliklerini kontrol edin. Sorun sürüyorsa su alma veya ısıtma kaynaklı olabilir."),
    ("Kombi basıncı düşüyor", "Basıncı kılavuzdaki değere getirin. Sık tekrar ediyorsa kaçak olabilir; teknik kontrol gerekir."),
    ("Klimadan su damlıyor", "Cihazı kapatıp prizden çekin. Tahliye hattı tıkanmış veya filtre kirlenmiş olabilir."),
    ("Fırın ısınmıyor", "Sigortayı ve ayarı kontrol edin. Rezistans veya termostat arızasında elektrikli parçalara dokunmayın."),
]

SSS = [
    ("Servis kaydı nasıl oluşturulur?", "Telefonla arayabilir, WhatsApp'tan yazabilir ya da sayfadaki formu doldurabilirsiniz. Form mesajınızı WhatsApp'ta hazır açar, siz yalnızca gönderirsiniz."),
    ("Hangi cihazlara bakıyorsunuz?", "Buzdolabı, çamaşır makinesi, bulaşık makinesi, fırın ve ocak gibi beyaz eşyalar ile kombi ve klimalara arıza, bakım ve onarım hizmeti veriyoruz."),
    ("Ücreti ne zaman öğrenirim?", "Arıza tespitinden sonra, işleme başlamadan önce. Onay vermezseniz işlem yapılmaz."),
    ("Hafta sonu randevu veriyor musunuz?", "Evet, hafta içi ve hafta sonu randevu ile adreste servis veriyoruz."),
    ("Kişisel bilgilerim nasıl kullanılıyor?", "Paylaştığınız ad, telefon ve adres yalnızca servis kaydınız için kullanılır. Ayrıntılar Gizlilik ve KVKK sayfamızdadır."),
]
