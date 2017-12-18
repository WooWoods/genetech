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
    if form.validate_on_submit():
        testname = form.report_type.data
        geneinfo = Genes.query.filter_by(testname=testname).first()
        if not geneinfo:
            flash('你输入的检测项目不存在')
        genotype = form.genotype.data
        riskinfo = Genotypes.query.filter_by(gene_id=geneinfo.id, genotype=genotype).first()
        testdata = data_to_front(form, geneinfo, riskinfo)
        return render_template('report.html', testdata=testdata)
#    else:
#        print form.errors
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


    

