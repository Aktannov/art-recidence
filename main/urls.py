from django.urls import path

from . import views

urlpatterns = [
    path('', views.view),
    path('info', views.info),
    path('inffo', views.inffo),
    path('test', views.test),
    path('vet', views.vet),
    path('kart', views.kart),
    path('kino', views.kino),
    path('pict', views.pict),
    path('disc', views.disc),
    path('chedo', views.chedo),
    path('stoi', views.stoi),
    path('velo', views.velo),
    path('leo', views.leo),
    path('kmn', views.kmn),
    path('ben', views.ben),
    path('lev', views.lev),
    path('tay', views.tay),
    path('kmr', views.kmr),
    path('dvr', views.dvr),
    path('kvr', views.kvr),
    path('selk', views.selkin),
    path('bat', views.batink),
    path('ang', views.ang),
    path('moto', views.moto),
    path('uli', views.uli),
]
