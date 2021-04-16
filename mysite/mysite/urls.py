"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from mysite import views

urlpatterns = (
        [

            path('admin/', admin.site.urls),
            path('', views.login_view),

            # ADMİN GİRİŞ
            path('login/', views.login_view),
            path('logout/', views.logout_view),

            # YÖNETİM GİRİŞ
            path('yonetim/', views.admin_giris),
            path('sifre/', views.sifre_view),
            path('hata_yetki/', views.yetki_yok),

            # Solutions
            path('yonetim/solutions/', views.solutions_liste),
            path('yonetim/solutions/<int:pk>/', views.solutions_detay),
            path('yonetim/solutions/duzenle', views.solutions_ekle),
            path('yonetim/solutions/duzenle/<int:pk>/', views.solutions_ekle),
            path('yonetim/solutions/sil/<int:pk>/', views.solutions_sil),
            path('yonetim/solutions/detay/<int:pk>/', views.solutions_detay),

            # Ekip
            path('yonetim/ekip/', views.ekip_liste),
            path('yonetim/ekip/<int:pk>/', views.ekip_detay),
            path('yonetim/ekip/duzenle', views.ekip_ekle),
            path('yonetim/ekip/duzenle/<int:pk>/', views.ekip_ekle),
            path('yonetim/ekip/sil/<int:pk>/', views.ekip_sil),
            path('yonetim/ekip/detay/<int:pk>/', views.ekip_detay),

            #OnlineTakvim
            path('yonetim/onlinetakvim/', views.onlinetakvim_liste),
          #  path('yonetim/onlinetakvim/<int:pk>/', views.onlinetakvim_detay),
            path('yonetim/onlinetakvim/duzenle', views.onlinetakvim_ekle),
            path('yonetim/onlinetakvim/duzenle/<int:pk>/', views.onlinetakvim_ekle),
            path('yonetim/onlinetakvim/sil/<int:pk>/', views.onlinetakvim_sil),
           # path('yonetim/onlinetakvim/detay/<int:pk>/', views.onlinetakvim_detay),

            # """ Kullanıcılar """
            path('yonetim/kullanici/', views.kullanici_liste),
            path('yonetim/kullanici/<int:pk>/', views.kullanici_detay),
            path('yonetim/kullanici/duzenle', views.kullanici_kayit),
            path('yonetim/kullanici/duzenle/<int:pk>/', views.kullanici_kayit),
            path('yonetim/kullanici/sil/<int:pk>/', views.kullanici_sil),
            path('yonetim/kullanici/detay/<int:pk>/', views.kullanici_detay),

            # ckeditor
            path('ckeditor/', include('ckeditor_uploader.urls')),
        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)
