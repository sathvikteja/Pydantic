from pydantic import BaseModel, EmailStr, computed_field
from typing import List,Dict

class Patient(BaseModel):
    
    name: str
    age: int 
    weight: float
    height: float
    married: bool
    allergies: list[str]
    contact_details: Dict[str,str]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round( self.weight / (self.height**2),2)
        return bmi

def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('inserted')


def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.bmi)
    print('updated')

patient_info= {'name':'teja','email':'abc@gmail.com','age':20, 'weight':60, 'height':1.73 ,'married':True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'123456'}}

patient1 = Patient(**patient_info)

update_patient_data(patient1)