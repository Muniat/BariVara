# Generated by Django 3.0.3 on 2020-03-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BariVara', '0021_auto_20200313_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='house_pics/'),
        ),
    ]