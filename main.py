import sys, time, os, shutil
from pathlib import Path

# Get arguments
files = sys.argv[1:]

valid_files = []


if len(files) > 1:
    for file in files:
        path = Path(file)

        if path and path.is_file():
            valid_files.append(path)
else:
    
    directory = ""
    valid_dir = False
    
    while not valid_dir:
        
        directory = input("Enter directory: ")
        if os.path.isdir(directory):
            
            directory = Path(directory)
            files_tmp = []
            
            for file in directory.iterdir():
                if file.is_file():
                    files_tmp.append(file)

            print("\nFound files:", len(files_tmp))
            print("Preview (3)", files_tmp[:3])

            if input("\nWould you like to use these files? (y/n) ") == "y":
                valid_dir = True
                valid_files = files_tmp
                

# Sort the files based on name
def getValue(value):
    name = value.stem

    try:
        name = int(name)
    except Exception as err:
        print("Invalid name:", name)
        return name
    
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
