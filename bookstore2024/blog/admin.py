from django.contrib import admin
from .models import Book, tipos, syggrafeas, ekdotikos_oikos

admin.site.register(Book)
admin.site.register(tipos)
admin.site.register(syggrafeas)
admin.site.register(ekdotikos_oikos)