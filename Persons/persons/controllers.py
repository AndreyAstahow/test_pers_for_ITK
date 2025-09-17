from fastapi import APIRouter

from database.models import PersonsModel
from database.schema import PersonsSchema
from typing import Optional
from .service import Service

client = APIRouter()

@client.get('/list/')
def list(age: Optional[int] = None):
    return Service.get_all(age)

@client.get('/get/')
def get_by_id(id: int):
    return Service.get_by_id(id)

@client.post('/create/')
def create(persons: PersonsSchema):
    return Service.create(persons)

@client.post('/update/')
def update(id: int, name: str, age: int):
    return Service.update(id, name, age)

@client.delete('/delete/')
def delete(id: int):
    return Service.delete(id)