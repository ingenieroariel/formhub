from main.tests.test_base import MainTestCase
from odk_logger import sample_data_tools
import os
from django.conf import settings
from odk_viewer.models.data_dictionary import DataDictionary

class TestSampleData(MainTestCase):
    def setUp(self):
        MainTestCase.setUp(self)

    def test_publish_xls_form(self):
        path_to_xls = os.path.join(settings.PROJECT_ROOT, "odk_logger", "fixtures", "test_forms", "tutorial.xls")
        sample_data_tools.publish_xls_form(self.user, path_to_xls, True, True)

        self.assertEqual(DataDictionary.objects.count(), 1)