# Generated by Django 2.0.5 on 2018-05-25 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_management', '0003_auto_20180524_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='featured_picture',
            field=models.ImageField(blank=True, null=True, upload_to='featured_pictures/%Y/', verbose_name='featured picture'),
        ),
    ]
