from peewee import *

# db = SqliteDatabase('people.db')
db = PostgresqlDatabase('postgres', user='postgres', password='com123',
                           host='localhost', port=5432)

class Person(Model):
    name = CharField()
    birthday = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([Person])
uncle_bob = Person(name='Bob', birthday="1960")
uncle_bob.save() # bob is now stored in the database

grandma = Person.select().where(Person.name == 'Bob').get()

print(grandma.name)