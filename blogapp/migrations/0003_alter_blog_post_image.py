# Generated by Django 4.1 on 2022-08-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_rename_post_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
