


# # Create a nested router for tasks related to users

# # Add the nested routes to the main router



from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Task.views import TaskViewSet,TaskCreateViewSet,StatusViewSet,PriorityViewSet,TeamViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'task/create',TaskCreateViewSet)
router.register(r'task-status', StatusViewSet)
router.register(r'task-priority',PriorityViewSet)
router.register(r'team',TeamViewSet)

urlpatterns = [
    path('', include(router.urls))
]
