# Generated by Django 3.2.5 on 2021-07-16 17:39

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
                ('num', models.TextField(null=True)),
                ('district', models.TextField(null=True)),
                ('park_division', models.TextField(null=True)),
                ('park_name', models.TextField(null=True)),
                ('road_address', models.TextField(null=True)),
                ('parcel_address', models.TextField(null=True)),
                ('park_overview', models.TextField(null=True)),
                ('park_area', models.TextField(null=True)),
                ('main_facility', models.TextField(null=True)),
                ('sporting_goods', models.TextField(null=True)),
                ('guidemap', models.TextField(null=True)),
                ('direction', models.TextField(null=True)),
                ('use_notes', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('park_number', models.TextField(null=True)),
                ('latitude', models.TextField(null=True)),
                ('longitude', models.TextField(null=True)),
                ('shortcut', models.TextField(null=True)),
                ('grade', models.TextField(null=True)),
                ('keyword', models.TextField(null=True)),
            ],
        ),
    ]
