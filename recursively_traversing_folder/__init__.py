# Script for copying the contents of repository folders to another repository.

# Operating logic:
# 1) The path to the source repository is transferred to the 'origin' variable
# 2) The path to the repository is passed where we will copy the contents of the folders - the 'target' variable
# 3) Recursively traverse 'origin', copying the contents until we go through all the elements
# 4) Display a message that the copying has been completed

# Mini project for learning recursion.

# shutil.copytree('C:\Development\iphone_photo\photo_to_copy', 'C:\Development\iphone_photo\photo_to_insert')
# The function copies the entire contents of one directory to another without changes.
