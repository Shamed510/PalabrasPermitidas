# Generated by Django 4.0.2 on 2022-02-06 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Palabras', '0004_alter_palabra_datecreated_alter_palabra_datedeleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palabra',
            name='dateDeleted',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='palabra',
            name='lastUpdate',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
