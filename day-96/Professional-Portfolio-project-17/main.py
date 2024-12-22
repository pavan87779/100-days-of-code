import os
import shutil

# Define paths for Downloads and the subfolders
downloads_path = os.path.expanduser('~/Downloads')

folder_mapping = {
    'pdf': 'Assignments',
    'pptx': 'Lectures',
    'py': 'Python',
    'txt': 'TextFiles',
    'docx': 'Documents'
}

# Create subfolders if they don't exist
for folder in folder_mapping.values():
    folder_path = os.path.join(downloads_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to move files to the appropriate folder
def organize_files():
    for file_name in os.listdir(downloads_path):
        file_path = os.path.join(downloads_path, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension and check if it's in the mapping
        file_extension = file_name.split('.')[-1].lower()

        if file_extension in folder_mapping:
            folder_name = folder_mapping[file_extension]
            destination_folder = os.path.join(downloads_path, folder_name)
            destination_path = os.path.join(destination_folder, file_name)

            # Check if file already exists in destination folder
            if os.path.exists(destination_path):
                print(f"File {file_name} already exists in {folder_name}, skipping...")
                continue

            try:
                # Move file to the corresponding folder
                shutil.move(file_path, destination_path)
                print(f"Moved {file_name} to {folder_name}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

# Run the file organization function
organize_files()
