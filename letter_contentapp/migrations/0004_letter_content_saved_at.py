# Generated by Django 3.2.18 on 2023-11-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter_contentapp', '0003_alter_letter_content_tema'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter_content',
            name='saved_at',
            field=models.DateTimeField(null=True),
        ),
    ]
