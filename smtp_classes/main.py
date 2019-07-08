import smtp_classes.classes



##генератор почт в текстовый файл, на выходе дает логин + домен + пароль
def generate_emails_to_txt(number):
    email_list = []
    for n in range(number):
        new_email = smtp_classes.classes.Email()#создаем экземпляр класса
        new_email = new_email.email_generator() #обращаеся к методу созданного экземпляра
        email_list.append(new_email) # добавляем в список
    with open('email.txt', 'w') as file: # пишем в файл сгенерированные почты
        for email in email_list:
            file.write("%s\n" % email)


if __name__ == "__main__":
    generate_emails_to_txt(number = 20) # генерация почтовых ящиков
    check = smtp_classes.classes.EmailPrepare(txt='email.txt') # "типа разделение на потоки" на ру и ком зоны
    check_ru, check_com = check.email_for_check() # формируем\фильтруем сгенерированны ящика на ру и ком зоны
    print('check_ru = ', check_ru)
    print('check_com =', check_com)
    good_email_ru = []
    bad_email_ru = []
    good_email_com = []
    bad_email_com = []

    #каждый ящик засовываем в класс и проверяем
    for i in range(len(check_ru)):
        email_to_check_ru = smtp_classes.classes.EmailChecker(email = check_ru[i])#
        check_ok = email_to_check_ru.knock_knock()
        if check_ok:
            good_email_ru.append(check_ru[i])
        else:
            bad_email_ru.append(check_ru[i])



    for j in range(len(check_com)):
        email_to_check_com = smtp_classes.classes.EmailChecker(email=check_com[j])
        check_ok = email_to_check_com.knock_knock()
        if check_ok:
            good_email_com.append(check_ru[j])
        else:
            bad_email_com.append(check_ru[j])

    print('\n'
          '================\n'
          'results\n'
          '================\n')
    print('bad_email_ru = ', bad_email_ru)
    print('good_email_ru =', good_email_ru)
    print('bad_email_com = ', bad_email_com)
    print('good_email_com =', good_email_com)

    to_do_1 = smtp_classes.classes.MakeResult(email_list=bad_email_ru, txt = 'bad_email_ru.txt')
    to_do_1.write_email()

    to_do_2 = smtp_classes.classes.MakeResult(email_list=good_email_ru, txt = 'good_email_ru.txt')
    to_do_2.write_email()

    to_do_3 = smtp_classes.classes.MakeResult(email_list=bad_email_com, txt = 'bad_email_com.txt')
    to_do_3.write_email()

    to_do_4 =smtp_classes.classes.MakeResult(email_list=good_email_com, txt = 'good_email_com.txt')
    to_do_4.write_email()
