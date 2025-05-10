import os

def rename_files_in_directory(directory, prefix):
    try:
        files = os.listdir(directory)
        count = 1

        for filename in files:
            file_path = os.path.join(directory, filename)
            if os.path.isfile(file_path):
                extension = os.path.splitext(filename)[1]
                new_name = f"{prefix}_{count}{extension}"
                new_path = os.path.join(directory, new_name)
                os.rename(file_path, new_path)
                print(f"Renamed: {filename} -> {new_name}")
                count += 1

        print("Renaming complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder_path = input("Enter the full path of the folder: ")
    file_prefix = input("Enter the prefix for new filenames: ")
    rename_files_in_directory(folder_path, file_prefix)