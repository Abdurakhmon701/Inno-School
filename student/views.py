from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.generics import get_object_or_404

from .serializers import NewsUzSerializers, NewsRuSerializers, NewsEnSerializers
from .models import NewsModel


class NewsViewUzRetrieveAPI(APIView):
	def get(self, request, pk):
		news = get_object_or_404(NewsModel, id=pk, status=True)
		serializer = NewsUzSerializers(news)
		return Response(serializer.data)


class NewsViewRuRetrieveAPI(APIView):
	def get(self, request, pk):
		news = get_object_or_404(NewsModel, id=pk, status=True)
		serializer = NewsRuSerializers(news)
		return Response(serializer.data)


class NewsViewEnRetrieveAPI(APIView):
	def get(self, request, pk):
		news = get_object_or_404(NewsModel, id=pk, status=True)
		serializer = NewsEnSerializers(news)
		return Response(serializer.data)


class ListNewsUzAPI(ListAPIView):
	serializer_class = NewsUzSerializers
	queryset = NewsModel.objects.filter(status=True).order_by("-id")
	pagination_class = LimitOffsetPagination


class ListNewsRuAPI(ListAPIView):
	serializer_class = NewsRuSerializers
	queryset = NewsModel.objects.filter(status=True).order_by("-id")
	pagination_class = LimitOffsetPagination


class ListNewsEnAPI(ListAPIView):
	serializer_class = NewsEnSerializers
	queryset = NewsModel.objects.filter(status=True).order_by("-id")
	pagination_class = LimitOffsetPagination





