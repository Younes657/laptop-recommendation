
from sqlalchemy import and_ , or_
from expert_system import db
from expert_system.models import laptop
from expert_system import app
def laptops_filtration(result):
    laptops = []
    with app.app_context():
        match result :
            case "Laptop(High)":
                laptops1db = laptop.query.filter(and_(laptop.processor_type == "i7" , laptop.generation_int >= 11000 , laptop.storage_capacity >= 256 , laptop.ram >= 8 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops1 = []
                for laptopdb in laptops1db:
                    laptops1.append(laptopdb.to_dict())
                laptops2db = laptop.query.filter(and_(laptop.processor_type == "i9" , laptop.generation_int >= 9000 , laptop.storage_capacity >= 256 , laptop.ram >= 8 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops2 = []
                for laptopdb in laptops2db:
                    laptops2.append(laptopdb.to_dict())
                laptops3db = laptop.query.filter(and_(laptop.processor_type == "i5" , laptop.generation_int >= 13000 , laptop.storage_capacity >= 256 , laptop.ram >= 8 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops3 = []
                for laptopdb in laptops3db:
                    laptops3.append(laptopdb.to_dict())
                laptops = laptops1 + laptops2 + laptops3

            case "Laptop(AlmostHigh)":
                laptops1db = laptop.query.filter(and_(laptop.processor_type == "i5" , laptop.generation_int >= 11000 , laptop.storage_capacity >= 256 , laptop.ram >= 8 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops1 = []
                for laptopdb in laptops1db:
                    laptops1.append(laptopdb.to_dict())
                laptops2db = laptop.query.filter(and_(laptop.processor_type == "i7" , laptop.generation_int <= 10900  , laptop.storage_capacity >= 256 , laptop.ram >= 8 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops2 = []
                for laptopdb in laptops2db:
                    laptops2.append(laptopdb.to_dict())
                
                laptops = laptops1 + laptops2
                
            case "Laptop(Medium)":
                laptops1db = laptop.query.filter(and_(laptop.processor_type == "i5" , laptop.generation_int.between(10900 , 7000) , laptop.storage_capacity >= 256 , laptop.ram >= 8 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops1 = []
                for laptopdb in laptops1db:
                    laptops1.append(laptopdb.to_dict())
                laptops2db = laptop.query.filter(and_(laptop.processor_type == "i3" , laptop.generation_int >= 11000 , laptop.storage_capacity >= 256 , laptop.ram >= 4 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"]) )).all()
                laptops2 = []
                for laptopdb in laptops2db:
                    laptops2.append(laptopdb.to_dict())
                laptops = laptops1 + laptops2
               
            case "Laptop(AlmostLow)":
                laptops1db = laptop.query.filter(and_(laptop.processor_type == "i5" , laptop.generation_int <= 6900 , laptop.storage_capacity >= 128 , laptop.ram >= 4 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops1 = []
                for laptopdb in laptops1db:
                    laptops1.append(laptopdb.to_dict())
                laptops2db = laptop.query.filter(and_(laptop.processor_type == "i3" , laptop.generation_int <= 10900  , laptop.storage_capacity >= 256 , laptop.ram >= 4 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                laptops2 = []
                for laptopdb in laptops2db:
                    laptops2.append(laptopdb.to_dict())
                laptops = laptops1 + laptops2
                
            case "Laptop(Low)":
                laptopsdb = laptop.query.filter(and_(laptop.processor_type == "i3" , laptop.generation_int <= 6900 , laptop.storage_capacity >= 128 , laptop.ram >= 4 , laptop.battery_life.in_(["3H","4H","5H","6H","7H"])  )).all()
                for laptopdb in laptopsdb:
                    laptops.append(laptopdb.to_dict())
               
    
    return laptops
