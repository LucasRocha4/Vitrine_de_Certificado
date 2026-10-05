from django.db import models
from django.core.validators import FileExtensionValidator


class Certificado(models.Model):
	CATEGORIAS = (
		('FACULDADE', 'Faculdade'),
		('ALURA', 'Alura'),
		('INGLES', 'Curso de Inglês'),
		('OUTROS', 'Outros'),
	)

	titulo = models.CharField(max_length=200, verbose_name='Título do Curso')
	instituicao = models.CharField(max_length=150, verbose_name='Instituição')
	categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='OUTROS')
	data_conclusao = models.DateField(verbose_name='Data de Conclusão')
	documento = models.FileField(
		upload_to='certificados/',
		verbose_name='PDF do Certificado',
		validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
	)
	link_validacao = models.URLField(
		blank=True,
		null=True,
		verbose_name='Link de Validação (Opcional)',
	)

	def __str__(self):
		return f'{self.titulo} - {self.instituicao}'

	class Meta:
		ordering = ['-data_conclusao']
