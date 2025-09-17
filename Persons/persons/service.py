from fastapi_sqlalchemy import db

from typing import Optional

from database.models import PersonsModel
from database.schema import PersonsSchema

class Service():
    def get_all(age: Optional[int] = None):
        data = db.session.query(PersonsModel).all()
        if age is not None:
            data = db.session.query(PersonsModel).filter(PersonsModel.age == age).all()
            return data
        return data
    
    def get_by_id(id: int):
        data = db.session.query(PersonsModel).filter(PersonsModel.id == id).first()
        return data
    
    def create(person: PersonsSchema):
        db_pers = PersonsModel(name=person.name, age=person.age)
        db.session.add(db_pers)
        db.session.commit()
        return db_pers
    
    def update(id: int, name: str, age: int):
        data = db.session.query(PersonsModel).filter(PersonsModel.id == id).first()
        data.name = name
        data.age = age
        db.session.add(data)
        db.session.commit()
        db.session.refresh(data)
        return data
    
    def delete(id: int):
        data = db.session.query(PersonsModel).filter(PersonsModel.id == id).first()
        db.session.delete((data))
        db.session.commit()