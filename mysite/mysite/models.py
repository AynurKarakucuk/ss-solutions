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
    aciklama=models.CharField(max_length=150, verbose_name='Açıklama', blank=True)


class Egitim(models.Model):
    id = models.IntegerField(primary_key=True)
    altmenuadi = models.CharField(max_length=100, verbose_name='Menü Adi')
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    img = models.ImageField(blank=True, null=True, )
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )
    sira = models.IntegerField(blank=True)


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


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    blogad = models.CharField(max_length=100, verbose_name='Menü Adi')
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    img = models.ImageField(blank=True, null=True, )
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )
    sira = models.IntegerField(blank=True)


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
