print("Ласкаво просимо до калькулятору!")
expected_code = "100"
#login------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    user_code = input("Уведіть логін для початку роботи (Логін у назві калькулятору) ")
    if user_code == expected_code:
        print("Логін вірний. Можете працювати!")
        break
    else:
        print("Невірний логін. Спробуйте ще раз!")
#selcoperation------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    try:
        first = int(input('Введіть перше число 1: '))
        second = int(input('Введіть друге число 2: '))
        v = int(input('Який вид операції потрібно виконати?  \n 1 Плюсування \n 2 Віднімання \n 3 Ділення \n 4 Множення \n'))
        if v not in [1, 2, 3, 4]:
            print("Некоректний вибір операції. Будь ласка, виберіть знову вид операції.")
            continue
#plus------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        if v == 1:
            r = first + second
            t = 'плюсування'
#minus------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif v == 2:
            r = first - second
            t = 'віднімання'
#divison------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif v == 3:
            if second == 0:
                print('''Помилка!
Ділити на нуль неможна.''')# Тут помилку виправив, але не через zerodevisionerror, бо пришлось б повністю змінювати структуру коду, а якщо змінювати то втрачається унікальність
                continue
            r = float(first / second)
            t = 'ділення'
#multip------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        elif v == 4:
            r = first * second
            t = 'множення'
#result or error------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        print('Ваш результат', t, '=', r)
    except ValueError:
        print("Помилка! Введіть коректне число.")
#exit or not exit------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    abc = input('Завершити роботу? Так / Hi ')#тут теж виправив, не знаю чого воно не працювало раніше, або працювало лише через пробіл, але зараз працює
    if abc == 'Так':
        break
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
