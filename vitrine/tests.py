from django.test import TestCase
from django.urls import reverse
from .models import Certificado


class CertificateGalleryTests(TestCase):
	def create_certificate(self, title, category):
		return Certificado.objects.create(
			titulo=title,
			instituicao='Instituição de teste',
			categoria=category,
			data_conclusao='2025-01-01',
			documento=f'certificados/{title}.pdf',
		)

	def test_home_has_one_random_feature_per_requested_category(self):
		self.create_certificate('ingles-a', 'INGLES')
		self.create_certificate('alura-a', 'ALURA')
		self.create_certificate('alura-b', 'ALURA')
		self.create_certificate('faculdade-a', 'FACULDADE')

		response = self.client.get(reverse('index'))

		self.assertEqual(response.status_code, 200)
		featured = response.context['featured_certificates']
		self.assertEqual([item['key'] for item in featured], ['INGLES', 'ALURA', 'FACULDADE'])
		self.assertEqual(len({item['key'] for item in featured}), 3)
		self.assertEqual(featured[0]['certificate'].titulo, 'ingles-a')
		self.assertIn(featured[1]['certificate'].titulo, {'alura-a', 'alura-b'})
		self.assertEqual(featured[2]['certificate'].titulo, 'faculdade-a')

	def test_category_sections_include_all_certificates(self):
		self.create_certificate('alura-a', 'ALURA')
		self.create_certificate('alura-b', 'ALURA')

		response = self.client.get(reverse('index'))

		sections = {section['key']: section for section in response.context['category_sections']}
		self.assertEqual(sections['ALURA']['certificates'].count(), 2)
