# Generated by Django 3.0.8 on 2020-08-31 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_auto_20200725_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(choices=[('Bad', '1'), ('Average', '2'), ('Good', '3'), ('Excellent', '4'), ('Best', '5')], default=None, max_length=100)),
            ],
        ),
    ]
