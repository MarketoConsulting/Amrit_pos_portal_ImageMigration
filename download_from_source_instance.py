'''
Customer: PosPortal
Source Account String: posportal
Destination Account String: osf

Summary:
This project will migrate Images from old instance to new instance

Detailed documents can be found here https://github.com/MarketoConsulting/marketo_migration
'''

from marketo_migration.marketo_export import MarketoExport

# instance 'posportal'
src_munchkin_id = "744-ING-119"  # EDIT
client_id = "76912e30-329c-4dff-8c14-fc13f2ca9b3a"  # EDIT
client_secret = "jVkt2yHHZvqwKG4NYBSafNZhr5himUAX"  # EDIT

project_name = "posportal"  # EDIT
project_version = 1  # EDIT
download_object = MarketoExport(src_munchkin_id, client_id, client_secret, project_name, project_version)

#number_of_folders = download_object.get_folders(clear=True)
#number_of_files = download_object.get_files()

list_of_records=[]
list_of_records.extend(download_object.mc.execute(method='browse_folders', root=15, maxDepth=50, maxReturn=200))
column_names = ['id', 'name', 'folderId_type', 'description', 'folderType', 'createdAt', 'updatedAt', 'path',
                'isSystem', 'url', 'workspace', 'isArchive', 'parent_id', 'parent_type', 'accessZoneId']
folders_created = download_object.process_records('folder', column_names, list_of_records=list_of_records)

#initially get all the folders and files. Then check if Images and Files folder have come in the folder or not.
#if not, then use the list_records[] piece of code to get the data in the DB

#def get_folders():
    # 1 Lead Database, 2 Design Studio, 3 Marketing Activities, 4 Analytics
#    list_of_records = download_object.mc.execute(method='browse_folders', root=18, maxDepth=50, maxReturn=200)
#    column_names = ['id', 'name', 'folderId_type', 'description', 'folderType', 'createdAt', 'updatedAt', 'path',
#                    'isSystem', 'url', 'workspace', 'isArchive', 'parent_id', 'parent_type', 'accessZoneId']
#    folders_created = download_object.process_records('folder', column_names, list_of_records=list_of_records)
#    return len(folders_created)

#folder_count = get_folders()
#print('%s folders downloaded'.format(folder_count,))