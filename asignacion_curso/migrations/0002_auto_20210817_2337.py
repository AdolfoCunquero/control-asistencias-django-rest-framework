# Generated by Django 3.2.6 on 2021-08-18 05:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seccion', '0004_alter_seccion_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asignacion_curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='asignacioncurso',
            unique_together={('section', 'username_student')},
        ),
        migrations.AlterModelTable(
            name='asignacioncurso',
            table='asignacion_curso',
        ),
    ]