from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import UserCreateSerializer, TodoSerializer
from todo.models import Todo
from .permissions import IsOwner
# Create your views here.

User = get_user_model()

class SignupView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class TodoListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TodoSerializer

    # Filtering and search
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['completed']          
    search_fields = ['title', 'description']  
    ordering_fields = ['created_at', 'updated_at'] 
    ordering = ['-created_at'] 

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
