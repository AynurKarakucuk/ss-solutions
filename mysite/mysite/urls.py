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
            #ANASAYFA
            path('admin/', admin.site.urls),
            path('', views.anasayfa_home),

            path('onlinerandevu/<int:pk>/<str:saat>', views.onlinerandevu_ekle),
            path('onlinebilgi/', views.onlinerandevu_ekle),
            path('onlinesatis/', views.onlinesatis_list),
            path('onlinesatis/<int:pk>/', views.onlinesatis_list),
            path('onlinesatis_satis/<int:pk>/', views.siparis_ekle),
            path('onlinerandevu/', views.takvim_goster),
            path('form/', views.form_post),
            path('yorum/<int:pk>/', views.yorum_post),

            #SOLUTİONS
            path('hakkimizda/', views.hakkimizda),
            path('sss/', views.sss),
            path('gizlilik/', views.gizlilik),
            path('iletisim/', views.iletisim),
            path('koc/', views.koc),
            path('blog/', views.blog_goster),
            path('blog/<int:pk>/', views.blog_goster),
            path('hizmetler/<int:pk>/', views.hizmet_goster),
            path('hizmetler/', views.hizmet_goster),
            path('duyurular/<int:pk>', views.duyuru),
            path('duyurular/', views.duyuru),
            path('egitim/<int:pk>/', views.egitim_goster),


            # ADMIN GİRİŞ
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

            # URUN
            path('yonetim/urun/', views.urun_liste),
            path('yonetim/urun/<int:pk>/', views.urun_detay),
            path('yonetim/urun/duzenle', views.urun_ekle),
            path('yonetim/urun/duzenle/<int:pk>/', views.urun_ekle),
            path('yonetim/urun/sil/<int:pk>/', views.urun_sil),
            path('yonetim/urun/detay/<int:pk>/', views.urun_detay),

            #MENU
            path('yonetim/menu/', views.menu_liste),
            path('yonetim/menu/<int:pk>/', views.menu_detay),
            path('yonetim/menu/duzenle', views.menu_ekle),
            path('yonetim/menu/duzenle/<int:pk>/', views.menu_ekle),
            path('yonetim/menu/sil/<int:pk>/', views.menu_sil),
            path('yonetim/menu/detay/<int:pk>/', views.menu_detay),

            # Form
            path('yonetim/form/', views.form_liste),
            path('yonetim/form/<int:pk>/', views.form_detay),
            path('yonetim/form/sil/<int:pk>/', views.form_sil),
            path('yonetim/form/detay/<int:pk>/', views.form_detay),

            # Yorum
            path('yonetim/yorum/', views.yorum_liste),
            path('yonetim/yorum/sil/<int:pk>/', views.yorum_sil),
            path('yonetim/yorum/duzenle/<int:pk>/', views.yorum_duzenle),

            # ckeditor
            path('ckeditor/', include('ckeditor_uploader.urls')),
        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)
