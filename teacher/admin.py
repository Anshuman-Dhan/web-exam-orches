from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
from django.apps import apps


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
        
