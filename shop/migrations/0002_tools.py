# Generated by Django 4.1.7 on 2023-04-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tools_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=300)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]