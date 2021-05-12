from myrequests import FirstTypeRequest
from class_init import Tourist, Hike_
from db_init import db

Tourist.query.filter_by(name='test_name').delete()
db.session.commit()