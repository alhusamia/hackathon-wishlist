# Generated by Django 3.0.3 on 2020-02-20 11:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0012_wisherlist_unique_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wisherlist',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='wisherlist',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
