# Generated by Django 3.2.7 on 2022-09-24 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirpapp', '0002_post_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
