import os

# remove all files from the "/vids" directory
for filename in os.listdir("vids"):
    file_path = os.path.join("vids", filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# remove all files from the /out" directory
for filename in os.listdir("out"):
    file_path = os.path.join("out", filename)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

# clear contents of the "list.txt" file
with open("list.txt", "w") as f:
    f.write("")

# clear contents of the "out.txt" file
with open("out.txt", "w") as f:
    f.write("")
