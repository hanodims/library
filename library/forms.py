from django import forms
from .models import Person,Book,Borrow,Search
from django.contrib.auth.models import User



class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }


class SigninForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class MemberForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = '__all__'

        

class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = '__all__'