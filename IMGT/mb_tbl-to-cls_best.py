#!/usr/bin/env python
import os
import sys

filename_tbl = sys.argv[1]

seq_len = dict()
seq_type = dict()
f_tbl = open(filename_tbl,'r')
for line in f_tbl:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    seq_id = tokens[0]
    align_len = int(tokens[3])
    bit_score = float(tokens[13])
    cls_type = tokens[1].split('|')[3]
    
    if( not seq_type.has_key(seq_id) ):
        seq_type[seq_id] = dict()
        seq_len[seq_id] = int(tokens[6])

    strand = '+'
    if( int(tokens[10]) > int(tokens[11]) ):
        strand = '-'

    if( not seq_type[seq_id].has_key(cls_type) ):
        seq_type[seq_id][cls_type] = {'ref_id':tokens[1], 'align_len':align_len, 'q_start':int(tokens[7]), 'q_end':int(tokens[8]), 'bits':bit_score, 'strand':strand}
    elif( seq_type[seq_id][cls_type]['bits'] < bit_score ):
        seq_type[seq_id][cls_type] = {'ref_id':tokens[1], 'align_len':align_len, 'q_start':int(tokens[7]), 'q_end':int(tokens[8]), 'bits':bit_score, 'strand':strand}
f_tbl.close()

#@SRR060697.348572	132	J-REGION	refseq1470|TRBJ1-1*01|F|J-REGION	+	38	64	102
f_out = open('%s.cls_best'%filename_tbl,'w')
for seq_id in sorted(seq_type.keys()):
    for cls_type in sorted(seq_type[seq_id].keys()):
        tmp = seq_type[seq_id][cls_type]
        f_out.write('%s\t%d\t%s\t%s\t%s\t%d\t%d\t%d\n'%(seq_id,seq_len[seq_id],cls_type,tmp['ref_id'],tmp['strand'],tmp['align_len'],tmp['q_start'],tmp['q_end']))
f_out.close()
