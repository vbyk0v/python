import random
import string




class Email:
    ##генерация случайного пароля
    def email_generator(self):
        password = ''
        for i in range (random.randint(6, 20)):
            t = random.choice(string.ascii_letters[0:10])
            password = password + str(t)

    ##генерация случайного логина
        login = ''
        for i in range(random.randint(3, 20)):
            t = random.choice(string.ascii_letters[0:10])
            login = login + str(t)

        domain_name = ['@mail.ru',
                       '@yandex.ru',
                       '@outlook.com',
                       '@google.com']
        #склеивание логина + домен + пароль
        email_full = login + str(domain_name[random.randint(0, 3)]) + ":" + password
        return email_full

class EmailPrepare():
    def __init__(self, txt):
        self.txt = txt

    def email_for_check(self):
        lines_ru = []
        lines_com = []
        with open(str(self.txt)) as file:
            lines = file.read().splitlines()

        for i in range(len(lines)):
            if "ru" in lines[i]:
                lines_ru.append(lines[i])
            elif "com" in lines[i]:
                lines_com.append(lines[i])
        return lines_ru, lines_com

class EmailChecker():
    #тут я играюсь с default вместо self для понимания
    def __init__(default, email):
        default.email = email
        default.login = email.split('@')[0] # тут какая то магия
        default.password = email.split(':')[1] # из интернета
        default.smtp = 'smtp'


    def knock_knock(default):
        print("\n\n"
              "============")
        print("mail = ", default.email)
        print ('default_login = ', default.login)
        print('default_password = ', default.password)
        print('default.smtp = ', default.smtp)

        #эмулятор соединения, так на яндекс я зайти не могу
        connection = len(default.login) \
                     + len(default.password) \
                     + len(default.smtp)

        success = connection - random.randint(0, 100)
        if success >= 5:
            print('=============\n'
                  'success login!')
            return True
        elif success < 5:
            print('=============\n'
                  'bad login!')
            return False


class MakeResult:
    def __init__(default, email_list, txt):

        default.email_list = email_list
        default.txt = txt

    def write_email(default):
        with open(default.txt, 'w') as file:
            for email in default.email_list:
                file.write("%s\n" % email)
