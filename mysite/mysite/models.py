from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget


class Solutions(models.Model):
    id = models.IntegerField(primary_key=True)
    altmenuadi = models.CharField(max_length=100, verbose_name='Menü Adi')
    baslik = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField(verbose_name="içerik", null=True, blank=True)
    img = models.ImageField(blank=True, null=True, )
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')
    dosya = models.FileField(blank=True, null=True, )
    sira = models.IntegerField(blank=True)


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
    saat = models.DateTimeField()
    durum = models.BooleanField(blank=True, null=True, verbose_name='Aktif')


class OnlineRandevu(models.Model):
    id = models.IntegerField(primary_key=True)
    onlinetakvimid = models.IntegerField()
    tarih = models.DateTimeField()
    saat = models.DateTimeField()
    adisoyadi = models.CharField(max_length=100, verbose_name='Adı Soyadı')
    eposta = models.EmailField()
    tel = models.IntegerField()



