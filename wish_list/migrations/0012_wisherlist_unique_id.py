# Generated by Django 3.0.3 on 2020-02-20 11:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0011_auto_20200220_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='wisherlist',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
