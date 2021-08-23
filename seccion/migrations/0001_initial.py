# Generated by Django 3.2.6 on 2021-08-23 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(default='A', max_length=1)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('status', models.BooleanField(default=True)),
                ('course_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curso.curso')),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
                'db_table': 'section',
            },
        ),
    ]
