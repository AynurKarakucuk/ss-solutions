from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from phonenumber_field.modelfields import PhoneNumberField


class Solutions(models.Model):
    id = models.IntegerField(primary_key=True)
    altmenuadi = models.CharField(max_length=100, verbose_name='Menü Adi')
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    img = models.ImageField(blank=True, null=True, )
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )
    sira = models.PositiveSmallIntegerField(blank=True)
    aciklama=models.CharField(max_length=500, verbose_name='Açıklama', blank=True)


# class Egitim(models.Model):
#     id = models.IntegerField(primary_key=True)
#     altmenuadi = models.CharField(max_length=100, verbose_name='Menü Adi')
#     baslik = models.CharField(max_length=100, verbose_name='Başlık')
#     icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
#     img = models.ImageField(blank=True, null=True, )
#     durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
#     dosya = models.FileField(blank=True, null=True, )
#     sira = models.IntegerField(blank=True)


class Ekip(models.Model):
    id = models.IntegerField(primary_key=True)
    adisoyadi = models.CharField(max_length=100, verbose_name='Adı Soyadı')
    unvan = models.CharField(max_length=100, verbose_name='Ünvan')
    icerik = RichTextField(verbose_name="Öz Geçmiş", null=True, blank=True)
    img = models.ImageField(blank=True, null=True, verbose_name='Resim')
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )
    sira = models.IntegerField(blank=True, verbose_name='Sıra')
    tel = models.CharField(max_length=100, verbose_name='Telefon')
    eposta = models.EmailField(verbose_name='e-posta')

#
# class Blog(models.Model):
#     id = models.IntegerField(primary_key=True)
#     blogad = models.CharField(max_length=100, verbose_name='Menü Adi')
#     baslik = models.CharField(max_length=100, verbose_name='Başlık')
#     icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
#     img = models.ImageField(blank=True, null=True, )
#     durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
#     dosya = models.FileField(blank=True, null=True, )
#     sira = models.IntegerField(blank=True)


class OnlineTakvim(models.Model):
    id = models.IntegerField(primary_key=True)
    tarih = models.DateTimeField()

    saat0 = models.TimeField(blank=True, null=True, unique=False, verbose_name='1. Saat ')
    saat1 = models.TimeField(blank=True, null=True, verbose_name='2. Saat ')
    saat2 = models.TimeField(blank=True, null=True, verbose_name='3. Saat ')
    saat3 = models.TimeField(blank=True, null=True, verbose_name='4. Saat ')
    saat4 = models.TimeField(blank=True, null=True, verbose_name='5. Saat ')
    saat5 = models.TimeField(blank=True, null=True, verbose_name='6. Saat ')
    saat6 = models.TimeField(blank=True, null=True, verbose_name='7. Saat ')
    saat7 = models.TimeField(blank=True, null=True, verbose_name='8. Saat ')
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')

    class Meta:
        ordering = ['tarih']


class OnlineRandevu(models.Model):
    id = models.IntegerField(primary_key=True)
    onlinetakvimid = models.IntegerField()
    tarih = models.DateTimeField()
    saat = models.TimeField()
    adisoyadi = models.CharField(max_length=100, verbose_name='Adı Soyadı')
    eposta = models.EmailField(verbose_name='e-posta')
    tel = models.IntegerField(verbose_name='Telefon')

class Urun(models.Model):
    id=models.IntegerField(primary_key=True)
    urunadi=models.CharField(max_length=100, verbose_name='Ürün Adı')
    urunfiyat=models.CharField(max_length=100, verbose_name='Ürün Fiyatı')
    aciklama=RichTextField(verbose_name="Tanıtım", null=True, blank=True)
    img = models.ImageField(blank=True, null=True, )

class Siparis(models.Model):
    adsoyad=models.CharField(max_length=100, verbose_name='Adı Soyadı')
    tel=models.IntegerField(verbose_name='Telefon')
    eposta = models.EmailField(verbose_name='E Posta')
    adres = models.CharField(max_length=500, verbose_name='Adres')
    urunid= models.IntegerField()
    kkno = models.CharField(max_length=100, verbose_name='Kredi Kartı Numarası')
    kkad = models.CharField(max_length=100, verbose_name='Kredi Kartı Üzerinde ki Ad Soyad')
    kksonkt = models.CharField(max_length=100, verbose_name='Son Kullanma Tarihi')
    kkcvv = models.IntegerField(verbose_name='Güvenlik Kodu')

class Menu(models.Model):
    menuadi = models.CharField(max_length=100, verbose_name='Menu Adi')
    ustmenuadi = models.CharField(max_length=100, verbose_name='Bağlantı Yapılacak Menü Adı', blank=True, null=True)
    editor = RichTextField(verbose_name="Sayfa İçeriği", null=True, blank=True)
    sira = models.IntegerField(verbose_name="Alt Menu Sırası", null=True, blank=True)
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )


class Form(models.Model):
    formNo = models.IntegerField(verbose_name="Sıra Numarası", null=True, blank=True)
    adsoyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    eposta = models.EmailField()
    tel = models.CharField(max_length=100, verbose_name="Telefon Numarası")
    konu = models.CharField(max_length=100, verbose_name="Konu")
    mesaj = models.CharField(max_length=100, verbose_name="Mesaj")
    olus_tarih = models.DateTimeField()


class Yorum(models.Model):
    adsoyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    eposta = models.EmailField()
    tel = models.CharField(max_length=100, verbose_name="Telefon Numarası")
    konu = models.CharField(max_length=100, verbose_name="Konu")
    mesaj = models.CharField(max_length=100, verbose_name="Mesaj")
    olus_tarih = models.DateTimeField()
    durum = models.BooleanField(blank=True, null=True, verbose_name='Durum')
    onay = models.BooleanField(blank=True, null=True, verbose_name='Onay')


