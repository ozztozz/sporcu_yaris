from django import forms
from .models import Takim,Sporcu,Antrenman,Ozellikler
from datetime import date


add_class="""class='bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-primary-500 dark:focus:border-primary-500'>"""
          

class FormTakim(forms.ModelForm):
   
   class Meta:
       model = Takim
       fields = '__all__'

   def __init__(self, *args, **kwargs):
        super(FormTakim, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = add_class
           
class FormSporcu(forms.ModelForm):

   class Meta:
       model = Sporcu
       fields = '__all__'
       widgets = {
            'dogum_tarihi': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'})
        }
       
   def __init__(self, *args, **kwargs):
        super(FormSporcu, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = add_class
           
         
class FormAntrenman(forms.ModelForm):

   class Meta:
       model = Antrenman
       fields = '__all__'
       widgets = {
            'gun': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'}),
            'takimlar': forms.CheckboxSelectMultiple()
        }
       
   def __init__(self, *args, **kwargs):
        super(FormAntrenman, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = add_class
                          