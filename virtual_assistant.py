import datetime
import random
import json
date_time = datetime.datetime.now()
true_log = 'erdemas'
true_pass = 2736
user_info = dict()
users_notes = dict()
def save_user_info(user_info):
    with open('user_info.json', 'w') as file:
        json.dump(user_info, file)
def load_user_info():
    with open('user_info.json', 'r') as file:
        global user_info
        if json.load(file):
            user_info = json.load(file)
def menu():
    print('1 - калькулятор')
    print('2 - дата и время')
    print('3 - игры')
    print('4 - заметки')
def add_note(title, text):
    global users_notes
    users_notes[title] = text
    print('Заметка успешно добавлена!')
def display_notes():
    if len(users_notes) == 0:
        print('заметок нету')
    else:
        for title, text in users_notes.items():
            print(f'{title}: {text}')
def delete_note():
    if len(users_notes) == 0:
        print('тебе нечего удалять:)')
    else:
        display_notes()
        choice = input('выбери заметку которую хочешь удалить')
        if choice in users_notes.keys():
            del users_notes[choice]
            print('заметка удалена')
        else:
            print('такой заметки нет')
def save_notes():
    with open('users_notes.json', 'w') as file:
        json.dump(users_notes, file)
def update_notes():
    with open('users_notes.json', 'r') as file:
        global users_notes
        users_notes = json.load(file)
def menu_notes():
    while True:
        print('1 - добавить заметку')
        print('2 - посмотреть заметки')
        print('3 - удалить заметку')
        print('4 - закончить выбор')
        choice_notes = int(input('выбери-->'))
        while choice_notes not in(1, 2, 3, 4):
            print('извини,но такого выбора нету')
            choice_notes = int(input('выбери-->'))
        if choice_notes == 1:
            title = input('введи название заметки-->')
            text = input('введи текст заметки-->')
            add_note(title, text)
            save_notes()
        elif choice_notes == 2:
            display_notes()
        elif choice_notes == 3:
            delete_note()
            save_notes()
        elif choice_notes == 4:
            break
def main():
    update_notes()
print('перед тем как мной воспользоваться,пожалуйста введи свой пароль и логин')
user_log = input('ввести логин:')
user_pass = int(input('ввести пароль:'))
while user_log != true_log or user_pass != true_pass:
    print('похоже то-что вы ввели неправильные данные')
    user_log = input('введите логин:')
    user_pass = int(input('введите пароль:'))
else:
    print(f'')
menu()
print('выбери то-что тебе надо')
choice3 = int(input('напиши сюда-->'))
while choice3 not in (1, 2, 3, 4):
    print('извини,но такого выбора нету')
    choice3 = int(input('напиши сюда-->'))
