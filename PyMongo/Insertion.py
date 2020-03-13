import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

information = mydb.EmployeeInfo

record = [{
        'fname': 'Prikshit',
        'lname': 'Gakhar'
        },{
        'fname': 'Mohit',
        'lname': 'Sharma'
        }]

information.insert(record)