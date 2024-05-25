from typing import Optional, List

from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy.sql.expression import delete as sql_delete
from sqlalchemy import func


db = SQLModel()

def configure(app):
    app.db = db



class Title(SQLModel, table=True):
	
	id: Optional[int] = Field(default=None, primary_key=True)
	code: int 
	quantity: str
	price: float
	person_id: int

class Person(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	doc:str
	tipe_doc:str
	adress: str
	contact:str

class User(SQLModel, table=True):

	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	position:str #usuario, admin, gerente;
	email:str
	password:str







engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)



def add_title(id: int):
	with Session(engine) as session:
		order = Order(person_id=id)
		session.add(order)
		session.commit()
		session.refresh(order)
		return order


def add_title_default( code:str, quantity:str,price:str,person_id:int):
	with Session(engine) as session:

		title = Title(code=code,quantity=quantity,price=price,person_id=person_id)
		session.add(title)
		session.commit()
		session.refresh(title)
		return title

