from django.db import models
from django.contrib.auth.models import User


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
    ispn = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='log')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='log')
    start_date = models.DateField(auto_now=False, auto_now_add=True)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    available = models.BooleanField(default=True)


  

#Delete model
class Search(models.Model):
    search_by = models.CharField(max_length=120, choices=[('title','Name'),('gener','Gener'),('ISPN','ISPN')],default='Name')
    keyword = models.CharField(max_length=250)

    def __str__(self):
        return self.keyword


