









#         if user_id:
#             return TaskAssignment.objects.filter(tkaassigneeuseridfk=user_id)
#         else:
#             return TaskAssignment.objects.all()







"""Views for tasks"""

from rest_framework import viewsets,authentication,permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import TaskAssignment,TaskView,User,Task,TaskStatus,TaskPriority,Team
from .serializers import TaskSerializer,TaskFilter, TaskViewSerializer,StatusSerializer,TaskAssignmentSerializer,CustomTaskCreateSerializer,PrioritySerializer,TeamSerializer

from django.http import JsonResponse


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskView.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['taskStatus']
    ordering_fields = ['taskStartDate','taskEndDate']
    ordering_fields = ['taskStartDate']
    

    def get_queryset(self):
        user = self.request.user
        if self.request.method == 'GET':
            return TaskView.objects.all()
            # return TaskView.objects.filter(tkaAssignee_id= user)
        else:
            return TaskAssignment.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskViewSerializer
        else:
            return TaskAssignmentSerializer

class TaskCreateViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CustomTaskCreateSerializer
        elif self.action == 'put':
            return CustomTaskCreateSerializer
        else:
            return TaskSerializer


class CreateTask(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        user = request.user  # This will be the authenticated user
        
         # Get task data from the request
        task_data = request.data
        task_name = task_data.get("taskName")
        task_description = task_data.get("taskDescription")
        task_status_id = task_data.get("taskStatusId")
        task_priority_id = task_data.get("taskPriorityId")
        task_start_date = task_data.get("taskStartDate")
        task_end_date = task_data.get("taskEndDate")

        # Create a new task with the provided data
        new_task = Task.objects.create(taskName=task_name,taskDescription=task_description,taskStatusId=task_status_id,taskPriorityId=task_priority_id,taskStartDate=task_start_date,taskEndDate=task_end_date)

        # Create a task assignment
        task_assignment = TaskAssignment.objects.create(tkaTask=new_task, tkaAssignee=user,taskAssigner=user)

        return JsonResponse({"message": "Task and assignment created successfully"})
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = TaskStatus.objects.all()
    serializer_class = StatusSerializer

class PriorityViewSet(viewsets.ModelViewSet):
    queryset = TaskPriority.objects.all()
    serializer_class = PrioritySerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer