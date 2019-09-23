
  
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship("Comment", backref="pitches", lazy = "dynamic")

    def __repr__(self):
      return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)



      
class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer,primary_key = True)
    cat_name = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'category',lazy="dynamic")


    def __repr__(self):
        return f'Category {self.name}'

    def save_category(self):
        db.session.add(self)
        db.session.commit()
       
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories


    
class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    Message = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
    
    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitch(cls,id):
        pitch = Pitch.query.filter_by(category_id=id).all()
        return pitch
    
   
    def __repr__(self):
        return f'Pitch {self.name}'



class Comment(db.Model):
    #User comments

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    feedback = db.column(db.String)
    time_posted = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    
    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment
