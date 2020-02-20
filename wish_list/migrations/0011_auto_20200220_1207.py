# Generated by Django 3.0.3 on 2020-02-20 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wish_list', '0010_auto_20200220_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wisherlist',
            name='wisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
