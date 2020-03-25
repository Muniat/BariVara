# Generated by Django 3.0.3 on 2020-03-12 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BariVara', '0018_remove_advertisements_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisements',
            name='image',
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='house_pics/')),
                ('advertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BariVara.advertisements')),
            ],
        ),
    ]