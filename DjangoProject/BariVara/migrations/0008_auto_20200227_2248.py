# Generated by Django 3.0.3 on 2020-02-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BariVara', '0007_auto_20200227_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(upload_to='house_pics'),
        ),
    ]
