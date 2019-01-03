'''
Customer: PosPortal
Source Account String: posportal
Destination Account String: osf

Summary:
This project will migrate Images from old instance to new instance

Detailed documents can be found here https://github.com/MarketoConsulting/marketo_migration
'''

from marketo_migration.marketo_import import MarketoImport

# instance 'osf'
dest_munchkin_id = "905-CSJ-579"  # EDIT
client_id = "3ceb6d76-d103-4e11-9f95-0f8b633fb15d"  # EDIT
client_secret = "8xsyR1aAIbJsGxEVJWneyfiaBd8BDhTI"  # EDIT

# instance 'posportal'
src_munchkin_id = "744-ING-119"  # EDIT
src_client_id = "76912e30-329c-4dff-8c14-fc13f2ca9b3a"  # EDIT
src_client_secret = "jVkt2yHHZvqwKG4NYBSafNZhr5himUAX"  # EDIT

project_name = "posportal"  # EDIT
project_version = 1  # EDIT
import_object = MarketoImport(src_munchkin_id, dest_munchkin_id, client_id, client_secret, project_name, project_version)

#We can map the Images and Files (parent folder) in folder_ids also and set Recursive = true,
# then all the folders under the parent folder will also be mapped with images.

# But, if we have mapped sub folders individually, and when we are mapping the parent folder, ensure Recursive = false

#folder = import_object.import_folders(src_folder_id=15, dest_folder_id=34, mode='create_new',
#                                      nested=True, recursive=True)
folder_ids = [15]
import_object.import_files(folder_ids, start_at=0, recursive=True)