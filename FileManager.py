import os
import shutil


download_folder =r'C:\Users\Fathima Fazlina\OneDrive\Desktop\HTML'
destination_folder =r'C:\Users\Fathima Fazlina\OneDrive\Desktop\organized'

folders = ['Images', 'Documents', 'Audio', 'Videos', 'Others']

for folder in folders:
    os.makedirs(os.path.join(destination_folder, folder), exist_ok=True)

for filename in os.listdir(download_folder):
    if os.path.isfile(os.path.join(download_folder, filename)):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(os.path.join(download_folder, filename), os.path.join(destination_folder, 'Images', filename))
        elif filename.endswith(('.pdf', '.docx', '.txt')):
            shutil.move(os.path.join(download_folder, filename), os.path.join(destination_folder, 'Documents', filename))
        elif filename.endswith(('.mp3', '.wav')):
            shutil.move(os.path.join(download_folder, filename), os.path.join(destination_folder, 'Audio', filename))
        elif filename.endswith(('.mp4', '.avi')):
            shutil.move(os.path.join(download_folder, filename), os.path.join(destination_folder, 'Videos', filename))
        else:
            shutil.move(os.path.join(download_folder, filename), os.path.join(destination_folder, 'Others', filename))

print("Files organized successfully!")