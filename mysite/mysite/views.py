from django.views.generic import TemplateView
from django.views.generic.base import ContextMixin
from mysite.models import *
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
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
from datetime import datetime, time

from .models import Solutions, OnlineTakvim, OnlineRandevu, Ekip, Urun, Siparis, Menu, Form



class ViewMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(common_var='some common value', user=self.request.user)
        return context

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


@login_required
def menu_detay(request, pk: int):
    menu = Menu.objects.get(id=pk)

    context = {
        'menu': menu,
    }

    return render(request, 'yonetim/menu/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def menu_ekle(request, pk: int = None):
    menu = Menu.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.MenuForm(request.POST, request.FILES, instance=menu)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/menu/')

    else:

        f = forms.MenuForm(instance=menu)

    context = {
        'baslik': 'Menü Düzenle' if pk else 'Menü Ekle',
        'form': f,
    }

    return render(request, 'yonetim/menu/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def menu_liste(request):
    menu = Menu.objects.all()

    context = {'menu': menu}

    return render(request, 'yonetim/menu/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def menu_sil(request, pk: int):
    menu = Menu.objects.get(id=pk)

    if request.method == 'POST':
        menu.delete()

        return redirect('/yonetim/menu/')

    context = {
        'menu': menu,
    }

    return render(request, 'yonetim/menu/sil.html', context)


"""Ürünler"""


@login_required
def urun_detay(request, pk: int):
    urun = Urun.objects.get(id=pk)

    context = {
        'urun': urun,
    }

    return render(request, 'yonetim/urun/detay.html', context)


@login_required(login_url=settings.LOGIN_URL)
def urun_ekle(request, pk: int = None):
    urun = Urun.objects.get(id=pk) if pk else None
    if request.method == 'POST':
        f = forms.UrunForm(request.POST, request.FILES, instance=urun)

        if f.is_valid():
            f.save()

            return redirect('/yonetim/urun/')

    else:

        f = forms.UrunForm(instance=urun)

    context = {
        'baslik': 'Ürün Düzenle' if pk else 'Ürün Ekle',
        'form': f,
    }

    return render(request, 'yonetim/urun/duzenle.html', context)


@login_required(login_url=settings.LOGIN_URL)
def urun_liste(request):
    urun = Urun.objects.all()

    context = {'urun': urun}

    return render(request, 'yonetim/urun/liste.html', context)


@login_required(login_url=settings.LOGIN_URL)
def urun_sil(request, pk: int):
    urun = Urun.objects.get(id=pk)

    if request.method == 'POST':
        urun.delete()

        return redirect('/yonetim/urun/')

    context = {
        'urun': urun,
    }

    return render(request, 'yonetim/urun/sil.html', context)



""" WEB SAYFASI"""


def anasayfa_home(request):
    hizmetler = Solutions.objects.filter(altmenuadi="hizmetler", durum=True).order_by('sira')
    duyurular = Solutions.objects.filter(altmenuadi="duyurular", durum=True).order_by('sira')
    iletisim = Solutions.objects.filter(altmenuadi="iletisim").first()
    gizlilik = Solutions.objects.filter(altmenuadi="gizlilik").first()
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

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
        'menuler': menuler,
        'menuanasayfa': menuanasayfa,
        'title': "SS Solutions Coaching",
    }
    return render(request, 'anasayfa/anasayfa.html', context)


def menuicerik_goster(request, pk:int):
    menuicerik = Menu.objects.filter(id=pk, durum=True).first()
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    if menuicerik is None:
        context = {'baslik': "Güncelleniyor",
                   'menuicerik': menuicerik,
                   'menuler': menuler,
                   'menuanasayfa': menuanasayfa,
                   }

        return render(request, 'anasayfa/menuicerik.html', context)
    else:

        context = {
            'menuicerik': menuicerik,
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
        }
        return render(request, 'anasayfa/menuicerik.html', context)


def solutions_goster(request, baslik, pk: int):
    bilgi = Solutions.objects.filter(id=pk, durum=True).first()
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    if bilgi is None:
        context = {'baslik': "Güncelleniyor",
                   'bilgi': bilgi,
                   'menuler': menuler,
                   'menuanasayfa': menuanasayfa,
                   }

        return render(request, 'anasayfa/solutions_detay.html', context)
    else:

        context = {
            'bilgi': bilgi,
            'baslik': baslik,
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
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
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    if pk:
        bilgi = Solutions.objects.get(id=pk)
        context = {
            'bilgi': bilgi,
            'veri': "hizmet",
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
        }
        return render(request, 'anasayfa/solutions_detay.html', context)
    else:
        bilgi1 = Solutions.objects.filter(durum=True, altmenuadi="hizmetler")
        bilgi = bilgi1.order_by('sira')

        context = {
            'bilgi': bilgi,
            'baslik': "HİZMETLERİMİZ",
            'veri.id': bilgi[0].id,
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,

        }

        return render(request, 'anasayfa/solutions_liste.html', context)



def egitim_goster(request, pk: int):
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)
    bilgi = Solutions.objects.filter(altmenuadi="egitim", durum=True, sira=pk).first()
    context = {
            'bilgi': bilgi,
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
    }
    return render(request, 'anasayfa/solutions_detay.html', context)


def takvim_goster(request):
    bilgi1 = OnlineTakvim.objects.filter(durum=True)
    bilgi = bilgi1.order_by('tarih')
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    context = {
        'bilgi': bilgi,
        'baslik': "ONLİNE RANDEVU",
        'tarih.id': bilgi[0].id,
        'menuler': menuler,
        'menuanasayfa': menuanasayfa,
        'gunler': ['Pazar','Pazar2','Pazar3','Pazar2423']
    }
    return render(request, 'anasayfa/onlinerandevu.html', context)


def onlinerandevu_ekle(request, pk: int, saat: str):
    bilgi = OnlineTakvim.objects.get(id=pk)
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    context = {
        'bilgi': bilgi,
        'saat': saat,
        'baslik': "RANDEVU AL",
        'errors': '',
        'onlinetakvimid': bilgi.id,
        'menuler': menuler,
        'menuanasayfa': menuanasayfa,
    }

    if request.method == 'POST':
        f = forms.OnlineRandevuForm(request.POST, request.FILES)

        if f.is_valid():
            data = f.cleaned_data
            data.update({"tarih": bilgi.tarih.date()})
            o = OnlineRandevu(**data)
            o.save()

            for i in range(8):
                fname = "saat{}".format(i)
                print(fname, getattr(bilgi, fname))
                if saat in str(getattr(bilgi, fname)):
                    setattr(bilgi, fname, None)
                    bilgi.save()
                    print(getattr(bilgi, fname))
                    break

            # skarakucuk @ sssolutioncoaching.com

            subject, from_email, to = 'Randevunuz', 'aynur@karakucuk.net', '{eposta}'.format(eposta=o.eposta)
            text_content = "Sayın {ad}, {tarih} tarihinde saat: {saat} randevunuz alınmıştır.".format(ad=o.adisoyadi,
                                                                                                      tarih=o.tarih,
                                                                                                      saat=o.saat)
            # o.adisoyadi, 'adlı kişi', o.tarih, 'tarihinde saat', o.saat, 'randevu almıştır.', o.eposta, o.tel,
            # html_content = '<p>This is an <strong>important</strong> message.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            # msg.attach_alternative(html_content, "text/html")
            msg.send()

            # return redirect('/onlinedeneme/', adisoyadi=o.adisoyadi)
            # return redirect(reverse('/onlinedeneme/', kwargs={'adisoyadi': o.adisoyadi}))
            randevus = OnlineRandevu.objects.filter(adisoyadi=o.adisoyadi)

            context = {'randevus': randevus,
                       'menuler': menuler,
                       'menuanasayfa': menuanasayfa,
                       }

            return render(request, 'anasayfa/onlinebilgi.html', context)

        else:
            context.update({'errors': f.errors})

    return render(request, 'anasayfa/onlinerandevu_ekle.html', context)



""" Anasayfa Online Satış"""


def onlinesatis_list(request, pk: int = None):
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)
    if pk:
        urun = Urun.objects.get(id=pk)
        context = {
            'urun': urun,
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
        }
        return render(request, 'anasayfa/onlinesatis_detay.html', context)
    else:
        urun1 = Urun.objects.all()
        urun = urun1.order_by('urunfiyat')

        context = {
            'urun': urun,
            'baslik': "Eğitimlerimiz",
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
        }

        return render(request, 'anasayfa/onlinesatis.html', context)


""" Sipariş"""


@login_required(login_url=settings.LOGIN_URL)
def siparis_ekle(request, pk: int = None):
    urun = Urun.objects.get(id=pk) if pk else None
    errors = ''
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    if request.method == 'POST':
        f = forms.SiparisForm(request.POST, request.FILES)

        if f.is_valid():
            data = f.cleaned_data
            f.save()

            context = {

                'adsoyad': data.get("adsoyad"),
                'urun': urun,
                'menuler': menuler,
                'menuanasayfa': menuanasayfa,
            }

            return render(request, 'anasayfa/onlinesatis_satislist.html', context)

        errors = f.errors

    else:

        f = forms.SiparisForm()

    context = {
        # 'urunid': urun.id,
        'form': f,
        'urun': urun,
        'errors': errors,
        'menuler': menuler,
        'menuanasayfa': menuanasayfa,
    }

    return render(request, 'anasayfa/onlinesatis_satis.html', context)


def onlinesatis_satis(request, pk: int):
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)

    if pk:
        urun = Urun.objects.get(id=pk)
        siparis = Siparis.objects.all()

        context = {
            'urun': urun,
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
        }
        return render(request, 'anasayfa/onlinesatis_detay.html', context)
    else:
        urun1 = Urun.objects.all()
        urun = urun1.order_by('urunfiyat')

        context = {
            'urun': urun,
            'baslik': "Eğitimlerimiz",
            'menuler': menuler,
            'menuanasayfa': menuanasayfa,
        }

        return render(request, 'anasayfa/onlinesatis.html', context)


