from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView, TodoDetailView, TodoListCreateView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="api-signup"),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("todos/", TodoListCreateView.as_view(), name="api-todo-create"),
    path("todos/<int:pk>/", TodoDetailView.as_view(), name="api-todo-detail")
]