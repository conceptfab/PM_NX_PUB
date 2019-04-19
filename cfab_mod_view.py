'''
Moduł zawierający widoki list
'''
import logging
import os

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


# logging.disable(logging.CRITICAL)

# TODO dodać kolory


def view_projects_list(projects_dict):
    '''
    Krótka lista projektów
    :param projects_dict: słownik projektu
    :return:
    '''
    logging.debug('cfab_mod_view: view_projects_list / short list')
    null_list = []
    print('\n')
    print('Lista projektów:' + '\n')  # TODO dodać do stringów
    if projects_dict != null_list:
        # Wyswietlam prosta liste projektów
        for projects in projects_dict:
            print('  ' + projects['prj_number'] +
                  ' ' + projects['prj_client'] +
                  ' ' + projects['prj_name'] +
                  ' | ' + projects['prj_desc'])
    elif projects_dict == null_list:
        # Nie wyświetlam listy
        print("NULL")  # TODO dopisac komentarz
        return
    print('\n')


def view_long_projects_list(path, projects_dict):
    '''
    Długa lista projektów
    :param path: ścieżka projektu to mierzenia MB
    :param projects_dict: słownik projektu
    :return: wyświetla liste
    '''
    logging.debug('cfab_mod_view: view_projects_list / short list')
    null_list = []
    print('\n')
    print('Rozszerzona lista projektów:' + '\n')  # TODO dodać do stringów

    if projects_dict != null_list:
        # Wyswietlam prosta liste projektów
        for projects in projects_dict:
            start_path = path + '/' + projects['prj_full_name']  # TODO dodać do stringów
            print(projects['prj_number'] +
                  ' | ROK: ' + projects['prj_year'] +
                  ' | KOD: ' + projects['prj_code'] +
                  ' | ROZMIAR FOLDERU: ' +
                  (str(get_size(start_path)) + ' MB'))
            print('    KLIENT: ' + projects['prj_client'] + ' | NAZWA: ' + projects['prj_name'])
            print('    OPIS: ' + projects['prj_desc'])
            # print('    STATUS: ' + projects['prj_status']
            print('    STATUS: ' + (str(get_status(start_path)))
                  + ' | BUDŻET: ' + projects['prj_budget']
                  + ' | TERMIN: ' + projects['prj_term'])
            print('')


    elif projects_dict == null_list:
        # Nie wyświetlam listy
        print("NULL")
    print('\n')


def get_size(start_path):
    '''
    Funkcja sprawdza ile MB zajmuje projekt
    :param start_path: sciezka projektu
    :return:
    '''
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            total_size += os.path.getsize(file_path)
    total_size = total_size / 1000 / 1000
    total_size = round(total_size, 2)
    if total_size == 0:
        total_size = ' - - '
    return total_size


def get_status(real_path):
    '''
    Funckja sprawdza czy folder projektu istnieje
    @param real_path: sciezka do dolderu
    @return:
    '''
    if os.path.isdir(real_path) is False:
        status = 'Nieaktywny/Archiwalny'
    else:
        status = 'Aktywny'
    return status
