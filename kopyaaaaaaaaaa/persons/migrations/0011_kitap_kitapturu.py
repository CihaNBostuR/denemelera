# Generated by Django 4.1.6 on 2023-05-05 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0010_remove_kitap_dersturu_remove_kitap_kitapturu_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitap',
            name='kitapturu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.kitapturu'),
        ),
    ]
