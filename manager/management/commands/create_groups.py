from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from base.models import Candidate
from application.models import Application
from jobs.models import Job
from manager.models import HRManager

class Command(BaseCommand):
    help = 'Create default groups and permissions'

    def handle(self, *args, **kwargs):
        # Define groups and their permissions
        groups = {
            'HRAdmin': [
                'add_hrmanager', 'change_hrmanager', 'delete_hrmanager', 'view_hrmanager', 
                'add_candidate', 'change_candidate', 'delete_candidate', 'view_candidate',
                'add_application', 'change_application', 'delete_application', 'view_application',
                'add_job', 'change_job', 'delete_job', 'view_job'
            ],
            'HR': [
                'view_hrmanager', 'add_candidate', 'change_candidate', 'view_candidate', 
                'add_application', 'change_application', 'view_application', 
                'add_job', 'change_job', 'view_job'
            ],
            'HREmp': [
                'view_hrmanager', 'view_candidate', 'view_application', 'view_job'
            ]
        }

        # Ensure content types for all models exist
        models = [Candidate, Application, Job, HRManager]
        for model in models:
            content_type = ContentType.objects.get_for_model(model)
            if not content_type:
                self.stdout.write(self.style.ERROR(f'ContentType for {model} not found'))

        for group_name, permissions in groups.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Group {group_name} created'))
            else:
                self.stdout.write(self.style.WARNING(f'Group {group_name} already exists'))

            # Add permissions to group
            for perm in permissions:
                app_label, codename = perm.split('_', 1)
                try:
                    permission = Permission.objects.get(codename=codename)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission {perm} not found'))

        self.stdout.write(self.style.SUCCESS('Groups and permissions have been set up successfully'))
