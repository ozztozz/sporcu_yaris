from django import forms
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteInplaceWidget,SummernoteWidget
from main.models import Blog,Antrenor


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    username.widget.attrs['class']="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    
    password.widget.attrs['class']="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
    
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
    widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
    


class BlogForm(forms.ModelForm):
   
   class Meta:
       model = Blog
       fields = ['tur','baslik', 'aktif','author','resim','metin']
       widgets = {'metin': SummernoteWidget()}

   def __init__(self, *args, **kwargs):
        add_class="""class='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'>"""
          
        super(BlogForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
           
            if not visible.name=='metin':
                visible.field.widget.attrs['class'] = add_class

class AntrenorForm(forms.ModelForm):
   
   class Meta:
       model = Antrenor
       fields = ['adi','soyadi', 'unvan','telefon','resim','instagram','ozet','ozgecmis','aktif']
       widgets = {'ozgecmis': SummernoteWidget(),}


   def __init__(self, *args, **kwargs):
        add_class="""class='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'>"""
          
        super(AntrenorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
           
            if not visible.name=='ozgecmis':
                visible.field.widget.attrs['class'] = add_class