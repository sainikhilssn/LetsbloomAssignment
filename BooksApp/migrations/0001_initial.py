# Generated by Django 5.0 on 2023-12-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
                ('published', models.DateField()),
            ],
        ),
    ]
