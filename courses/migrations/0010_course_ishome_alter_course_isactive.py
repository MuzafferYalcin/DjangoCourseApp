# Generated by Django 4.2.2 on 2023-08-15 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_category_options_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isHome',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]