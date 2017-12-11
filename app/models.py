# -×- coding:utf-8 -*-

from datetime import datetime
import bleach
from flask import current_app
from . import db


class Genes(db.Model):
    __tablename__ = 'genes'
    id = db.Column(db.Integer, primary_key=True)
    testname = db.Column(db.String(64), unique=True, index=True)
    gan = db.Column(db.Float, default=None)
    wei = db.Column(db.Float, default=None)
    fei = db.Column(db.Float, default=None)
    shidao = db.Column(db.Float, default=None)
    biyan = db.Column(db.Float, default=None)
    jiazhuangxian = db.Column(db.Float, default=None)
    linba = db.Column(db.Float, default=None)
    dachang = db.Column(db.Float, default=None)
    pangguang = db.Column(db.Float, default=None)
    yixian = db.Column(db.Float, default=None)
    dannang = db.Column(db.Float, default=None)
    baixuebing = db.Column(db.Float, default=None)
    qianliexian = db.Column(db.Float, default=None)
    gaowan = db.Column(db.Float, default=None)
    ruxian = db.Column(db.Float, default=None)
    gongjin = db.Column(db.Float, default=None)
    luanchao = db.Column(db.Float, default=None)
    zigongneimo = db.Column(db.Float, default=None)
    
    genotypes = db.relationship('Genotypes', backref='gene')

class Genotypes(db.Model):
    __tablename__ = 'genotype'
    id = db.Column(db.Integer, primary_key=True)
    genotype = db.Column(db.String(64), index=True)
    gan = db.Column(db.Float, default=None)
    wei = db.Column(db.Float, default=None)
    fei = db.Column(db.Float, default=None)
    shidao = db.Column(db.Float, default=None)
    biyan = db.Column(db.Float, default=None)
    jiazhuangxian = db.Column(db.Float, default=None)
    linba = db.Column(db.Float, default=None)
    dachang = db.Column(db.Float, default=None)
    pangguang = db.Column(db.Float, default=None)
    yixian = db.Column(db.Float, default=None)
    dannang = db.Column(db.Float, default=None)
    baixuebing = db.Column(db.Float, default=None)
    qianliexian = db.Column(db.Float, default=None)
    gaowan = db.Column(db.Float, default=None)
    ruxian = db.Column(db.Float, default=None)
    gongjin = db.Column(db.Float, default=None)
    luanchao = db.Column(db.Float, default=None)
    zigongneimo = db.Column(db.Float, default=None)

    gene_id = db.Column(db.Integer, db.ForeignKey('genes.id'))
    
    
