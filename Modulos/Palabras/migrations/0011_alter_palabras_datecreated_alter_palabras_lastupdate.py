# Generated by Django 4.0.2 on 2022-02-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Palabras', '0010_alter_palabras_datecreated_alter_palabras_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palabras',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='palabras',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]