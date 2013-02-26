#!/usr/bin/python
import os
import sys

seq_list = dict()
seq_h = ''
filename_fa = 'imgtrefseq.fasta'
f_fa = open(filename_fa,'r')
for line in f_fa:
    if( line.startswith('>') ):
        seq_h = line.strip()
        seq_list[seq_h] = []
    else:
        seq_list[seq_h].append( line.strip().upper() )
f_fa.close()

f_out = dict()
for tmp_h in seq_list.keys():
    tokens = tmp_h.replace(' ','_').split('|')
    tmp_species = tokens[2]
    tmp_acc = tokens[1]
    tmp_type = tmp_acc[:3]
    if( tmp_species.find('Homo_sapiens') >= 0 ):
        tmp_tag = 'HUMAN_%s'%tmp_type
        if( not f_out.has_key(tmp_tag) ):
            f_out[tmp_tag] = open('imgtrefseq.%s.fasta'%tmp_tag,'w')
        f_out[tmp_tag].write('%s|%s|%s|%s\n%s\n'%(tmp_h.split()[0],tmp_acc,tokens[3],tokens[4],''.join(seq_list[tmp_h])))

for tmp_tag in f_out.keys():
    f_out[tmp_tag].close()
