import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

empinfo = mydb.empinfo

records=[
        {
        'firstname':'Siddhant',
        'lastname':'Pathak',
        'department':'Analytics',
        'qualification':'BE',
        'age':23
        
        },
        {
        'firstname':'Sarthak',
        'lastname':'Mittal',
        'department':'Analytics',
        'qualification':'statistics',
        'age':44
        
        },
        {
        'firstname':'Pulkit',
        'lastname':'Ahuja',
        'department':'Analytics',
        'qualification':'masters',
        'age':69
        
        },
        {
        'firstname':'Harshit',
        'lastname':'Jain',
        'department':'Analytics',
        'qualification':'masters',
        'age':15
        
        },
        {
        'firstname':'Shiv',
        'lastname':'Kumar',
        'department':'Analytics',
        'qualification':'phd',
        'age':76
        
        },
        {
        'firstname':'Sagar',
        'lastname':'Aggarwal',
        'department':'Analytics',
        'qualification':'masters',
        'age':34
        
        }]

empinfo.insert_many(records)

empinfo.find_one()

for record in empinfo.find():
    print(record.keys())
    
for record in empinfo.find({'firstname': 'Siddhant'}):
    print(record)
    
for record in empinfo.find({'qualification': {'$in': ['phd', 'master']}}):
    print(record)

for record in empinfo.find({'qualification': 'master', 'age': {'$lt': 35}}):
    print(record)

for record in empinfo.find({'$or': [{'firstname': 'Siddhant'}, {'qualification': 'masters'}]}):
    print(record['firstname'], record['qualification'])


inventory = mydb.inventory

inventory.insert_many( [
   { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
   { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
   { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
   { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
   { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" }
]);

for records in inventory.find({'size': { 'h': 14, 'w': 21,'uom': "cm" }}):
    print(records)
