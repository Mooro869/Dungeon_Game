# -*- coding: utf-8 -*-
import time
import random
import pygame

# Запуск музыки
pygame.mixer.init()
pygame.mixer.music.set_volume(0.0)  # настройка громкости
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()

# Характеристика волшебника
wizard = dict(Имя='Волшебник', Сила=15, Здоровье=85)
# Характеристика рыцаря
knight = dict(Имя='Рыцарь', Сила=10, Здоровье=90)
# Гоблин
goblin = dict(Имя='Гоблин', Сила=10, Здоровье=10)
# Слайм
slime = dict(Имя='Слайм', Сила=5, Здоровье=30)
# Скелет
skeleton = dict(Имя='Скелет', Сила=15, Здоровье=20)
# Паук
spider = dict(Имя='Паук', Сила=10, Здоровье=15)
# МЕГА-ГОБЛИН(Босс)
mega_goblin = dict(Имя='МЕГА-ГОБЛИН', Сила=13, Здоровье=70)
# Начало
print('Я приветствую вас в своей игре!')
time.sleep(3)
print('Это игра, в которой вы будете путешествовать по подземелью.')
time.sleep(5)
print('Вы будете сражаться с разными монстрами.')
time.sleep(3)
print('Но перед началом я дам вам несколько советов(пожеланий), чтобы немного облегчить прохождение.')
time.sleep(5)
print('Первый совет: если вы захотите сбежать от монстра, тогда он вас заденет и отнимет несколько здоровья.')
time.sleep(7)
print('Второй совет(пожелание): при выборе ответа обязательно используйте целое число!')
time.sleep(5)
print('Перед тем как я вам предложу выбрать персонажа, покажу характеристику каждого из них.')
time.sleep(3)
print(f'Волшебник - здоровье:{wizard["Здоровье"]}, сила:{wizard["Сила"]}')
time.sleep(3)
print(f'Рыцарь - здоровье:{knight["Здоровье"]}, сила:{knight["Сила"]}')
# Момент выбора персонажа
time.sleep(3)
character = int(input('Настал момент выбора персонажа - 1.Волшебник или 2.Рыцарь: '))
# КОД ВОЛШЕБНИКА
if character == 1:  # волшебник
    print('Вы выбрали волшебника, хороший выбор!')
    time.sleep(3)
    print('Вы заходите в подземелье и видите дверь.')
    time.sleep(5)
    wizard_door1 = int(input('Пройдя дальше вы видите дверь - 1.Войти: '))
    if wizard_door1 == 1:
        print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь')
        time.sleep(5)
        print(f'Вы видите перед собой гоблина с характеристиками - здоровье:{goblin["Здоровье"]}, '
              f'сила:{goblin["Сила"]}')
        goblin_wizard1 = int(input('1.Атаковать или 2.Сбежать(при попытке сбежать вы потеряйте 4 здоровья): '))
        if goblin_wizard1 == 1:  # вы выбрали атаку
            while wizard['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                w_push = random.randint(1, 15)
                g_push = random.randint(1, 10)
                goblin['Здоровье'] -= w_push
                wizard['Здоровье'] -= g_push
            if wizard['Здоровье'] <= 0:
                hp = goblin['Здоровье'] = 10
                print('Вы погибли от руки гоблина!')
            else:
                hp = goblin['Здоровье'] = 10
                print('Вы победили гоблина!')
                time.sleep(1)
                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                time.sleep(3)
                wizard_door2 = int(input('Пройдя дальше вы видите две двери, в какую войдете - 1 или 2: '))
                if wizard_door2 == 1:  # первая дверь
                    print('Вы выбрали первую дверь.') # +
                    time.sleep(3)
                    print('В комнате вы увидели сундук. Открывайте его и получайте +10 здоровья.')
                    wizard['Здоровье'] += 10
                    time.sleep(5)
                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                    time.sleep(5)
                    print('Вы проходите дальше и видите две двери.')
                    time.sleep(5)
                    wizard_door3 = int(input('Пройдя вперед вы видите две двери, в какую войдете - 1 или 2: '))
                    if wizard_door3 == 1:  # 3/5 дверей
                        print('Длинный проход, весь в плесени и паутине вел к двери.')
                        time.sleep(5)
                        print(f'Вы видите перед собой скелета с характеристиками - здоровье:{skeleton["Здоровье"]}, '
                              f'сила:{skeleton["Сила"]}')
                        time.sleep(8)
                        skeleton_wizard1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                     '2.Сбежать(при попытке сбежать вы потеряйте 5 здоровья): '))
                        if skeleton_wizard1 == 1:  # атаковать
                            print('Вы выбрали атаковать.')
                            time.sleep(3)
                            while wizard['Здоровье'] > 0 and skeleton['Здоровье'] > 0:
                                w_push = random.randint(1, 15)
                                s_push = random.randint(1, 15)
                                skeleton['Здоровье'] -= w_push
                                wizard['Здоровье'] -= s_push
                            if wizard['Здоровье'] <= 0:
                                hp = skeleton['Здоровье'] == 20
                                print('Вы погибли от руки скелета!')
                            else:
                                hp = skeleton['Здоровье'] == 20
                                print('Вы убили скелета!')
                                time.sleep(1)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(3)
                                print('Вы проходите дальше и видите две двери.')
                                time.sleep(5)
                                wizard_door4 = int(input('Какую дверь вы хотите выбрать - 1 или 2: '))
                                if wizard_door4 == 1: # первая дверь
                                    print('Вы выбрали первую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы увидели сундук. Открывайте его и получайте +15 здоровья.')
                                    wizard['Здоровье'] += 15
                                    time.sleep(5)
                                    print('Вы его открывайте и получайте +15 здоровья.')
                                    time.sleep(5)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(6)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта сбежать у вас нету, так как это единственный выход из '
                                              'подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                              f'сила:{wizard["Сила"]}')
                                        time.sleep(5)
                                        print('Вы атакуете монстра!')
                                        time.sleep(1)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif wizard_door4 == 2:  # вторая дверь
                                    print('Длинный проход, весь в плесени и паутине вел к двери.')
                                    time.sleep(5)
                                    print(f'Вы видите перед собой гоблина с характеристиками - '
                                          f'здоровье:{goblin["Здоровье"]}, сила:{goblin["Сила"]}')
                                    time.sleep(7)
                                    goblin_wizard2 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 3 здоровья): '))
                                    if goblin_wizard2 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            g_push = random.randint(1, 10)
                                            goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= g_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = goblin['Здоровье'] == 15
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = goblin['Здоровье'] == 15
                                            print('Вы победили гоблина!')
                                            time.sleep(5)
                                            print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                            time.sleep(6)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if wizard_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный '
                                                      'выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(9)
                                                print(f'Ваши характеристики - здоровье: '
                                                      f'{wizard["Здоровье"]}, сила:{wizard["Сила"]}')
                                                time.sleep(5)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    w_push = random.randint(1, 15)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= w_push
                                                    wizard['Здоровье'] -= mg_push
                                                if wizard['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif goblin_wizard2 == 2:  # сбежать
                                        print('Вы выбрали: сбежать.')
                                        wizard['Здоровье'] -= 3
                                        time.sleep(3)
                                        if wizard['Здоровье'] <= 0:
                                            print('Вы погибли от потери здоровья!')
                                        else:
                                            print('У вас удалось сбежать, но вы потеряли 3 здоровья.')
                                            time.sleep(3)
                                            print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                            time.sleep(5)
                                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                            time.sleep(5)
                                            print('Вы входите в другую дверь.')
                                            time.sleep(3)
                                            print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                                  f'здоровье:{slime["Здоровье"]}')
                                            time.sleep(7)
                                            print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                                            time.sleep(8)
                                            while wizard['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                                w_push = random.randint(1, 15)
                                                sl_push = random.randint(1, 5)
                                                slime['Здоровье'] -= w_push
                                                wizard['Здоровье'] -= sl_push
                                            if wizard['Здоровье'] <= 0:
                                                hp = slime['Здоровье'] == 30
                                                print('Вы погибли от слайма!')
                                            else:
                                                hp = slime['Здоровье'] == 30
                                                print('Вы победили слайма.')
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', wizard['Здоровье'])
                                                time.sleep(6)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if wizard_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(7)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print(f'Ваши характеристики - здоровье: '
                                                          f'{wizard["Здоровье"]}, сила:{wizard["Сила"]}')
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        w_push = random.randint(1, 15)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= w_push
                                                        wizard['Здоровье'] -= mg_push
                                                    if wizard['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                        elif skeleton_wizard1 == 2:  # сбежать
                            print('Вы выбрали: сбежать.')
                            wizard['Здоровье'] -= 4
                            time.sleep(3)
                            if wizard['Здоровье'] <= 0:
                                print('Вы погибли от потери здоровья!')
                            else:
                                print('У вас удалось сбежать, но вы потеряли 4 здоровья.')
                                time.sleep(3)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(7)
                                print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                time.sleep(5)
                                print('Вы входите в другую дверь.')
                                time.sleep(5)
                                print('В комнате стало как-то тихо, но вы немного прошли и увидели сундук.')
                                time.sleep(8)
                                wizard['Здоровье'] += 15
                                print('Вы его открывайте и получайте + 15 здоровья.')
                                time.sleep(5)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(6)
                                print('Вы проходите дальше и видите две двери.')
                                time.sleep(5)
                                wizard_door4 = int(input('Какую дверь вы хотите выбрать - 1 или 2: '))
                                if wizard_door4 == 1:
                                    print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                                    time.sleep(5)
                                    print(f'Вы видите перед собой гоблина с характеристиками - '
                                          f'здоровье:{goblin["Здоровье"]}, сила:{goblin["Сила"]}')
                                    time.sleep(7)
                                    goblin_wizard2 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 3 здоровья): '))
                                    if goblin_wizard2 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(5)
                                        while wizard['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            g_push = random.randint(1, 10)
                                            goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= g_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = goblin['Здоровье'] == 15
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = goblin['Здоровье'] == 15
                                            print('Вы победили гоблина.')
                                            time.sleep(3)
                                            print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if wizard_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print(
                                                    'Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                    'подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                                time.sleep(9)
                                                print('Вы начинайте атаковать монстра.')
                                                time.sleep(3)
                                                while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    w_push = random.randint(1, 15)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= w_push
                                                    wizard['Здоровье'] -= mg_push
                                                if wizard['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif goblin_wizard2 == 2:  # сбежать
                                        print('Вы выбрали: сбежать.')
                                        wizard['Здоровье'] -= 3
                                        time.sleep(3)
                                        if wizard['Здоровье'] <= 0:
                                            print('Вы погибли от потери здоровья!')
                                        else:
                                            print('У вас удалось сбежать, но вы потеряли 3 здоровья.')
                                            time.sleep(3)
                                            print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                            time.sleep(7)
                                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                            time.sleep(5)
                                            print('Вы входите в другую дверь.')
                                            time.sleep(3)
                                            print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                                  f'здоровье:{slime["Здоровье"]}')
                                            time.sleep(10)
                                            print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                                            time.sleep(8)
                                            while wizard['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                                w_push = random.randint(1, 15)
                                                sl_push = random.randint(1, 5)
                                                slime['Здоровье'] -= w_push
                                                wizard['Здоровье'] -= sl_push
                                            if wizard['Здоровье'] <= 0:
                                                print('Вы погибли от слайма!')
                                                hp = slime['Здоровье'] == 30
                                            else:
                                                hp = slime['Здоровье'] == 30
                                                print('Вы победили слайма.')
                                                time.sleep(3)
                                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                                time.sleep(6)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if wizard_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как это '
                                                          'единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                          f'сила:{wizard["Сила"]}')
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        w_push = random.randint(1, 15)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= w_push
                                                        wizard['Здоровье'] -= mg_push
                                                    if wizard['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                    elif wizard_door3 == 2:  # третья дверь
                        print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                        time.sleep(5)
                        print(f'Вы видите перед собой гоблина с характеристиками - здоровье:{goblin["Здоровье"]}, '
                              f'сила:{goblin["Сила"]}')
                        time.sleep(7)
                        goblin_wizard3 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                   '(при попытке сбежать вы потеряйте 3 здоровья): '))
                        if goblin_wizard3 == 1:  # атаковать
                            print('Вы выбрали: атаковать.')
                            time.sleep(3)
                            while wizard['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                w_push = random.randint(1, 15)
                                g_push = random.randint(1, 10)
                                goblin['Здоровье'] -= w_push
                                wizard['Здоровье'] -= g_push
                            if wizard['Здоровье'] <= 0:
                                hp = goblin['Здоровье'] == 15
                                print('Вы погибли от руки гоблина!')
                            else:
                                hp = goblin['Здоровье'] == 15
                                print('Вы убили гоблина!')
                                time.sleep(3)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(6)
                                print('Пройдя дальше вы видите две двери.')
                                time.sleep(3)
                                wizard_door4 = int(input('Какую дверь вы хотите выбрать - 1 или 2: '))
                                if wizard_door4 == 1:
                                    print('Вы выбрали первую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы заметили сундук.')
                                    time.sleep(3)
                                    wizard['Здоровье'] += 15
                                    print('В сундуке было +15 здоровья.')
                                    time.sleep(3)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(7)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта "Cбежать" у вас нету, так как '
                                              'это единственный выход из подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                              f'сила:{wizard["Сила"]}')
                                        time.sleep(9)
                                        print('Вы начинайте атаковать монстра.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif wizard_door4 == 2:
                                    print('Вы выбрали вторую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы заметили сундук.')
                                    time.sleep(3)
                                    print('В сундуке было +15 здоровья.')
                                    wizard['Здоровье'] += 15
                                    time.sleep(3)
                                    print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                          f'сила:{wizard["Сила"]}')
                                    time.sleep(6)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта "Cбежать" у вас нету, '
                                              'так как это единственный выход из подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                              f'сила:{wizard["Сила"]}')
                                        time.sleep(9)
                                        print('Вы начинайте атаковать гоблина.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif goblin_wizard3 == 2:  # сбежать
                                    print('Вы выбрали: сбежать.')
                                    time.sleep(3)
                                    wizard['Здоровье'] -= 3
                                    if wizard['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья!')
                                    else:
                                        print('Вы сбежали, но потеряли 3 здоровья.')
                                        time.sleep(3)
                                        print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                        time.sleep(7)
                                        print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                        time.sleep(5)
                                        print('Вы входите в другую дверь.')
                                        time.sleep(3)
                                        print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                              f'здоровье:{slime["Здоровье"]}')
                                        time.sleep(10)
                                        print('Напонимаем: раз уж вы уже выбирали вариант "сбежать", второй раз его '
                                              'использовать нельзя, вы автоматический будете атаковать монстра.')
                                        time.sleep(8)
                                        while wizard['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= sl_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли от слайма!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма.')
                                            time.sleep(3)
                                            print('Немного пройдя вперед, вы замечайте две двери.')
                                            time.sleep(5)
                                            wizard_door4 = int(input('Какую дверь вы хотите выбрать - 1 или 2: '))
                                            if wizard_door4 == 1:
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(3)
                                                print('В комнате вы заметили сундук.')
                                                time.sleep(3)
                                                print('В сундуке было +15 здоровья.')
                                                time.sleep(3)
                                                wizard['Здоровье'] += 15
                                                print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                                time.sleep(6)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if wizard_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                          f'сила:{wizard["Сила"]}')
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать монстра.')
                                                    time.sleep(3)
                                                    while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        w_push = random.randint(1, 15)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= w_push
                                                        wizard['Здоровье'] -= mg_push
                                                    if wizard['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif wizard_door4 == 2:
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(3)
                                                print('В комнате вы заметили сундук.')
                                                time.sleep(3)
                                                wizard['Здоровье'] += 15
                                                print('В сундуке было +15 здоровья.')
                                                time.sleep(3)
                                                print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                                time.sleep(6)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if wizard_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как это '
                                                          'единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                          f'сила:{wizard["Сила"]}')
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        w_push = random.randint(1, 15)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= w_push
                                                        wizard['Здоровье'] -= mg_push
                                                    if wizard['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                elif wizard_door2 == 2:  # 2/5 # вторая дверь
                    print('Вы выбрали вторую дверь.')
                    time.sleep(3)
                    print('В комнате вы заметили сундук.')
                    time.sleep(3)
                    wizard['Здоровье'] += 15
                    print('В сундуке было +15 здоровья.')
                    time.sleep(3)
                    print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                    time.sleep(6)
                    print('Пройдя дальше вы видите две двери.')
                    time.sleep(3)
                    wizard_door3 = int(input('Какую дверь вы хотите выбрать - 1 или 2: '))
                    if wizard_door3 == 1:
                        print('Проходя дальше, вы видите темный и плохо освещенный проход, но в '
                              'далеке находится дверь.')
                        time.sleep(6)
                        print(f'Вы видите скелета с характеристиками: здоровье здоровье:{skeleton["Здоровье"]}, '
                              f'сила:{skeleton["Сила"]}')
                        time.sleep(8)
                        skeleton_wizard1 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                     '(при попытке сбежать вы потеряйте 5 здоровья): '))
                        if skeleton_wizard1 == 1:  # атаковать
                            print('Вы выбрали: атаковать!')
                            time.sleep(3)
                            while wizard['Здоровье'] > 0 and skeleton['Здоровье'] > 0:
                                w_push = random.randint(1, 15)
                                s_push = random.randint(1, 15)
                                skeleton['Здоровье'] -= w_push
                                wizard['Здоровье'] -= s_push
                            if wizard['Здоровье'] <= 0:
                                hp = skeleton['Здоровье'] == 20
                                print('Вы победили!')
                            else:
                                hp = skeleton['Здоровье'] == 20
                                print('Вы победили скелета!')
                                time.sleep(3)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(3)
                                print('Пройдя дальше вы видите две двери.')
                                time.sleep(3)
                                wizard_door4 = int(input('Какую дверь вы хотите выбрать - 1 или 2: '))
                                if wizard_door4 == 1:
                                    print('Вы выбрали первую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы заметили сундук.')
                                    time.sleep(3)
                                    wizard['Здоровье'] += 15
                                    print('В сундуке было +15 здоровья.')
                                    time.sleep(3)
                                    print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                    time.sleep(6)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                              'из подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: '
                                              f'{wizard["Здоровье"]}, сила:{wizard["Сила"]}')
                                        time.sleep(9)
                                        print('Вы начинайте атаковать гоблина.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif wizard_door4 == 2:
                                    print('Вы выбрали вторую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы заметили сундук.')
                                    time.sleep(3)
                                    wizard['Здоровье'] += 15
                                    print('В сундуке было +15 здоровья.')
                                    time.sleep(3)
                                    print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                    time.sleep(6)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                              'подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: '
                                              f'{wizard["Здоровье"]}, сила:{wizard["Сила"]}')
                                        time.sleep(9)
                                        print('Вы начинайте атаковать гоблина.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                        elif skeleton_wizard1 == 2:  # сбеажать
                            print('Вы выбрали: сбежать.')
                            wizard['Здоровье'] -= 7
                            time.sleep(3)
                            if wizard['Здоровье'] <= 0:
                                print('Вы погибли от потери здоровья!')
                            else:
                                print('Вы сбежали, но у вас отнялось 7 здоровья.')
                                time.sleep(3)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(7)
                                print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                time.sleep(5)
                                print(f'Вы видите перед собой скелета с характеристиками - '
                                      f'здоровье:{skeleton["Здоровье"]}, сила:{skeleton["Сила"]}')
                                time.sleep(6)
                                print('Раз уж вы уже сбегали, больше этого варианта у вас не будет, '
                                      'вы автоматический будете атаковать монстра.')
                                time.sleep(5)
                                while wizard['Здоровье'] > 0 and skeleton['Здоровье'] > 0:
                                    w_push = random.randint(1, 15)
                                    s_push = random.randint(1, 15)
                                    skeleton['Здоровье'] -= w_push
                                    wizard['Здоровье'] -= s_push
                                if wizard['Здоровье'] <= 0:
                                    hp = skeleton['Здоровье'] == 20
                                    print('Вы погибли от скелета!')
                                else:
                                    print('Вы победили скелета!')
                                    hp = skeleton['Здоровье'] == 20
                                    time.sleep(1)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(3)
                                    print('Вы проходите дальше и видите две двери.')
                                    time.sleep(3)
                                    wizard_door4 = int(input('Какую дверь вы выберите - 1 или 2: '))
                                    if wizard_door4 == 1:  # первая дверь
                                        print('Вы выбрали первую дверь.')
                                        time.sleep(3)
                                        print('В комнате вы заметили сундук.')
                                        time.sleep(3)
                                        wizard['Здоровье'] += 15
                                        print('В сундуке было +15 здоровья.')
                                        time.sleep(3)
                                        print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                        time.sleep(6)
                                        print('Вы проходите дальше и видите одну большую дверь.')
                                        time.sleep(5)
                                        print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                        time.sleep(5)
                                        wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                        if wizard_door5 == 1:
                                            print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                            time.sleep(6)
                                            print('Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                  'подземелья.')
                                            time.sleep(10)
                                            print(f'Вы видите перед собой гоблина с характеристиками: '
                                                  f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                            time.sleep(7)
                                            print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                  f'сила:{wizard["Сила"]}')
                                            time.sleep(9)
                                            print('Вы начинайте атаковать гоблина.')
                                            time.sleep(3)
                                            while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                w_push = random.randint(1, 15)
                                                mg_push = random.randint(1, 13)
                                                mega_goblin['Здоровье'] -= w_push
                                                wizard['Здоровье'] -= mg_push
                                            if wizard['Здоровье'] <= 0:
                                                hp = mega_goblin['Здоровье'] == 70
                                                print('Вы погибли от руки гоблина!')
                                            else:
                                                hp = mega_goblin['Здоровье'] == 70
                                                print('Вы победили гоблина!')
                                                time.sleep(1)
                                                print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif wizard_door4 == 2:
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(3)
                                            print('В комнате вы заметили сундук.')
                                            time.sleep(3)
                                            wizard['Здоровье'] += 15
                                            print('В сундуке было +15 здоровья.')
                                            time.sleep(3)
                                            print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                            time.sleep(6)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if wizard_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print(
                                                    'Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                    'подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                      f'сила:{wizard["Сила"]}')
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    w_push = random.randint(1, 15)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= w_push
                                                    wizard['Здоровье'] -= mg_push
                                                if wizard['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                        elif wizard_door3 == 2:
                            print('Слабо освещенный проход ведет к заветной двери.')
                            time.sleep(3)
                            print(f'Вы видите перед собой скелета с характеристиками - здоровье:{skeleton["Здоровье"]}, сила:{skeleton["Сила"]}')
                            time.sleep(8)
                            skeleton_wizard1 = int(input(
                                'Что вы хотите выбрать - 1.Атаковать или 2.Сбежать(при попытке сбежать вы потеряйте 5 '
                                'здоровья): '))
                            if skeleton_wizard1 == 1:  # атаковать
                                print('Вы выбрали: атаковать.')
                                time.sleep(3)
                                while wizard['Здоровье'] > 0 and skeleton['Здоровье'] > 0:
                                    w_push = random.randint(1, 15)
                                    s_push = random.randint(1, 15)
                                    skeleton['Здоровье'] -= w_push
                                    wizard['Здоровье'] -= s_push
                                if wizard['Здоровье'] <= 0:
                                    hp = skeleton['Здоровье'] == 20
                                    print('Вы погибли от слайма!')
                                else:
                                    hp = skeleton['Здоровье'] == 20
                                    print('Вы победили скелета!')
                                    time.sleep(1)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(3)
                                    wizard_door4 = int(
                                        input('Пройдя дальше вы видите две двери, какую выберите - 1 или 2: '))
                                    if wizard_door4 == 1:
                                        print('Вы выбрали первую дверь.')
                                        time.sleep(3)
                                        print('В комнате вы заметили сундук.')
                                        time.sleep(3)
                                        wizard['Здоровье'] += 15
                                        print('В сундуке было +15 здоровья.')
                                        time.sleep(3)
                                        print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                        time.sleep(6)
                                        print('Вы проходите дальше и видите одну большую дверь.')
                                        time.sleep(5)
                                        print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                        time.sleep(5)
                                        wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                        if wizard_door5 == 1:
                                            print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                            time.sleep(6)
                                            print('Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                  'подземелья.')
                                            time.sleep(10)
                                            print(f'Вы видите перед собой гоблина с характеристиками: '
                                                  f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                            time.sleep(7)
                                            print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                  f'сила:{wizard["Сила"]}')
                                            time.sleep(9)
                                            print('Вы начинайте атаковать гоблина.')
                                            time.sleep(3)
                                            while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                w_push = random.randint(1, 15)
                                                mg_push = random.randint(1, 13)
                                                mega_goblin['Здоровье'] -= w_push
                                                wizard['Здоровье'] -= mg_push
                                            if wizard['Здоровье'] <= 0:
                                                hp = mega_goblin['Здоровье'] == 70
                                                print('Вы погибли от руки гоблина!')
                                            else:
                                                hp = mega_goblin['Здоровье'] == 70
                                                print('Вы победили гоблина!')
                                                time.sleep(1)
                                                print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif wizard_door4 == 2:
                                        print('Вы выбрали вторую дверь.')
                                        time.sleep(3)
                                        print('В комнате вы заметили сундук.')
                                        time.sleep(3)
                                        wizard['Здоровье'] += 15
                                        print('В сундуке было +15 здоровья.')
                                        time.sleep(3)
                                        print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                        time.sleep(6)
                                        print('Вы проходите дальше и видите одну большую дверь.')
                                        time.sleep(5)
                                        print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                        time.sleep(5)
                                        wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                        if wizard_door5 == 1:
                                            print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                            time.sleep(6)
                                            print('Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                  'подземелья.')
                                            time.sleep(10)
                                            print(f'Вы видите перед собой гоблина с характеристиками: '
                                                  f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                            time.sleep(7)
                                            print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                  f'сила:{wizard["Сила"]}')
                                            time.sleep(9)
                                            print('Вы начинайте атаковать гоблина.')
                                            time.sleep(3)
                                            while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                w_push = random.randint(1, 15)
                                                mg_push = random.randint(1, 13)
                                                mega_goblin['Здоровье'] -= w_push
                                                wizard['Здоровье'] -= mg_push
                                            if wizard['Здоровье'] <= 0:
                                                hp = mega_goblin['Здоровье'] == 70
                                                print('Вы погибли от руки гоблина!')
                                            else:
                                                hp = mega_goblin['Здоровье'] == 70
                                                print('Вы победили гоблина!')
                                                time.sleep(1)
                                                print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                            elif skeleton_wizard1 == 2:  # сбежать
                                print('Вы выбрали: сбежать.')
                                wizard['Здоровье'] -= 5
                                time.sleep(3)
                                if wizard['Здоровье'] <= 0:
                                    print('Вы погибли от скелета!')
                                else:
                                    print('Вы сбежали, но потеряли 5 здоровья.')
                                    time.sleep(3)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(5)
                                    print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                    time.sleep(3)
                                    print('Вы входите в другую дверь.')
                                    time.sleep(3)
                                    print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                          f'здоровье:{slime["Здоровье"]}')
                                    time.sleep(10)
                                    print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                          'использовать нельзя, вы автоматический будете атаковать монстра.')
                                    time.sleep(7)
                                    print('Вы атакуйте слайма.')
                                    time.sleep(1)
                                    while wizard['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                        w_push = random.randint(1, 15)
                                        sl_push = random.randint(1, 5)
                                        slime['Здоровье'] -= w_push
                                        wizard['Здоровье'] -= sl_push
                                    if wizard['Здоровье'] <= 0:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы погибли от слайма!')
                                    else:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы победили слайма.')
                                        time.sleep(3)
                                        print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                        time.sleep(3)
                                        print('Вы проходите дальше и видите две двери.')
                                        time.sleep(3)
                                        wizard_door4 = int(input('Какую дверь вы выберите - 1 или 2: '))
                                        if wizard_door4 == 1:
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(3)
                                            print('В комнате вы заметили сундук.')
                                            time.sleep(3)
                                            wizard['Здоровье'] += 15
                                            print('В сундуке было +15 здоровья.')
                                            time.sleep(3)
                                            print(f'Теперь у вас здоровья: {wizard["Здоровье"]}')
                                            time.sleep(6)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if wizard_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print(
                                                    'Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                    'подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                      f'сила:{wizard["Сила"]}')
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    w_push = random.randint(1, 15)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= w_push
                                                    wizard['Здоровье'] -= mg_push
                                                if wizard['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif wizard_door4 == 2:
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(3)
                                            print('В комнате вы заметили сундук.')
                                            time.sleep(3)
                                            wizard['Здоровье'] += 15
                                            print('В сундуке было +15 здоровья.')
                                            time.sleep(3)
                                            print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                            time.sleep(6)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if wizard_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print(
                                                    'Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                                    'подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                                      f'сила:{wizard["Сила"]}')
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    w_push = random.randint(1, 15)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= w_push
                                                    wizard['Здоровье'] -= mg_push
                                                if wizard['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                    elif goblin_wizard1 == 2:  # вы выбрали сбежать, дверей 1/5
                        print('Вы выбрали: сбежать.')
                        wizard['Здоровье'] -= 5
                        time.sleep(3)
                        if wizard['Здоровье'] <= 0:
                            print('Вы погибли от потери здоровья.')
                        else:
                            print('Вы сбежали, но вы потеряли 5 здоровья.')
                            time.sleep(3)
                            print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                            time.sleep(3)
                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                            time.sleep(5)
                            print('Вы входите в другую дверь.')
                            time.sleep(3)
                            print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                  f'здоровье:{slime["Здоровье"]}')
                            time.sleep(7)
                            print(
                                'Напоминаем: раз уж вы уже выбирали вариант сбежать, второй раз его использовать '
                                'нельзя, вы автоматический будете атаковать монстра.')
                            time.sleep(10)
                            print('Вы атакуйте слайма.')
                            time.sleep(3)
                            while wizard['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                w_push = random.randint(1, 15)
                                sl_push = random.randint(1, 5)
                                slime['Здоровье'] -= w_push
                                wizard['Здоровье'] -= sl_push
                            if wizard['Здоровье'] <= 0:
                                hp = slime['Здоровье'] == 30
                                print('Вы погибли от слайма!')
                            else:
                                hp = slime['Здоровье'] == 30
                                print('Вы убили слайма.')
                                time.sleep(3)
                                print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                time.sleep(3)
                                wizard_door4 = int(
                                    input('Пройдя дальше вы видите две двери, какую выберите - 1 или 2: '))
                                if wizard_door4 == 1:
                                    print('Вы выбрали первую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы заметили сундук.')
                                    time.sleep(3)
                                    wizard['Здоровье'] += 15
                                    print('В сундуке было +15 здоровья.')
                                    time.sleep(3)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(6)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                              'подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                              f'сила:{wizard["Сила"]}')
                                        time.sleep(9)
                                        print('Вы начинайте атаковать гоблина.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif wizard_door4 == 2:
                                    print('Вы выбрали вторую дверь.')
                                    time.sleep(3)
                                    print('В комнате вы заметили сундук.')
                                    time.sleep(3)
                                    wizard['Здоровье'] += 15
                                    print('В сундуке было +15 здоровья.')
                                    time.sleep(3)
                                    print(f'Теперь у вас здоровья:{wizard["Здоровье"]}')
                                    time.sleep(6)
                                    print('Вы проходите дальше и видите одну большую дверь.')
                                    time.sleep(5)
                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                    time.sleep(5)
                                    wizard_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                    if wizard_door5 == 1:
                                        print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                        time.sleep(6)
                                        print('Варианта "Cбежать" у вас нету, так как это единственный выход из '
                                              'подземелья.')
                                        time.sleep(10)
                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                              f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                        time.sleep(7)
                                        print(f'Ваши характеристики - здоровье: {wizard["Здоровье"]}, '
                                              f'сила:{wizard["Сила"]}')
                                        time.sleep(9)
                                        print('Вы начинайте атаковать гоблина.')
                                        time.sleep(3)
                                        while wizard['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                            w_push = random.randint(1, 15)
                                            mg_push = random.randint(1, 13)
                                            mega_goblin['Здоровье'] -= w_push
                                            wizard['Здоровье'] -= mg_push
                                        if wizard['Здоровье'] <= 0:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = mega_goblin['Здоровье'] == 70
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Поздравляю, вы прошли игру!')
# КОД РЫЦАРЯ
elif character == 2:  # Рыцарь
    print('Вы выбрали рыцаря, хороший выбор!')
    time.sleep(3)
    knight_door1 = int(input('Пройдя вперед вы видите дверь: 1.Войти: '))
    if knight_door1 == 1:
        print('Длинный проход, весь в плесени и паутине вел к двери')
        time.sleep(5)
        print('Вы видите скелета с характеристиками: здоровье -', skeleton.get('Здоровье'), 'сила -',
              skeleton.get('Сила'))
        time.sleep(8)
        knight_skeleton1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                     '2.Сбежать(при попытке сбежать вы потеряйте 5 здоровья.): '))
        if knight_skeleton1 == 1:  # атака
            print('Вы выбрали: атаковать.')
            time.sleep(1)
            while knight['Здоровье'] > 0 and skeleton['Здоровье'] > 0:
                k_push = random.randint(1, 10)
                s_push = random.randint(1, 15)
                skeleton['Здоровье'] -= k_push
                knight['Здоровье'] -= s_push
            if knight['Здоровье'] <= 0:
                hp = skeleton['Здоровье'] == 20
                print('Вы погибли от скелета!')
            else:
                hp = skeleton['Здоровье'] == 20
                print('Вы победили скелета!')
                time.sleep(3)
                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                time.sleep(3)
                knight_door2 = int(input('Пройдя дальше вы видите две двери, в какую войдете - 1 или 2: '))
                if knight_door2 == 1:  # первая дверь
                    print('Слабо освещенный проход ведет к заветной двери')
                    time.sleep(3)
                    print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'), 'сила - ',
                          spider.get('Сила'))
                    time.sleep(8)
                    knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                               '2.Сбежать(при попытке сбежать вы потеряйте 5 здоровья): '))
                    if knight_spider1 == 1:  # атаковать
                        print('Вы выбрали: атаковать.')
                        time.sleep(1)
                        while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                            k_push = random.randint(1, 10)
                            sp_push = random.randint(1, 10)
                            spider['Здоровье'] -= k_push
                            knight['Здоровье'] -= sp_push
                        if knight['Здоровье'] <= 0:
                            hp = spider['Здоровье'] == 15
                            print('Вы погибли от паука!')
                        else:
                            hp = spider['Здоровье'] == 15
                            print('Вы победили паука!')
                            time.sleep(1)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(3)
                            knight_door3 = int(input('Пройдя дальше вы видите две двери, в какую войдете - 1 или 2: '))
                            if knight_door3 == 1:  # первая дверь
                                print('Длинный проход, весь в плесени и паутине вел к двери.')
                                time.sleep(5)
                                print('Вы видите слайма с характеристиками: здоровье - ',
                                      slime.get('Здоровье'), 'сила - ', slime.get('Сила'))
                                knight_slime1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                          '2.Сбежать(при попытке сбежать вы потеряйте 7 здоровья): '))
                                if knight_slime1 == 1:  # атаковать
                                    print('Вы выбрали: атаковать.')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        sl_push = random.randint(1, 5)
                                        slime['Здоровье'] -= k_push
                                        knight['Здоровье'] -= sl_push
                                    if knight['Здоровье'] <= 0:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы погибли от слайма!')
                                    else:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы победили слайма.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(3)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif knight_door4 == 2:  # вторая дверь
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_slime1 == 2:  # сбежать -7
                                    print('Вы выбрали: сбежать.')
                                    knight['Здоровье'] -= 7
                                    time.sleep(1)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья!')
                                    else:
                                        print('У вас удалось сбежать, но вы потеряли 7 здоровья.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья: ', knight.get('Здоровье'))
                                        time.sleep(3)
                                        knight_door4 = int(input('Немного пройдя вперед вы видите две двери, '
                                                                 'в какую войдете - 1 или 2:'))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif knight_door4 == 2:  # вторая дверь
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                            elif knight_door3 == 2:  # вторая дверь
                                print('Длинный проход, весь в плесени и паутине вел к двери.')
                                time.sleep(5)
                                print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                                      goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                                knight_goblin1 = int(input('1.Атаковать или '
                                                           '2.Сбежать(при попытке сбежать вы потеряйте 3 здоровья): '))
                                if knight_goblin1 == 1:  # атака
                                    print('Вы выбрали: атаковать')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        g_push = random.randint(1, 10)
                                        goblin['Здоровье'] -= k_push
                                        knight['Здоровье'] -= g_push
                                    if knight['Здоровье'] <= 0:
                                        hp = goblin['Здоровье'] = 10
                                        print('Вы погибли от руки гоблина!')
                                    else:
                                        hp = goblin['Здоровье'] = 10
                                        print('Вы победили гоблина!')
                                        time.sleep(1)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(3)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif knight_door4 == 2:  # вторая дверь
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_goblin1 == 2:  # сбежать -3 хп
                                    print('Вы выбрали: сбежать')
                                    knight['Здоровье'] -= 3
                                    time.sleep(3)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья.')
                                    else:
                                        print('Вам удалось сбежать, но вы потеря 3 здоровья.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(3)
                                        print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                        time.sleep(5)
                                        print('Вы входите в другую дверь.')
                                        time.sleep(3)
                                        print('Вы встретили слайма, его сила - ', slime.get('Сила'), 'его здоровье - ',
                                              slime.get('Здоровье'))
                                        time.sleep(7)
                                        print('Напоминаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                              'использовать нельзя, вы автоматический будете атаковать монстра.')
                                        time.sleep(7)
                                        print('Вы атакуйте слайма.')
                                        time.sleep(3)
                                        while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sl_push
                                        if knight['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли от слайма!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма.')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                          'сила -', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                    elif knight_spider1 == 2:  # сбежать -5
                        print('Вы выбрали: сбежать.')
                        knight['Здоровье'] -= 5
                        time.sleep(3)
                        if knight['Здоровье'] <= 0:
                            print('Вы погибли от потери здоровья.')
                        else:
                            print('Вам удалось сбежать, но вы потеряли 5 здоровья.')
                            time.sleep(3)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(3)
                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                            time.sleep(3)
                            print('Вы входите в другую дверь.')
                            time.sleep(3)
                            print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                  f'здоровье:{slime["Здоровье"]}')
                            time.sleep(7)
                            print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                            time.sleep(7)
                            print('Вы атакуйте слайма.')
                            time.sleep(3)
                            while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                k_push = random.randint(1, 10)
                                sl_push = random.randint(1, 5)
                                slime['Здоровье'] -= k_push
                                knight['Здоровье'] -= sl_push
                            if knight['Здоровье'] <= 0:
                                hp = slime['Здоровье'] == 30
                                print('Вы погибли от слайма!')
                            else:
                                hp = slime['Здоровье'] == 30
                                print('Вы победили слайма!')
                                time.sleep(1)
                                knight_door3 = int(input('Пройдя дальше вы видите две двери, '
                                                         'в какую хотите войти - 1 или 2: '))
                                if knight_door3 == 1:  # первая дверь
                                    print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                                    time.sleep(5)
                                    print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                                          goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                                    knight_goblin1 = int(input('1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 3 здоровья): '))
                                    if knight_goblin1 == 1:  # атака
                                        print('Вы выбрали: атаковать')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            g_push = random.randint(1, 10)
                                            goblin['Здоровье'] -= k_push
                                            knight['Здоровье'] -= g_push
                                        if knight['Здоровье'] <= 0:
                                            hp = goblin['Здоровье'] = 10
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = goblin['Здоровье'] = 10
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(3)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(5)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(5)
                                                    print('Вы начинайте атаковать гоблина(варианта "Cбежать" '
                                                          'у вас нету, так как это единственный выход из подземелья).')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif knight_goblin1 == 2:  # сбежать -3 хп
                                        print('Вы выбрали: сбежать')
                                        knight['Здоровье'] -= 3
                                        time.sleep(1)
                                        if knight['Здоровье'] <= 0:
                                            print('Вы погибли от потери здоровья.')
                                        else:
                                            print('Вам удалось сбежать, но вы потеряли 3 здоровья.')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            print('Раз уж из одной двери вы сбежали, тогда вам стоит '
                                                  'зайти в другую дверь.')
                                            time.sleep(5)
                                            knight_door4 = int(input('Выберите действие - 1.Войти: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы входите в другую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_door3 == 2:  # вторая дверь
                                    print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                                    time.sleep(5)
                                    print('Вы видите слайма с характеристиками: здоровье - ',
                                          slime.get('Здоровье'), 'сила - ', slime.get('Сила'))
                                    knight_slime1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                              '2.Сбежать(при попытке сбежать вы '
                                                              'потеряйте 7 здоровья): '))
                                    if knight_slime1 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sl_push
                                        if knight['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма.')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                                elif knight_door4 == 2:  # вторая дверь
                                                    print('Вы выбрали вторую дверь.')
                                                    time.sleep(1)
                                                    print('Немного осмотревшись вы увидели сундук. '
                                                          'Вы его открывайте и получайте + 15 здоровья.')
                                                    knight['Здоровье'] += 15
                                                    time.sleep(3)
                                                    print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                    time.sleep(3)
                                                    print('Вы проходите дальше и видите одну большую дверь.')
                                                    time.sleep(5)
                                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                    time.sleep(5)
                                                    knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                    if knight_door5 == 1:
                                                        print('Вы входите в комнату и видите '
                                                              'огромного гоблина перед собой.')
                                                        time.sleep(6)
                                                        print('Варианта "Cбежать" у вас нету, так как '
                                                              'это единственный выход из подземелья.')
                                                        time.sleep(10)
                                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                                              f'здоровье:{mega_goblin["Здоровье"]}, '
                                                              f'сила:{mega_goblin["Сила"]}')
                                                        time.sleep(7)
                                                        print('Ваши характеристики: здоровье - ',
                                                              knight.get('Здоровье'),
                                                              'сила - ', knight.get('Сила'))
                                                        time.sleep(9)
                                                        print('Вы начинайте атаковать гоблина.')
                                                        time.sleep(3)
                                                        while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                            k_push = random.randint(1, 10)
                                                            mg_push = random.randint(1, 13)
                                                            mega_goblin['Здоровье'] -= k_push
                                                            knight['Здоровье'] -= mg_push
                                                        if knight['Здоровье'] <= 0:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы погибли от руки гоблина!')
                                                        else:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы победили гоблина!')
                                                            time.sleep(1)
                                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif knight_slime1 == 2:  # сбежать -7 хп
                                        print('Вы выбрали: сбежать.')
                                        knight['Здоровье'] -= 7
                                        time.sleep(1)
                                        if knight['Здоровье'] <= 0:
                                            print('Вы погибли от потери здоровья!')
                                        else:
                                            print('Вам удалось сбежать, но вы потеряли 7 здоровья.')
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                            time.sleep(5)
                                            print('Вы входите в другую дверь.')
                                            time.sleep(3)
                                            print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                                                  goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                                            time.sleep(6)
                                            print('Напоминаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                                            time.sleep(5)
                                            print('Вы начинайте атаковать гоблина.')
                                            time.sleep(3)
                                            while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                                k_push = random.randint(1, 10)
                                                g_push = random.randint(1, 10)
                                                goblin['Здоровье'] -= k_push
                                                knight['Здоровье'] -= g_push
                                            if knight['Здоровье'] <= 0:
                                                hp = goblin['Здоровье'] = 10
                                                print('Вы погибли от руки гоблина!')
                                            else:
                                                hp = goblin['Здоровье'] = 10
                                                print('Вы победили гоблина!')
                                                time.sleep(1)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(5)
                                                knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                         'в какую хотите войти - 1 или 2: '))
                                                if knight_door4 == 1:  # первая дверь
                                                    print('Вы выбрали первую дверь.')
                                                    time.sleep(1)
                                                    print('Немного осмотревшись вы увидели сундук. '
                                                          'Вы его открывайте и получайте + 15 здоровья.')
                                                    knight['Здоровье'] += 15
                                                    time.sleep(3)
                                                    print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                    time.sleep(3)
                                                    print('Вы проходите дальше и видите одну большую дверь.')
                                                    time.sleep(5)
                                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                    time.sleep(5)
                                                    knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                    if knight_door5 == 1:
                                                        print('Вы входите в комнату и видите огромного '
                                                              'гоблина перед собой.')
                                                        time.sleep(6)
                                                        print('Варианта "Cбежать" у вас нету, так как '
                                                              'это единственный выход из подземелья.')
                                                        time.sleep(10)
                                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                                              f'здоровье:{mega_goblin["Здоровье"]}, '
                                                              f'сила:{mega_goblin["Сила"]}')
                                                        time.sleep(7)
                                                        print('Ваши характеристики: здоровье - ',
                                                              knight.get('Здоровье'),
                                                              'сила - ', knight.get('Сила'))
                                                        time.sleep(9)
                                                        print('Вы начинайте атаковать гоблина.')
                                                        time.sleep(3)
                                                        while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                            k_push = random.randint(1, 10)
                                                            mg_push = random.randint(1, 13)
                                                            mega_goblin['Здоровье'] -= k_push
                                                            knight['Здоровье'] -= mg_push
                                                        if knight['Здоровье'] <= 0:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы погибли от руки гоблина!')
                                                        else:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы победили гоблина!')
                                                            time.sleep(1)
                                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                                    elif knight_door4 == 2:  # вторая дверь
                                                        print('Вы выбрали вторую дверь.')
                                                        time.sleep(1)
                                                        print('Немного осмотревшись вы увидели сундук. '
                                                              'Вы его открывайте и получайте + 15 здоровья.')
                                                        knight['Здоровье'] += 15
                                                        time.sleep(3)
                                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                        time.sleep(3)
                                                        print('Вы проходите дальше и видите одну большую дверь.')
                                                        time.sleep(5)
                                                        print(
                                                            'Это выход из подземелья, но его охраняет огромный гоблин.')
                                                        time.sleep(5)
                                                        knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                        if knight_door5 == 1:
                                                            print('Вы входите в комнату и видите огромного '
                                                                  'гоблина перед собой.')
                                                            time.sleep(6)
                                                            print('Варианта "Cбежать" у вас нету, так как '
                                                                  'это единственный выход из подземелья.')
                                                            time.sleep(10)
                                                            print(f'Вы видите перед собой гоблина с характеристиками: '
                                                                  f'здоровье:{mega_goblin["Здоровье"]}, '
                                                                  f'сила:{mega_goblin["Сила"]}')
                                                            time.sleep(7)
                                                            print('Ваши характеристики: здоровье - ',
                                                                  knight.get('Здоровье'),
                                                                  'сила - ', knight.get('Сила'))
                                                            time.sleep(9)
                                                            print('Вы начинайте атаковать гоблина.')
                                                            time.sleep(3)
                                                            while knight['Здоровье'] > 0 \
                                                                    and mega_goblin['Здоровье'] > 0:
                                                                k_push = random.randint(1, 10)
                                                                mg_push = random.randint(1, 13)
                                                                mega_goblin['Здоровье'] -= k_push
                                                                knight['Здоровье'] -= mg_push
                                                            if knight['Здоровье'] <= 0:
                                                                hp = mega_goblin['Здоровье'] == 70
                                                                print('Вы погибли от руки гоблина!')
                                                            else:
                                                                hp = mega_goblin['Здоровье'] == 70
                                                                print('Вы победили гоблина!')
                                                                time.sleep(1)
                                                                print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                elif knight_door2 == 2:  # вторая дверь
                    print('Проходя дальше, вы видите темный и плохо освещенный проход, но в далеке находится дверь.')
                    time.sleep(6)
                    print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                          goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                    knight_goblin1 = int(input('1.Атаковать или 2.Сбежать'
                                               '(при попытке сбежать вы потеряйте 3 здоровья): '))
                    if knight_goblin1 == 1:  # атака
                        print('Вы выбрали: атаковать')
                        time.sleep(1)
                        while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                            k_push = random.randint(1, 10)
                            g_push = random.randint(1, 10)
                            goblin['Здоровье'] -= k_push
                            knight['Здоровье'] -= g_push
                        if knight['Здоровье'] <= 0:
                            hp = goblin['Здоровье'] = 10
                            print('Вы погибли от руки гоблина!')
                        else:
                            hp = goblin['Здоровье'] = 10
                            print('Вы победили гоблина!')
                            time.sleep(1)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(5)
                            knight_door3 = int(input('Пройдя дальше вы видите две двери, '
                                                     'в какую хотите войти - 1 или 2: '))
                            if knight_door3 == 1:  # первая дверь
                                print('Проходя дальше, вы видите темный и плохо освещенный '
                                      'проход, но в далеке находится дверь.')
                                time.sleep(6)
                                print('Вы видите слайма с характеристиками: здоровье - ',
                                      slime.get('Здоровье'), 'сила - ', slime.get('Сила'))
                                knight_slime1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                          '2.Сбежать(при попытке сбежать вы потеряйте 7 здоровья): '))
                                if knight_slime1 == 1:  # атаковать
                                    print('Вы выбрали: атаковать.')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        sl_push = random.randint(1, 5)
                                        slime['Здоровье'] -= k_push
                                        knight['Здоровье'] -= sl_push
                                    if knight['Здоровье'] <= 0:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы погибли от слайма!')
                                    else:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы победили слайма.')
                                        time.sleep(1)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(5)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного '
                                                      'гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как '
                                                      'это единственный выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                      'сила -', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_slime1 == 2:  # сбежать -7 хп
                                    print('Вы выбрали: сбежать.')
                                    knight['Здоровье'] -= 7
                                    time.sleep(1)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья')
                                    else:
                                        print('Вам удалось сбежать, но вы потеряли 7 здоровья.')
                                        time.sleep(5)
                                        print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                        time.sleep(3)
                                        print('Вы входите в другую дверь.')
                                        time.sleep(3)
                                        print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                              f'здоровье:{slime["Здоровье"]}')
                                        time.sleep(7)
                                        print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                              'использовать нельзя, вы автоматический будете атаковать монстра.')
                                        time.sleep(7)
                                        print('Вы атакуйте слайма.')
                                        time.sleep(3)
                                        while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sl_push
                                        if knight['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли от слайма!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                          'сила -', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                                elif knight_door4 == 2:  # вторая дверь
                                                    print('Вы выбрали вторую дверь.')
                                                    time.sleep(1)
                                                    print('Немного осмотревшись вы увидели сундук. '
                                                          'Вы его открывайте и получайте + 15 здоровья.')
                                                    knight['Здоровье'] += 15
                                                    time.sleep(3)
                                                    print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                    time.sleep(3)
                                                    print('Вы проходите дальше и видите одну большую дверь.')
                                                    time.sleep(5)
                                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                    time.sleep(5)
                                                    knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                    if knight_door5 == 1:
                                                        print('Вы входите в комнату и видите огромного '
                                                              'гоблина перед собой.')
                                                        time.sleep(6)
                                                        print('Варианта "Cбежать" у вас нету, так как '
                                                              'это единственный выход из подземелья.')
                                                        time.sleep(10)
                                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                                              f'здоровье:{mega_goblin["Здоровье"]}, '
                                                              f'сила:{mega_goblin["Сила"]}')
                                                        time.sleep(7)
                                                        print('Ваши характеристики: здоровье - ',
                                                              knight.get('Здоровье'),
                                                              'сила - ', knight.get('Сила'))
                                                        time.sleep(9)
                                                        print('Вы начинайте атаковать гоблина.')
                                                        time.sleep(3)
                                                        while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                            k_push = random.randint(1, 10)
                                                            mg_push = random.randint(1, 13)
                                                            mega_goblin['Здоровье'] -= k_push
                                                            knight['Здоровье'] -= mg_push
                                                        if knight['Здоровье'] <= 0:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы погибли от руки гоблина!')
                                                        else:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы победили гоблина!')
                                                            time.sleep(1)
                                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                            elif knight_door3 == 2:  # вторая дверь
                                print('Слабо освещенный проход ведет к заветной двери')
                                time.sleep(1)
                                print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'),
                                      'сила - ', spider.get('Сила'))
                                time.sleep(8)
                                knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                           '2.Сбежать(при попытке сбежать вы потеряйте 5 здоровья): '))
                                if knight_spider1 == 1:  # атаковать
                                    print('Вы выбрали: атаковать.')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        sp_push = random.randint(1, 10)
                                        spider['Здоровье'] -= k_push
                                        knight['Здоровье'] -= sp_push
                                    if knight['Здоровье'] <= 0:
                                        hp = spider['Здоровье'] == 15
                                        print('Вы погибли от паука!')
                                    else:
                                        hp = spider['Здоровье'] == 15
                                        print('Вы победили паука!')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(5)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного '
                                                      'гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как '
                                                      'это единственный выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                      'сила -', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_spider1 == 2:  # сбежать -5 хп
                                    print('Вы выбрали: сбежать.')
                                    knight['Здоровье'] -= 5
                                    time.sleep(1)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья!')
                                    else:
                                        print('Вам удалось сбежать, но вы потеряли 5 здоровья.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight['Здоровье'])
                                        time.sleep(5)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного '
                                                      'гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как '
                                                      'это единственный выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                      'сила -', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                    elif knight_goblin1 == 2:  # сбежать -3 хп
                        print('Вы выбрали: сбжеать')
                        knight['Здоровье'] -= 3
                        time.sleep(1)
                        if knight['Здоровье'] <= 0:
                            print('Вы погибли от потери здоровья.')
                        else:
                            print('Вам удалось сбежать, но вы потеряли 3 здоровья.')
                            time.sleep(3)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(5)
                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                            time.sleep(5)
                            print('Вы входите в другую дверь.')
                            time.sleep(3)
                            print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                  f'здоровье:{slime["Здоровье"]}')
                            time.sleep(7)
                            print('Напонимаем: раз уж вы уже выбирали вариант "сбежать", второй раз его '
                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                            time.sleep(8)
                            while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                k_push = random.randint(1, 10)
                                sl_push = random.randint(1, 5)
                                slime['Здоровье'] -= k_push
                                knight['Здоровье'] -= sl_push
                            if knight['Здоровье'] <= 0:
                                hp = slime['Здоровье'] == 30
                                print('Вы погибли от слайма!')
                            else:
                                hp = slime['Здоровье'] == 30
                                print('Вы победили слайма.')
                                time.sleep(3)
                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                time.sleep(5)
                                knight_door3 = int(input('Пройдя дальше вы видите две двери, '
                                                         'в какую хотите войти - 1 или 2: '))
                                if knight_door3 == 1:  # первая дверь
                                    print('Слабо освещенный проход ведет к заветной двери.')
                                    time.sleep(3)
                                    print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'),
                                          'сила - ', spider.get('Сила'))
                                    time.sleep(8)
                                    knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 5 здоровья): '))
                                    if knight_spider1 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sp_push = random.randint(1, 10)
                                            spider['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sp_push
                                        if knight['Здоровье'] <= 0:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы погибли от паука!')
                                        else:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы победили паука!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_door3 == 2:
                                    print('Длинный проход, весь в плесени и паутине вел к двери.')
                                    time.sleep(5)
                                    print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'),
                                          'сила - ', spider.get('Сила'))
                                    time.sleep(8)
                                    knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 5 здоровья): '))
                                    if knight_spider1 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sp_push = random.randint(1, 10)
                                            spider['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sp_push
                                        if knight['Здоровье'] <= 0:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы погибли от паука!')
                                        else:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы победили паука!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
        elif knight_skeleton1 == 2:  # сбежать -5 хп
            print('Вы выбрали: сбежать.')
            knight['Здоровье'] -= 5
            time.sleep(1)
            if knight['Здоровье'] <= 0:
                print('Вы погибли от потери здоровья.')
            else:
                print('Вам удалось сбежать, но вы потеряли 5 здоровья.')
                time.sleep(3)
                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                time.sleep(3)
                knight_door2 = int(input('Пройдя дальше вы видите две двери, в какую войдете - 1 или 2: '))
                if knight_door2 == 1:  # первая дверь
                    print('Длинный проход, весь в плесени и паутине вел к двери.')
                    time.sleep(5)
                    print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'), 'сила - ',
                          spider.get('Сила'))
                    time.sleep(8)
                    knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                               '2.Сбежать(при попытке сбежать вы потеряйте 5 здоровья): '))
                    if knight_spider1 == 1:  # атаковать
                        print('Вы выбрали: атаковать.')
                        time.sleep(1)
                        while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                            k_push = random.randint(1, 10)
                            sp_push = random.randint(1, 10)
                            spider['Здоровье'] -= k_push
                            knight['Здоровье'] -= sp_push
                        if knight['Здоровье'] <= 0:
                            hp = spider['Здоровье'] == 15
                            print('Вы погибли от паука!')
                        else:
                            hp = spider['Здоровье'] == 15
                            print('Вы победили паука!')
                            time.sleep(1)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(3)
                            knight_door3 = int(input('Пройдя дальше вы видите две двери, в какую войдете - 1 или 2: '))
                            if knight_door3 == 1:  # первая дверь
                                print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                                time.sleep(5)
                                print('Вы видите слайма с характеристиками: здоровье - ',
                                      slime.get('Здоровье'), 'сила - ', slime.get('Сила'))
                                knight_slime1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                          '2.Сбежать(при попытке сбежать вы потеряйте 7 здоровья): '))
                                if knight_slime1 == 1:  # атаковать
                                    print('Вы выбрали: атаковать.')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        sl_push = random.randint(1, 5)
                                        slime['Здоровье'] -= k_push
                                        knight['Здоровье'] -= sl_push
                                    if knight['Здоровье'] <= 0:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы погибли от слайма!')
                                    else:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы победили слайма.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(3)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif knight_door4 == 2:  # вторая дверь
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_slime1 == 2:  # сбежать -7
                                    print('Вы выбрали: сбежать.')
                                    knight['Здоровье'] -= 7
                                    time.sleep(1)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья!')
                                    else:
                                        print('У вас удалось сбежать, но вы потеряли 7 здоровья.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья: ', knight.get('Здоровье'))
                                        time.sleep(3)
                                        knight_door4 = int(input('Немного пройдя вперед вы видите две двери, '
                                                                 'в какую войдете - 1 или 2:'))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif knight_door4 == 2:  # вторая дверь
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                            elif knight_door3 == 2:  # вторая дверь
                                print('Проходя дальше, вы видите темный и плохо освещенный проход, '
                                      'но в далеке находится дверь.')
                                time.sleep(6)
                                print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                                      goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                                knight_goblin1 = int(input('1.Атаковать или '
                                                           '2.Сбежать(при попытке сбежать вы потеряйте 3 здоровья): '))
                                if knight_goblin1 == 1:  # атака
                                    print('Вы выбрали: атаковать')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        g_push = random.randint(1, 10)
                                        goblin['Здоровье'] -= k_push
                                        knight['Здоровье'] -= g_push
                                    if knight['Здоровье'] <= 0:
                                        hp = goblin['Здоровье'] = 10
                                        print('Вы погибли от руки гоблина!')
                                    else:
                                        hp = goblin['Здоровье'] = 10
                                        print('Вы победили гоблина!')
                                        time.sleep(1)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(3)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                        elif knight_door4 == 2:  # вторая дверь
                                            print('Вы выбрали вторую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                      'из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                      'сила - ', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_goblin1 == 2:  # сбежать -3 хп
                                    print('Вы выбрали: сбежать')
                                    knight['Здоровье'] -= 3
                                    time.sleep(3)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья.')
                                    else:
                                        print('Вам удалось сбежать, но вы потеря 3 здоровья.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(3)
                                        print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                        time.sleep(5)
                                        print('Вы входите в другую дверь.')
                                        time.sleep(3)
                                        print('Вы встретили слайма, его сила - ', slime.get('Сила'), 'его здоровье - ',
                                              slime.get('Здоровье'))
                                        time.sleep(7)
                                        print('Напоминаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                              'использовать нельзя, вы автоматический будете атаковать монстра.')
                                        time.sleep(7)
                                        print('Вы атакуйте слайма.')
                                        time.sleep(3)
                                        while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sl_push
                                        if knight['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли от слайма!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма.')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                          'сила -', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                    elif knight_spider1 == 2:  # сбежать -5
                        print('Вы выбрали: сбежать.')
                        knight['Здоровье'] -= 5
                        time.sleep(3)
                        if knight['Здоровье'] <= 0:
                            print('Вы погибли от потери здоровья.')
                        else:
                            print('Вам удалось сбежать, но вы потеряли 5 здоровья.')
                            time.sleep(3)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(3)
                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                            time.sleep(3)
                            print('Вы входите в другую дверь.')
                            time.sleep(3)
                            print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                  f'здоровье:{slime["Здоровье"]}')
                            time.sleep(7)
                            print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                            time.sleep(7)
                            print('Вы атакуйте слайма.')
                            time.sleep(3)
                            while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                k_push = random.randint(1, 10)
                                sl_push = random.randint(1, 5)
                                slime['Здоровье'] -= k_push
                                knight['Здоровье'] -= sl_push
                            if knight['Здоровье'] <= 0:
                                hp = slime['Здоровье'] == 30
                                print('Вы погибли от слайма!')
                            else:
                                hp = slime['Здоровье'] == 30
                                print('Вы победили слайма!')
                                time.sleep(1)
                                knight_door3 = int(input('Пройдя дальше вы видите две двери, '
                                                         'в какую хотите войти - 1 или 2: '))
                                if knight_door3 == 1:  # первая дверь
                                    print('Проходя дальше, вы видите темный и плохо освещенный '
                                          'проход, но в далеке находится дверь.')
                                    time.sleep(6)
                                    print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                                          goblin.get('Здоровье'), ',сила -', goblin.get('Сила'))
                                    knight_goblin1 = int(input('1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 3 здоровья): '))
                                    if knight_goblin1 == 1:  # атака
                                        print('Вы выбрали: атаковать')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            g_push = random.randint(1, 10)
                                            goblin['Здоровье'] -= k_push
                                            knight['Здоровье'] -= g_push
                                        if knight['Здоровье'] <= 0:
                                            hp = goblin['Здоровье'] = 10
                                            print('Вы погибли от руки гоблина!')
                                        else:
                                            hp = goblin['Здоровье'] = 10
                                            print('Вы победили гоблина!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif knight_goblin1 == 2:  # сбежать -3 хп
                                        print('Вы выбрали: сбежать')
                                        time.sleep(1)
                                        knight['Здоровье'] -= 3
                                        if knight['Здоровье'] <= 0:
                                            print('Вы погибли от потери здоровья.')
                                        else:
                                            print('Вам удалось сбежать, но вы потеряли 3 здоровья.')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Раз уж из одной двери вы сбежали, тогда вам стоит '
                                                  'зайти в другую дверь.')
                                            time.sleep(5)
                                            knight_door4 = int(input('Выберите действие - 1.Войти: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы входите в другую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_door3 == 2:  # вторая дверь
                                    print('Слабо освещенный проход ведет к заветной двери.')
                                    time.sleep(3)
                                    print('Вы видите слайма с характеристиками: здоровье - ',
                                          slime.get('Здоровье'), 'сила - ', slime.get('Сила'))
                                    knight_slime1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                              '2.Сбежать(при попытке сбежать вы '
                                                              'потеряйте 7 здоровья): '))
                                    if knight_slime1 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sl_push
                                        if knight['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли от слайма!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма.')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                                elif knight_door4 == 2:  # вторая дверь
                                                    print('Вы выбрали вторую дверь.')
                                                    time.sleep(1)
                                                    print('Немного осмотревшись вы увидели сундук. '
                                                          'Вы его открывайте и получайте + 15 здоровья.')
                                                    knight['Здоровье'] += 15
                                                    time.sleep(3)
                                                    print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                    time.sleep(3)
                                                    print('Вы проходите дальше и видите одну большую дверь.')
                                                    time.sleep(5)
                                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                    time.sleep(5)
                                                    knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                    if knight_door5 == 1:
                                                        print('Вы входите в комнату и видите '
                                                              'огромного гоблина перед собой.')
                                                        time.sleep(6)
                                                        print('Варианта "Cбежать" у вас нету, так как '
                                                              'это единственный выход из подземелья.')
                                                        time.sleep(10)
                                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                                              f'здоровье:{mega_goblin["Здоровье"]}, '
                                                              f'сила:{mega_goblin["Сила"]}')
                                                        time.sleep(7)
                                                        print('Ваши характеристики: здоровье - ',
                                                              knight.get('Здоровье'),
                                                              'сила - ', knight.get('Сила'))
                                                        time.sleep(9)
                                                        print('Вы начинайте атаковать гоблина.')
                                                        time.sleep(3)
                                                        while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                            k_push = random.randint(1, 10)
                                                            mg_push = random.randint(1, 13)
                                                            mega_goblin['Здоровье'] -= k_push
                                                            knight['Здоровье'] -= mg_push
                                                        if knight['Здоровье'] <= 0:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы погибли от руки гоблина!')
                                                        else:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы победили гоблина!')
                                                            time.sleep(1)
                                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                    elif knight_slime1 == 2:  # сбежать -7 хп
                                        print('Вы выбрали: сбежать.')
                                        knight['Здоровье'] -= 7
                                        time.sleep(1)
                                        if knight['Здоровье'] <= 0:
                                            print('Вы погибли от потери здоровья!')
                                        else:
                                            print('Вам удалось сбежать, но вы потеряли 7 здоровья.')
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                            time.sleep(5)
                                            print('Вы входите в другую дверь.')
                                            time.sleep(3)
                                            print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                                                  goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                                            time.sleep(6)
                                            print('Напоминаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                                            time.sleep(5)
                                            print('Вы начинайте атаковать гоблина.')
                                            time.sleep(3)
                                            while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                                                k_push = random.randint(1, 10)
                                                g_push = random.randint(1, 10)
                                                goblin['Здоровье'] -= k_push
                                                knight['Здоровье'] -= g_push
                                            if knight['Здоровье'] <= 0:
                                                hp = goblin['Здоровье'] = 10
                                                print('Вы погибли от руки гоблина!')
                                            else:
                                                hp = goblin['Здоровье'] = 10
                                                print('Вы победили гоблина!')
                                                time.sleep(1)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(5)
                                                knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                         'в какую хотите войти - 1 или 2: '))
                                                if knight_door4 == 1:  # первая дверь
                                                    print('Вы выбрали первую дверь.')
                                                    time.sleep(1)
                                                    print('Немного осмотревшись вы увидели сундук. '
                                                          'Вы его открывайте и получайте + 15 здоровья.')
                                                    knight['Здоровье'] += 15
                                                    time.sleep(3)
                                                    print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                    time.sleep(3)
                                                    print('Вы проходите дальше и видите одну большую дверь.')
                                                    time.sleep(5)
                                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                    time.sleep(5)
                                                    knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                    if knight_door5 == 1:
                                                        print('Вы входите в комнату и видите огромного '
                                                              'гоблина перед собой.')
                                                        time.sleep(6)
                                                        print('Варианта "Cбежать" у вас нету, так как '
                                                              'это единственный выход из подземелья.')
                                                        time.sleep(10)
                                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                                              f'здоровье:{mega_goblin["Здоровье"]}, '
                                                              f'сила:{mega_goblin["Сила"]}')
                                                        time.sleep(7)
                                                        print('Ваши характеристики: здоровье - ',
                                                              knight.get('Здоровье'),
                                                              'сила - ', knight.get('Сила'))
                                                        time.sleep(9)
                                                        print('Вы начинайте атаковать гоблина.')
                                                        time.sleep(3)
                                                        while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                            k_push = random.randint(1, 10)
                                                            mg_push = random.randint(1, 13)
                                                            mega_goblin['Здоровье'] -= k_push
                                                            knight['Здоровье'] -= mg_push
                                                        if knight['Здоровье'] <= 0:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы погибли от руки гоблина!')
                                                        else:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы победили гоблина!')
                                                            time.sleep(1)
                                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                                    elif knight_door4 == 2:  # вторая дверь
                                                        print('Вы выбрали вторую дверь.')
                                                        time.sleep(1)
                                                        print('Немного осмотревшись вы увидели сундук. '
                                                              'Вы его открывайте и получайте + 15 здоровья.')
                                                        knight['Здоровье'] += 15
                                                        time.sleep(3)
                                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                        time.sleep(3)
                                                        print('Вы проходите дальше и видите одну большую дверь.')
                                                        time.sleep(5)
                                                        print(
                                                            'Это выход из подземелья, но его охраняет огромный гоблин.')
                                                        time.sleep(5)
                                                        knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                        if knight_door5 == 1:
                                                            print('Вы входите в комнату и видите огромного '
                                                                  'гоблина перед собой.')
                                                            time.sleep(6)
                                                            print('Варианта "Cбежать" у вас нету, так как '
                                                                  'это единственный выход из подземелья.')
                                                            time.sleep(10)
                                                            print(f'Вы видите перед собой гоблина с характеристиками: '
                                                                  f'здоровье:{mega_goblin["Здоровье"]}, '
                                                                  f'сила:{mega_goblin["Сила"]}')
                                                            time.sleep(7)
                                                            print('Ваши характеристики: здоровье - ',
                                                                  knight.get('Здоровье'),
                                                                  'сила - ', knight.get('Сила'))
                                                            time.sleep(9)
                                                            print('Вы начинайте атаковать гоблина.')
                                                            time.sleep(3)
                                                            while knight['Здоровье'] > 0 \
                                                                    and mega_goblin['Здоровье'] > 0:
                                                                k_push = random.randint(1, 10)
                                                                mg_push = random.randint(1, 13)
                                                                mega_goblin['Здоровье'] -= k_push
                                                                knight['Здоровье'] -= mg_push
                                                            if knight['Здоровье'] <= 0:
                                                                hp = mega_goblin['Здоровье'] == 70
                                                                print('Вы погибли от руки гоблина!')
                                                            else:
                                                                hp = mega_goblin['Здоровье'] == 70
                                                                print('Вы победили гоблина!')
                                                                time.sleep(1)
                                                                print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                elif knight_door2 == 2:  # вторая дверь
                    print('Длинный проход, весь в плесени и паутине вел к двери.')
                    time.sleep(5)
                    print('Вы видите перед собой гоблина с характеристиками: здоровье -',
                          goblin.get('Здоровье'), ',' 'сила -', goblin.get('Сила'))
                    knight_goblin1 = int(input('1.Атаковать или 2.Сбежать'
                                               '(при попытке сбежать вы потеряйте 3 здоровья): '))
                    if knight_goblin1 == 1:  # атака
                        print('Вы выбрали: атаковать')
                        time.sleep(1)
                        while knight['Здоровье'] > 0 and goblin['Здоровье'] > 0:
                            k_push = random.randint(1, 10)
                            g_push = random.randint(1, 10)
                            goblin['Здоровье'] -= k_push
                            knight['Здоровье'] -= g_push
                        if knight['Здоровье'] <= 0:
                            hp = goblin['Здоровье'] = 10
                            print('Вы погибли от руки гоблина!')
                        else:
                            hp = goblin['Здоровье'] = 10
                            print('Вы победили гоблина!')
                            time.sleep(1)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(5)
                            knight_door3 = int(input('Пройдя дальше вы видите две двери, '
                                                     'в какую хотите войти - 1 или 2: '))
                            if knight_door3 == 1:  # первая дверь
                                print('Длинный проход, весь в плесени и паутине вел к двери.')
                                time.sleep(5)
                                print('Вы видите слайма с характеристиками: здоровье - ',
                                      slime.get('Здоровье'), 'сила - ', slime.get('Сила'))
                                knight_slime1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                          '2.Сбежать(при попытке сбежать вы потеряйте 7 здоровья): '))
                                if knight_slime1 == 1:  # атаковать
                                    print('Вы выбрали: атаковать.')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        sl_push = random.randint(1, 5)
                                        slime['Здоровье'] -= k_push
                                        knight['Здоровье'] -= sl_push
                                    if knight['Здоровье'] <= 0:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы погибли от слайма!')
                                    else:
                                        hp = slime['Здоровье'] == 30
                                        print('Вы победили слайма.')
                                        time.sleep(1)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(5)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного '
                                                      'гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как '
                                                      'это единственный выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                      'сила -', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_slime1 == 2:  # сбежать -7 хп
                                    print('Вы выбрали: сбежать.')
                                    knight['Здоровье'] -= 7
                                    time.sleep(1)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья')
                                    else:
                                        print('Вам удалось сбежать, но вы потеряли 7 здоровья.')
                                        time.sleep(5)
                                        print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                                        time.sleep(3)
                                        print('Вы входите в другую дверь.')
                                        time.sleep(3)
                                        print(f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                              f'здоровье:{slime["Здоровье"]}')
                                        time.sleep(7)
                                        print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                              'использовать нельзя, вы автоматический будете атаковать монстра.')
                                        time.sleep(7)
                                        print('Вы атакуйте слайма.')
                                        time.sleep(3)
                                        while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sl_push = random.randint(1, 5)
                                            slime['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sl_push
                                        if knight['Здоровье'] <= 0:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы погибли от слайма!')
                                        else:
                                            hp = slime['Здоровье'] == 30
                                            print('Вы победили слайма!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                          'сила -', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                                elif knight_door4 == 2:  # вторая дверь
                                                    print('Вы выбрали вторую дверь.')
                                                    time.sleep(1)
                                                    print('Немного осмотревшись вы увидели сундук. '
                                                          'Вы его открывайте и получайте + 15 здоровья.')
                                                    knight['Здоровье'] += 15
                                                    time.sleep(3)
                                                    print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                    time.sleep(3)
                                                    print('Вы проходите дальше и видите одну большую дверь.')
                                                    time.sleep(5)
                                                    print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                    time.sleep(5)
                                                    knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                    if knight_door5 == 1:
                                                        print('Вы входите в комнату и видите огромного '
                                                              'гоблина перед собой.')
                                                        time.sleep(6)
                                                        print('Варианта "Cбежать" у вас нету, так как '
                                                              'это единственный выход из подземелья.')
                                                        time.sleep(10)
                                                        print(f'Вы видите перед собой гоблина с характеристиками: '
                                                              f'здоровье:{mega_goblin["Здоровье"]}, '
                                                              f'сила:{mega_goblin["Сила"]}')
                                                        time.sleep(7)
                                                        print('Ваши характеристики: здоровье - ',
                                                              knight.get('Здоровье'),
                                                              'сила - ', knight.get('Сила'))
                                                        time.sleep(9)
                                                        print('Вы начинайте атаковать гоблина.')
                                                        time.sleep(3)
                                                        while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                            k_push = random.randint(1, 10)
                                                            mg_push = random.randint(1, 13)
                                                            mega_goblin['Здоровье'] -= k_push
                                                            knight['Здоровье'] -= mg_push
                                                        if knight['Здоровье'] <= 0:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы погибли от руки гоблина!')
                                                        else:
                                                            hp = mega_goblin['Здоровье'] == 70
                                                            print('Вы победили гоблина!')
                                                            time.sleep(1)
                                                            print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                            elif knight_door3 == 2:  # вторая дверь
                                print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                                time.sleep(5)
                                print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'),
                                      'сила - ', spider.get('Сила'))
                                time.sleep(8)
                                knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или '
                                                           '2.Сбежать(при попытке сбежать вы потеряйте 5 здоровья): '))
                                if knight_spider1 == 1:  # атаковать
                                    print('Вы выбрали: атаковать.')
                                    time.sleep(1)
                                    while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                                        k_push = random.randint(1, 10)
                                        sp_push = random.randint(1, 10)
                                        spider['Здоровье'] -= k_push
                                        knight['Здоровье'] -= sp_push
                                    if knight['Здоровье'] <= 0:
                                        hp = spider['Здоровье'] == 15
                                        print('Вы погибли от паука!')
                                    else:
                                        hp = spider['Здоровье'] == 15
                                        print('Вы победили паука!')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                        time.sleep(5)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного '
                                                      'гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как '
                                                      'это единственный выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                      'сила -', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_spider1 == 2:  # сбежать -5 хп
                                    print('Вы выбрали: сбежать.')
                                    knight['Здоровье'] -= 5
                                    time.sleep(1)
                                    if knight['Здоровье'] <= 0:
                                        print('Вы погибли от потери здоровья!')
                                    else:
                                        print('Вам удалось сбежать, но вы потеряли 5 здоровья.')
                                        time.sleep(3)
                                        print('Теперь у вас здоровья:', knight['Здоровье'])
                                        time.sleep(5)
                                        knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                 'в какую хотите войти - 1 или 2: '))
                                        if knight_door4 == 1:  # первая дверь
                                            print('Вы выбрали первую дверь.')
                                            time.sleep(1)
                                            print('Немного осмотревшись вы увидели сундук. '
                                                  'Вы его открывайте и получайте + 15 здоровья.')
                                            knight['Здоровье'] += 15
                                            time.sleep(3)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(3)
                                            print('Вы проходите дальше и видите одну большую дверь.')
                                            time.sleep(5)
                                            print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                            time.sleep(5)
                                            knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                            if knight_door5 == 1:
                                                print('Вы входите в комнату и видите огромного '
                                                      'гоблина перед собой.')
                                                time.sleep(6)
                                                print('Варианта "Cбежать" у вас нету, так как '
                                                      'это единственный выход из подземелья.')
                                                time.sleep(10)
                                                print(f'Вы видите перед собой гоблина с характеристиками: '
                                                      f'здоровье:{mega_goblin["Здоровье"]}, '
                                                      f'сила:{mega_goblin["Сила"]}')
                                                time.sleep(7)
                                                print('Ваши характеристики: здоровье -', knight.get('Здоровье'),
                                                      'сила -', knight.get('Сила'))
                                                time.sleep(9)
                                                print('Вы начинайте атаковать гоблина.')
                                                time.sleep(3)
                                                while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                    k_push = random.randint(1, 10)
                                                    mg_push = random.randint(1, 13)
                                                    mega_goblin['Здоровье'] -= k_push
                                                    knight['Здоровье'] -= mg_push
                                                if knight['Здоровье'] <= 0:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы погибли от руки гоблина!')
                                                else:
                                                    hp = mega_goblin['Здоровье'] == 70
                                                    print('Вы победили гоблина!')
                                                    time.sleep(1)
                                                    print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print('Вы входите в комнату и видите огромного '
                                                          'гоблина перед собой.')
                                                    time.sleep(6)
                                                    print('Варианта "Cбежать" у вас нету, так как '
                                                          'это единственный выход из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                    elif knight_goblin1 == 2:  # сбежать -3 хп
                        print('Вы выбрали: сбжеать')
                        knight['Здоровье'] -= 3
                        time.sleep(1)
                        if knight['Здоровье'] <= 0:
                            print('Вы погибли от потери здоровья.')
                        else:
                            print('Вам удалось сбежать, но вы потеряли 3 здоровья.')
                            time.sleep(3)
                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                            time.sleep(5)
                            print('Раз уж из одной двери вы сбежали, тогда вы заходите в другую дверь.')
                            time.sleep(5)
                            print('Вы входите в другую дверь.')
                            time.sleep(3)
                            print(
                                f'Там вы встретили слайма его характеристика - сила:{slime["Сила"]}, '
                                f'здоровье:{slime["Здоровье"]}')
                            time.sleep(7)
                            print('Напонимаем: раз уж вы уже выбирали вариант сбежать, второй раз его '
                                  'использовать нельзя, вы автоматический будете атаковать монстра.')
                            time.sleep(8)
                            while knight['Здоровье'] > 0 and slime['Здоровье'] > 0:
                                k_push = random.randint(1, 10)
                                sl_push = random.randint(1, 5)
                                slime['Здоровье'] -= k_push
                                knight['Здоровье'] -= sl_push
                            if knight['Здоровье'] <= 0:
                                hp = slime['Здоровье'] == 30
                                print('Вы погибли от слайма!')
                            else:
                                hp = slime['Здоровье'] == 30
                                print('Вы победили слайма.')
                                time.sleep(3)
                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                time.sleep(5)
                                knight_door3 = int(input('Пройдя дальше вы видите две двери, '
                                                         'в какую хотите войти - 1 или 2: '))
                                if knight_door3 == 1:  # первая дверь
                                    print('Немного пройдя по плохо освещенной комнате, вы находите и входите в дверь.')
                                    time.sleep(5)
                                    print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'),
                                          'сила - ',
                                          spider.get('Сила'))
                                    time.sleep(8)
                                    knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 5 здоровья): '))
                                    if knight_spider1 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sp_push = random.randint(1, 10)
                                            spider['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sp_push
                                        if knight['Здоровье'] <= 0:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы погибли от паука!')
                                        else:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы победили паука!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                elif knight_door3 == 2:
                                    print('Проходя дальше, вы видите темный и плохо освещенный '
                                          'проход, но в далеке находится дверь.')
                                    time.sleep(6)
                                    print('Вы видите паука с характеристиками: здоровье - ', spider.get('Здоровье'),
                                          'сила - ', spider.get('Сила'))
                                    time.sleep(8)
                                    knight_spider1 = int(input('Что вы хотите выбрать - 1.Атаковать или 2.Сбежать'
                                                               '(при попытке сбежать вы потеряйте 5 здоровья): '))
                                    if knight_spider1 == 1:  # атаковать
                                        print('Вы выбрали: атаковать.')
                                        time.sleep(1)
                                        while knight['Здоровье'] > 0 and spider['Здоровье'] > 0:
                                            k_push = random.randint(1, 10)
                                            sp_push = random.randint(1, 10)
                                            spider['Здоровье'] -= k_push
                                            knight['Здоровье'] -= sp_push
                                        if knight['Здоровье'] <= 0:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы погибли от паука!')
                                        else:
                                            hp = spider['Здоровье'] == 15
                                            print('Вы победили паука!')
                                            time.sleep(1)
                                            print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                            time.sleep(5)
                                            knight_door4 = int(input('Пройдя дальше вы видите две двери, '
                                                                     'в какую хотите войти - 1 или 2: '))
                                            if knight_door4 == 1:  # первая дверь
                                                print('Вы выбрали первую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')
# СДЕЛАНО
                                            elif knight_door4 == 2:  # вторая дверь
                                                print('Вы выбрали вторую дверь.')
                                                time.sleep(1)
                                                print('Немного осмотревшись вы увидели сундук. '
                                                      'Вы его открывайте и получайте + 15 здоровья.')
                                                knight['Здоровье'] += 15
                                                time.sleep(3)
                                                print('Теперь у вас здоровья:', knight.get('Здоровье'))
                                                time.sleep(3)
                                                print('Вы проходите дальше и видите одну большую дверь.')
                                                time.sleep(5)
                                                print('Это выход из подземелья, но его охраняет огромный гоблин.')
                                                time.sleep(5)
                                                knight_door5 = int(input('Хотите ли вы войти туда - 1.Да: '))
                                                if knight_door5 == 1:
                                                    print(
                                                        'Вы входите в комнату и видите огромного гоблина перед собой.')
                                                    time.sleep(6)
                                                    print(
                                                        'Варианта "Cбежать" у вас нету, так как это единственный выход '
                                                        'из подземелья.')
                                                    time.sleep(10)
                                                    print(f'Вы видите перед собой гоблина с характеристиками: '
                                                          f'здоровье:{mega_goblin["Здоровье"]}, '
                                                          f'сила:{mega_goblin["Сила"]}')
                                                    time.sleep(7)
                                                    print('Ваши характеристики: здоровье - ', knight.get('Здоровье'),
                                                          'сила - ', knight.get('Сила'))
                                                    time.sleep(9)
                                                    print('Вы начинайте атаковать гоблина.')
                                                    time.sleep(3)
                                                    while knight['Здоровье'] > 0 and mega_goblin['Здоровье'] > 0:
                                                        k_push = random.randint(1, 10)
                                                        mg_push = random.randint(1, 13)
                                                        mega_goblin['Здоровье'] -= k_push
                                                        knight['Здоровье'] -= mg_push
                                                    if knight['Здоровье'] <= 0:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы погибли от руки гоблина!')
                                                    else:
                                                        hp = mega_goblin['Здоровье'] == 70
                                                        print('Вы победили гоблина!')
                                                        time.sleep(1)
                                                        print('Поздравляю, вы прошли игру!')