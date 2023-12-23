import csv

class Users:
    @staticmethod
    def create_user(datalist):
        with open('users.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(datalist) 

    @staticmethod
    def create_tovar(datalist):
        with open('tovars.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(datalist)   


class Database:
    users = []
    tovars = []

    @staticmethod
    def add_user(username, password, role):
        new_user = Users(username, password, role)
        Database.users.append(new_user)

database = Database()
usermenager = Users()


def get_user():
    database.users = []
    
    with open('users.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        
        for row in reader:
            database.users.append(row)
    
    return database.users


def get_tovar():
    database.tovars = []
    
    with open('tovars.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        
        for row in reader:
            database.tovars.append(row)
    
    return database.tovars


def out_red(text):
    print("\033[31m {}" .format(text))
def out_white(text):
    print("\033[37m {}" .format(text))

def get__name(id):
    for row in database.tovars:
        if id in row[0]:
            return row[1]
    return None 

def get_enter(a):
    if a == 1:
        print("Ввудите название")
        nameproduct = input()
        print("Введите цену")
        priceproduct = input()
        print("Введите id товара")
        idstovar = input()
        usermenager.create_tovar([f"{idstovar}", f"{nameproduct}", f"{priceproduct}"])
        get_tovar()
        main()
    if a == 2:
        for row in database.tovars:
            print("{:<5} {:<10} {:<10}".format(row[0], row[1], row[2]))
        
        print("Впишите id товара для покупки")
        buy = int(input())
        print(f"Спасибо за покупку!")
        main()

def main():
    get_user()
    get_tovar()
    print("Добро пожаловать на стадион)")
    
    out_white("1.Авторизация \n2.Регистрация")
    auth = int(input("Выберите действие: "))
    if auth == 1: 
        print("Введите имя")
        name = input()
        if login(name) == True:
            print("Вы авторизованы!!!! \n Выберите действие: \n1.Добавить товар \n2.Открыть магазин снеков")
            deystvie = int(input())
            get_enter(deystvie)
        if login(name) == False:
            print("Пройдите регистрацию")
            main()
    if auth == 2: #Рега
        out_white("Введите имя")
        name = input()
        out_white("Впишите роль")
        role = input()
        usermenager.create_user([1, f"{name}", f"{role}"])

def login(name):
    for row in database.users:
        if name in row:
            return True
    return False

def Get_Role(name):
    for row in database.users:
        if name in row:
            return row[2]  
    return None  

def rolepass(name):
    if Get_Role(name) == 'Админ':
        print(Get_Role(name))
    if Get_Role(name) == 'Клиент':
        print(Get_Role(name))
    if Get_Role(name) == None:
        print("Ошибка!")

main()