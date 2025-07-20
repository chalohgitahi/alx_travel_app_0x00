from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        pass
    

class ConversationViewSet(viewsets.ModelViewSet):
    # owner_id = request.user.user_id
    # queryset = Conversation.objects.filter(user_id=owner_id)
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['conversation_id', 'created_at']
    ordering = ['created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        pass

    def get_search_fields(self, view, request):
        if request.query_params.get('m'):
            return ['title']
        return super().get_search_fields(view, request)