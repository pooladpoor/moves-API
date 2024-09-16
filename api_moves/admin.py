from django.contrib import admin
from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    pass
