import yaml
from peewee import *

with open("C:\\Users\\hamed\\Desktop\\ab\\py2\\1\\config\\db.yaml") as f:
    config = yaml.safe_load(f.read())

db = PostgresqlDatabase(
    database=config['database'],
    user=config['username'],
    password=config['password'],
    host=config['host'],
    port=config['port']
)

class BaseModel(Model):  
    class Meta:
        database = db

class Person(BaseModel):  
    name = CharField()
    family = CharField()

class QModel:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with db:
            db.create_tables([Person])  # Updated class name

    def register(self, username, password):
        with db:
            Person.create(name=username, family=password)  # Updated class name

    def update_user(self, old_username, new_username, new_password):
        with db:
            query = Person.update(name=new_username, family=new_password).where(Person.name == old_username)
            query.execute()

    def delete_user(self, username):
        with db:
            query = Person.delete().where(Person.name == username)
            query.execute()

    def user_exists(self, username):
        return Person.select().where(Person.name == username).exists()

    def check_password(self, username, password):
        user = Person.get_or_none(Person.name == username)
        if user and user.family == password:
            return True
        return False

