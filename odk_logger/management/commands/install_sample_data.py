from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
import settings
import os
import glob
from odk_viewer.models.data_dictionary import DataDictionary
from odk_logger import import_tools
from odk_logger.sample_data_tools import publish_xls_form

class Command(BaseCommand):
    args = '<username>'
    help = 'Install sample data and associate it with username'
    id_string = "good_eats" # id_string of the sample file we would like to install

    def handle(self, *args, **options):
        fixtureDir = os.path.join(settings.PROJECT_ROOT, "odk_logger", "fixtures", "sample_data")
        try:
            username = args[0]
        except IndexError:
            raise CommandError("You must specify the username to associate with the sample data as an argument")

        # check if user exists
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError("You must create a user with username '%s'" % username)

        # check if data already exists
        dd = DataDictionary.objects.filter(id_string=self.id_string, user__username=username)
        if(dd):
            # looks like sample data is already installed we could clear and re-install, for now we exit
            self.stdout.write("Sample data is already installed..\n")
        else:
            # publish the form
            path_to_xls = os.path.join(fixtureDir, self.id_string, "forms", self.id_string + ".xls")
            dd = publish_xls_form(user, path_to_xls, shared=True, shared_data=True)

            # install sample response data
            instanceDir = os.path.join(fixtureDir, self.id_string, "instances/*")

            # each directory contains an instance plus its attachments
            for file in glob.glob(instanceDir):
                if(os.path.isdir(file)):
                    self.stdout.write("Installing instance from %s\n" % file)
                    import_tools.import_instance(file, "submitted_via_web", user)
