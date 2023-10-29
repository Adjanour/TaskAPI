# from django.urls import re_path ,path, include
# from rest_framework.routers import DefaultRouter
# from rest_framework_nested import routers
# from .viewsets import TaskViewSet, TaskAddViewSet,TaskDetailsViewSet, SubTaskDetailsViewSet, UserViewSet, TaskAssignmentViewSet, TeamViewSet, ProjectViewSet, TaskStatusViewSet, TaskPriorityViewSet

# router = DefaultRouter()
# router.register(r'tasks', TaskDetailsViewSet)
# router.register(r'task-add', TaskAddViewSet)
# router.register(r'subtask-details', SubTaskDetailsViewSet)
# router.register(r'users', UserViewSet)
# router.register(r'task-assignments', TaskAssignmentViewSet)
# router.register(r'teams', TeamViewSet)
# router.register(r'projects', ProjectViewSet)
# router.register(r'task-statuses', TaskStatusViewSet)
# router.register(r'task-priorities', TaskPriorityViewSet)


# # Create a nested router for tasks related to users
# user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
# user_router.register(r'task-assignments', TaskAssignmentViewSet)

# # Add the nested routes to the main router
# router.registry.extend(user_router.registry)


# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(user_router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Task.views import TaskViewSet,TaskCreateViewSet,StatusViewSet,PriorityViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'task/create',TaskCreateViewSet)
router.register(r'task-status', StatusViewSet)
router.register(r'task-priority',PriorityViewSet)

urlpatterns = [
    path('', include(router.urls))
]
