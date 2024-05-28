from typing import Optional, List

from sqlmodel import SQLModel ,or_, Field, create_engine, Session, select, Relationship
from sqlalchemy.sql.expression import delete as sql_delete
from sqlalchemy import func


db = SQLModel()

def configure(app):
    app.db = db




class Person(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	name:str
	doc:str
	tipe_doc:str
	adress: str
	contact:str
	titles:List['Title']=Relationship()


class Title(SQLModel, table=True):
	
	id: Optional[int] = Field(default=None, primary_key=True)
	code: int 
	quantity: str
	price: float
	person_id: int = Field(foreign_key='person.id')



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

def get_titles_default():
	with Session(engine) as session:
		
		query = select(Title.id, 
			Title.code, 
			Title.price, 
			Person.name, 
			Title.quantity).join(Person , Person.id == Title.person_id)		
		data = session.exec(query).all()
		
		return data

def get_title_id(id:int):
	with Session(engine) as session:
		title = session.get(Title , id)
		
		return title

		





"""
person def
"""


def get_person_default():
	with Session(engine) as session:
		query = select(Person) #.join(Question_exam)		
		data = session.exec(query).all()
		
		return data



def add_person_default( name:str, doc_number:str, doc:str  , adress:str , contact:str):
	with Session(engine) as session:

		person = Person(name=name, tipe_doc=doc, doc=doc_number, adress=adress , contact=contact)
		session.add(person)
		session.commit()
		session.refresh(person)
		return person


def get_person_id(id:int):
	with Session(engine) as session:
		person = session.get(Person , id)
		
		return person , person.titles




"""
user def
"""

def get_login_default(email:str , password:str):
	with Session(engine) as session:
		query = select(User) #.join(Question_exam)		
		
		query = query.where(User.email == email , User.password == password )
		
		data = session.exec(query).first()
		
		return data



def get_login_id(user_id:str):
	with Session(engine) as session:
		user = session.get(User , id)
		
		return user