# -*- coding:utf-8 -*-
import os
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, current_app, send_from_directory
#from flask_weasyprint import HTML, render_pdf
import pdfkit

from . import main
from .forms import OrderForm
from .. import db
from ..models import Genes, Genotypes


@main.route('/', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    if form.validate_on_submit():
        testname = form.report_type.data
        geneinfo = Genes.query.filter_by(testname=testname).first()
        if not geneinfo:
            flash('你输入的检测项目不存在')
        genotype = form.genotype.data
        riskinfo = Genotypes.query.filter_by(gene_id=geneinfo.id, genotype=genotype).first()
        testdata = data_to_front(form, geneinfo, riskinfo)
        html = render_template('pdf_template.html', testdata=testdata)
        #css = url_for('static', filename='css/pdfpage.css')
        #css = os.path.join(path, '../%s' % css)
        css = '/home/woods/project/genetech/app/static/css/pdfpage.css'
        options = {
            'page-size': 'A4',
            'margin-top': '0.60in',
            'margin-right': '0.25in',
            'margin-bottom': '0.20in',
            'margin-left': '0.25in',
            'encoding': 'UTF-8',
             }
        #output = os.path.join(current_app.root_path, 'downloads/report.pdf')
        output = 'app/downloads/report.pdf' 
        pdfkit.from_string(html, output, css=css, options=options)
        return render_template('report.html', testdata=testdata)
#    else:
#        print form.errors
    return render_template('infogather.html', form=form)

@main.route('/downloads/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    downloads = os.path.join(current_app.root_path, 'downloads')
    print downloads
    return send_from_directory(directory=downloads, filename=filename, as_attachment=True)
    
        
def data_to_front(form, geneinfo, riskinfo):
    data = {}
    data['username'] = form.username.data
    data['gender'] = form.gender.data
    data['ID'] = form.ID.data
    data['testname'] = form.report_type.data
    data['reportnum'] = form.report_num.data
    data['testdate'] = form.test_time.data
    data['reportdanwei'] = form.report_danwei.data
    data['inspect'] = form.inspect_danwei.data
    data['reportdate'] = form.report_time.data
    genotype = form.genotype.data
    data['genotype'] = genotype
    if genotype == '+/-':
        data['level'] = 'middle'
    if genotype == '-/-':
        data['level'] = 'low'
    if genotype == '+/+':
        data['level'] = 'high'

    data.setdefault('ref', {})['wei'] = geneinfo.wei
    data.setdefault('ref', {})['fei'] = geneinfo.fei
    data.setdefault('ref', {})['shidao'] = geneinfo.shidao
    data.setdefault('ref', {})['pangguang'] = geneinfo.pangguang
    data.setdefault('ref', {})['ruxian'] = geneinfo.ruxian
    data.setdefault('ref', {})['gongjin'] = geneinfo.gongjin
    data.setdefault('ref', {})['qianliexian'] = geneinfo.qianliexian

    data.setdefault('risk', {})['wei'] = riskinfo.wei
    data.setdefault('risk', {})['fei'] = riskinfo.fei
    data.setdefault('risk', {})['shidao'] = riskinfo.shidao
    data.setdefault('risk', {})['pangguang'] = riskinfo.pangguang
    data.setdefault('risk', {})['ruxian'] = riskinfo.ruxian
    data.setdefault('risk', {})['gongjin'] = riskinfo.gongjin
    data.setdefault('risk', {})['qianliexian'] = riskinfo.qianliexian
    return data


    

