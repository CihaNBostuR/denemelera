# Generated by Django 4.1.6 on 2023-05-04 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0006_remove_person_city_remove_person_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasimYili',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='DersTuru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='YayinEvi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('basimyili', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.basimyili')),
            ],
        ),
        migrations.CreateModel(
            name='Sinif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('yayinevi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.yayinevi')),
            ],
        ),
        migrations.CreateModel(
            name='KitapTuru',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('sinif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.sinif')),
            ],
        ),
        migrations.CreateModel(
            name='Kitap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basimyili', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.basimyili')),
                ('dersturu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.dersturu')),
                ('kitapturu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.kitapturu')),
                ('sinif', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.sinif')),
                ('yayinevi', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persons.yayinevi')),
            ],
        ),
        migrations.AddField(
            model_name='dersturu',
            name='kitapturu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.kitapturu'),
        ),
    ]
