from django.contrib import admin
from .models import *
# Register your models here.
from django.apps import apps


admin.site.register(Student)
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
        