import yaml
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("C:\\Users\\hamed\\Desktop\\ab\\py2\\1\\config\\db.yaml") as f:  # Updated file path
    config = yaml.safe_load(f.read())

DATABASE_URL = f"postgresql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Person(Base):  # Updated class name to follow PEP8
    __tablename__ = 'person'
    name = Column(String, primary_key=True)
    family = Column(String)

Base.metadata.create_all(engine)

class QModel:

    def register(self, username, password):
        user = session.query(Person).filter(Person.name == username).first()
        if user:
            return False  # User already exists

        new_person = Person(name=username, family=password)
        session.add(new_person)
        session.commit()
        return True

    def update_user(self, old_username, new_username, new_password):
        user = session.query(Person).filter(Person.name == old_username).first()
        if user:
            user.name = new_username
            user.family = new_password
            session.commit()
            return True
        return False

    def delete_user(self, username):
        user = session.query(Person).filter(Person.name == username).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

    def check_password(self, username, password):
        user = session.query(Person).filter(Person.name == username).first()
        if user and user.family == password:
            return True
        return False

