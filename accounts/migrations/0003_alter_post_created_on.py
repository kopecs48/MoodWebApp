# Generated by Django 4.1.2 on 2022-10-31 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
