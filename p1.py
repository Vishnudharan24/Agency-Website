import os

def change_file_extension(directory):
    # Get list of files in the directory
    files = os.listdir(directory)
    
    # Iterate through each file
    for file_name in files:
        # Check if the file ends with .php extension
        if file_name.endswith('.php'):
            # Rename the file with .html extension
            new_file_name = os.path.splitext(file_name)[0] + '.html'
            try:
                os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
                print("File '{}' renamed to '{}'".format(file_name, new_file_name))
            except Exception as e:
                print("Error renaming file '{}': {}".format(file_name, str(e)))

# Get the current working directory
current_directory = os.getcwd()

# Call the function to change file extensions
change_file_extension(current_directory)
