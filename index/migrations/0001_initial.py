# Generated by Django 4.1.1 on 2023-06-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
