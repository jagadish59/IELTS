# Generated by Django 3.0 on 2021-10-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0006_shorttrickget'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]