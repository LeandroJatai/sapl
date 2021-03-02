# Generated by Django 2.2.13 on 2021-02-28 00:52

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0017_auto_20210225_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispositivo',
            name='imagem_cropping',
            field=image_cropping.fields.ImageRatioField('imagem', '100x100', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text='O recorte de imagem é possível após a atualização.', hide_image_field=False, size_warning=True, verbose_name='Recorte de Imagem'),
        ),
    ]