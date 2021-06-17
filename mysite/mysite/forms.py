from __future__ import absolute_import

from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget
from datetimewidget.widgets import TimeWidget
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from datetime import datetime
import mysite.models

""" Solutions Form"""


class SolutionsForm(forms.ModelForm):
    icerik = RichTextUploadingFormField(
        # config_name="my-custom-toolbar",
        required=False,

    )
    altmenuadi = forms.ChoiceField(
        choices=[
            ("hakkimizda", "Hakkımızda"),
            ("sss", "Sıkça Sorulan Sorular"),
            ("duyurular", "Duyurular"),
            ("gizlilik", "Gizlilik Politikası"),
            ("iletisim", "Bize Ulaşın"),
            ("egitim", "Eğitimler"),
            ("blog", "Blog"),
            ("kocluk", "Koçluk"),
            ("hizmetler", "Hizmetlerimiz"),

        ],

    )

    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = mysite.models.Solutions
        fields = ['altmenuadi', 'baslik', 'icerik', 'aciklama', 'durum', 'dosya', 'img', 'sira']


""" Ekip Form"""


class EkipForm(forms.ModelForm):
    icerik = RichTextUploadingFormField(
        # config_name="my-custom-toolbar",
        label="Öz Geçmiş",
        required=False,

    )

    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = mysite.models.Ekip
        fields = ['adisoyadi', 'unvan', 'tel', 'eposta', 'img', 'icerik', 'dosya', 'sira', 'durum']


"""Online Takvim"""


class OnlineTakvimForm(forms.ModelForm):
    durum = forms.BooleanField(required=False, label="Aktif")

    class Meta:
        model = mysite.models.OnlineTakvim
        fields = ['tarih', 'saat0', 'saat1', 'saat2', 'saat3', 'saat4', 'saat5', 'saat6', 'saat7', 'durum']
        ordering = ['tarih']
        dateDateOptions = {
            'format': 'dd/mm/yyyy HH:ii',
            'autoclose': True,
            'showMeridian': True
        }
        dateTimeOptions = {
            'format': 'HH:ii:ss P',
            'autoclose': True,
            'showMeridian': True
        }

        widgets = {
            'tarih': DateWidget(options=dateDateOptions, usel10n=True, bootstrap_version=3),
            'saat0': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat1': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat2': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat3': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat4': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat5': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat6': TimeWidget(usel10n=True, bootstrap_version=3),
            'saat7': TimeWidget(usel10n=True, bootstrap_version=3),
        }


class OnlineRandevuForm(forms.ModelForm):
    tarih = forms.CharField(required=False)
    saat = forms.CharField(required=False)

    class Meta:
        model = mysite.models.OnlineRandevu
        fields = ['tarih', 'saat', 'adisoyadi', 'eposta', 'tel', 'onlinetakvimid']

    def clean_tarih(self):
        return ""

    # def validate(self, value):
    #     for tarih in value:
    #         return []
    #     super().validate(value)


""" Şifre İşlemleri """


class YoneticiForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class YoneticiSifreForms(PasswordChangeForm):
    pass
    # class Meta:
    #     model = User
    #     fields = ()


class AdminSifreResetForms(SetPasswordForm):
    pass


""" URUN FORMS"""


class UrunForm(forms.ModelForm):
    aciklama = RichTextUploadingFormField(
        # config_name="my-custom-toolbar",
        label="Tanıtım",
        required=False,

    )

    class Meta:
        model = mysite.models.Urun
        fields = ['urunadi', 'urunfiyat', 'aciklama', 'img']


""" Satış Form"""


class SiparisForm(forms.ModelForm):
    urunid = forms.IntegerField(required=False)

    class Meta:
        model = mysite.models.Siparis
        fields = ['adsoyad', 'tel', 'eposta', 'adres', 'urunid', 'kkno', 'kkad', 'kksonkt', 'kkcvv']


class MenuForm(forms.ModelForm):
    editor = RichTextUploadingFormField(
        # config_name="my-custom-toolbar",
        label="Editör",
        required=False,

    )
    menuler = mysite.models.Menu.objects.all()

    ustmenuadi = forms.ChoiceField(
        choices=[
            # ("anasayfa", "Anasayfa"),
            ("{id}".format(id=menu.menuadi), menu.menuadi) for menu in menuler
        ],
    )

    class Meta:
        model = mysite.models.Menu
        fields = ['menuadi', 'ustmenuadi', 'editor', 'dosya', 'sira', 'durum']


class FormForm(forms.ModelForm):
    olus_tarih = forms.DateTimeField(required=False)

    class Meta:
        model = mysite.models.Form
        fields = ['adsoyad', 'tel', 'eposta', 'konu', 'mesaj', 'olus_tarih']


class YorumForm(forms.ModelForm):
    olus_tarih = forms.DateTimeField(required=False)
    konu = forms.CharField(required=False)
    class Meta:
        model = mysite.models.Yorum
        fields = ['adsoyad', 'eposta', 'konu', 'mesaj', 'olus_tarih', 'onay', 'durum']
