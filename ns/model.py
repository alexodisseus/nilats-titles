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
	quantity: int
	price: float
	person_id:str #para cintrolar os preço dos produtos que entram



engine = create_engine('sqlite:///db.db')

SQLModel.metadata.create_all(engine)



def add_title(id: int):
	with Session(engine) as session:
		order = Order(person_id=id)
		session.add(order)
		session.commit()
		session.refresh(order)
		return order



