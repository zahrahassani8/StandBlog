# Generated by Django 5.0.1 on 2024-03-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to='profile-pic'),
        ),
    ]
