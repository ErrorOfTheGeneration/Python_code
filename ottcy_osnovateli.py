import collections
spisok = {
    "Гарольд Абельсон": "Лого",
    "Кеннет Юджин Айверсон": "APL",
    "Андрей Александреску": "D",
    "Альфред Ахо": "AWK",
    "Джереми Ашкенас": "сoffeeScript",
    "Стивен Ричард Борн": "C",
    "Уолтер Брайт": "D",
    "Джон Бэкус": "Фортран",
    "Гвидо Ван Россум": "Python",
    "Никлаус Вирт": "Паскаль, Модула-2, Оберон",
    "Дон Дудс": "Intercal",
    "Джеймс Гослинг": "Java",
    "Пол Грэм": "Lisp",
    "Оле-Йохан Даль": "Симула",
    "Эдсгер Вибе Дейкстра": "Алгол",
    "Роберту Иерузалимски": "Lua",
    "Жан Давид Ишбиа": "Ада, LIS",
    "Джон Джордж Кемени": "Basic",
    "Брайан Уилсон Керниган": "AWK",
    "Дональд Эрвин Кнут": "Metafont",
    "Ксавье Лерой": "OCaml",
    "Томас Курц": "Basic",
    "Алан Кёртис Кэй": "Smalltalk",
    "Джеймс Лайон": "Intercal",
    "Легалов Александр Иванович": "Пифагор",
    "Расмус Лердорф": "PHP",
    "Барбара Лисков": "Клу",
    "Джон Маккарти": "Лисп",
    "Юкихиро Мацумото": "Ruby",
    "Бертран Мейер": "Эйфель",
    "Робин Милнер": "ML",
    "Чарльз Мур": "Форт",
    "Петер Наур": "Алгол",
    "Кристен Нюгор": "Симула",
    "Маркус Хендрик Овермарс": "",
    "Родриго Баррето де Оливейра": "Boo",
    "Джон Оустерхаут": "Tcl",
    "Роб Пайк": "Go, Limbo, Sawzall, Newsqueak",
    "Сеймур Пейперт": "Logo",
    "Святослав Пестов": "Factor",
    "Деннис Макалистэйр Ритчи": "BCOL, B, C",
    "Дон Сайм": "F#",
    "Ричард Мэттью Столлман": "GNU",
    "Бьёрн Страуструп": "C++",
    "Дэвид А. Тёрнер": "SASL, KRC, Miranda",
    "Кен Томпсон": "C",
    "Ларри Уолл": "Perl",
    "Рэндалл Хайд": "HLA",
    "Андерс Хейлсберг": "Delphi",
    "Ричард Хикки": "Clojure",
    "Грейс Хоппер": "COBOL",
    "Конрад Эрнст Отто Цузе": "Планкалкюль"
}
print("Что вы хотите сделать?\n    1) Отсортировать словарь\n    2) Найти язык программирования")
operation  = int(input("Введите номер: "))
if operation == 1: # Выполнение операции "сортировка"
    sorted_list = collections.OrderedDict(sorted(spisok.items())) # Отсортировали массив по ключам
    for key, value in sorted_list.items():
        print(key, ",    Язык программирования: ", value)
else:
    while True: # Проверка на ошибки ввода ключа
        try:
            name = input("\nВведите имя создателя: ")
            print("\nСоздатель языков программирования: ", spisok[name])
            break
        except KeyError:
            print("Введите имя и фамилию полностью")
