# Generated by Django 4.0.6 on 2022-08-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0004_alter_comment_body_alter_post_body_alter_post_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(max_length=5000),
        ),
    ]