if choice3 == 1:
    print('хорошо,ты выбрал калькулятор')
    print('выбери тогда для чего тебе нужен калькулятор')
    print('1 - обычный пример')
    print('2 - пример с тремя цифрами')
    print('3 - площадь квадрата,прямоугольника')
    print('4 - площадь треугольника')
    print('5 - таблица умножения')
    print('6 - среднее арифметическое оценок')
    choice_calculator = int(input('выбери то-что тебе нужно-->'))
    while choice_calculator not in (1, 2, 3, 4, 5, 6):
        print('извини,но такого выбора нету')
        choice_calculator = int(input('выбери то-что тебе нужно-->'))
    if choice_calculator == 1:
        print('хорошо,тогда что тебе нужно посчитать?')
        print('1 - сумма = +')
        print('2 - разность = -')
        print('3 - произвeдение = *')
        print('4 - частное = /')
        print('5 - степень')
        choice_calculator2 = int(input('выбери-->'))
        while choice_calculator2 not in (1, 2, 3, 4, 5):
            print('извини,но такого выбора нету')
            choice_calculator2 = int(input('выбери-->'))
        if choice_calculator2 == 1:
            print('хорошо,выбери тогда слогаемые')
            num1 = int(input('выбери первое слогаемое-->'))
            num2 = int(input('выбери второе слогаемое-->'))
            print(f'{num1+num2} ответ твоего примера')
        elif choice_calculator2 == 2:
            print('хорошо,выбери тогда слогаемые')
            num3 = int(input('выбери первое слогаемое-->'))
            num4 = int(input('выбери второе слогаемое-->'))
            print(f'{num3 - num4} ответ твоего примера')
        elif choice_calculator2 == 3:
            print('хорошо,выбери тогда слогаемые')
            num5 = int(input('выбери первое слогаемое-->'))
            num6 = int(input('выбери второе слогаемое-->'))
            print(f'{num5 * num6} ответ твоего примера')
        elif choice_calculator2 == 4:
            print('хорошо,выбери тогда слогаемые')
            num7 = int(input('выбери первое слогаемое-->'))
            num8 = int(input('выбери второе слогаемое-->'))
            print(f'{num7 / num8} ответ твоего примера')
        elif choice_calculator2 == 5:
            print('хорошо,выбери тогда слогаемые')
            num9 = int(input('выбери первое слогаемое-->'))
            num10  = int(input('выбери второе слогаемое-->'))
            print(f'{num9 ** num10} вот ответ твоего примера')
        else:
            print('такого варианта нету')
    elif choice_calculator == 2:
        print('хорошо,выбери тогда первый знак')
        print('+ - сложение')
        print('- - вычитание ')
        print('* - умножение')
        print('/ - деление')
        choice_calculator3 = input('напиши сюда первый знак-->')
        while choice_calculator3 not in ("+", "-", "*", "/",):
            print('извини,но такого выбора нету')
            choice_calculator3 = input('напиши сюда первый знак-->')
        if choice_calculator3 == '+' or '-' or '*' or '/':
            print('хорошо,тогда выбери второй знак')
            print('+ - сложение')
            print('- - вычитание ')
            print('* - умножение')
            print('/ - деление')
        choice_calculator4 = input('напиши сюда второй знак-->')
        while choice_calculator3 not in ("+", "-", "*", "/",):
            print('извини,но такого выбора нету')
            choice_calculator4 = input('напиши сюда первый знак-->')
        if choice_calculator3 == ('+') or ('-') or ('*') or ('/'):
            print('хорошо,теперь выбери числа')
            num11 = int(input('выбери первую цифру-->'))
            num12 = int(input('выбери вторую цифру-->'))
            num13 = int(input('выбери третью цифру-->'))
            example = str(num11) + choice_calculator3 + str(num12) + choice_calculator4 + str(num13)
            result = eval(example)
            print(result)
            print('это решение твоего примера')
        else:
            print('такого варианта нету')
    elif choice_calculator == 3:
        print('хорошо')
        print('вот напиши данные которые тебе нужны:')
        a1 = int(input('напиши длинну квадрата,прямоугольника-->'))
        b1 = int(input('напиши ширинну квадрата,прямоугольника-->'))
        print(f'{a1*b1} в квадрате,это площадь квадрата')
    elif choice_calculator == 4:
        print('хорошо,тогда напиши данные для площади треугольника')
        a2 = int(input('напиши основание треугольника'))
        h1 = int(input('напиши высоту треугольника'))
        print(f'{a2 * h1 / 2},вот площадь треугольника')
    elif choice_calculator == 5:
        for i in range(1, 11):
            for k in range(1, 10):
                print(f'{i} * {k} = {k * i}')
            print('--------------')
    elif choice_calculator == 6:
        subjects = ['Математика',
                        'Физика',
                        'Русс.яз',
                        'Лит. яз',
                        'Англ.яз',
                        'Физкультура',
                        'Биология',
                        'Информатика',
                        'Труды',
                        'Природа',
                        'География',
                        'Рисование',
                        'Химия',]
        grades = {}
        total = 0
        for subject in subjects:
            grade = int(input(f'введи среднюю оценку по {subject}: '))
            grades[subject] = grade
            total += grade
            print('твой оценки по предметам:')
            for subject, grade in grades.items():
                print(f'{subject}: {grade}')
        average = total / len(subjects)
        print(f'средняя годовая оценка:{average:.2f}')
    else:
        print('извини,но у меня пока-что нету вольше функций')
elif choice3 == 2:
    print('хорошо,тогда выбери то-что тебе надо')
    print('1 - только время')
    print('2 - только дата')
    print('3 - время с датой')
    choice_time = int(input('выбери то-что тебе нужно-->'))
    while choice_time not in (1, 2, 3):
        print('извини,но такого выбора нету')
        choice_time = int(input('выбери то-что тебе нужно-->'))
    if choice_time == 1:
        print(f'{date_time.time()} время сейчас')
    elif choice_time == 2:
        print(f'{date_time.date()} дата сегодня')
    elif choice_time == 3:
        print(f'{date_time} время и дата сейчас')
