# Generated by Django 2.2.1 on 2019-05-23 14:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ap_pat', models.CharField(max_length=50)),
                ('ap_mat', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('delete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
            ],
            options={
                'db_table': 'Alumno',
            },
        ),
    ]
