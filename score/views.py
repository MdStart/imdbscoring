from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
#from django.http import Http404
#from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
    RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	IsAdminUser,
	AllowAny,
	IsAuthenticated,
	IsAuthenticatedOrReadOnly,
	)

from score.models import ImdbScore
from score import serializers


class ImdbScoreCreateAPIView(CreateAPIView):
    """
    This class defines the create behavior of REST API named score API.
    Through this class Admin can create API data for score API & can view the same data  
    """

    queryset = ImdbScore.objects.all()
    serializer_class = serializers.ImdbScoreSerializer
    """
    Permission class to restrict user permission for CRUD on score API   
    """
    permission_classes = (IsAuthenticated,IsAdminUser,)
    
    """
    This function saves the post data into database through create behavior class for score API   
    """
    def perform_create(self, serializer):
        serializer.save()


class ImdbScoreDataAPIView(ListAPIView):
    """
    This class query all the existing score API data from database & display to all the users 
    through django_rest_framework's inbuild html template  
    """
    queryset = ImdbScore.objects.all()
    serializer_class = serializers.ImdbScoreSerializer
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination


class ImdbScoreUpdateAPIView(RetrieveUpdateAPIView):
    """
    This class allows the users to perform Update operation on score API 
    """
    queryset = ImdbScore.objects.all()
    serializer_class = serializers.ImdbScoreSerializer
    lookup_field = 'id'
    """
    Permission class to restrict user permission for CRUD on score API   
    """
    permission_classes = (IsAuthenticated,IsAdminUser,)


    def get_object(self):
        id = self.kwargs['id']
        return get_object_or_404(ImdbScore, id=id)

    def perform_update(self, serializer):
        serializer.save()
       



class ImdbScoreDeleteAPIView(DestroyAPIView):
    """
    This class allows users to perform delete operation over API data 
    """
    queryset = ImdbScore.objects.all()
    serializer_class = serializers.ImdbScoreSerializer
    lookup_field = 'id'
    """
    Permission class to restrict user permission for CRUD on score API   
    """
    permission_classes = (IsAuthenticated,IsAdminUser,)
    
    def get_object(self):
        id = self.kwargs['id']
        return get_object_or_404(ImdbScore, id=id)


class ImdbScoreSearchAPIView(ListAPIView):
    """
    This class allows users to perform search operation over API data through various search fields 
    """
    serializer_class = serializers.ImdbScoreSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['name', 'director', 'imdb_score','popularity99']
    
    """
    This funcrions search over the allowed search_fields & return the query result 
    """
    def get_queryset(self, *args, **kwargs):
        queryset_list = ImdbScore.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(name__icontains=query)|
                    Q(director__icontains=query)|
                    Q(imdb_score__icontains=query) |
                    Q(popularity99__icontains=query)
                    ).distinct()
        return queryset_list
