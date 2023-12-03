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

from Task.models import TaskAssignment, TaskView,Task,TaskStatus,TaskPriority,Team
import datetime
import django_filters


def parse_time_format(time_string):
    # Parse the time string into a datetime object
    time_object = datetime.datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Convert the datetime object to a format that Django can handle
    django_time_format = '%Y-%m-%dT%H:%M:%S.%fZ'
    django_time_string = time_object.strftime(django_time_format)

    return django_time_string
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('taskId','taskName','taskDescription','taskStatusId','taskPriorityId','taskStartDate','taskEndDate')

# class TaskSerializer(serializers.ModelSerializer):
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)

#         # Format taskStartDate and taskEndDate to the desired format
#         representation['taskStartDate'] = instance.taskStartDate.strftime('%Y-%m-%d')
#         representation['taskEndDate'] = instance.taskEndDate.strftime('%Y-%m-%d')

#         return representation

#     class Meta:
#         model = Task
#         fields = ('taskId', 'taskName', 'taskDescription', 'taskStatusId', 'taskPriorityId', 'taskStartDate', 'taskEndDate')

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
        fields = ('taskId',
            'taskName',
            'taskDescription',
            'taskPriority',
            'taskStatus',
            'tkaAssigner_id',
            'taskStartDate',
            'taskCreatedDate',
            'taskEndDate',
            'AssignerFullName',
            'tkaAssignee_id',
            'tkaId',
            'tkaTask_id',
            'fullName', 
            'taskDuration',
            'taskProgress',
            'taskSlug',)
        
    
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

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class TaskFilter(django_filters.FilterSet):
    class Meta:
        model = TaskView
        fields = {'taskStatus':['exact'],'taskPriority':['exact'],'tkaAssigner_id':['exact']}