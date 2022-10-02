from django.shortcuts import render
from api.pagination import CustomPagination, PaginationAPIView
from rest_framework import status
from rest_framework.response import Response
from apps.categorys.models import CategoryModel


# Create your views here.
from apps.categorys.serializers import CategorySerializer, CategoryBlogsSerializer


class Category(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request):
        category_query = CategoryModel.objects.all()
        serializer = CategoryBlogsSerializer(category_query, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


class CategoryDetail(PaginationAPIView):
    pagination_class = CustomPagination

    def get(self, request, pk):
        category_query = CategoryModel.objects.filter(id=pk)
        serializer = CategoryBlogsSerializer(category_query, many=True)
        result = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(result)


