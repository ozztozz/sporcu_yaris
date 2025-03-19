from django.contrib import admin
from .models import Takim,Sporcu,Antrenman,Ozellikler,HaftalikAntrenman,Yarislar,Barajlar
from django.conf.locale.es import formats as es_formats
es_formats.TIME_FORMAT = "H:i:s.u"
# Register your models here.

admin.site.register(Takim)
admin.site.register(Sporcu)
admin.site.register(Antrenman)
admin.site.register(Ozellikler)
admin.site.register(HaftalikAntrenman)
admin.site.register(Yarislar)
admin.site.register(Barajlar)