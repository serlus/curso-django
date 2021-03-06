# Generated by Django 3.0.8 on 2020-07-27 02:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('inicio', models.DateField()),
                ('fin', models.DateField()),
                ('matriculas', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
