from rest_framework import serializers
from .models import NewsModel


class NewsUzSerializers(serializers.ModelSerializer):
	class Meta:
		model = NewsModel
		fields = ['title_uz', 'description_uz', 'photo1', 'photo2', 'photo3', 'video1', 'video2']


class NewsRuSerializers(serializers.ModelSerializer):
	class Meta:
		model = NewsModel
		fields = ['title_ru', 'description_ru', 'photo1', 'photo2', 'photo3', 'video1', 'video2']


class NewsEnSerializers(serializers.ModelSerializer):
	class Meta:
		model = NewsModel
		fields = ['title_en', 'description_en', 'photo1', 'photo2', 'photo3', 'video1', 'video2']
	
