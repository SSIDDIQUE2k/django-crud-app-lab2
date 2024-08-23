from django.contrib import admin
from .models import Animal, Feeding

admin.site.register(Animal)
# Register the new Feeding model
admin.site.register(Feeding)
