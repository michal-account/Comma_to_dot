import os
from os.path import join

char1 = ','
char2 = '.'

def comma_to_dots(file_name):

    if not os.path.isfile(original_file_path):
        print('File does not exist.')
        exit()
        
    with open(file_name, 'r') as file:
        txt = file.read()

    converted_file = txt.replace(char1, char2)

    return converted_file


def create_new_file(file_content):

    print('Creating a new file')
    path = input('Enter the path where you want to save your new file: ')
    name = input('Type the name of your new file: ')
    file_path = join(path, name)

    try:
        with open(file_path, 'w') as file:
            file.write(file_content)
        print('New file created')
    except Exception as e:
        print(f'Something went wrong during file creation: {e}')

original_file_path = input('Enter the path to file that you want to convert: ')

converted_file = comma_to_dots(original_file_path)

if converted_file:
    create_new_file(converted_file)
else:
    print('No conversion performed.')