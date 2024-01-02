import os
import shutil


def recursive_copy(origin, target):
    """A function for recursively copying files from a repository."""

    if not os.path.isdir(origin):
        raise Exception(f'Specify the path to the repository with the files. Current path: {origin}')
    
    folders = os.listdir(origin) # Create a variable with repository elements.

    for item in folders: # Iterate through the objects in the repository.
        inside_folder = origin + '\\' + item

        if os.path.isdir(inside_folder): # If the object is a folder, we fall into it.
            recursive_copy(inside_folder, target)

        else:
            shutil.copy(inside_folder, target) # Otherwise, copy the object.


if __name__ == '__main__':
    recursive_copy(origin='C:\\Development\\iphone_photo\\copy', target='C:\\Development\\iphone_photo\\insert')
    print('Success!')
