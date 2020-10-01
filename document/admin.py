from django.contrib import admin
from .models import DocumentMaster, DocumentRow

admin.site.register(DocumentRow)
admin.site.register(DocumentMaster)