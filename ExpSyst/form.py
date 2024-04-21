from flask_wtf import FlaskForm
from wtforms import SelectField ,SubmitField#, StringField, PasswordField
from wtforms.validators import DataRequired #,Length, EqualTo, Email, ValidationError



class SlectForm(FlaskForm):
    selectProcessor = SelectField("choose you processor performance" , choices= [("High", "High") , ("Medium" ,"Medium"), ("Low" , "Low")] , validators=[DataRequired()])
    selectRam = SelectField("choose you Ram performance" , choices= [("High", "High") , ("Medium" ,"Medium"), ("Low" , "Low")] , validators=[DataRequired()])
    selectStorage = SelectField("choose you storeage performance" , choices= [("Large", "Large") , ("Medium" ,"Medium"), ("Small" , "Small")] , validators=[DataRequired()])
    selectBattryLife = SelectField("choose you Battry Life" , choices= [("Long", "Long") , ("Medium" ,"Medium"), ("Short" , "Short")] , validators=[DataRequired()])
    selectBudget = SelectField("choose you processor performance" , choices= [("Luxury", "Luxury") , ("Moderate" ,"Moderate"), ("Economic" , "Economic")] , validators=[DataRequired()])
    submit = SubmitField(label='Submit')






# pip install email_validator









