from django.core.validators import FileExtensionValidator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vitrine', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificado',
            old_name='imagem',
            new_name='documento',
        ),
        migrations.AlterField(
            model_name='certificado',
            name='documento',
            field=models.FileField(
                upload_to='certificados/',
                validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                verbose_name='PDF do Certificado',
            ),
        ),
    ]