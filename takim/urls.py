from django.urls import path
from .views import base,takim_list,takim_ekle,takim_guncelle,sporcu_list,sporcu_ekle,sporcu_guncelle,antrenman_list,antrenman_ekle,antrenman_guncelle,haftalik_antrenman,antrenman_yap
from .views import gunluk_ekle,htmx_sporcu_ekle,yaris_list,sporcu_detail

urlpatterns = [
    path('',base,name='takim'),
    path('takimlar/',takim_list,name='takim_list'),
    path('takim_ekle/',takim_ekle,name='takim_ekle'),
    path('takim_guncelle/<int:id>/',takim_guncelle,name='takim_guncelle'),
    path('sporcular/',sporcu_list,name='sporcu_list'),
    path('sporcu_ekle/',sporcu_ekle,name='sporcu_ekle'),
    path('sporcu_guncelle/<int:id>/',sporcu_guncelle,name='sporcu_guncelle'),
    path('antrenman/',antrenman_list,name='antrenman_list'),
    path('antrenman_ekle/',antrenman_ekle,name='santrenman_ekle'),
    path('antrenman_guncelle/<int:id>/',antrenman_guncelle,name='antrenman_guncelle'),
    path('haftalik/',haftalik_antrenman,name='haftalik_list'),


    path('antrenman_yap/',antrenman_yap,name='antrenman'),
    path('gunluk_ekle/',gunluk_ekle,name='gunluk_ekle'),
    path('htmx_sporcu_ekle/',htmx_sporcu_ekle,name='htmx_sporcu_ekle'),


    path('yarislar/',yaris_list,name='yaris_list'),
    path('sporcu_detail/<int:sporcu_id>',sporcu_detail,name='sporcu_detail'),


]
