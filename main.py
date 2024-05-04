# # Connecting to Google Drive
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import input_entry
import check_creds
from quickstart import friday

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

# # Take input master_folder and file_folder from user(CR)
# [master_folder, file_folder, roll_no]
folder_name_list = input_entry.input_entries() 

# # View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == folder_name_list[0]): # Access master_folder
      fileID = file['id']
      print("TEST folder id: ", fileID)
      break

# # Accessing files in folders
fileList = drive.ListFile({'q': f"'{fileID}' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
   # Get the folder ID that you want
  if(file['title'] == folder_name_list[1]): # Access file_folder
      fileID = file['id']
      print("inside folder id: ", fileID)
      break

fileList = drive.ListFile({'q': f"'{fileID}' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
   # Get the folder ID that you want
  if(check_creds.check_name(file['title'], folder_name_list[2])): # Access the specific file
      fileID = file['id']
      print("the person's file id: ", fileID)
      file2 = drive.CreateFile({'id': fileID}).Trash()
      break
# Initialize GoogleDriveFile instance with file id.
# file2 = drive.CreateFile({'id': fileID})
# file2.Trash()  # Move file to trash.
# file2.UnTrash()  # Move file out of trash.
# file2.Delete()  # Permanently delete the file.

# # Google Form Response Deletion
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the file ID that you want
  if(file['title'] == folder_name_list[0]): 
      fileID = file['id']
      print("TEST folder id: ", fileID)
      break