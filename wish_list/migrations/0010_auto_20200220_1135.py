# Generated by Django 3.0.3 on 2020-02-20 09:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wish_list', '0009_auto_20200220_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wisherlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dream', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='wisherlist',
            name='wisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wish_list.Users'),
        ),
    ]