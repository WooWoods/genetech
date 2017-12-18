# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import Required, Length


class OrderForm(FlaskForm):
    username = StringField('user name', validators=[Required()])
    gender = SelectField('Gender', choices=[('男', '男'), ('女', '女')], validators=[Required()])
    ID = StringField('identification NO.', validators=[Required()])
    report_type = StringField('report type, gene', default='卫士基因检测-I',validators=[Required()])
    genotype = StringField('genotype', default='+/-',validators=[Required()])
    test_time = DateField('Testing date', format='%Y-%m-%d', default=datetime.utcnow() - timedelta(days=5))
    report_num = StringField('report number', validators=[Required()])
    report_danwei = StringField('report institution', default='中科院团队上海基因检测实验室',validators=[Required()])
    inspect_danwei = StringField('inspection institution', default='/',validators=[Required()])
    report_time = DateField('Testing date', format='%Y-%m-%d', default=datetime.utcnow)
    submit = SubmitField('Submit')

    
