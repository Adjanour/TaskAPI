# from rest_framework import viewsets
# from .models import Tbltaskassignment,TblTask2, TaskDetails, SubTaskDetails, UserDetails, Tblteam, Tblproject, TaskAssignment, Tbltaskstatus, Tblpriority
# from .serializers import UserPostSerializer,TaskSerializer,TaskAddSerializer, TaskDetailsSerializer, SubtaskDetailsSerializer, UserDetailsSerializer, TaskAssignmentSerializer, TeamDetailsSerializer, ProjectDetailsSerializer, TaskStatusSerializer, TaskPrioritySerializer
# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated



# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = TaskDetails.objects.all()
#     serializer_class = TaskSerializer

# class TaskAddViewSet(viewsets.ModelViewSet):
#     queryset = TblTask2.objects.all()
#     serializer_class = TaskAddSerializer

# class TaskDetailsViewSet(viewsets.ModelViewSet):
#     queryset = TaskDetails.objects.all()
#     serializer_class = TaskDetailsSerializer

# class SubTaskDetailsViewSet(viewsets.ModelViewSet):
#     queryset = SubTaskDetails.objects.all()
#     serializer_class = SubtaskDetailsSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = UserDetails.objects.all()
#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return UserDetailsSerializer
#         else:
#             return UserPostSerializer

# class TaskAssignmentViewSet(viewsets.ModelViewSet):
#     queryset = TaskAssignment.objects.all()
#     serializer_class = TaskAssignmentSerializer

#     def get_queryset(self):
#         user_id = self.kwargs.get('user_pk')  # Use get to avoid KeyError

#         if user_id:
#             return TaskAssignment.objects.filter(tkaassigneeuseridfk=user_id)
#         else:
#             return TaskAssignment.objects.all()


# class TeamViewSet(viewsets.ModelViewSet):
#     queryset = Tblteam.objects.all()
#     serializer_class = TeamDetailsSerializer

# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Tblproject.objects.all()
#     serializer_class = ProjectDetailsSerializer

# class TaskStatusViewSet(viewsets.ModelViewSet):
#     queryset = Tbltaskstatus.objects.all()
#     serializer_class = TaskStatusSerializer

# class TaskPriorityViewSet(viewsets.ModelViewSet):
#     queryset = Tblpriority.objects.all()
#     serializer_class = TaskPrioritySerializer

# from rest_framework.authentication import SessionAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import viewsets

"""Views for tasks"""

from rest_framework import viewsets,authentication,permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import TaskAssignment,TaskView,User,Task,TaskStatus,TaskPriority
from .serializers import TaskSerializer, TaskViewSerializer,StatusSerializer,TaskAssignmentSerializer,CustomTaskCreateSerializer,PrioritySerializer

from django.http import JsonResponse


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if self.request.method == 'GET':
            return TaskView.objects.filter(tkaAssignee_id= user)
        else:
            return TaskAssignment.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TaskViewSerializer
        else:
            return TaskAssignmentSerializer

class TaskCreateViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
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
