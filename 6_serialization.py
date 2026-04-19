from pydantic import BaseModel

class Address(BaseModel):
    
    city:str
    state:str
    pin:str
       
    
class Patient(BaseModel):
    name:str
    gender:str
    age:int
    address: Address
    
address_dict={'city':'gurgoan','state':'haryana','pin':'122001'}

address1= Address(**address_dict)

patient_dict={'name':'teja','gender':'male','age':20,'address':address1}

patient1= Patient(**patient_dict)

print(patient1)

temp=patient1.model_dump()
print(temp)
print(type(temp))

temp2=patient1.model_dump_json()
print(temp2)

temp3=patient1.model_dump(include=['name','gender'])
print(temp3)

temp4=patient1.model_dump(exclude=['name'])
print(temp4)