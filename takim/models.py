from django.db import models
from main.models import Antrenor
from datetime import date

# Create your models here.


DAY_OF_WEEKS_CHOICES = (
    
    (1,"Pazartesi"),
    (2,"Salı"),
    (3,"Çarsamba"),
    (4,"Perşembe"),
    (5,"Cuma"),
    (6,"Cumartesi"),
    (8, "Pazar"),
  
)
ANTRENMAN_YERI = (
    ('Hacettepe', "Hacettepe"),
    ('Atlas', "Atlas"),
)
ANTRENMAN_TURU = (
    ('Yüzme', "Yüzme"),
    ('Kara', "Kara"),
)
CINSIYET = (
    ('Erkek', "Erkek"),
    ('Kadın', "Kadın"),
)

class Takim (models.Model):
    adi=models.CharField(max_length=30)
    antrenor=models.ManyToManyField(Antrenor)
    resim=models.ImageField(null=True,blank=True)
    aktif=models.BooleanField(default=True)
    def __str__(self):
        return self.adi

class Sporcu (models.Model):
    adi=models.CharField(max_length=30)
    soyadi=models.CharField(max_length=30)
    anne=models.CharField(max_length=30)
    baba=models.CharField(max_length=30)
    cinsiyet=models.CharField(max_length=30,choices=CINSIYET)
    dogum_tarihi=models.DateField()
    okulu=models.CharField(max_length=30)
    resim=models.ImageField(upload_to='media/')
    telefon=models.CharField(max_length=10)
    telefon_veli=models.CharField(max_length=10)
    aktif=models.BooleanField(default=True)
    takim=models.ForeignKey(Takim,on_delete=models.CASCADE)
    def __str__(self):
        return self.adi +' '+ self.soyadi

class Ozellikler(models.Model):
    boy=models.IntegerField()
    kilo=models.IntegerField()
    tarih=models.DateField(auto_now_add=True)
    sporcu=models.ForeignKey(Sporcu,on_delete=models.CASCADE)


class HaftalikAntrenman(models.Model):
    dayofweek=models.IntegerField(choices=DAY_OF_WEEKS_CHOICES)
    baslangic=models.TimeField()
    bitis=models.TimeField(null=True)
    takim=models.ForeignKey(Takim,on_delete=models.CASCADE)
    yer=models.TextField(choices=ANTRENMAN_YERI,null=True)
    tur=models.TextField(choices=ANTRENMAN_TURU,null=True)
  
    def __str__(self):
        return str(self.dayofweek)

class Antrenman(models.Model):
    gun=models.DateField(auto_now_add=True)
    takimlar=models.ManyToManyField(Takim)
    sporcular=models.ManyToManyField(Sporcu,null=True,blank=True)
    mesafe=models.IntegerField(default=0)

    class Meta:
        ordering=['-gun']

class Yarislar(models.Model):
    yaris=models.CharField(max_length=100)
    sehir=models.CharField(max_length=100)
    tarih=models.DateField()
    cinsiyet=models.CharField(max_length=100)
    mesafe=models.CharField(max_length=100)
    brans=models.CharField(max_length=100)
    kategori=models.CharField(max_length=100)
    siralama=models.CharField(max_length=100)
    sporcu=models.CharField(max_length=100)
    yas=models.IntegerField()
    takim=models.CharField(max_length=100)
    zaman=models.TimeField()
    puan=models.CharField(max_length=100)
    sporcu_id=models.ForeignKey(Sporcu,on_delete=models.CASCADE)

    def __str__(self):
        return self.yaris +'-'+ self.mesafe +self.brans


class Barajlar (models.Model):
    yaris=models.CharField(max_length=100)
    sehir=models.CharField(max_length=100)
    tarih=models.DateField(max_length=100)
    cinsiyet=models.CharField(max_length=100)
    mesafe=models.CharField(max_length=100)
    brans=models.CharField(max_length=100)
    yas=models.IntegerField()
    baraj_turu=models.CharField(max_length=100)
    baraj=models.TimeField()

    def __str__(self):
        return self.sehir+ '-'+ self.cinsiyet +'-'+  self.mesafe +'-'+  self.brans
