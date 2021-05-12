from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from class_init import Tourist, Hike_, Coach, Manager
from datetime import datetime
from mytools import get_age
from db_init import db

names = ['Chris', 'Matrin', 'Paolo', 'Ann', 'Sophi_Nikol', 'Jackson', 'Will', 'Pablo', 'Bodak', 'Yi', 'Yen', 'Xun',
         'Tyga', 'Victoria', 'Poul', 'Jastin', 'Drake', 'Nicki', 'Offset', 'Migos', 'Pablo', 'Maria', 'Nataly',
         'Xun', 'Victoria', 'DjSnake', 'Iggy', 'Cardi', 'Pitbull', 'Aiden', 'Selena', 'KidInk', 'DjKhaled', 'Akon']

years_in_sport = [1, 4, 6, 3, 10, 3, 2, 0, 0, 1, 9, 4, 3, 3, 4, 1, 2,
                  5, 7, 3, 2, 8, 3, 2, 0, 1, 0, 2, 1, 1, 1, 4, 3, 0]

ages = [23, 23, 30, 18, 22, 21, 20, 26, 19, 29, 25, 39, 20, 21, 20, 23, 18,
        30, 20, 19, 19, 20, 21, 20, 22, 27, 28, 25, 30, 20, 21, 20, 23, 23]

best_hike = [1, 3, 4, 2, 4, 3, 1, 1, 0, 2, 5, 4, 1, 2, 3, 4, 5,
             1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4, 5, 2, 1, 4, 1, 1]

sections = ['swimming', 'MMA', 'gym', 'athlete']
groups = ['amateur', 'sportsmen', 'coach']
sexes = ['M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'F', 'M', 'M', 'M', 'F', 'M', 'M', 'M',
         'F', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'M', 'M', 'M']

type_of_competitions = ['running', 'swimming', 'jumping', 'weightlifting']

# create coach part
coach_indx = [years_in_sport.index(x) for x in years_in_sport if x > 5]
coach_names = [names[i] for i in coach_indx]
num_groups = []  # fill it by max len(group)
salaries = [12500, 11500, 12000, 10000, 15000]
training_time = [datetime(2021, 5, 15, 9, 30),
                 datetime(2021, 5, 15, 12),
                 datetime(2021, 5, 15, 17, 30),
                 datetime(2021, 5, 15, 21, 30),
                 datetime(2021, 5, 15, 13)]

# create hike part
hike_types = ['on_foot', 'mountain', 'equestrian', 'water', 'mountain']
routes = ['Colosseum', 'Pompeii and Mount Vesuvius', 'Leaning Tower of Pisa', 'Lake Como', 'Cinque Terre']
hours_per_route = [10, 15, 10, 12, 13]
start_date = [datetime(2021, 6, 12),
              datetime(2021, 6, 13),
              datetime(2021, 7, 14),
              datetime(2021, 7, 15),
              datetime(2021, 8, 16)]
instructor_names = ['Paolo', 'Yen', 'Richard', 'Offset', 'Jonson']
distance_from_cur_point = [20, 240, 360, 660, 450]
difficulties = [1, 5, 3, 3, 4]

# create manager part
manager_salaries = [20000, 20500, 20700, 19500, 20000]
year_of_birth = [1975, 1976, 1980, 1990, 1976]
year_of_start = [2001, 2006, 2008, 2010, 2019]
manager_names = ['Ostin', 'Saint', 'Shoa', 'Chun', 'Daniel']


def create_tourist_table():
    db.create_all()
    for i in range(len(ages)):
        if years_in_sport[i] <= 1:
            group = 'amateur'
            competition_ = None
        elif years_in_sport[i] < 5:
            group = 'sportsman'
            competition_ = type_of_competitions[i % len(type_of_competitions)]
        else:
            group = 'coach'
            competition_ = type_of_competitions[i % len(type_of_competitions)]
        person = Tourist(name=names[i],
                         age=ages[i],
                         the_best=best_hike[i],
                         section=sections[i % len(sections)],
                         group_=group,
                         sex=sexes[i],
                         competition=competition_)
        db.session.add(person)
    try:
        return db.session.commit()
    except:
        return db.session.rollback()


def create_coach_table():
    db.create_all()
    for i in range(len(coach_names)):
        coach = Coach(coach_name=coach_names[i],
                      n_groups=1,
                      time=training_time[i],
                      salary=salaries[i])
        db.session.add(coach)
    try:
        return db.session.commit()
    except:
        return db.session.rollback()


def create_hike_table():
    db.create_all()
    for i in range(len(names)):
        person = Hike_(type_=hike_types[i % len(hike_types)],
                       can_visit=None,
                       route=routes[i % len(routes)],
                       route_time=hours_per_route[i % len(hours_per_route)],
                       period=start_date[i % len(start_date)],
                       instructor_name=instructor_names[i % len(instructor_names)],
                       length=distance_from_cur_point[i % len(distance_from_cur_point)],
                       difficulty=difficulties[i % len(difficulties)])
        db.session.add(person)
    try:
        return db.session.commit()
    except:
        return db.session.rollback()


def create_manager_table():
    db.create_all()
    for i in range(len(manager_names)):
        person = Manager(manager_name=manager_names[i],
                         salary=manager_salaries[i],
                         year_of_birth=year_of_birth[i],
                         age=get_age(year_of_birth[i]),
                         year_of_start=year_of_start[i])
        db.session.add(person)
    try:
        return db.session.commit()
    except:
        return db.session.rollback()


