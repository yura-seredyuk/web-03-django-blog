# Generated by Django 3.2.7 on 2021-09-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, height_field=100, upload_to='images/%Y/%m/%d/', width_field=100),
        ),
    ]
