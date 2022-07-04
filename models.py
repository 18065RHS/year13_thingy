from main import db

class Found_Items(db.Model):
    __tablename__ = 'Found_Items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80))
    where_found = db.Column(db.String)
    description = db.Column(db.String())
    

class Lost_Items(db.Model):
    __tablename__ = 'Lost_Items'

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80))
    where_lost = db.Column(db.String)
    description = db.Column(db.String())
 
    #def __str__(self):
        #return self.name

