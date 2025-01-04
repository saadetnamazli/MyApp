

# Register your models here.
from django.contrib import admin
from .models import Worker, Message  # Import your models here

# Register your models so they appear in the Django admin
admin.site.register(Worker)
admin.site.register(Message)

