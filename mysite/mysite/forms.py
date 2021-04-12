from __future__ import absolute_import

from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms
from datetimewidget.widgets import DateTimeWidget
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
            ("egitim", "Kurumsal Eğitimler"),
            ("blog", "Blog"),

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

        widgets = {
            'tarih': DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True, bootstrap_version=3),
            'saat':  DateTimeWidget(attrs={'id': "yourdatetimeid"}, usel10n=True, bootstrap_version=3)
        }


