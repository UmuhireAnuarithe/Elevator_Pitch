

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')



# class PitchForm(FlaskForm):

#     title = StringField('Pitch title',validators=[Required()])
#     Pitch = TextAreaField('Your pitch')
#     submit = SubmitField('Submit')


class CategoryForm(FlaskForm):
    name = StringField('Pitch', validators=[Required()])
    title = TextAreaField('Pitch')
    submit = SubmitField()


class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    pitch_content = TextAreaField('Write Pitch', validators=[Required()])  
    category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[Required()])  
    submit = SubmitField('Submit')
