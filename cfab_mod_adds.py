'''
Funkcje dodatkowe: wysłanie projektu do TODOIST, wysłanie maila przez gmail
'''
from email.mime.text import MIMEText
from random import randint
from smtplib import SMTP_SSL as SMTP


from pytodoist import todoist


def addtodoist(project_dict, login, password):
    '''
    Funkcja wysyła do projekt do TODOIST
    :param project_dict: słownik projektu
    :param login: login
    :param password: hasło
    :return:
    '''

    prj_todoist = project_dict['prj_full_name'].replace('_', ' ')

    user = todoist.login(login, password)
    rnd = randint(0, 21)

    if rnd == 0:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_GREEN)
    elif rnd == 1:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_PINK)
    elif rnd == 2:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_ORANGE)
    elif rnd == 3:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_GOLD)
    elif rnd == 4:
        user.add_project(prj_todoist, color=todoist.ProjectColor.PALE_BLUE)
    elif rnd == 5:
        user.add_project(prj_todoist, color=todoist.ProjectColor.PALE_BROWN)
    elif rnd == 6:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_PINK)
    elif rnd == 7:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_GRAY)
    elif rnd == 8:
        user.add_project(prj_todoist, color=todoist.ProjectColor.PALE_RED)
    elif rnd == 9:
        user.add_project(prj_todoist, color=todoist.ProjectColor.YELLOW_ORANGE)
    elif rnd == 10:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIGHT_AQUA)
    elif rnd == 11:
        user.add_project(prj_todoist, color=todoist.ProjectColor.BRIGHT_CYAN)
    elif rnd == 12:
        user.add_project(prj_todoist, color=todoist.ProjectColor.BRIGHT_PINK)
    elif rnd == 13:
        user.add_project(prj_todoist, color=todoist.ProjectColor.CRIMSON)
    elif rnd == 14:
        user.add_project(prj_todoist, color=todoist.ProjectColor.ORANGE)
    elif rnd == 15:
        user.add_project(prj_todoist, color=todoist.ProjectColor.LIME_GREEN)
    elif rnd == 15:
        user.add_project(prj_todoist, color=todoist.ProjectColor.DARK_CYAN)
    elif rnd == 17:
        user.add_project(prj_todoist, color=todoist.ProjectColor.ARTIC_BLUE)
    elif rnd == 18:
        user.add_project(prj_todoist, color=todoist.ProjectColor.SKY_BLUE)
    elif rnd == 19:
        user.add_project(prj_todoist, color=todoist.ProjectColor.CORNFLOWER_BLUE)
    elif rnd == 20:
        user.add_project(prj_todoist, color=todoist.ProjectColor.BLACK)
    else:
        user.add_project(prj_todoist, color=todoist.ProjectColor.MEDIUM_GRAY)

    print('TODOIST - add project')  # TODO dodac do stringow


def send_email(project_dict, gmail, gpassword, tomail):
    '''
    Funkcja wysyła maila
    :param project_dict: słownik projektu
    :param gmail: adres gmail
    :param gpassword: hasło
    :param tomail: adres odbiorcy
    :return:
    '''

    fromaddr = gmail
    msg = MIMEText(project_dict['prj_desc'], 'plain')
    toaddr = tomail
    msg['To'] = toaddr
    msg['Subject'] = project_dict['prj_full_name']

    server = SMTP('smtp.gmail.com')
    server.login(fromaddr, gpassword)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    print('SEND MAIL')  # TODO dodac do stringow
