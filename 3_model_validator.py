from pydantic import BaseModel, EmailStr, model_validator
from typing import List,Dict,Optional, Annotated

class Patient(BaseModel):
    
    name: str
    email: EmailStr
    age: int 
    weight: float
    married: bool
    allergies: list[str]  
    contact_details: Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emrgency contact')
        return model
    
def insert_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('inserted')


def update_patient_data(patient: Patient):
    
    print(patient.name)
    print(patient.age)
    print('updated')

patient_info= {'name':'teja','email':'abc@gmail.com','age':80, 'weight':60, 'married':True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'123456','emergency':'3434535'}}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)