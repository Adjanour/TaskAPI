from rest_framework import viewsets
from .models import TblTask2, TaskDetails, SubTaskDetails, UserDetails, Tblteam, Tblproject, TaskAssignment, Tbltaskstatus, Tblpriority
from .serializers import UserPostSerializer,TaskSerializer,TaskAddSerializer, TaskDetailsSerializer, SubtaskDetailsSerializer, UserDetailsSerializer, TaskAssignmentSerializer, TeamDetailsSerializer, ProjectDetailsSerializer, TaskStatusSerializer, TaskPrioritySerializer



class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskSerializer

class TaskAddViewSet(viewsets.ModelViewSet):
    queryset = TblTask2.objects.all()
    serializer_class = TaskAddSerializer

class TaskDetailsViewSet(viewsets.ModelViewSet):
    queryset = TaskDetails.objects.all()
    serializer_class = TaskDetailsSerializer

class SubTaskDetailsViewSet(viewsets.ModelViewSet):
    queryset = SubTaskDetails.objects.all()
    serializer_class = SubtaskDetailsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserDetailsSerializer
        else:
            return UserPostSerializer

class TaskAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')  # Use get to avoid KeyError

        if user_id:
            return TaskAssignment.objects.filter(tkaassigneeuseridfk=user_id)
        else:
            return TaskAssignment.objects.all()


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Tblteam.objects.all()
    serializer_class = TeamDetailsSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Tblproject.objects.all()
    serializer_class = ProjectDetailsSerializer

class TaskStatusViewSet(viewsets.ModelViewSet):
    queryset = Tbltaskstatus.objects.all()
    serializer_class = TaskStatusSerializer

class TaskPriorityViewSet(viewsets.ModelViewSet):
    queryset = Tblpriority.objects.all()
    serializer_class = TaskPrioritySerializer




