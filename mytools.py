from datetime import date


def get_age(year_of_birth):
    today = date.today()
    age = today.year - year_of_birth
    return age


def split_kwargs(cl_obj1, cl_obj2, **kwargs):
  atrr_cl_1 = [x for x in list(cl_obj1.__dict__.keys()) if not x[0].startswith('_')]
  atrr_cl_2 = [x for x in list(cl_obj2.__dict__.keys()) if not x[0].startswith('_')]
  cl1_kwargs = {x: kwargs[x] for x in kwargs if x in atrr_cl_1}
  cl2_kwargs = {x: kwargs[x] for x in kwargs if x in atrr_cl_2}
  return cl1_kwargs, cl2_kwargs


