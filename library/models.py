from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    name = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    member = models.BooleanField(default=False)

    def __str__(self):
        return self.name.username
   

    


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    description = models.TextField()
    gener = models.CharField(max_length=120)
    ISPN = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, auto_now_add=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    available = models.BooleanField(default=True)


  



class Search(models.Model):
    searchBy = models.CharField(max_length=120, choices=[('title','Name'),('gener','Gener'),('ISPN','ISPN')],default='Name')
    keyword = models.CharField(max_length=250)

    def __str__(self):
        return self.keyword


