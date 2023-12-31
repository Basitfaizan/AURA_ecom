# Generated by Django 4.2.3 on 2023-08-01 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentications', '0006_alter_profile_first_name_alter_profile_gender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('userName', models.CharField(blank=True, max_length=100, null=True)),
                ('phoneNumber', models.IntegerField(blank=True, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(max_length=1000)),
                ('state', models.CharField(max_length=100)),
                ('alternateNumber', models.IntegerField(blank=True, null=True)),
                ('userAdd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
