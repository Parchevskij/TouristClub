from flask import render_template, url_for, request
import os
from myrequests import SixthTypeRequest, FirstTypeRequest, SecondTypeRequest, FifthTypeRequest, \
    ThirteenthTypeRequest, TwelfthTypeRequest, NinethTypeRequest
from db_init import db, app
from create_table import training_time, start_date, routes, \
    difficulties, hike_types, hours_per_route, instructor_names, distance_from_cur_point
from class_init import Tourist, Hike_
from mytools import split_kwargs


db.create_all()


@app.route('/')
@app.route('/tourist', methods=['GET', 'POST'])
def text():
    return render_template('main_page.html')


@app.route('/manager', methods=['GET', 'POST'])
def manager():
    request_ = SixthTypeRequest()
    rows = request_()[0]

    if request.method == 'POST':
        salary = request.form.get('salary')
        age = request.form.get('age')
        year_of_start = request.form.get('year')
        name = request.form.get('name')

        kwargs = {'salary': salary,
                  'age': age,
                  'year_of_start': year_of_start,
                  'manager_name': name}

        full_kwargs = {x: kwargs[x] for x in kwargs if kwargs[x] is not None and kwargs[x] != ' '}
        rows = request_(**full_kwargs)[0]
    return render_template('manager.html', rows=rows)


@app.route('/amateur', methods=['GET', 'POST'])
def amateur():
    request_ = FirstTypeRequest()
    rows, am_num = request_(group_='amateur')

    get_coach = SecondTypeRequest()
    coach_rows, coach_number = get_coach(group_='coach')

    get_hike = FifthTypeRequest()
    hike_rows, hike_num = get_hike(group_='amateur')

    if request.method == 'POST':
        section = request.form.get('section')
        sex = request.form.get('sex')
        best = request.form.get('best')

        kwargs = {'section': section,
                  'sex': sex,
                  'the_best': best}

        full_kwargs = {x: kwargs[x] for x in kwargs if kwargs[x] is not None and kwargs[x] != ' '}
        rows, am_num = request_(group_='amateur', **full_kwargs)
        # section with coaches

        coach_section = request.form.get('coach_section')
        coach_age = request.form.get('coach_age')
        # coach_salary = request.form.get('coach_salary')
        coach_sex = request.form.get('coach_sex')
        coach_time = request.form.get('coach_time')

        coach_kwargs = {'section': coach_section,
                        'age': coach_age,
                        # 'salary': coach_salary, # use it in coach mode
                        'sex': coach_sex,
                        'time': coach_time}

        coach_kwargs = {x: coach_kwargs[x] for x in coach_kwargs if coach_kwargs[x] is not None
                        and coach_kwargs[x] != ' '}

        coach_rows, coach_number = get_coach(group_='coach', **coach_kwargs)

        # section with hikes
        hike_type = request.form.get('hike_type')
        route = request.form.get('route')
        route_time = request.form.get('route_time')
        period = request.form.get('period')
        instructor_name = request.form.get('instructor_name')

        hike_kwargs = {'type_': hike_type,
                       'route': route,
                       'route_time': route_time,
                       'period': period,
                       'instructor_name': instructor_name}

        hike_kwargs = {x: hike_kwargs[x] for x in hike_kwargs if hike_kwargs[x] is not None
                        and hike_kwargs[x] != ' '}

        hike_rows, hike_number = get_hike(group_='amateur', **hike_kwargs)

    return render_template('amateur.html',
                           rows=rows,
                           am_num=am_num,
                           coach_rows=coach_rows,
                           coach_number=coach_number,
                           training_time=training_time,
                           hike_rows=hike_rows,
                           start_date=start_date)


@app.route('/sportsman', methods=['GET', 'POST'])
def sportsman():
    request_ = FirstTypeRequest()
    sp_rows, sp_num = request_(group_='sportsman')
    if request.method == 'POST':
        section = request.form.get('section')
        sex = request.form.get('sex')
        competitions = request.form.get('competition')

        kwargs = {'section': section,
                  'sex': sex,
                  'competition': competitions}

        full_kwargs = {x: kwargs[x] for x in kwargs if kwargs[x] is not None and kwargs[x] != ' '}
        sp_rows, sp_num = request_(group_='sportsman', **full_kwargs)

    return render_template('sportsman.html',
                           sp_rows=sp_rows,
                           sp_num=sp_num)


@app.route('/coach', methods=['GET', 'POST'])
def coach():
    second = SecondTypeRequest()
    rows, number = second()

    get_team = TwelfthTypeRequest()
    get_team = get_team()[0]
    if request.method == 'POST':
        section = request.form.get('section')
        salary = request.form.get('salary')
        time = request.form.get('time')

        kwargs = {'section': section,
                  'salary': salary,
                  'time': time}

        full_kwargs = {x: kwargs[x] for x in kwargs if kwargs[x] is not None and kwargs[x] != ' '}
        rows, number = second(**full_kwargs)

    return render_template('coach.html',
                           rows=rows,
                           number=number,
                           training_time=training_time,
                           get_team=get_team)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    difficulty = zip(routes, difficulties, hike_types)
    if request.method == 'POST':
        name = request.form.get('name')
        the_best = request.form.get('best')
        sex = request.form.get('sex')
        route = request.form.get('route')
        section = request.form.get('section')
        age = request.form.get('age')
        year = request.form.get('year')
        group = 'amateur'
        can_visit = True

        if int(year) <= 1:
            group = 'amateur'
        elif int(year) > 1:
            group = 'sportsman'

        route_indx = routes.index(route)
        route_difficulty = difficulties[route_indx]
        route_type = hike_types[route_indx]
        hpr = hours_per_route[route_indx]
        start = start_date[route_indx]
        instr_name = instructor_names[route_indx]
        distance = distance_from_cur_point[route_indx]

        kwargs = {'name': name,
                  'the_best': the_best,
                  'sex': sex,
                  'section': section,
                  'age': age,
                  'route': route,
                  'group_': group,
                  'type_': route_type,
                  'route_time': hpr,
                  'period': start,
                  'instructor_name': instr_name,
                  'length': distance,
                  'competition': None,
                  'can_visit': True,
                  'difficulty': route_difficulty}

        if route_difficulty <= int(the_best):
            if route_type == 'water':
                if section == 'swimming':
                    tourist_kwargs, hike_kwargs = split_kwargs(Tourist, Hike_, **kwargs)
                    Tourist.create_tourist(**tourist_kwargs)
                    Hike_.create_hike(**hike_kwargs)
            else:
                tourist_kwargs, hike_kwargs = split_kwargs(Tourist, Hike_, **kwargs)
                Tourist.create_tourist(**tourist_kwargs)
                Hike_.create_hike(**hike_kwargs)

    return render_template('registration.html',
                           routes=routes,
                           difficulty=difficulty)


if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 4444)),
            debug=True)