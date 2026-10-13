from django.contrib import admin
from . import models

admin.site.register(models.Films)
admin.site.register(models.Genre)
admin.site.register(models.FeedBack)

