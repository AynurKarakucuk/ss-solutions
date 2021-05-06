from mysite.models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.db import models
from django.template import RequestContext

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.conf import settings

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.urls import reverse
from django.views import generic
from . import forms
from datetime import datetime

from .models import Solutions, OnlineTakvim, OnlineRandevu

"""
Yönetim Sayfaları başlangıç
"""
""" 
Login
"""


@login_required()
def sifre_view(request):
    if request.method == "POST":
        f = forms.YoneticiSifreForms(request.user, request.POST)
        if f.is_valid():
            f.save()

            return redirect('/yonetim/')
    else:
        f = forms.YoneticiSifreForms(request.user)

    context = {
        'baslik': 'MENU DÜZENLE',
        'form': f,
    }

    return render(request, 'yonetim/sifre.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'yonetim/ana_sayfa.html')


    context = {
        "hata": True if request.POST else False,
    }

    return render(request, 'yonetim/login.html', context)


@login_required
def admin_giris(request):
    return render(request, 'anasayfa/base.html')


def logout_view(request):
    logout(request)

    return redirect('/login')


def yetki_yok(request):
    return render(request, 'yonetim/hata.html')


""" 
Login bitiş
"""




"""
solutions
"""


@login_required
def solutions_detay(request, pk: int):
    solutions = Solutions.objects.get(id=pk)

    context = {
        'solutions': solutions,
    }

    return render(request, 'yonetim/solutions/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def solutions_ekle(request, pk: int = None):
    solutions = Solutions.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.SolutionsForm(request.POST, request.FILES, instance=solutions)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/solutions/')

    else:

        f = forms.SolutionsForm(instance=solutions)

    context = {
        'baslik': 'ALT MENU DÜZENLE' if pk else 'ALT MENU EKLE',
        'form': f,
    }

    return render(request, 'yonetim/solutions/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def solutions_liste(request):
    solutions = Solutions.objects.all()
    blog = Solutions.objects.filter(altmenuadi__in=['blog', 'kocluk', 'sss', 'hakkimizda', 'iletisim', 'gizlilik'])
    duyurular = Solutions.objects.filter(altmenuadi='duyurular')
    hizmetler = Solutions.objects.filter(altmenuadi="hizmetler")
    egitim = Solutions.objects.filter(altmenuadi="egitim")

    context = {'solutions': solutions,
               'egitim': egitim,
               'blog': blog,
               'duyurular': duyurular,
               'hizmetler': hizmetler,

               }

    return render(request, 'yonetim/solutions/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def solutions_sil(request, pk: int):
    solutions = Solutions.objects.get(id=pk)

    if request.method == 'POST':
        solutions.delete()

        return redirect('/yonetim/solutions/')

    context = {
        'solutions': solutions,
    }

    return render(request, 'yonetim/solutions/sil.html', context)


"""
solutions Son
"""


"""
ekip başlangıç
"""


@login_required
def ekip_detay(request, pk: int):
    ekip = Ekip.objects.get(id=pk)

    context = {
        'ekip': ekip,
    }

    return render(request, 'yonetim/ekip/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def ekip_ekle(request, pk: int = None):
    ekip = Ekip.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.EkipForm(request.POST, request.FILES, instance=ekip)

        if f.is_valid():
            f.save()

            return redirect('yonetim/ekip/')

    else:

        f = forms.EkipForm(instance=ekip)

    context = {
        'baslik': 'Ekip Düzenle' if pk else 'Ekip Ekle',
        'form': f,
    }

    return render(request, 'yonetim/ekip/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def ekip_liste(request):
    ekip = Ekip.objects.all()

    context = {'ekip': ekip}

    return render(request, 'yonetim/ekip/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def ekip_sil(request, pk: int):
    ekip = Ekip.objects.get(id=pk)

    if request.method == 'POST':
        ekip.delete()

        return redirect('/yonetim/ekip/')

    context = {
        'ekip': ekip,
    }

    return render(request, 'yonetim/ekip/sil.html', context)


"""
online takvim başlangıç
"""


@login_required
def onlinetakvim_detay(request, pk: int):
    onlinetakvim = OnlineTakvim.objects.get(id=pk)

    context = {
        'onlinetakvim': onlinetakvim,
    }

    return render(request, 'yonetim/online/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def onlinetakvim_ekle(request, pk: int = None):
    onlinetakvim = OnlineTakvim.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.OnlineTakvimForm(request.POST, request.FILES, instance=onlinetakvim)

        if f.is_valid():
            f.save()
            return redirect('/yonetim/onlinetakvim/')
    else:
        f = forms.OnlineTakvimForm(instance=onlinetakvim)

    context = {
        'baslik': 'Online Takvim Düzenle' if pk else 'Online Takvim Ekle',
        'form': f,
    }

    return render(request, 'yonetim/online/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def onlinetakvim_liste(request):
    onlinetakvim = OnlineTakvim.objects.all()

    context = {
                'onlinetakvim': onlinetakvim,
               }

    return render(request, 'yonetim/online/liste.html', context)



@login_required(login_url=settings.LOGIN_URL)
def onlinetakvim_sil(request, pk: int):
    onlinetakvim = OnlineTakvim.objects.get(id=pk)

    if request.method == 'POST':
        onlinetakvim.delete()

        return redirect('/yonetim/onlinetakvim/')

    context = {
        'onlinetakvim': onlinetakvim,
    }

    return render(request, 'yonetim/online/sil.html', context)

""" KULLANICILAR VİEWS"""


@login_required
def kullanici_detay(request, pk: int):
    kullanici = User.objects.get(id=pk)

    context = {
        'kullanici': kullanici,
    }

    return render(request, 'yonetim/kullanici/duzenle.html', context)


def kullanici_kayit(request, pk: int = None):
    kullanici = User.objects.get(id=pk) if pk else None
    if request.method == "POST":
        f = forms.YoneticiForms(request.POST)
        if f.is_valid():
            f.save()

            return redirect('/yonetim/kullanici/')
    else:

        f = forms.YoneticiForms(instance=kullanici)

    context = {
        'baslik': 'KULLANICI DÜZENLE' if pk else 'KULLANICI EKLE',
        'form': f,
    }

    return render(request, 'yonetim/kullanici/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
@user_passes_test(lambda u: u.is_superuser, login_url=settings.YETKI_HATA_URL, redirect_field_name='')
def kullanici_liste(request):
    # xdkfldkjdkjkdjgkj
    kullanici = User.objects.all()

    context = {'kullanici': kullanici}

    return render(request, 'yonetim/kullanici/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def kullanici_sil(request, pk: int):
    kullanici = User.objects.get(id=pk)

    if request.method == 'POST':
        kullanici.delete()

        return redirect('/yonetim/kullanici/')

    context = {
        'kullanici': kullanici,
    }

    return render(request, 'yonetim/kullanici/sil.html', context)


""" WEB SAYFASI"""


def anasayfa_home(request):

    hizmetler = Solutions.objects.filter(altmenuadi="hizmetler", durum=True).order_by('sira')
    duyurular = Solutions.objects.filter(altmenuadi="duyurular", durum=True).order_by('sira')
    iletisim = Solutions.objects.filter(altmenuadi="iletisim").first()
    gizlilik = Solutions.objects.filter(altmenuadi="gizlilik").first()

    ds = []
    i = 0
    for d in duyurular:
        _d = d.__dict__
        _d.update({"active": i == 0, "sira": str(i)})
        ds.append(_d)
        i += 1

    context = {
        'hizmetler': hizmetler,
        'duyurular': ds,
        'iletisim': iletisim,
        'gizlilik': gizlilik,
    }
    return render(request, 'anasayfa/anasayfa.html', context)

def solutions_goster(request, baslik, pk: int):
    bilgi = Solutions.objects.filter(id=pk, durum=True).first()

    if bilgi is None:
        context = {'baslik': "Güncelleniyor",
                   'bilgi': bilgi,
                   }

        return render(request, 'anasayfa/solutions_detay.html', context)
    else:

        context = {
            'bilgi': bilgi,
            'baslik': baslik,
            # 'post.title': alan,
        }
        return render(request, 'anasayfa/solutions_detay.html', context)

def iletisim(request):
    bilgi = Solutions.objects.filter(altmenuadi="iletisim").first()
    return solutions_goster(request, "İLETİŞİM", bilgi.id)

def hakkimizda(request):
    bilgi = Solutions.objects.filter(altmenuadi="hakkimizda").first()
    return solutions_goster(request, "HAKKIMIZDA", bilgi.id)

def sss(request):
    bilgi = Solutions.objects.filter(altmenuadi="sss").first()
    return solutions_goster(request, "SIKÇA SORULAN SORULAR", bilgi.id)

def gizlilik(request):
    bilgi = Solutions.objects.filter(altmenuadi="gizlilik").first()
    return solutions_goster(request, "GİZLİLİK POLİTİKASI", bilgi.id)

def blog(request):
    bilgi = Solutions.objects.filter(altmenuadi="blog").first()
    return solutions_goster(request, "BLOG", bilgi.id)

def koc(request):
    bilgi = Solutions.objects.filter(altmenuadi="kocluk").first()
    return solutions_goster(request, "KOÇLUK", bilgi.id)

def hizmet_goster(request, pk: int = None):
    if pk:
        bilgi = Solutions.objects.get(id=pk)
        context = {
            'bilgi': bilgi,
            'veri': "hizmet",
        }
        return render(request, 'anasayfa/solutions_detay.html', context)
    else:
        bilgi1 = Solutions.objects.filter(durum=True, altmenuadi="hizmetler")
        bilgi = bilgi1.order_by('sira')

        context = {
            'bilgi': bilgi,
            'baslik': "HİZMETLERİMİZ",
            'veri.id': bilgi[0].id,

        }

        return render(request, 'anasayfa/solutions_liste.html', context)

def takvim_goster(request, pk: int = None):
    if pk:
        bilgi = OnlineTakvim.objects.get(id=pk)
        kisi = OnlineRandevu.objects.all()
        context = {
            'bilgi': bilgi,
            'kisi' : kisi,
            'baslik': "ONLİNE RANDEVU AL",
        }
        return render(request, 'anasayfa/onlinerandevu_ekle.html', context)
    else:
        bilgi1 = OnlineTakvim.objects.filter(durum=True)
        bilgi = bilgi1.order_by('tarih')
        context = {
            'bilgi': bilgi,
            'baslik': "ONLİNE RANDEVU",
            'tarih.id': bilgi[0].id,
        }
        return render(request, 'anasayfa/onlinerandevu.html', context)

