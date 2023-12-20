import os
import shutil

def organize_files(directory):
    # Create folders for different file types if they don't exist
    folders = ['Images', 'Documents', 'Videos', 'Others']
    for folder in folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Get a list of all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        file_path = os.path.join(directory, file)

        # Check the file type based on the extension
        _, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        # Define the destination folder based on the file type
        if file_extension in ['.jpg', '.png', '.gif', '.jpeg']:
            destination_folder = os.path.join(directory, 'Images')
        elif file_extension in ['.doc', '.docx', '.pdf', '.txt']:
            destination_folder = os.path.join(directory, 'Documents')
        elif file_extension in ['.mp4', '.avi', '.mkv', '.mov']:
            destination_folder = os.path.join(directory, 'Videos')
        else:
            destination_folder = os.path.join(directory, 'Others')

        # Move the file to the appropriate folder
        shutil.move(file_path, os.path.join(destination_folder, file))

    print("Files organized successfully!")

# Replace 'your_directory_path' with the path to the directory you want to organize
directory_to_organize = r'C:\Users\kodur\OneDrive\Desktop\nk'
organize_files(directory_to_organize)
