# Generated by Django 3.0.3 on 2020-02-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BariVara', '0013_auto_20200228_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisements',
            name='image',
            field=models.FileField(default='defaulthouse.jpg', upload_to='house_pics'),
        ),
    ]