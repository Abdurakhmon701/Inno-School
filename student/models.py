from django.db import models


class NewsModel(models.Model):
    title_uz = models.CharField(max_length=256, db_column="title_uz")
    title_ru = models.CharField(max_length=256, db_column="title_ru")
    title_en = models.CharField(max_length=256, db_column="title_en")
    description_uz = models.TextField(db_column="description_uz")
    description_ru = models.TextField(db_column="description_ru")
    description_en = models.TextField(db_column="description_en")
    status = models.BooleanField(default=False, db_column="status")
    photo1 = models.ImageField(upload_to='images/', blank=True, null=True, db_column="photo1")
    photo2 = models.ImageField(upload_to='images/', blank=True, null=True, db_column="photo2")
    photo3 = models.ImageField(upload_to='images/', blank=True, null=True, db_column="photo3")
    video1 = models.FileField(upload_to='videos/', blank=True, null=True, db_column="video1")
    video2 = models.FileField(upload_to='videos/', blank=True, null=True, db_column="video2")
    created_at = models.DateTimeField(auto_now_add=True, db_column="created_at")
    updated_at = models.DateTimeField(auto_now=True, db_column="updated_at")

    def __str__(self):
        return self.title_ru


