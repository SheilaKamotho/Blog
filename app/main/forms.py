from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,length,DataRequired
from flask_wtf.file import FileField,file_allowed

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')

class UploadBlog(FlaskForm):
    blog=TextAreaField('Write Blog:',validators=[DataRequired()])
    submit=SubmitField('Post Blog')

class CommentsForm(FlaskForm):
    comment=TextAreaField('Type comment:', validators=[DataRequired()])
    submit=SubmitField('Post Comment')