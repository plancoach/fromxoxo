# Generated by Django 3.2.18 on 2023-11-14 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('expire_from', models.DateTimeField(null=True)),
                ('finished_at', models.DateTimeField(null=True)),
                ('progress', models.CharField(choices=[('progress1', 'progress1'), ('progress2', 'progress2'), ('progress3', 'progress3'), ('done', 'done')], default='progress1', max_length=20)),
                ('state', models.CharField(choices=[('unchecked', '미확인'), ('checked', '확인 완료'), ('saved', '저장 완료')], default='unchecked', max_length=20)),
                ('qr', models.ImageField(upload_to='letter/')),
                ('url', models.CharField(max_length=100)),
                ('saver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_saver', to=settings.AUTH_USER_MODEL)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='letter_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
