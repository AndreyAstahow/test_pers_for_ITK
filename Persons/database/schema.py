from pydantic import BaseModel

class PersonsSchema(BaseModel):
    name: str
    age: int

    class Config:
        orm_mode = True