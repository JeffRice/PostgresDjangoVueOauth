# Generated by Django 3.2.13 on 2022-07-03 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='text',
            new_name='token',
        ),
        migrations.AddField(
            model_name='note',
            name='user',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
