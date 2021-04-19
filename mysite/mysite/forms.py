from __future__ import absolute_import

from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms
from datetimewidget.widgets import DateTimeWidget
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
        fields = ['altmenuadi', 'baslik', 'icerik', 'durum', 'dosya', 'img', 'sira']


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
        fields = ['tarih', 'saat', 'durum']
        ordering = ['tarih']
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii',
            'autoclose': True,
            'showMeridian': True
        }

        widgets = {
            'tarih': DateTimeWidget(options=dateTimeOptions, usel10n=True, bootstrap_version=3),
            'saat':  DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True, bootstrap_version=3),
        }


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
