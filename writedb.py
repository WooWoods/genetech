# -*- coding:utf-8 -*-
import re

from collections import defaultdict
#from ..models import Genes, Genotypes
#from .. import db

def read_genes():
    dic = defaultdict(dict)
    for line in file('risk.txt'):
        if re.search(r'^\s$', line):
            continue
        arr = line.strip().split()
        dic[arr[0]][arr[1]] = arr[2]
    return dic

def read_genotype():
    dic = defaultdict(lambda: defaultdict(dict))
    for line in file('genotyperisk.txt'):
        if re.search(r'^\s$', line):
            continue
        arr = line.strip().split()
        dic[arr[0]][arr[1]][arr[2]] = arr[3]
    return dic

#dic_gene = read_genes()
#dic_genotype = read_genotype()

def write_gene(dic_gene, Genes, db):
    for gene in dic_gene:
        inner = dic_gene[gene]
        record = Genes(testname=gene,
                      wei=inner.get('wei', None),
                      fei=inner.get('fei', None),
                      shidao=inner.get('shidao', None),
                      pangguang=inner.get('pangguang', None),
                      qianliexian=inner.get('qianliexian', None),
                      ruxian=inner.get('ruxian', None),
                      gongjin=inner.get('gongjin', None),
                      )
        db.session.add(record)
    db.session.commit()

def write_genotype(dic_genotype, Genes, Genotypes, db):
    for gene in dic_genotype:
        gene_rec = Genes.query.filter_by(testname=gene).first()
        for gt in dic_genotype[gene]:
            inner=dic_genotype[gene][gt]
            record = Genotypes(genotype=gt, 
                              wei=inner.get('wei', None),
                              fei=inner.get('fei', None),
                              shidao=inner.get('shidao', None),
                              pangguang=inner.get('pangguang', None),
                              qianliexian=inner.get('qianliexian', None),
                              ruxian=inner.get('ruxian', None),
                              gongjin=inner.get('gongjin', None),
                              gene=gene_rec,
                              )
	    db.session.add(record)
    db.session.commit()
        
    
        
