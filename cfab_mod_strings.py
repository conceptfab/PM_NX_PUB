'''
    Baza stringów
'''
import locale

from pref import colors


# TODO - uzupelnienie stringow
# TODO - moze tlumaczenie


def strings_list():
    '''

    :return:
    '''
    # language = locale.getdefaultlocale() na mac os jest błąd
    language = 'pl_PL'
    # print (locale.getdefaultlocale())
    language = language[0]
    if language == 'pl_PL':
        print("POLSKI")
        strings = strings_pl()

    else:
        strings = strings_pl()  # domyślny zestaw stringów

    return strings


def strings_pl():
    '''

    :return:
    '''
    color = colors()
    strings = [
        color[0] + '...Uruchamiam CONCEPTFAB PM NX 0.4 DEV',  # 0
        color[3] + ' Plik ustawień istnieje: ',# 1
        color[4] + ' Błąd: Plik z ustawieniami nie istnieje',  # 2
        color[1] + ' Tworzę pusty plik z ustawieniami',  # 3
        color[1] + ' Uzupełnij plik ustawień i uruchom program ponownie', # 4
        color[1] + ' Czytam plik: ',  # 5
        color[1] + ' Błąd: Nie znaleziono folderu projektów ',  # 6
        color[1] + ' Brakuje listy projektów.\nTworzę nową - pustą. ',  # 7
        color[1] + ' \nKatalog projektów: ', # 8
        color[1] + ' Lista projektów: ',  # 9
        color[1] + ' Czy chcesz dodać nowy projekt? ',  # 10
        color[1] + ' ( T )',  # 11
        color[1] + ' Aktualizować listę projektów? ',  # 12
        color[1] + ' ( A )',  # 13
        color[1] + ' Czy opuścić program? ',  # 14
        color[1] + ' ( Q )',  # 15
        color[1] + ' Jaki jest Twój wybór?  ',  # 16
        color[1] + ' | Status projektu: ',  # 17
        color[1] + ' Data utworzenia: ',  # 18
        color[1] + ' Termin zakończenia ',  # 19
        color[1] + ' Projekt po terminie',  # 20
        color[1] + ' Aktywny ',  # 21
        color[1] + ' Nieaktywny ',  # 22
        color[1] + ' W archiuwm',  # 23
        color[1] + ' Budżet',  # 24
        color[1] + ' Rozmiar',  # 25
        color[1] + ' Wyświetlić rozszerzoną listę projektów? ',  # 26
        color[1] + ' ( W )',  # 27
        color[1] + ' NULL ',  # 28
        color[1] + ' NULL ',  # 29
        color[1] + ' NULL ',  # 30
        color[1] + ' Długa lista: ',  # 31
        color[1] + ' Zamykam program',  # 32
        color[1] + ' Dokonaj wyboru:',  # 33
        color[1] + ' Tworzę nowy projekt:',  # 34
        color[1] + ' Numer projektu: ',  # 35
        color[1] + ' Rok: ',  # 36
        color[1] + ' Podaj nazwę klienta: ',  # 36
        color[1] + ' Wprowadzono: ',  # 37
        color[1] + ' Podaj nazwę projektu: ',  # 38
        color[1] + ' Podaj termin realizacji: ',  # 39
        color[1] + ' Podaj budzet realizacji: ',  # 40
        color[1] + ' Info: ',  # 41
        color[1] + ' NULL ',  # 42
        color[1] + ' NULL ',  # 43
        color[1] + ' NULL ',  # 44
        color[1] + ' Folder projektu został utworzony',  # 45
        color[1] + ' ERROR: Nie utworzono folderu. Folder o takiej nazwie już istnieje',  # 46
        color[1] + ' Folder projektów istnieje',  # 47
        color[1] + ' ...Folder projektów istnieje...',  # 48
        color[1] + ' ...Plik listy projektów istnieje...',  # 49
        color[1] + ' BŁĄD: plik nie został znaleziony: ',  # 50
        color[1] + ' Dodano projekt do Todoist: ',  # 51
        color[1] + ' BŁĄD: Zawartość pliku jest nieprawidłowa ',  # 52
        color[1] + ' BŁĄD: JSON FileNotFoundError',  # 53
        color[1] + ' BŁĄD: JSON TypeError',  # 54
        color[1] + ' Lista projektów została zaaktualizowana',  # 55
        color[1] + ' Dodano projekt do Todoist: ',  # 56
    ]
    return strings
