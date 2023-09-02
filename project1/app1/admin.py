from django.contrib import admin
from .models import registration,homepage,products,login,changepassword

# Register your models here.
admin.site.register(registration)
admin.site.register(homepage)
admin.site.register(products)
admin.site.register(login)
admin.site.register(changepassword)


