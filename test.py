import os

def delete_tmpfiles(directory):
    """Recursively delete all .tmpfile files in the given directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".tempfile"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    directory = "./"  # Change this to your target directory
    if os.path.exists(directory) and os.path.isdir(directory):
        delete_tmpfiles(directory)
    else:
        print("Directory does not exist or is not a valid directory.")
