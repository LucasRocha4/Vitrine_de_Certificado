from django.contrib import admin
from .models import Certificado


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'instituicao', 'categoria', 'data_conclusao')
	list_filter = ('categoria', 'instituicao')
