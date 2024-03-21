'''
    This script is just a test script that creates a file and write 'Goofy Goobers.' in it
'''

import os

network_drive_path = "X:\\"
file_content = "Goofy Goobers."

# Access the content of the network drive
try:
    # List files and directories in the network drive
    contents = os.listdir(network_drive_path)
    print(f"Contents of {network_drive_path}:")
    for item in contents:
        print(item)

    # Create a text file in the network drive
    file_path = os.path.join(network_drive_path, "test.txt")
    with open(file_path, "w") as file:
        file.write(file_content)
        print(f"Text file created at: {file_path}")

except OSError as e:
    print(f"Error accessing {network_drive_path}: {e}")
