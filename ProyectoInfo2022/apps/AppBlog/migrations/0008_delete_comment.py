# Generated by Django 4.0.6 on 2022-08-19 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0007_remove_comment_email_alter_comment_body_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
