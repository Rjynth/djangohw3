# Generated by Django 5.1.2 on 2024-10-26 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.URLField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]
