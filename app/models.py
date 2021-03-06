from . import db

class Character(db.Model):
    """Character data

    Model used to store all character related data:

    Attributes: 
        hanzi: Stores chinese character
        pinyin: Romanized word for chinese character
        english: English translation of chinese character
        book_volume: Associated book volume the character appears in
        character_set: Associated chapter from book

    """
    id = db.Column(db.Integer, primary_key=True)
    hanzi = db.Column(db.String(10), nullable=False)
    pinyin = db.Column(db.String(50), nullable=False)
    english = db.Column(db.String(50), nullable=False)
    book_volume = db.Column(db.Integer, nullable=False)
    character_set = db.Column(db.Integer, nullable=False)

    def __init__(self, hanzi, pinyin, english, book_volume, character_set):
        """ Character constructor """
        self.hanzi = hanzi
        self.pinyin = pinyin
        self.english = english
        self.book_volume = book_volume
        self.character_set = character_set

    def __repr__(self): 
        """Overriding string representaiton of Character object 

        Args:
            self: Character instance
        
        Return: 
            objFormat : String format representation of Character Object

        """
        objFormat = f'{self.hanzi} : {self.pinyin} : {self.english} : \
        {self.book_volume} : {self.character_set}'
        return objFormat 
