# Generated by Django 4.1 on 2022-09-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0004_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_image',
            field=models.ImageField(upload_to='doctor'),
        ),
    ]