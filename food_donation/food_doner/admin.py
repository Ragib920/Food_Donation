from django.contrib import admin

# Register your models here.
from .models import Doner_Post
from .models import profile

admin.site.register(Doner_Post)
admin.site.register(profile)