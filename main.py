def print_hi(name):

    print(f'Hi, {name}')
def print4():
    a = input("Name ")
    b = input("Age ")
    print('Знаешь, ' + a + ', ты уже не молод(-а), тебе целых ' + b + ' лет, а ты до сих пор здесь')
def print1():
    a = 'Дмитрий'
    print(a)
def print2():
    a = 'Дмитрий'
    b = '20'
    print('Меня зовут ' + a + ', мне ' + b + ' лет. Я студент этого замечательного ВУЗа...')
def print3():
    a = 'Дмитрий \n'
    a *= 5
    print(a)
def print5():
    b = int(input("Age "))
    if b < 20:
        print('Ха-ха, попался, школьник')
    elif b > 30:
        print('Ну ты и старпёр')
    else:
        print('Ты теряешь свои лучшие годы здесь, задумайся, идиот')
def print6():
    a = input('Name ')
    b = a[::-1]
    c = a[(len(a)-3)::]
    d = a[:5]
    a = a[1:(len(a)-1)]
    print(a, b, c, d)
def print7():
    a = input('Name ')
    b = int(input('Age '))
    a = len(a)
    c = b//10 * b%10
    b = b//10 + b%10
    print(a,b,c)
def print8():
    a = input('Name ')
    b = a.upper()
    c = a.lower()
    a = a[0].upper() + a[1:-1] + a[-1]
    print(a,b,c)
def print9():
    d = 0
    c = 0
    a = input('Name ')
    if a.isalpha() == True:
        d = 1
    else:
        print('Ошибка при вводе имени')
    b = input('Age ')
    try:
        int(b)
        c = 1
    except ValueError:
        print('Ошибка при вводе возраста')
    if c == 1:
        if c > 150 or c < 0:
            print('Ошибка при вводе возраста')
        else:
            c = 2
    if d == 1 and c ==2:
        print('ok')
def print10():
    a = int(input('Реши что-то типа "Сколько будет 2+2*2?"  '))
    while a != 6:
        a = int(input('Попробуй ещё раз, что ли  '))
    print('Поздравляю, если ты дошёл сюда с первого раза, то твоё iq выше 30')
if __name__ == '__main__':
    print4()