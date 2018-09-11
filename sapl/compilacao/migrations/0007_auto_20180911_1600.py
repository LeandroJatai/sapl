# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-21 13:54
from __future__ import unicode_literals

from django.db import migrations, models


def insert_relacionamento_entre_dispositivos(apps, schema_editor):

    TipoDispositivoRelationship = apps.get_model(
        'compilacao', 'TipoDispositivoRelationship')

    try:
        rel = TipoDispositivoRelationship()
        rel.filho_permitido_id = 3
        rel.pai_id = 125
        rel.filho_de_insercao_automatica = False
        rel.perfil_id = 3
        rel.quantidade_permitida = -1
        rel.permitir_variacao = False
        rel.save()
    except:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0006_auto_20180321_1054'),
    ]

    operations = [
        migrations.RunPython(insert_relacionamento_entre_dispositivos),
    ]
