import sys, time, os, shutil
from pathlib import Path

# Get arguments
files = sys.argv[1:]


# Verify all arguments are valid files
valid_files = []

for file in files:
    path = Path(file)

    if path and path.is_file():
        valid_files.append(path)


# Sort the files based on name
def getValue(value):
    name = value.stem
    return int(name)

# Options to reverse because Blender sometimes likes it backwards
valid_files.sort(key=getValue, reverse=False)


# Create a temporary directory
output_dir = "output_" + str(int(time.time()))
os.makedirs(output_dir)

print("Created output folder:", output_dir)


# Copy and rename files
for i in range(len(valid_files)):

    file = valid_files[i]

    src = file.resolve()
    dst = output_dir + "\\" + str(i) + file.suffix
    shutil.copy2(src, dst)

print("Finished copying files.")
