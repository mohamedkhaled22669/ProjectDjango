# Generated by Django 3.1 on 2020-09-23 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures'),
        ),
    ]
