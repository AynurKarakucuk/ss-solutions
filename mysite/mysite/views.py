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

    return render(request, 'admin/sifre.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'yonetim/ana_sayfa.html')
            # return redirect('/yonetim')

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


""" 
Login bitiş
"""


def anasayfa(request):
    return render(request, 'anasayfa/base.html')


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

    context = {'solutions': solutions}

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

            return redirect('/yonetim/ekip/')

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

    context = {'onlinetakvim': onlinetakvim}

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

