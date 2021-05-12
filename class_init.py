from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from db_init import db


class Tourist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    the_best = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(25), nullable=True)
    group_ = db.Column(db.String(10), nullable=True)
    sex = db.Column(db.String(5), nullable=False)
    competition = db.Column(db.String(30), nullable=True)

    def __init__(self, name, age, the_best, section, group_, sex, competition):
        self.name = name
        self.age = age
        self.the_best = the_best
        self.section = section
        self.group_ = group_
        self.sex = sex
        self.competition = competition

    @classmethod
    def create_tourist(cls, **kwargs):
        person = cls(**kwargs)
        db.session.add(person)
        db.session.commit()


class Coach(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    n_groups = db.Column(db.Integer, nullable=True)
    time = db.Column(db.Integer, nullable=True)
    salary = db.Column(db.Integer, nullable=True)

    def __init__(self, coach_name, n_groups, time, salary):
        self.name = coach_name
        self.n_groups = n_groups
        self.time = time
        self.salary = salary

    @classmethod
    def create_coach(cls, **kwargs):
        coach = cls(**kwargs)
        db.session.add(coach)
        db.session.commit()


class Hike_(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    type_ = db.Column(db.String(10), nullable=True)
    can_visit = db.Column(db.Boolean, nullable=True)
    route = db.Column(db.String(25), nullable=True)
    route_time = db.Column(db.Integer, nullable=True)
    period = db.Column(db.Integer, nullable=True)
    instructor_name = db.Column(db.String(20), nullable=False)
    length = db.Column(db.Integer, nullable=True)
    difficulty = db.Column(db.Integer, nullable=False)  # from 1 to 10

    def __init__(self, type_, can_visit, route, route_time, period, instructor_name, length, difficulty):
        self.type_ = type_
        self.can_visit = can_visit
        self.route = route
        self.route_time = route_time
        self.period = period
        self.instructor_name = instructor_name
        self.length = length
        self.difficulty = difficulty

    @classmethod
    def create_hike(cls, **kwargs):
        hike = cls(**kwargs)
        db.session.add(hike)
        db.session.commit()


class Manager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manager_name = db.Column(db.String(25), nullable=True)
    salary = db.Column(db.Integer, nullable=True)
    year_of_birth = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    year_of_start = db.Column(db.Integer, nullable=True)

    def __init__(self, manager_name, salary, year_of_birth, age, year_of_start):
        self.manager_name = manager_name
        self.salary = salary
        self.year_of_birth = year_of_birth
        self.age = age
        self.year_of_start = year_of_start

    @classmethod
    def create_manager(cls, **kwargs):
        manager = cls(**kwargs)
        db.session.add(manager)
        db.session.commit()

'''class CoachLoading_(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Date, nullable=True)

    def __init__(self, time):
        self.time = time'''

