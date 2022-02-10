# Generated by Django 3.2.7 on 2021-10-06 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('author', models.CharField(max_length=30)),
                ('desc', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]