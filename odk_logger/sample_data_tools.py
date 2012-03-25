from odk_viewer.models.data_dictionary import DataDictionary
from odk_logger import import_tools

def publish_xls_form(user, path_to_xls, shared=False, shared_data=False):
    xlsFile = import_tools.django_file(path_to_xls, "xls_file", "application/xls")
    return DataDictionary.objects.create(
        user=user,
        xls=xlsFile,
        shared=shared,
        shared_data=shared_data
    )