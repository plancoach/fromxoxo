# Generated by Django 3.2.18 on 2023-11-08 21:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('letterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter_like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letter_like', to=settings.AUTH_USER_MODEL)),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letter_like', to='letterapp.letter')),
            ],
            options={
                'unique_together': {('customuser', 'letter')},
            },
        ),
    ]
