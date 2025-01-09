from database import Base
import sqlalchemy.orm as orm
from sqlalchemy import Integer, String, DateTime
import datetime

class Client(Base):
  __tablename__ = 'clients'
  id = orm.mapped_column(Integer, primary_key=True, autoincrement=True)
  name = orm.mapped_column(String)
  email = orm.mapped_column(String)
  sended_emails = orm.mapped_column(Integer, default=0)





