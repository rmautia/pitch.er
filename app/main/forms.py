from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    text = TextAreaField('Text')
    category = SelectField('Type',choices=[('survey','Survey pitch'),('idea','Idea pitch'),('promotion','Promotion pitch')],validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:',validators=[Required()])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):

 title = StringField('Pitch title',validators=[Required()])

 text = TextAreaField('Text')

 category = SelectField ('Type',choices=[('survey','Survey pitch'),('idea','Idea pitch'),('promotion','Promotion pitch')],validators=[Required()])

 submit = SubmitField('Submit') 