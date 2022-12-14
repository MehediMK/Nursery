# Generated by Django 4.0.4 on 2022-06-13 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=150, verbose_name='Plants Name')),
                ('pimage', models.ImageField(upload_to='plantimage', verbose_name='Plant Image')),
                ('ptype', models.CharField(blank=True, max_length=100)),
                ('plight', models.CharField(blank=True, max_length=100)),
                ('pprice', models.IntegerField()),
                ('pmaintain', models.CharField(blank=True, max_length=100)),
                ('pwatersc', models.CharField(blank=True, max_length=100)),
                ('pdesc', models.TextField(blank=True, max_length=600)),
                ('pquantity', models.IntegerField()),
            ],
        ),
    ]
