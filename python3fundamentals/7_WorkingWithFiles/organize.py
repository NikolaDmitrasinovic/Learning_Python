import os
import shutil

# Define the directory to organize
directory_to_organize = "your/target/folder"  # Change this to your target folder
print("path:", directory_to_organize)

# Define file type categories and their extensions
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

# Create subfolders for each category if they don't already exist
def create_subfolders():
    for category in file_categories:
        category_folder = os.path.join(directory_to_organize, category)
        print("Folder:", category_folder)
        os.makedirs(category_folder, exist_ok=True)

# Function to move files into respective folders based on their extension
def organize_files():
    for filename in os.listdir(directory_to_organize):
        file_path = os.path.join(directory_to_organize, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to corresponding category folder
        file_moved = False
        for category, extensions in file_categories.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                dest_folder = os.path.join(directory_to_organize, category)
                print(directory_to_organize, dest_folder)
                #shutil.move(file_path, os.path.join(dest_folder, filename))
                file_moved = True
                break

        # Optional: Handle files with unknown extensions
        if not file_moved:
            print(f"Unknown file type for '{filename}'; left in original folder.")

# Run the functions
create_subfolders()
organize_files()

print("Files organized successfully.")

