# # -*- coding: utf-8 -*-
import random

from django.contrib.auth.models import User

from jobs.models import Category, Job
from clients.models import Profile


def create_test_categories():
    titles = [('vent', 'вентиляция'), ('krov', 'кровля'),
     ('sant', 'сантехника'), ('otdel', 'отделочные работы'), ('stroi', 'строительные работы'),
     ('elect', 'электрика'), ('kanal', 'канализация')]
    cats = list()

    for title in titles:
        cats.append(Category(name=title[0], ru_name=title[1], description=f'description of {title}'))

    Category.objects.bulk_create(cats)


def create_test_zakazchiki():
    names = ['Елена', 'Дугара', 'Стелла', 'АМТА', 'ИГОРЬ',
     'дядя Слава', 'Петя', 'Александр самогон', 'Ольга Буузы',
     'мясопродукты Закамны']
    shops = list()

    for name in names:
        profile = Profile.objects.get_or_create_profile_viber(viber_id=str(random.randint(10, 500)),
            viber_name=name)
        profile.mark_as_zakazchik()


def create_test_jobs(images=False):
    create_test_categories()
    create_test_zakazchiki()
    User.objects.create_superuser(username='kaizerj',email='kzrster@gmail.com', password='jikozfree')
    
    titles = ['Ремонтные работы', 'Требуются сварщики', "Требуются каменщики", "Кровельные работы",
     "Ремонт квартиры", " Установить кондиционер", "Построить свинокомплекс", "Поклеить обои",
     "Вырыть канаву", "Укладка ковролина", "Бетонные работы", "Очистить каналюгу", "Кирпичная кладка",
     "Вырубить лес", "Построить дом", "Построить гараж", "Построить баню", "Демонтаж здания",
     "Построить пандус", ]

    categories = Category.objects.all().values_list('id', flat=True)

    for zakazchik in Profile.objects.filter(zakazchik=True):
        for i in range(0, random.randint(1, 7)):
            cat = Category.objects.get(pk=random.choice(categories))
            title = random.choice(titles)
            job = Job.objects.create_job(title=title, category=cat,
             budget=round(random.randint(1000, 50000), -3), zakazchik=zakazchik, address='Улан-Удэ',
             description=f'Описание {title}', )
            
            if images:
                pass
                # add images
