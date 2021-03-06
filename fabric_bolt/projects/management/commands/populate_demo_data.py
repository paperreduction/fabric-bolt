from django.core.management.base import BaseCommand

from fabric_bolt.hosts.models import Host
from fabric_bolt.projects.models import Project, Stage, Configuration


class Command(BaseCommand):

    def handle(self, *args, **options):
        project = Project.objects.create(
            name='Demo Project',
            description='This is a demo project for for testing and development purposes. '
                        'This was generated by running fabric-bolt populate_demo_data.',

        )

        stage = Stage.objects.create(
            project=project,
            name='Demo Stage',

        )

        host = Host.objects.create(
            name='sandbox.fabricbolt.io',
            alias='Demo Host',
        )

        stage.hosts.add(host)

        Configuration.objects.create(
            stage=stage,
            project=project,
            key='comment_text',
            task_name='update_sandbox_site',
            data_type=Configuration.STRING_TYPE,
            prompt_me_for_input=True,
            task_argument=True,
        )
