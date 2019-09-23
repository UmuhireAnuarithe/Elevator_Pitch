

from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField,SelectField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')


#Pitch Form
class PitchForm(FlaskForm):
    category_id = SelectField('Pick A Category', choices=[('1', 'Sales'), ('2', 'Product'), ('3', 'Secrets'), ('4', ('Confessions'), ('5', 'Reviews'))])
    comment = TextAreaField('Comments')
    submit = SubmitField('Submit Commennt')

# #Comment Form
# class CommentForm(FlaskForm):
#     comment = TextAreaField('Comment', validators=[Required()])
#     submit = SubmitField()
#     vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])


class CategoryForm(FlaskForm):
    name = StringField('cat_name', validators=[Required()])
    # title = TextAreaField('Pitch')
    submit = SubmitField()


# class PitchForm(FlaskForm):
#     title = StringField('Pitch Title', validators=[Required()])
#     author = StringField('Author', validators=[Required()])
#     pitch_content = TextAreaField('Write Pitch', validators=[Required()])  
#     category = RadioField('Pick Category', choices=[('Pickup Lines', 'Pickup Lines'), ('Interview Pitch', 'Interview Pitch'), ('Product Pitch', 'Product Pitch'), ('Promotion Pitch', 'Promotion Pitch')], validators=[Required()])  
#     submit = SubmitField('Submit')
