# Generated by Django 5.0.7 on 2024-07-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(max_length=255)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
