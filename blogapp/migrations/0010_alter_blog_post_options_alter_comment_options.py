# Generated by Django 4.1 on 2022-08-06 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0009_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog_post',
            options={'ordering': ('created_on',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
    ]
