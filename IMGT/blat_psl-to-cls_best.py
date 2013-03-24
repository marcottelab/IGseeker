#!/usr/bin/python
import os
import sys

filename_psl = sys.argv[1]

q2best = dict()
f_psl = open(filename_psl,'r')
for line in f_psl:
    line = line.strip()
    if( line.startswith('psLayout') or line.startswith('match') or line.startswith('---') ):
        continue
    tokens = line.split("\t")
    if( len(tokens) < 18 ):
        continue
    match_len = int(tokens[0])
    mismatch_len = int(tokens[1])
    q_gap_count = int(tokens[4])
    q_gap_bases = int(tokens[5])
    strand = tokens[8]
    q_id = tokens[9]
    q_len = int(tokens[10])
    q_start = int(tokens[11])
    q_end = int(tokens[12])
    t_id = tokens[13]
    t_class = t_id.split('|')[-1]

    align_len = match_len - mismatch_len - q_gap_bases
    #print q_id,t_class,align_len

    if( not q2best.has_key(q_id) ):
        q2best[q_id] = dict()
    if( not q2best[q_id].has_key(t_class) ):
        q2best[q_id][t_class] = {'q_len':q_len, 't_id':t_id, 'align_len':align_len, 'strand':strand, 'q_start':q_start, 'q_end':q_end}
    elif( q2best[q_id][t_class]['align_len'] < align_len ):
        q2best[q_id][t_class] = {'q_len':q_len, 't_id':t_id, 'align_len':align_len, 'strand':strand, 'q_start':q_start, 'q_end':q_end}
f_psl.close()

f_out = open('%s.cls_best'%(filename_psl.replace('.blat_psl','')),'w')
for tmp_q in q2best.keys():
    for tmp_t_cls in q2best[tmp_q].keys():
        tmp_q2best = q2best[tmp_q][tmp_t_cls]
        f_out.write("%s\t%d\t%s\t%s\t%s\t%d\t%d\t%d\n"%(tmp_q,tmp_q2best['q_len'],tmp_t_cls,tmp_q2best['t_id'],tmp_q2best['strand'],tmp_q2best['align_len'],tmp_q2best['q_start'],tmp_q2best['q_end']))
f_out.close()