elif choice3 == 3:
    print('хорошо,вы выбрал игры')
    print('вот доступные игры:')
    print('1 - Камень-Ножницы-Бумага')
    print('2 - Орёл и Решка')
    print('3 - угадай число')
    print('4 - рандомные примеры')
    choice_game1 = int(input('выбери то-что ты хочешь-->'))
    while choice_game1 not in (1, 2, 3, 4):
        print('извини,но такого выбора нету')
        choice_game1 = int(input('выбери то-что тебе нужно-->'))
    if choice_game1 == 1:
        print('хорошо,ты выбрал игру:Камень-Ножницы-Бумага')
        print('1 - Камень')
        print('2 - Ножницы')
        print('3 - Бумага')
        choice_game2 = int(input('выбери то чем будешь ходить'))
        while choice_game2 not in (1, 2, 3):
            print('извини,но такого выбора нету')
            choice_game2 = int(input('выбери то-что тебе нужно-->'))
        comb = ['Камень','Ножницы','Бумага']
        user_choice = comb[choice_game2 - 1]
        bot_choice = random.randint(0, len(comb) - 1)
        bots_choice = comb[bot_choice]
        print(bots_choice, 'выбор ИИ')
        if user_choice == choice3:
            print('Ничья')
        elif (user_choice == 'Камень' and bots_choice == 'Ножницы') \
                or (user_choice == 'Ножницы' and bots_choice == 'Бумага') \
                or (user_choice == 'Бумага' and bots_choice == 'Камень'):
            print('Победа')
        else:
            print('Поражение')
    elif choice_game1 == 2:
        print('хороошо,ты выбрал игру:Орёл и Решка')
        print('1 - Орёл')
        print('2 - Решка')
        choice_game3 = int(input('выбер сторону-->'))
        while choice_game3 not in (1, 2):
            print('извини,но такого выбора нету')
            choice_game3 = int(input('выбери то-что тебе нужно-->'))
        variations = ['орёл', 'решка']
        user_choice2 = variations[choice_game3 - 1]
        bot_choice2 = random.randint(0, len(variations) - 1)
        bots_choice2 = variations[bot_choice2]
        print(f'выпал/а {bots_choice2}')
        if user_choice2 != bots_choice2:
            print('на этот раз ты проиграл')
        else:
            print('тебе повезло,ты выйграл!')
    elif choice_game1 == 3:
        print('хорошо,ты выбрал игру:Угадай число')
        print('1 - лёгкая сложность:1-25,15 попыток')
        print('2 - средняя сложность:1-50,10 попыток,бот неуверен в том что даёт правильные подсказки')
        print('3 - сложная сложность:1-100,8 попыток,бот никогда не скажет правду')
        choice_game4 = int(input('выбери сложность-->'))
        while choice_game4 not in (1, 2, 3):
            print('извини,но такого выбора нету')
            choice_game4 = int(input('выбери то-что тебе нужно-->'))
        if choice_game4 == 1:
            print('хорошо,ты выбрал лёгкую сложность')
            numbers = random.randint(0, 25)
            attempts = 15
            while True:
                if attempts == 0:
                    print('попытки закончились')
                    break
                answer = int(input('угадай число'))
                if answer == numbers:
                    print('ты угадал число')
                    break
                elif answer > numbers:
                    print('загаданное число меньше')
                elif answer < numbers:
                    print('загаданное число больше')
                attempts -= 1
        elif choice_game4 == 2:
            print('хорошо,ты выбрал среднюю сложность')
            numbers = random.randint(0, 50)
            attempts = 10
            while True:
                if attempts == 0:
                    print('попытки закончились')
                    break
                answer = int(input('угадай число'))
                if answer == numbers:
                    print('ты угадал число')
                    break
                elif answer > numbers:
                    bot_answer1 = ['возможно загаданное число меньше','я незнаю']
                    print(random.choice(bot_answer1))
                elif answer < numbers:
                    bot_answer2 = ['возможно загаданное число больше', 'я незнаю']
                    print(random.choice((bot_answer2)))
                attempts -= 1
        elif choice_game4 ==3:
            print('хорошо,ты выбрал сложную сложность')
            numbers = random.randint(0, 100)
            attempts = 8
            while True:
                if attempts == 0:
                    print('попытки закончились')
                    break
                answer = int(input('угадай число'))
                if answer == numbers:
                    print('ты угадал число')
                    break
                elif answer > numbers:
                    bot_answer3 = ['загаданное число больше','я тебе не скажу загаданное число']
                    print(random.choice((bot_answer3)))
                elif answer < numbers:
                    bot_answer4 = ['загаданное число меньше','я тебе не скажу загаданное число']
                    print(random.choice((bot_answer4)))
                attempts -= 1
    elif choice_game1 == 4:
        print('хорошо ты выбрал ранндомные примеры')
        print('1 - Лёгкий пример - две цифры')
        print('2 - Средний пример -  три цифры')
        solve_number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        solve_number2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        solve_number3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        operations = ['+', '-', '*', '/']
        operations2 = ['+', '-', '*', '/']
        random_num1 = random.choice(solve_number1)
        random_num2 = random.choice(solve_number2)
        random_num3 = random.choice(solve_number3)
        rand_operations = random.choice(operations)
        rand_operations2 = random.choice(operations2)
        choice_math_game1 = int(input('выбери сложность-->'))
        while choice_math_game1 not in(1, 2):
            print('извини но такого выбора нет')
            choice_math_game1 = int(input('выбери сложность-->'))
        if choice_math_game1 == 1:
            print('хорошо,ты выбрал лёгкую сложность')
            easy_example = (f'{random_num1} {rand_operations} {random_num2}')
            correct_answer = round(eval(easy_example))
            print(f'пример: {easy_example}')
            user_answer = float(input('введи ответ-->'))
            if user_answer == correct_answer:
                print('ты решил пример правильно,молодец')
            elif user_answer != correct_answer:
                print('ответ неправильный,но ничего страшного,получится в следующий раз!')
        elif choice_math_game1 == 2:
            print('хорошо,ты выбрал лёгкую сложность')
            normal_example = (f'{random_num1} {rand_operations} {random_num2} {rand_operations2} {random_num3}')
            correct_answer = round(eval(normal_example))
            print(f'пример: {normal_example}')
            user_answer = float(input('введи ответ-->'))
            if user_answer == correct_answer:
                print('ты решил пример правильно,молодец')
            elif user_answer != correct_answer:
                print('ответ неправильный,но ничего страшного,получится в следующий раз!')
elif choice3 == 4:
    menu_notes()