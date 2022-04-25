import datetime

from pymongo import MongoClient


def ex1():
    print(1.1)
    cursor = db.restaurants.find({"cuisine": "Indian"})
    count = 0
    for i in cursor:
        count += 1
        print(i["name"], "--", i["cuisine"])
    print(count, " - Number of restaurants with Indian cuisine")
    print(1.2)
    cursor = db.restaurants.find({"cuisine": {'$in': ["Indian", "Thai"]}})
    count = 0
    for i in cursor:
        count += 1
        print(i["name"], "--", i["cuisine"])
    print(count, " - Number of restaurants with Indian or Thai cuisine")
    print(1.3)
    cursor = db.restaurants.find({"address.street": "Rogers Avenue", "address.building": "1115", "address.zipcode": "11226"})
    for i in cursor:
        print(i["name"], "--", i["address"])


def ex2():
    i_coord = [-73.9557413, 40.7720266]
    i_address = {"building": "1480", "coord": i_coord, "street": "2 Avenue", "zipcode": "10075"}
    i_grades = [{"date": datetime.datetime(year=2014, month=10, day=1), "grade": "A", "score": "11"}]
    i_new_rest = {"restaurant_id": "41704620", "name": "Vella", "cuisine": "Italian", "borough": "Manhattan",
                  "grades": i_grades, "address": i_address}
    result = db.restaurants.insert_one(i_new_rest)
    cursor = db.restaurants.find({"restaurant_id": "41704620"})
    for i in cursor:
        print(i["name"], "--", i["cuisine"], i["address"], i["grades"])


def ex3():
    cursor = db.restaurants.find({"borough": "Manhattan"})
    c = 0
    for i in cursor:
        c += 1
    print(c, " - Manhattan rest. before deletion")

    cursor = db.restaurants.find({"cuisine": "Thai"})
    c = 0
    for i in cursor:
        c += 1
    print(c, " - Thai rest. before deletion")

    result = db.restaurants.delete_one({"borough": "Manhattan"})
    result = db.restaurants.delete_many({"cuisine": "Thai"})

    cursor = db.restaurants.find({"borough": "Manhattan"})
    c = 0
    for i in cursor:
        c += 1
    print(c, " - Manhattan rest. after deletion")

    cursor = db.restaurants.find({"cuisine": "Thai"})
    c = 0
    for i in cursor:
        c += 1
    print(c, " - Thai rest. after deletion")


def ex4():
    cursor = db.restaurants.find({"address.street": "Rogers Avenue"})
    c = 0
    for i in cursor:
        c += 1
    print(c, "- Number of restaurants initially")
    cursor = db.restaurants.find({"address.street": "Rogers Avenue"})
    bad_rest = []
    for i in cursor:
        # print(i['grades'])
        bad = 0
        count = 0
        for j in i['grades']:
            if j['grade'] == "C":
                bad = 1
                count += 1
        print(i['name'], " - Num of C grades ", count)
        if bad == 1 and count > 1:
            bad_rest.append(i['_id'])

    print(len(bad_rest), " - number of bad restaurants that would be deleted")
    cursor = db.restaurants.find({"address.street": "Rogers Avenue"})
    for i in cursor:
        if i['_id'] in bad_rest:
            print(i['name'], " - was deleted")
            db.restaurants.delete_one({"_id": i['_id']})
        else:
            print(i['name'], " - received one more C grade")
            db.restaurants.update_one(i, {'$set': {'grades': i['grades'] + [{'grade': 'C', 'score': 0, 'date': datetime.datetime.now()}]}})


client = MongoClient("mongodb://localhost")
db = client['testrestaurants']
# ex1()
# ex2()
# ex3()
# ex4()