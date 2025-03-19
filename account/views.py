from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import Basvuru
from main.models import Blog,Antrenor
from .forms import LoginForm , UserRegistrationForm,BlogForm,AntrenorForm



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
            username=cd['username'],
            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
    # Save the User object
            new_user.save()
        return render(request,'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request,'account/register.html',{'user_form': user_form})    

@login_required
def dashboard(request):
    basvuru_list=Basvuru.objects.all()
    return render(request,
        'dash/dashboard.html',
            {'basvuru_list': basvuru_list})

@login_required
def basvuru_detail(request,id):
    basvuru=get_object_or_404(Basvuru,id=id)
    return render(request,'dash/basvuru_detail.hetml',{'basvuru':basvuru})

@login_required
def blog_list(request):
    blog_list=Blog.objects.all()
    return render(request, 'dash/blog_list.html',{'blog_list':blog_list})


@login_required
def blog_ekle(request):
   if request.method == "POST":
       form = BlogForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('account_blog_list')  # Adjust this to your post list view
   else:
       form = BlogForm()
   return render(request, 'dash/create_post.html', {'form': form})


@login_required
def blog_update(request,slug):
    # dictionary for initial data with 
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    blog = get_object_or_404(Blog, slug = slug)
 
    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance = blog)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect(blog.get_absolute_url()) 
 
    # add form dictionary to context
    context["form"] = form
    context['blog']=blog
 
    return render(request, "dash/update_post.html", context)


@login_required
def antrenor_list(request):
    antrenor_list=Antrenor.objects.all()
    return render(request,'dash/antrenor_list.html',{'antrenor_list':antrenor_list})

@login_required
def antrenor_ekle(request):
   if request.method == "POST":
       form = AntrenorForm(request.POST,request.FILES)
       if form.is_valid():
           form.save()
           return redirect('antrenor_list')  # Adjust this to your post list view
   else:
       form = AntrenorForm()
   return render(request, 'dash/create_antrenor.html', {'form': form})


@login_required
def antrenor_update(request,id):
    antrenor = get_object_or_404(Antrenor, id = id)
    if request.method == 'POST':
        post=request.POST
        if request.FILES == None:
            post = request.POST.copy() # to make it mutable
            post['resim'] = antrenor.resim
        form=AntrenorForm(post,request.FILES,instance=antrenor)
        print (form)

        if form.is_valid():

            form.save()
            return redirect('antrenor_list') 
        else: #invalid case
            print (form.is_valid())  #form contains data and errors
            print (form.errors)
    # dictionary for initial data with 
    # field names as keys
 

    form = AntrenorForm(instance = antrenor)
    return render(request, "dash/update_antrenor.html", {'form':form,'antrenor':antrenor})