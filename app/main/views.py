from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import OrderForm
from .. import db
from ..models import Genes


@main.route('/', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    if form.validate_on_submit():
        
    return render_template('infogather.html', form=form)
        
        
    