def form_post(request):
    formlar = Form.objects.all()
    menuler = Menu.objects.filter(durum=True).exclude(ustmenuadi="Anasayfa").order_by('sira')
    menuanasayfa = Menu.objects.filter(ustmenuadi="Anasayfa", durum=True)
    context = {'deneme': "deneme"}
    if request.method == 'POST':
        f = forms.FormForm(request.POST, request.FILES)
        if f.is_valid():
            data = f.cleaned_data
            data['olus_tarih'] = datetime.now()
            o = Form(**data)
            o.save()

            # skarakucuk @ sssolutioncoaching.com
            #f_id = Form.objects.get(id=o.id)
            subject, from_email, to = 'Başvuru Formu', 'aynur@karakucuk.net', '{eposta}'.format(eposta=o.eposta)
            text_content = "Adı Soyadı: {ad}, " \
                           "E-posta: {eposta}," \
                           "Telefon: {tel}," \
                           "Konu: {konu}," \
                           "Mesaj: {mesaj}," \
                           "Tarih: {tarih}".format(ad=o.adsoyad, eposta=o.eposta, tel=o.tel, konu=o.konu, mesaj=o.mesaj, tarih=o.olus_tarih)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.send()

            context = {'formlar': o,
                       'menuler': menuler,
                       'menuanasayfa': menuanasayfa,
                       }

            return render(request, 'anasayfa/form.html', context)

        else:
            context = {'errors': f.errors,
                       'f': f,
                      
                       }

    return render(request, 'anasayfa/deneme1.html', context)


