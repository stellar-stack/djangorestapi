from django.urls import path
from .views import TaskLiStCreate,TaskDetail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('tasks/', TaskLiStCreate.as_view(), name="task-list"),
    path('tasks/<int:pk>/', TaskDetail.as_view(),name="task-detail")
]