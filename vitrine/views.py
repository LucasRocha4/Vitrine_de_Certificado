from django.shortcuts import render
from .models import Certificado


def index(request):
	featured_categories = ('INGLES', 'ALURA', 'FACULDADE')
	featured_certificates = [
		{
			'key': category,
			'label': dict(Certificado.CATEGORIAS)[category],
			'certificate': Certificado.objects.filter(categoria=category).order_by('?').first(),
		}
		for category in featured_categories
	]
	category_labels = dict(Certificado.CATEGORIAS)
	category_order = ('INGLES', 'ALURA', 'FACULDADE', 'OUTROS')
	category_sections = [
		{
			'key': category,
			'label': category_labels[category],
			'certificates': Certificado.objects.filter(categoria=category),
		}
		for category in category_order
	]
	return render(
		request,
		'vitrine/index.html',
		{
			'featured_certificates': featured_certificates,
			'category_sections': category_sections,
		},
	)
