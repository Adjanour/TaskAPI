# from rest_framework import serializers 
# from task.models import Tbluser,Tbltask,TblTask2,Tbltaskassignment, TaskDetails, SubTaskDetails, UserDetails,Tblteam,Tblproject,TaskAssignment,Tbltaskstatus,Tblpriority

# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tbltask
#         fields = '__all__'
#         # fields = ('tskidpk',
#         #           'tskname',
#         #           'tskdescription',
#         #           'statusid',
#         #         'tskcreateddate',
#         #         'tskpriorityidfk',
#         #         'startdate',
#         #         'tskenddate',
#         #         'tskisactive')
# class TaskAddSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TblTask2
#         fields = '__all__'
# class TaskDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaskDetails
#         fields = '__all__'

# class UserPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tbluser
#         fields = (
#             'userName',
#             'userEmail',
#             'userPassword',
#             'userFirstname',
#             'userLastname',
#             'userOthername',
#             'userGender',
#             'userDob',
#             'userTeamIdfk',
#             'userMobile',
#             'userIsActive'
#         )

# class SubtaskDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubTaskDetails
#         fields = '__all__'

# class UserDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserDetails
#         fields = '__all__'

# class TaskAssignmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaskAssignment
#         fields = '__all__'

# class TeamDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tblteam
#         fields = '__all__'

# class ProjectDetailsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tblproject
#         fields = '__all__'

# class TaskStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tbltaskstatus
#         fields = '__all__'

# class TaskPrioritySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tblpriority
#         fields = '__all__'

"""Serializers related to tasks"""

from rest_framework import serializers
from django.contrib.auth import get_user_model

from Task.models import TaskAssignment, TaskView,Task,TaskStatus,TaskPriority

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('taskId','taskName','taskDescription','taskStatusId','taskPriorityId','taskStartDate','taskEndDate')
    
    # def create(self, validated_data):
    #     user = 
    #     new_task = Task.objects.create(**validated_data)
    #     task_assignment = TaskAssignment.objects.create(task=new_task, tkaAssignee = User)
    #     return super().create(validated_data)

class TaskAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskAssignment
        fields = ('tkaTask','tkaAssignee','tkaAssigner')

class TaskViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskView
        fields = '__all__'

class CustomTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('taskId','taskName','taskDescription','taskStatusId','taskPriorityId','taskStartDate','taskEndDate')

    def create(self, validated_data):
        # Do some custom logic here
        serializer = TaskSerializer(data=validated_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = '__all__'

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskPriority
        fields = '__all__'

    