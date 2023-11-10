# Generated by Django 3.2.18 on 2023-11-08 21:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('letterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter_content',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tema', models.CharField(choices=[('blue', '블루'), ('pink', '핑크'), ('gray', '그레이'), ('yellow', '옐로우'), ('green', '그린'), ('purple', '퍼플')], default='pink', max_length=20)),
                ('content', models.TextField(max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='letter_content/')),
                ('letter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='letter_content', to='letterapp.letter')),
            ],
        ),
    ]
