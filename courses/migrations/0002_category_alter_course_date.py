# Generated by Django 4.2.2 on 2023-08-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
