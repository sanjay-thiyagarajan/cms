import graphene
from graphene_django import DjangoObjectType
from panel.models import Member, Task, Department, Role, Position, Domain, DomainMember, Application, Achievement, Submission

class MemberType(DjangoObjectType):
    class Meta:
        model = Member

class TaskType(DjangoObjectType):
    class Meta:
        model = Task

class DepartmentType(DjangoObjectType):
    class Meta:
        model = Department

class RoleType(DjangoObjectType):
    class Meta:
        model = Role

class PositionType(DjangoObjectType):
    class Meta:
        model = Position

class DomainType(DjangoObjectType):
    class Meta:
        model = Domain

class DomainMemberType(DjangoObjectType):
    class Meta:
        model = DomainMember

class ApplicationType(DjangoObjectType):
    class Meta:
        model = Application

class AchievementType(DjangoObjectType):
    class Meta:
        model = Achievement

class SubmissionType(DjangoObjectType):
    class Meta:
        model = Submission

class Query(graphene.ObjectType):
    members = graphene.List(MemberType)
    tasks = graphene.List(TaskType)
    department = graphene.List(DepartmentType)
    role = graphene.List(RoleType)
    position = graphene.List(PositionType)
    domain = graphene.List(DomainType)
    domainmember = graphene.List(DomainMemberType)
    application = graphene.List(ApplicationType)
    achievement = graphene.List(AchievementType)
    submission = graphene.List(SubmissionType)

    def resolve_members(self, info, **kwargs):
        return Member.objects.all()
    
    def resolve_tasks(self, info, **kwargs):
        return Task.objects.all()
    
    def resolve_departments(self,info,**kwargs):
        return Department.objects.all()

    def resolve_role(self,info,**kwargs):
        return Role.objects.all()

    def resolve_position(self,info,**kwargs):
        return Position.objects.all()

    def resolve_domain(self,info,**kwargs):
        return Domain.objects.all()

    def resolve_domainmember(self,info,**kwargs):
        return DomainMember.objects.all()

    def resolve_application(self,info,**kwargs):
        return Application.objects.all()

    def resolve_submission(self,info,**kwargs):
        return Submission.objects.all()