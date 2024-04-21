from ExpSyst import db

class Cart:
    def __init__(self, Processor, Ram , Storage , BattryLife , Budget):
        self.Processor = Processor
        self.Ram = Ram
        self.Storage = Storage
        self.BattryLife = BattryLife
        self.Budget = Budget

class laptop(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    brand = db.Column(db.String(length=100), nullable=False, unique=False)
    model = db.Column(db.String(length=100), nullable=False)
    processor_type = db.Column(db.String(length=100), nullable=False)
    generation = db.Column(db.String(length=100), nullable=True)
    ram_size= db.Column(db.String(length=100), nullable=False)
    storage_type = db.Column(db.String(length=100), nullable=True)
    storage_capacity = db.Column(db.String(length=100), nullable=True)
    display_size = db.Column(db.String(length=100), nullable=True)
    graphics_card = db.Column(db.String(length=100), nullable=True)
    battery_life = db.Column(db.String(length=100), nullable=True)
    price = db.Column(db.Numeric(20, 2), nullable=False)
    image_link = db.Column(db.String(length=255), nullable=True)
    def __repr__(self):
        return f'Item {self.brand}'
    def to_dict(self):
        return {
            'id' : self.id,
            'brand' : self.brand,
            'model' : self.model,
            'processor_type' : self.processor_type,
            'generation' : self.generation,
            'ram_size': self.ram_size,
            'storage_type' : self.storage_type,
            'storage_capacity' : self.storage_capacity,
            'display_size' : self.display_size,
            'graphics_card' : self.graphics_card,
            'battery_life' : self.battery_life,
            'price' :self.price,
            'image_link' :self.image_link
        }

# CREATE TABLE Laptop (
#     ID SERIAL PRIMARY KEY,
#     Brand VARCHAR(100),
#     Model VARCHAR(100),
#     Processor_Type VARCHAR(100),
#     Generation VARCHAR(100),
#     RAM_Size VARCHAR(100),
#     Storage_Type VARCHAR(100),
#     Storage_Capacity VARCHAR(100),
#     Display_Size VARCHAR(100),
#     Graphics_Card VARCHAR(100),
#     Battery_Life VARCHAR(100),
#     Price DECIMAL(20, 2)
# );
