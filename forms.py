from django import forms
from django.core.exceptions import ValidationError
from dbapp . models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def validatename(name):
    if name.endswith('a') != True:
        raise ValidationError('name is not ends with a')


class DataForm(forms.Form):
    name1=forms.CharField(max_length=10,required=False,initial='Suresh',validators=[validatename])
    name2=forms.CharField(max_length=10,widget=forms.Textarea(attrs={'style':'background-color:yellow;height:40px;border:4px solid black'}))
    date=forms.DateField(widget=forms.SelectDateWidget)

    def clean_name1(self):
        name=self.cleaned_data['name1']
        print(name)
        if name.startswith('S') != True:
            raise ValidationError("name should starat with s")
        else:
            return name

class EmpForm(forms.Form):
    empno=forms.IntegerField(required=True)
    empname=forms.CharField(max_length=20)
    salary=forms.IntegerField()
    department=forms.IntegerField()


class EmpModelForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields = '__all__'
    


class RegisterUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']



