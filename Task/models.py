from django.db import models
from User.models import User
from django.utils import timezone

class TaskPriority(models.Model):
    priorityId = models.AutoField(db_column='prIdpk', primary_key=True)  # Field name made lowercase.
    priorityName = models.CharField(db_column='prName', max_length=255)  # Field name made lowercase.
    priorityDescription = models.CharField(db_column='prDescription', max_length=255)  # Field name made lowercase.
    priorityCreateDdate = models.DateTimeField(db_column='tkaCreatedDate', auto_now_add=True)  # Field name made lowercase.
    priorityUpdateddate = models.DateTimeField(db_column='tkaUpdatedDate', auto_now=True)  # Field name made lowercase.
    priorityIsActive = models.BooleanField(db_column='prIsActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblpriority'


class Project(models.Model):
    projectId = models.AutoField(db_column='prjIdpk', primary_key=True)  # Field name made lowercase.
    projectName = models.CharField(db_column='prjName', max_length=255)  # Field name made lowercase.
    projectDescription = models.CharField(db_column='prjDescription', max_length=255)  # Field name made lowercase.
    projectIsActive = models.BooleanField(db_column='prjIsActive', blank=True, default=True)  # Field name made lowercase.
    projectStartDate = models.DateField(db_column='prjStartDate', blank=True, null=True)  # Field name made lowercase.
    projectEndDate = models.DateField(db_column='prjEndDate', blank=True, null=True)  # Field name made lowercase.
    projectCreateDdate = models.DateTimeField(db_column='tkaCreatedDate', auto_now_add=True)  # Field name made lowercase.
    projectUpdateddate = models.DateTimeField(db_column='tkaUpdatedDate', auto_now=True)  # Field name made lowercase.
    projectType = models.CharField(db_column='prjType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectStatus = models.CharField(db_column='prjStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    projectTeamId = models.IntegerField(db_column='prjTeamIdfk', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblproject'


class Subtask(models.Model):
    subtaskId = models.AutoField(db_column='stskIdpk', primary_key=True)  # Field name made lowercase.
    subtaskkTaskId = models.IntegerField(db_column='stskTaskIdfk', blank=True, null=True)  # Field name made lowercase.
    subtaskName = models.CharField(db_column='stskName', max_length=255)  # Field name made lowercase.
    subtaskDescription = models.CharField(db_column='stskDescription', max_length=255)  # Field name made lowercasesubtaskstatusid = models.IntegerField(db_column='sstatusId', blank=True, null=True)  # Field name made lowercase.
    subtaskCreateDdate = models.DateTimeField(db_column='tkaCreatedDate', auto_now_add=True)  # Field name made lowercase.
    subtaskUpdateddate = models.DateTimeField(db_column='tkaUpdatedDate', auto_now=True)  # Field name made lowercase.
    subtaskPriorityId = models.IntegerField(db_column='stskPriorityIdfk', blank=True, null=True)  # Field name made lowercasesubtaskstartdate = models.DateField(db_column='sstartDate', blank=True, null=True)  # Field name made lowercase.
    subtaskEndDate = models.DateField(db_column='stskEndDate', blank=True, null=True)  # Field name made lowercase.
    subtaskIsActive = models.BooleanField(db_column='stskIsActive', blank=True, default=True)  # Field name made lowercasubtask
    class Meta:
        managed = True
        db_table = 'tblsubtask'


class Task(models.Model):
    taskId = models.AutoField(db_column='tskIdpk', primary_key=True)  # Field name made lowercase.
    taskName = models.CharField(db_column='tskName', max_length=255)  # Field name made lowercase.
    taskDescription = models.CharField(db_column='tskDescription', max_length=255)  # Field name made lowercase.
    taskStatusId = models.IntegerField(db_column='statusId', blank=True, null=True)  # Field name made lowercase.
    taskCreateDdate = models.DateTimeField(db_column='tkaCreatedDate', auto_now_add=True)  # Field name made lowercase.
    taskUpdateddate = models.DateTimeField(db_column='tkaUpdatedDate', auto_now=True)  # Field name made lowercase.
    taskPriorityId = models.IntegerField(db_column='tskPriorityIdfk', blank=True, null=True)  # Field name made lowercase.
    taskStartDate = models.DateField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    taskEndDate = models.DateField(db_column='tskEndDate', blank=True, null=True)  # Field name made lowercase.
    taskIsActive = models.BooleanField(db_column='tskIsActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbltask'



class TaskAssignment(models.Model):
    tkaId = models.AutoField(db_column='tkaIdpk', primary_key=True)  # Field name made lowercase.
    tkaTask = models.ForeignKey(Task, on_delete=models.CASCADE)  # Field name made lowercase.
    tkaAssigner = models.IntegerField(db_column='tkaAssignerUserIdfk', blank=True, null=True)  # Field name made lowercase.
    tkaAssignee = models.ForeignKey(User, on_delete=models.CASCADE)  # Field name made lowercase.
    tkaRemarks = models.CharField(db_column='tkaRemarks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tkaCreateDdate = models.DateTimeField(db_column='tkaCreatedDate', auto_now_add=True)  # Field name made lowercase.
    tkaUpdateddate = models.DateTimeField(db_column='tkaUpdatedDate', auto_now=True)  # Field name made lowercase.
    tkaiIsActive = models.BooleanField(db_column='tkaIsActive', blank=True, default=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbltaskassignment'



class TaskStatus(models.Model):
    statusId = models.AutoField(db_column='stIdpk', primary_key=True)  # Field name made lowercase.
    statusName = models.CharField(db_column='stName', max_length=255)  # Field name made lowercase.
    statusDescription = models.CharField(db_column='stDescription', max_length=255)  # Field name made lowercase.
    statusCreateDdate = models.DateTimeField(db_column='tkaCreatedDate', auto_now_add=True)  # Field name made lowercase.
    statusUpdateddate = models.DateTimeField(db_column='tkaUpdatedDate', auto_now=True)  # Field name made lowercase.
    statusIsActive = models.BooleanField(db_column='stIsActive', blank=True,default=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tbltaskstatus'


class Team(models.Model):
    teamIdpk = models.AutoField(db_column='tmIdpk', primary_key=True)  # Field name made lowercase.
    teamName = models.CharField(db_column='tmName', max_length=255)  # Field name made lowercase.
    teamDescription = models.CharField(db_column='tmDescription', max_length=255)  # Field name made lowercase.
    teamCreatedDate = models.DateTimeField(db_column='tmCreatedDate', auto_now_add=True)  # Field name made lowercase.
    teamUpdatedDate = models.DateTimeField(db_column='tmUpdatedDate', auto_now=True)  # Field name made lowercase.
    teamIsActive = models.BooleanField(db_column='tmIsActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'tblteam'

class TaskView(models.Model):
    taskId = models.IntegerField(primary_key=True)
    taskName = models.CharField(max_length=255)
    taskDescription = models.TextField()
    taskPriority = models.CharField(max_length=255)
    taskStatus = models.CharField(max_length=255)
    tkaAssigner_id = models.IntegerField()
    taskStartDate = models.DateField(default=timezone.now)
    taskCreatedDate = models.DateTimeField(default=timezone.now)
    taskEndDate = models.DateField(default=timezone.now)
    AssignerFullName = models.CharField(max_length=255)
    tkaAssignee_id = models.ForeignKey(User, on_delete=models.CASCADE) 
    tkaId = models.IntegerField()
    tkaTask_id = models.IntegerField()
    fullName = models.CharField(max_length=255)
    taskDuration = models.IntegerField()
    taskProgress = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'TaskView'
