from jinja2 import Environment, FileSystemLoader, select_autoescape
import random
import os


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html'])
    )
    template = env.get_template('template.html')

    races = [
        "орк",
        "человек",
        "гном",
        "эльфы",
        "нежить",
        "гоблин",
        "троль"
    ]

    character_classes = [
        "охотник",
        "ассасин",
        "бард",
        "воин",
        "маг"
    ]

    clases_base = {
        "маг": {
            'skils':['Стрела лядяного огня', 'Снятие проклятия', 'Огненный взрыв', 'Ледяное конпье', 'Конус холода', 'Прилив сил', 'Морозный доспех'],
            'strength': random.randint(1,3),
            'agility': random.randint(1,3),
            'intelligence': 15,
            'luck': random.randint(1,3),
            'temper': random.randint(1,3),
            'image': "../images/wizard.png"
        },
        "воин": {
            'skils':['Блок щитом', 'Казнь', 'Рывок', 'Боевой крик', 'Вихрь', 'Парирование', 'Мощный удар', 'Глубокие раны'],
            'strength': 15,
            'agility':random.randint(1,3),
            'intelligence':random.randint(1,3),
            'luck':random.randint(1,3),
            'temper':random.randint(1,3),
            'image': "../images/warrior.png"
        },
        "охотник": {
            'skils':['Верный выстрел', 'Чародейский выстрел', 'Стенающая стрела', 'Стрелы ветра', 'Призыв питомца', 'Глаз зверя', 'Осветительная ракета', 'Приручение животного'],
            'strength':random.randint(1,3),
            'agility': 15,
            'intelligence':random.randint(1,3),
            'luck':random.randint(1,3),
            'temper':random.randint(1,3),
            'image': "../images/archer.png"
        },
        "ассасин": {
            'skils':['Отравление', 'Взлом замка', 'Подлый трюк', 'Исчезновение', 'Ложный выпад', 'Внезапный удар', 'Ошеломление', 'Спринт'],
            'strength':random.randint(1,3),
            'agility':random.randint(1,3),
            'intelligence':random.randint(1,3),
            'luck': 15,
            'temper':random.randint(1,3),
            'image': "../images/assasin.png"
        },
        "бард": {
            'skils':['Аккорды ветра', 'Аккорды воды', 'Исцеление', 'Соната жизни', 'Пауза', 'Плач сирен', 'Песнь ветра', 'Реквием'],
            'strength':random.randint(1,3),
            'agility':random.randint(1,3),
            'intelligence':random.randint(1,3),
            'luck':random.randint(1,3),
            'temper':15,
            'image': "../images/bard.webp"
        }
    }

    os.makedirs('cards',exist_ok=True)
    count = int(input("сколько карточек надо сделать? "))

    for number in range(count):
        character_name = input("введите имя персонажа: ")
        race = int(input("выберите расу:1 - орк, 2 - человек, 3 - гном, 4 - эльф, 5 - нежить, 6 - гоблин, 7 - троль: "))
        character_race = races[race - 1]
        character_class = int(input("выберите класс: 1 - охотник, 2 - ассасин, 3 - бард, 4 - воин, 5 - маг: "))
        character_class = character_classes[character_class - 1]
        character_strength = clases_base[character_class]["strength"]
        character_agility = clases_base[character_class]["agility"]
        character_intelligence = clases_base[character_class]["intelligence"]
        character_luck = clases_base[character_class]["luck"]
        character_temper = clases_base[character_class]["temper"]
        image = clases_base[character_class]["image"]

        skills = random.sample(clases_base[character_class]["skils"],3)
        first_skill = skills[0]
        second_skill = skills[1]
        third_skill = skills[2]

        rendered_page = template.render(name = character_name, race = character_race, character_class = character_class, strength = character_strength, agility = character_agility, intelligence = character_intelligence, luck = character_luck, temper = character_temper, image = image, first_skill = first_skill, second_skill = second_skill, third_skill = third_skill)

        with open(f'cards/index{number+1}.html', 'w', encoding="utf8") as file:
            file.write(rendered_page)


if __name__ == '__main__':
    main()