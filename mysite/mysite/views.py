# from ckeditor.widgets import CKEditorWidget
# from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin
# from django.core.exceptions import PermissionDenied
from django.shortcuts import render
# from django.db import models
# from django.template import RequestContext



from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
# from django.conf import settings

from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import logout
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator

# from django.urls import reverse
# from django.views import generic
# from . import forms



"""
Admin Sayfaları başlangıç
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


