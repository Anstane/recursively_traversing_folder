import os


def recursive_print(path, indent=''):
    """Function that prints the tree of folders."""

    if os.path.isdir(path):
        print(indent + os.path.basename(path) + '\\')

        items = os.listdir(path)

        for item in items:
            item_path = os.path.join(path, item)
            
            if os.path.isdir(item_path):
                recursive_print(item_path, indent + '    ')

            else:
                print(indent + '    ' + item)             


if __name__ == '__main__':
    recursive_print(path='C:\\Development\\algorithms')
