from data_collector import collect_data
from trainer import train_recognizer
from recognizer import recognize_people

people_path = '../../../Desktop/temp/Data/People'
faces_path = '../../../Desktop/temp/Data/Faces'
databases_path = '../../../Desktop/temp/Data/Database'
source_path = '../../../Desktop/temp/Data/Source'
lbph_database = 'LBPH_database.yml'
fisher_database = 'Fischer_database.yml'
face_width = 500
face_height = 500

print('What do you want to do?')
while True:
    command = input('Enter command >> ')

    if command == 'help':
        print(' CD - collect data\n'
              ' TR - train recognizer\n'
              ' RP - recognize people\n'
              ' exit - exit the program')
    elif command == 'CD':
        collect_data(people_path, faces_path)
    elif command == 'TR':
        train_recognizer(faces_path, databases_path, face_width, face_height)
    elif command == 'RP':
        recognize_people(databases_path, fisher_database, lbph_database, source_path, face_width, face_height)
    elif command == 'exit':
        break
    else:
        print(" Wrong command! Enter 'help' to see all commands")

print(" Exiting Program")
