# Generated by Django 3.2.5 on 2021-07-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parkmoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District', models.TextField(null=True)),
                ('Park_division', models.TextField(null=True)),
                ('Park_name', models.TextField(null=True)),
            ],
            options={
                'db_table': 'parkmoa_db',
            },
        ),
    ]