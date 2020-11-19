from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from models import User


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your Name"})
    phone = IntegerField('Phone', validators=[DataRequired()], render_kw={"placeholder": "Enter your Mobile number"})
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"placeholder": "Enter your message"})
    submit = SubmitField('Contact')


class PatientBedForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter Name"})
    age = IntegerField('Age', validators=[DataRequired()], render_kw={"placeholder": "Enter Age"})
    gender = SelectField('Gender', choices=[('choose gender', 'Choose Gender'),('male','Male'),('female','Female')])
    status = SelectField('Status', choices=[('choose patient status', 'Choose Patient Status'),('admitted', 'Admitted'),('discharged', 'Discharged')])
    phone = IntegerField('Phone', validators=[DataRequired()], render_kw={"placeholder": "Enter Mobile number"})
    address = StringField('Address', validators=[DataRequired()], render_kw={"placeholder": "Enter Address"})
    blood_group = SelectField('Blood Group', choices=[('choose blood group', 'Choose Blood Group'),('a +ve', 'A +ve'),('a -ve','A -ve'), ('b +ve', 'B +ve'), ('b -ve', 'B -ve'), ('ab +ve', 'AB +ve'), ('ab -vr', 'AB -vr'), ('o +ve', 'O +ve'), ('o -ve', 'O -ve')])
    bed_number = IntegerField('Bed Number', validators=[DataRequired()], render_kw={"placeholder": "Enter Bed Number"})
    bed_type = SelectField('Blood Group', choices=[('choose bed type','Choose Bed Type'),('ward', 'Ward'),('ward with oxygen', 'Ward with oxygen'),('icu', 'ICU'),('icu with oxygen', 'ICU with oxygen')])
    cost = IntegerField('Cost', validators=[DataRequired()], render_kw={"placeholder": "Enter Cost"})
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    name = StringField('User Name', validators=[DataRequired()], render_kw={"placeholder": "Enter Name"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter Password"})
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Re-Enter Password"})
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    name = StringField('User Name', validators=[DataRequired()], render_kw={"placeholder": "Enter User Name"})
    role = SelectField('Role', validators=[DataRequired()],choices=[('choose role', 'Choose Role'),('doctor', 'Doctor'),('nurse','Nurse'),('govt-officer','Govt. Officer')])
    gender = SelectField('Gender', choices=[('choose gender', 'Choose Gender'),('male','Male'),('female','Female'),('non-binary','Non-Binary')])
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Enter Password"})
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')], render_kw={"placeholder": "Re-Enter Password"})
    age = IntegerField('Age', validators=[DataRequired()], render_kw={"placeholder": "Enter Age"})
    phone = IntegerField('Phone', validators=[DataRequired()], render_kw={"placeholder": "Enter Mobile number"})
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder':'Email'})
    address = StringField('Address', validators=[DataRequired()], render_kw={"placeholder": "Enter Address"})
    submit = SubmitField('Register')

    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    def validate_phone(self, phone):
        if not 5000000000 < phone.data < 9999999999:
            raise ValidationError('Enter valid phone')







