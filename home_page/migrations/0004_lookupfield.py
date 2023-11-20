# Generated by Django 3.2.23 on 2023-11-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0003_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='LookupField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='lookup_images')),
                ('file', models.FileField(blank=True, null=True, upload_to='lookup_files')),
            ],
            options={
                'db_table': 'lookup_field',
            },
        ),
    ]