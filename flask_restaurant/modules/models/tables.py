from modules.__init__ import db


class Waiter(db.Colunm):
    __tablename__ = "waiters"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    phone = db.Column(db.String)

    def __init__(self, username, password, name, phone):
        self.username = username
        self.password = password
        self.name = name
        self.phone = phone

    def __repr__(self):
        # return "<User %r" %self.username
        return "%r" % self.username

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Tables(db.Model):
    __tablename__ = "Tables"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    waiter_id = db.Column(db.Integer, db.ForeignKey('waiter.id'))
    is_occupied = db.Column(db.Boolean)

    user = db.relationship('Waiter', foreign_keys=waiter_id)

    def __init__(self, number, waiter_id, is_occupied=False):
        self.number = number
        self.waiter_id = waiter_id
        self.is_occupied = is_occupied

    def __repr__(self):
        return "Table: %r" % self.number


class Dish(db.Model):
    __tablename__ = "Menu"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    price = db.Column(db.String)
    image = db.Column(db.String)
    number_asked = db.Column(db.Integer)

    def __init__(self, name, price, image, number_asked=0):
        self.name = name
        self.price = price
        self.image = image
        self.number_asked = number_asked

    def __repr__(self):
        return "Dish: %r" % self.name

    def getPrice(self):
        return "Price: %r" % self.price
