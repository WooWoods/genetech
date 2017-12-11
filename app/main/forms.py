# -*- coding:utf-8 -*-
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import Required, Length


class OrderForm(FlaskForm):
    username = StringField('user name', validators=[Required()])
    gender = SelectField('Gender', choices=[('male', '男'), ('female', '女')])
    ID = StringField('identification NO.', validators=[Required()])
    report_type = StringField('report type, gene', validators=[Required()])
    genotype = StringField('genotype', validators=[Required()])
    test_time = DateField('Testing date', format='%Y-%m-%d')
    report_num = StringField('report number', validators=[Required()])
    report_danwei = StringField('report institution', validators=[Required()])
    inspect_danwei = StringField('inspection institution', validators=[Required()])
    report_time = DateField('Testing date', format='%Y-%m-%d', default=datetime.utcnow)
    submit = SubmitField('submit')

    
