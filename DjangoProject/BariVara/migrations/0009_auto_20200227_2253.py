# Generated by Django 3.0.3 on 2020-02-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BariVara', '0008_auto_20200227_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(default='defaulthouse.jpg', upload_to='house_pics'),
        ),
    ]
