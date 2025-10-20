import random
# данные, используемые в тестах
new_correct_user = {'name': 'Evgeniya',
                    'e-mail': 'evgeniya_shimkova33fs'+str(random.randint(100, 999)) + '@ya.ru',
                    'password': str(random.randint(100000, 999999))}
new_user_wrong_password = {'name': 'Evgeniya',
                           'e-mail': 'evgeniya_shimkova33fs' + str(random.randint(100, 999)) + '@ya.ru',
                           'password': str(random.randint(10000, 99999))}
registered_user = {'name': 'Evgeniya',
                   'e-mail': 'evgeniya_shimkova33fs678@ya.ru',
                   'password': '123456'}

incorrect_password_text = 'Некорректный пароль'