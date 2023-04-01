# Generated by Django 4.1.7 on 2023-03-11 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(db_column='title_uz', max_length=256)),
                ('title_ru', models.CharField(db_column='title_ru', max_length=256)),
                ('title_en', models.CharField(db_column='title_en', max_length=256)),
                ('description_uz', models.TextField(db_column='description_uz')),
                ('description_ru', models.TextField(db_column='description_ru')),
                ('description_en', models.TextField(db_column='description_en')),
                ('status', models.BooleanField(db_column='status', default=False)),
                ('photo1', models.ImageField(blank=True, db_column='photo1', null=True, upload_to='images/')),
                ('photo2', models.ImageField(blank=True, db_column='photo2', null=True, upload_to='images/')),
                ('photo3', models.ImageField(blank=True, db_column='photo3', null=True, upload_to='images/')),
                ('photo4', models.ImageField(blank=True, db_column='photo4', null=True, upload_to='images/')),
                ('photo5', models.ImageField(blank=True, db_column='photo5', null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at')),
            ],
        ),
    ]