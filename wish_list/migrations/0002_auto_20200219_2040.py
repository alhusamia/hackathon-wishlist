# Generated by Django 3.0.3 on 2020-02-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wisherlist',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='wisherlist',
            name='time',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='wisherlist',
            name='url',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
