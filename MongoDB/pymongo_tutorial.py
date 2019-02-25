# Database Connections
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("localhost:27017")  # Specify the URI
db = client["mongodb"]  				 # Connect to mongo database

print(client.database_names())
# [u'JobsWizz-dev', u'admin', u'config', u'local', u'mongodb']


# Adding data to our User Collection in mongodb
def create():
        # Method 1
    response = db.User.insert_one({
        "email": "pymongo email",
        "first_name": "py",
        "last_name": "mongo",
        "phone_number": "pymongo phone"
    })
    print('Insert One Response', response)
    # <pymongo.results.InsertOneResult object at 0x7ff5bdc7baf0>

    # Method 2
    response = db.User.insert([{
        "email": "1",
        "first_name": "py",
        "last_name": "mongo",
        "phone_number": "pymongo phone"
    }, {
        "email": "2",
        "first_name": "py",
        "last_name": "mongo",
        "phone_number": "pymongo phone"
    }])
    print('Insert Response', response)
    # [ObjectId('5c737f440499047d92c3606d'), ObjectId('5c737f440499047d92c3606e')]

    # Method 3
    response = db.User.insert({
        "email": "single insert",
        "first_name": "py",
        "last_name": "mongo",
        "phone_number": "pymongo phone"
    })
    print('Single Insert Response:', response)
    # ObjectId('5c737fce0499047ea0d5a033')


def read():
    # Read all documents/records from User collection
    response = db.User.find()
    print('find() response', response)
    # <pymongo.cursor.Cursor object at 0x7f3cf75a0c50>

    for data in response:
        print(data['first_name'])  # Gives me first name value of each doc

    # Read selected/filterd document from User collection
    response = db.User.find_one({'first_name': 'py'})
    print('find_one() response', response)  # Gives me first doc
    """
    {u'phone_number': u'pymongo phone', u'first_name': u'py',
     u'_id': ObjectId('5c737e660499047bfb601b1b'), u'email': u'pymongo email',
     u'last_name': u'mongo'}
    """


def update():
    # Update single doc
    response = db.User.update_one({'first_name': 'py'},
                                  {"$set": {
                                      "first_name": "Prasad",
                                      "last_name": "Dalavi"
                                  }})
    print('update_one() response:', response)
    # <pymongo.results.UpdateResult object at 0x7f0dc9c3c9b0>

    response = db.User.update({'first_name': 'py'},
                              {"$set": {
                                  "first_name": "Prasad",
                                  "last_name": "same"
                              }},
                              False, True,
                              )
    # upsert = True for creating the new doc if query doesnot match
    # multi = True for updating multiple docs that meets with the query
    print('update() response:', response)
    # {'updatedExisting': True, u'nModified': 1, u'ok': 1.0, u'n': 1}


def delete():
    # Delete single record/document
    response = db.User.delete_one({'first_name': 'py'})
    print('delete_one() response:', response)
    # <pymongo.results.DeleteResult object at 0x7f309e816b40>

    # Delete all Selected record/document
    # Method 1
    response = db.User.delete_many({'first_name': 'Prasad'})
    print('delete_many() response:', response)
    # <pymongo.results.DeleteResult object at 0x7face5a6cb90>

    # Method 2
    response = db.User.remove({'last_name': 'same'})
    print('remove() response:', response)
    # {u'ok': 1.0, u'n': 4}


create()
read()
update()
delete()
