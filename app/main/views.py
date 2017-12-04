from datetime import datetime
from flask import render_template, session, redirect, url_for

from . import main
from .forms import ClientForm
from .. import db
from ..models import Genedb


@main.route('/', methods=['GET', 'POST'])
def index():
    form = ClientForm()
    

