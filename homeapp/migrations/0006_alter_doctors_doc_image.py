# Generated by Django 4.1 on 2022-09-19 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0005_alter_doctors_doc_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='doc_image',
            field=models.ImageField(upload_to='doctors'),
        ),
    ]