# Generated by Django 2.1.5 on 2020-02-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0013_auto_20200220_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wisherlist',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
