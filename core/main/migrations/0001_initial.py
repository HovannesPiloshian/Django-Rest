# Generated by Django 5.1 on 2024-08-24 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('number_of_rooms', models.IntegerField()),
                ('size_in_sq_ft', models.FloatField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='house_images/')),
            ],
            options={
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
            },
        ),
    ]
