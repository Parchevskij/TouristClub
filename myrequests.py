from create_table import create_manager_table, create_tourist_table, create_hike_table, create_coach_table
from class_init import Tourist, Hike_, Coach, Manager
from mytools import split_kwargs
from db_init import db


class FirstTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Tourist.id == 1)):
            print('Table Tourist is already exists')
        else:
            create_tourist_table()
        self.tourist = Tourist

    def __call__(self, **kwargs):
        request = self.tourist.query.filter_by(**kwargs)
        number = request.count()
        return request.all(), number


class SecondTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Coach.id == 1)):
            print('Table Coach is already exists')
        else:
            create_coach_table()

    def __call__(self, **kwargs):
        coach_kwargs, tourist_kwargs = split_kwargs(Coach, Tourist, **kwargs)
        request = (db.session.
               query(Tourist, Coach).
               filter_by(**tourist_kwargs).
               join(Coach, Tourist.name == Coach.name).
               filter_by(**coach_kwargs))
        number = request.count()
        return request.all(), number


class FifthTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)):
            print('Table Hike is already exists')
        else:
            create_hike_table()

    def __call__(self, **kwargs):
        hike_kwargs, tourist_kwargs = split_kwargs(Hike_, Tourist, **kwargs)
        request = (db.session.
               query(Tourist, Hike_).
               filter_by(**tourist_kwargs).
               join(Hike_, Tourist.id == Hike_.id).
               filter_by(**hike_kwargs))
        number = request.count()
        return request.all(), number


class SixthTypeRequest:
    def __init__(self):
        Manager.query.delete()
        create_manager_table()
        self.manager = Manager

    def __call__(self, **kwargs):
        request = self.manager.query.filter_by(**kwargs)
        number = request.count()
        return request.all(), number


class EighthTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)) and db.session.query(db.exists().where(Tourist.id == 1)):
            print('Tables Hike and Tourist already exists')
        else:
            create_hike_table()
            create_tourist_table()

    def __call__(self, *args, **kwargs):
        hike_kwars, tourist_kwargs = split_kwargs(Hike_, Tourist, **kwargs)
        if len(args) == 1:
            request = (db.session.
                       query(Hike_, Tourist).
                       filter(Hike_.period >= args[0]).
                       filter_by(**hike_kwars).
                       join(Tourist, Hike_.id == Tourist.id).
                       filter_by(**tourist_kwargs))
        elif len(args) == 1:
            request = (db.session.
                       query(Hike_, Tourist).
                       filter(Hike_.period >= args[0], Hike_.period <= args[1]).
                       filter_by(**hike_kwars).
                       join(Tourist, Hike_.id == Tourist.id).
                       filter_by(**tourist_kwargs))
        else:
            request = (db.session.
                       query(Hike_, Tourist).
                       filter_by(**hike_kwars).
                       join(Tourist, Hike_.id == Tourist.id).
                       filter_by(**tourist_kwargs))
        number = request.count()
        return request.all(), number


class NinethTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)):
            print('Table Hike is already exists')
        else:
            create_hike_table()

    def __call__(self, *args, **kwargs):
        if len(args) == 1:
            request = Hike_.query.filter(Hike_.length > args[0]).filter_by(**kwargs)
            number = request.count()
        else:
            request = Hike_.query.filter_by(**kwargs)
            number = request.count()
        return request.all(), number


class TenthTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)) and db.session.query(db.exists().where(Tourist.id == 1)):
            print('Tables Hike and Tourist already exists')
        else:
            create_hike_table()
            create_tourist_table()

    def __call__(self, *args, **kwargs):
        hike_kwargs, tourist_kwargs = split_kwargs(Hike_, Tourist, **kwargs)
        rows = db.session.query(Tourist, Hike_).join(Hike_, Tourist.id == Hike_.id).all()
        if 'can_visit' in kwargs.keys():
            for x, y in rows:
                if x.group_ == 'coach':
                    if int(x.the_best) < y.difficulty:
                        y.can_visit = False
                        db.session.commit()
                    else:
                        y.can_visit = True
                        db.session.commit()
                else:
                    if int(x.the_best) < y.difficulty and not (x.section == 'swimming' and y.type_ == 'water'):
                        y.can_visit = False
                        db.session.commit()
                    else:
                        y.can_visit = True
                        db.session.commit()
        request = (db.session.
                   query(Hike_, Tourist).
                   filter_by(**hike_kwargs).
                   join(Tourist, Hike_.id == Tourist.id).
                   filter_by(**tourist_kwargs))
        number = request.count()
        return request.all(), number


class EleventhTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)) and db.session.query(db.exists().where(Tourist.id == 1)):
            print('Tables Hike and Tourist already exists')
        else:
            create_hike_table()
            create_tourist_table()

    def __call__(self, **kwargs):
        hike_kwargs, tourist_kwargs = split_kwargs(Hike_, Tourist, **kwargs)
        request = db.session.query(Tourist, Hike_).filter_by(**tourist_kwargs).join(Hike_,
                                                                                    Tourist.id == Hike_.id).filter_by(**hike_kwargs)
        number = request.count()
        return request.all(), number


class TwelfthTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)) and db.session.query(db.exists().where(Tourist.id == 1)):
            print('Tables Hike and Tourist already exists')
        else:
            create_hike_table()
            create_tourist_table()

    def __call__(self, **kwargs):
        request = db.session.query(Tourist, Hike_).filter_by(group_='coach', name=Hike_.instructor_name).join(Hike_,
                                                                                                            Tourist.id == Hike_.id).filter_by(**kwargs)
        number = request.count()
        if number != 0:
            request = db.session.query(Tourist, Hike_).filter_by(section=request.all()[0][0].section).join(Hike_,
                                                                                                         Tourist.id == Hike_.id).filter_by(**kwargs)
            number = request.count()
        return request.all(), number


class ThirteenthTypeRequest:
    def __init__(self):
        if db.session.query(db.exists().where(Hike_.id == 1)) and db.session.query(db.exists().where(Tourist.id == 1)):
            print('Tables Hike and Tourist already exists')
        else:
            create_hike_table()
            create_tourist_table()

    def __call__(self, **kwargs):
        hike_kwargs, tourist_kwargs = split_kwargs(Hike_, Tourist, **kwargs)
        request = (db.session.
                   query(Hike_, Tourist).
                   filter_by(**hike_kwargs).
                   join(Tourist, Hike_.id == Tourist.id).
                   filter_by(**tourist_kwargs))
        number = request.count()
        return request.all(), number
