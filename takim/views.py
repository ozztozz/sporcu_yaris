from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Takim,Sporcu,Antrenman,Yarislar,HaftalikAntrenman,DAY_OF_WEEKS_CHOICES,BarajBrans,Barajlar,MESAFE
from .forms import FormTakim,FormSporcu,FormAntrenman
from datetime import  time, datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def base(request):
    return render(request,'base.html')

def takim_list(request):
    takim_list=Takim.objects.all()
    return render(request,'takim_list.html',{'takim_list':takim_list})

@login_required
def takim_ekle(request):
   if request.method == "POST":
       form = FormTakim(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('takim_list')  # Adjust this to your post list view
   else:
       form = FormTakim()
   return render(request, 'takim_ekle.html', {'form': form})

@login_required
def takim_guncelle(request,id):
    takim = get_object_or_404(Takim, id = id)
    if request.method == 'POST':
        post=request.POST
        if request.FILES == None:
            post = request.POST.copy() # to make it mutable
            post['resim'] = takim.resim
        form=FormTakim(post,request.FILES,instance=takim)
    
        if form.is_valid():
            form.save()
            return redirect('takim_list') 

    form = FormTakim(instance = takim)
    return render(request, "takim_ekle.html", {'form':form,'takim':takim})


def sporcu_list(request):
    sporcu_list=Sporcu.objects.all().order_by('takim','dogum_tarihi__year','adi')

    return render(request,'sporcu_list.html',{'sporcu_list':sporcu_list})

@login_required
def sporcu_ekle(request):
   if request.method == "POST":
       form = FormSporcu(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('sporcu_list')  # Adjust this to your post list view
   else:
       form = FormSporcu()
   return render(request, 'sporcu_ekle.html', {'form': form})

@login_required
def sporcu_guncelle(request,id):
    sporcu = get_object_or_404(Sporcu, id = id)
    if request.method == 'POST':
        post=request.POST
        post = request.POST.copy() # to make it mutable
        if request.FILES == None:
            post['resim'] = sporcu.resim

        
        form=FormSporcu(post,request.FILES,instance=sporcu)
    
        if form.is_valid():
            form.save()
            return redirect('sporcu_list') 

    form = FormSporcu(instance = sporcu)
    return render(request, "sporcu_ekle.html", {'form':form,'sporcu':sporcu})



def antrenman_list(request):
    antrenman_list=Antrenman.objects.all()
    return render(request,'antrenman_list.html',{'antrenman_list':antrenman_list})


@login_required
def antrenman_ekle(request):
   if request.method == "POST":
       form = FormAntrenman(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('antrenman_list')  # Adjust this to your post list view
   else:
       form = FormAntrenman()
       
   return render(request, 'antrenman_ekle.html', {'form': form})


@login_required
def antrenman_guncelle(request,id):
    antrenman = get_object_or_404(Antrenman, id = id)
    if request.method == 'POST':
        post=request.POST        
        form=FormAntrenman(post,instance=antrenman)
    
        if form.is_valid():
            form.save()
            return redirect('antrenman_list') 

    form = FormAntrenman(instance = antrenman)
    return render(request, "antrenman_ekle.html", {'form':form,'antrenman':antrenman})

def haftalik_antrenman(request):
    haftalik_list=HaftalikAntrenman.objects.all().order_by('dayofweek',)
    haftalik_nested={}
    for gun in DAY_OF_WEEKS_CHOICES:
        haftalik_nested[gun[1]]={'sabah':[],'aksam':[]}
    
    for antrenman in haftalik_list:
        gunluk=haftalik_nested.get(antrenman.get_dayofweek_display())
        donem= 'sabah' if antrenman.baslangic < time(13,00) else 'aksam'
        gunluk[donem].append(antrenman)
        
    print(haftalik_nested)    
    return render(request,'haftalik_antrenman.html',{'haftalik_list':haftalik_list,
                                                     'haftalik_nested':haftalik_nested})

def antrenman_yap(request):

    return render (request,'antrenman.html')
    gun=datetime.today().weekday()
    gun+=1
    gunluk_antrenman=HaftalikAntrenman.objects.filter(dayofweek=gun)
    return render(request,'antrenman.html',{'gunluk_antrenman':gunluk_antrenman})


def gunluk_ekle(request):
    takim_id=int(request.POST.get('antrenman'))
    takim=get_object_or_404(Takim,id=takim_id)
    yeni_antrenman=Antrenman()
    yeni_antrenman.save()
    yeni_antrenman.takimlar.add(takim)
    sporcu_list=Sporcu.objects.filter(takim=takim_id)
    response=render_to_string('sporcu_antrenman.html',{'sporcu_list':sporcu_list,'antrenman':yeni_antrenman})
    return HttpResponse(response)

@csrf_exempt
def htmx_sporcu_ekle(request):
    sporcu_id=int(request.POST.get('sporcu'))
    ekle_cikar=request.POST.get('ekle_cikar')
    print(ekle_cikar)
    sporcu_tek=get_object_or_404(Sporcu,id=sporcu_id)
    response=render_to_string('sporcu_antrenman.html',{'sporcu_tek':sporcu_tek,
                                                       'ekle_cikar':ekle_cikar})
    return HttpResponse(response)

def yaris_list(request):
    yaris_list=Yarislar.objects.all().order_by('brans','mesafe','zaman',)
     
    return render(request,'yaris_list.html',{'yaris_list':yaris_list})

from datetime import datetime,timedelta
from django.db.models import Min,Max




def sporcu_detail(request,uuid):
    sporcu=get_object_or_404(Sporcu,uuid=uuid)
    sporcu_yas=datetime.now().year-sporcu.dogum_tarihi.year
    

    yaris_sonuc=[]

    

    sporcu_yaris_list=Yarislar.objects.filter(sporcu_id=sporcu.id)
    sporcu_yarislar1=sporcu_yaris_list.values('mesafe','brans').filter(sporcu_id_id=sporcu.id).annotate(best_time=Min('zaman'),worst_time=Max('zaman'),son_yaris=Max('tarih')).order_by('brans','-mesafe')


    PRIORITY_ORDER = {
        '50':1,
        '100':2,
        '200':3,
        '400':4,
        '800':5,
        '1500':6,



        }
    sporcu_yarislar=sorted(
            sporcu_yarislar1,
            key=lambda x: [x['brans'],PRIORITY_ORDER[x['mesafe']]],
        )


    for yaris in sporcu_yarislar:
        eklenecek_yaris={}
        eklenecek_yaris['sporcu_yas']= sporcu_yas
        eklenecek_yaris['mesafe']=yaris['mesafe']
        eklenecek_yaris['brans']=yaris['brans']
        eklenecek_yaris['best_time']=yaris['best_time']
        eklenecek_yaris['son_yaris']=yaris['son_yaris']
        xValues = []
        yValues = []
        yaris_gecmisi=sporcu_yaris_list.filter(sporcu_id=sporcu.id,
                                                    brans=yaris['brans'],
                                                    mesafe=yaris['mesafe']
                                                    ).order_by('mesafe','brans','-tarih')[:7][::-1]
        
        worst_time=datetime.combine(datetime.now().date(), yaris['worst_time'])
        for g_yaris in yaris_gecmisi:
            xValues.append(g_yaris.tarih.strftime("%d.%m.%y"))
            if worst_time.minute>0:
                yValues.append(g_yaris.zaman.microsecond / 100000000+g_yaris.zaman.second/100+g_yaris.zaman.minute)
            else:
                yValues.append(g_yaris.zaman.second+g_yaris.zaman.microsecond / 1000000)
        eklenecek_yaris['xValues']=xValues
        eklenecek_yaris['yValues']=yValues

        baraj_list=Barajlar.objects.filter(tarih__gte=datetime.now(),
                                      yas__lte=sporcu_yas,
                                      yas_ust__gte=sporcu_yas,
                                      )

        
        for counter,baraj in enumerate(baraj_list):
                eklenecek_yaris['sehir'+str(counter)]=baraj.sehir
                eklenecek_yaris['tarih'+str(counter)]=baraj.tarih
                sehir_baraj=baraj.brans_baraj.filter(brans=yaris['brans'],mesafe=yaris['mesafe'],cinsiyet=sporcu.cinsiyet).first()
                
                if sehir_baraj:
                        eklenecek_yaris['baraj'+str(counter)]=sehir_baraj.baraj
                        best_full=datetime.combine(datetime.now().date(), yaris['best_time'])
                        best=best_full.minute*60+best_full.second
                        bar_full=datetime.combine(datetime.now().date(), sehir_baraj.baraj)
                        bar=bar_full.minute*60+bar_full.second
                        diff = datetime.combine(datetime.now().date(), yaris['best_time'])-datetime.combine(datetime.now().date(), sehir_baraj.baraj)
                        
                        fark=round(diff.seconds+diff.microseconds/1000000,1)
                        eklenecek_yaris['fark'+str(counter)]=fark
                        eklenecek_yaris['yuzde'+str(counter)]=int((bar/best*10))*10
                        kalan=int(((best-bar)/bar*135))*5
                        if kalan>60:
                            kalan=60
                        eklenecek_yaris['kalan'+str(counter)]=kalan
                    
                        
                else:
                        eklenecek_yaris['baraj'+str(counter)]=''
                        eklenecek_yaris['fark'+str(counter)]=''
        yaris_sonuc.append(eklenecek_yaris)

    return render(request,'sporcu_detail.html',{'sporcu':sporcu,
                                                'yaris_sonuc':yaris_sonuc,
                                              
                                                  })

