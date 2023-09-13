# Generated by Django 4.2.5 on 2023-09-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_artikel_bild'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adresse',
            name='datum',
        ),
        migrations.AlterField(
            model_name='artikel',
            name='preis',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='kunde',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
