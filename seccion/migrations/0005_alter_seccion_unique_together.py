# Generated by Django 3.2.6 on 2021-08-18 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_alter_curso_table'),
        ('seccion', '0004_alter_seccion_table'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seccion',
            unique_together={('course_code', 'section', 'year', 'semester')},
        ),
    ]