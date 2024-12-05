import os

def delete_files():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".md"):
                os.remove(os.path.join(root, file))

delete_files()