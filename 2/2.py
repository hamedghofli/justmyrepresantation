from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session

import yaml
with open("C:\\Users\\hamed\\Desktop\\ab\\py2\\1\\config\\db.yaml") as f:  # Updated file path
    config = yaml.safe_load(f.read())


class Base():
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str] = mapped_column(String(30))

DATABASE_URL = f"postgresql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)


s=Session(engine)
s.add (User(name="ttttttteeeeeeeeeest", fullname="Patrick Star"))
s.commit()