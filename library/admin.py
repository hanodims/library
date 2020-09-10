from django.contrib import admin
from .models import Person,Book,Borrow,Search

admin.site.register(Person)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Search)
