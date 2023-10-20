from django import forms

from courses.models import Course 

# class CreateCourseForm(forms.Form):
#     title = forms.CharField(
#         label='Kurs Başlığı',
#         required=True,
#         error_messages={'required':'bu alanı boş geçemezsiniz'},
#         widget= forms.TextInput(attrs={
#             'class':'form-control'
#         })
#         )
#     description = forms.CharField(widget=forms.Textarea(attrs={
#         'class':'form-control'
#     }),label="Kurs Açıklaması")
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={
#         'class':'form-control'
#     }))
#     datetime = forms.DateTimeField(widget=forms.TextInput(attrs={
#         'class':'form-control'
#     })
#     )

class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description", "image","categories")  
        labels = {
            'title': 'Kurs Adı',
            'description' : 'Açıklama'
        }
        widgets = {
            "title" : forms.TextInput(attrs={"class":'form-control'}),
            "description" : forms.Textarea(attrs={"class":'form-control'}),
            "categories": forms.CheckboxSelectMultiple(attrs={'class' : 'form-check '})
        }
        
class EditCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("title", "description","categories",'image',"isActive","isHome",)  
        labels = {
            'title': 'Kurs Adı',
            'description' : 'Açıklama'
        }
        widgets = {
            "title" : forms.TextInput(attrs={"class":'form-control'}),
            "description" : forms.Textarea(attrs={"class":'form-control'}),
            "categories": forms.CheckboxSelectMultiple(attrs={'class' : 'form-check '})
        }

class UploadForm(forms.Form):
    image = forms.FileField()