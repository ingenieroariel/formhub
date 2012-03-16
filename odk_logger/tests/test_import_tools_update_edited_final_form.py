from main.tests.test_base import MainTestCase
#from django.test import TestCase
from odk_logger.models import Instance
import os
import glob

from odk_logger.import_tools import import_instances_from_zip

CUR_PATH = os.path.abspath(__file__)
CUR_DIR = os.path.dirname(CUR_PATH)
DB_FIXTURES_PATH_UNFINISHED = os.path.join(CUR_DIR, 'data_from_sdcard_unfinished')
DB_FIXTURES_PATH_FINISHED = os.path.join(CUR_DIR, 'data_from_sdcard_finished')

from django.conf import settings


def images_count(username="bob"):
    images = glob.glob(os.path.join(settings.MEDIA_ROOT, username, 'attachments', '*'))
    return len(images)


class TestImportingEditedFinalizedDatabase(MainTestCase):
    def setUp(self):
        MainTestCase.setUp(self)
        self._publish_xls_file(
                               os.path.join(settings.PROJECT_ROOT, \
                                    "odk_logger", "fixtures", "test_forms", "tutorial.xls"))
    
    def tearDown(self):
        # delete everything we imported
        Instance.objects.all().delete() # ?
        if settings.TESTING_MODE:
            images = glob.glob(os.path.join(settings.MEDIA_ROOT, 'attachments', '*'))
            for image in images:
                os.remove(image)
            
    def test_updating_unfinished(self):
        import_instances_from_zip(os.path.join(DB_FIXTURES_PATH_UNFINISHED, "bulk_submission.zip"), self.user)
        import_instances_from_zip(os.path.join(DB_FIXTURES_PATH_FINISHED, "bulk_submission.zip"), self.user)
        instance_count = Instance.objects.count()
        self.assertEqual(instance_count, 1)
 