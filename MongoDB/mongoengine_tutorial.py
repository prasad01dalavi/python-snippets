from mongoengine import *


connect('mongodb')  # Connect to Mongo Database


class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    phone_number = StringField(max_length=10)


# Adding data to our User Collection in mongodb
def create():
    user = User(email='prasad01dalavi@gmail.com', first_name='Data',
                last_name='Scientist')
    user.phone_number = "898305xxxx"
    #user.save()


def read():
    # Read all documents/records from User collection
    for user in User.objects:
        print('Record:', user.email, user.first_name, user.last_name, user.phone_number)

    # Read selected/filterd document from User collection
    for user in User.objects(email='prasad01dalavi@gmail.com'):
        print('Filtered Record:', user.email, user.first_name, user.last_name)

def update():
    # Single record update
    User.objects(last_name='Guy').update_one(last_name='Boy')

    # Multiple record update
    User.objects(email='prasad01dalavi@gmail.com').update(email='prasad02dalavi@gmail.com')

def delete():
    # Delete single record/document
    User.objects.first().delete()

    # Delete Selected record/document
    User.objects(phone_number='898305xxxx').delete()

create()
read()
update()
delete()
