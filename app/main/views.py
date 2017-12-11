# -*- coding:utf-8 -*-
from datetime import datetime
from flask import render_template, session, redirect, url_for, flash

from . import main
from .forms import OrderForm
from .. import db
from ..models import Genes, Genotypes


@main.route('/', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    print('come here')
    if form.validate_on_submit():
        testname = form.report_type.data
        geneinfo = Genes.query.filter_by(testname=testname).first()
        print('i am here')
        if not geneinfo:
            flash('你输入的检测项目不存在')
        genotype = form.genotype.data
        riskinfo = Genotypes.query.filter_by(gene_id=geneinfo.id, genotype=genotype).first()
        testdata = data_to_front(form, geneinfo, riskinfo)
        return render_template('report.html', testdata=testdata)
    return render_template('infogather.html', form=form)
        
        
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
    data['reportdate'] = form.reportdate.data
    genotype = form.genotype.data
    data['genotype'] = genotype
    if genotype == '+/-':
        data['level'] = 'middle'
    if genotype == '-/-':
        data['level'] = 'low'
    if genotype == '+/+':
        data['level'] = 'high'

    data['ref']['wei'] = geneinfo.wei
    data['ref']['fei'] = geneinfo.fei
    data['ref']['shidao'] = geneinfo.shidao
    data['ref']['pangguang'] = geneinfo.pangguang
    data['ref']['ruxian'] = geneinfo.ruxian
    data['ref']['gongjin'] = geneinfo.gongjin
    data['ref']['qianliexian'] = geneinfo.qianliexian

    data['risk']['wei'] = riskinfo.wei
    data['risk']['fei'] = riskinfo.fei
    data['risk']['shidao'] = riskinfo.shidao
    data['risk']['pangguang'] = riskinfo.pangguang
    data['risk']['ruxian'] = riskinfo.ruxian
    data['risk']['gongjin'] = riskinfo.gongjin
    data['risk']['qianliexian'] = riskinfo.qianliexian


    

