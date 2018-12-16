from flask import Flask, render_template, request
from flask_wtf import Form 
from wtforms import StringField, TextField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import InputRequired

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
