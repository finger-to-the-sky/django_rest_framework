# Generated by Django 4.1.5 on 2023-01-10 16:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('6d579199-4c3b-497d-9320-1ad158190760'), primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]