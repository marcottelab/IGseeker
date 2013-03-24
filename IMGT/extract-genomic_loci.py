#!/usr/bin/python
import os
import sys

filename_psl = sys.argv[1]
filename_fa = sys.argv[2]

margin_len = 20000
min_start = 0
max_end = 0

f_psl = open(filename_psl,'r')
is_start = 0
for line in f_psl:
    if( line.startswith('----------') ):
        is_start = 1
        continue
    if( is_start == 0 ):
        continue
    tokens = line.strip().split("\t")
    t_start = int(tokens[15])
    t_end = int(tokens[16])
    if( t_end < t_start ):
        tmp = t_start
        t_start = t_end
        t_end = tmp

    if( min_start == 0 ):
        min_start = t_start
        max_end = t_end
    if( min_start > t_start ):
        min_start = t_start
    if( max_end < t_end ):
        max_end = t_end
f_psl.close()
sys.stderr.write('min:%d max:%d len:%d\n'%(min_start,max_end,max_end-min_start))

seq_list = []
f_genome = open(filename_fa,'r')
for line in f_genome:
    if( line.startswith('>') ):
        continue
    seq_list.append( line.strip() )
f_genome.close()

DB_name = filename_psl.split('.')[1]
tmp_seq = ''.join(seq_list)
print ">%s.%d-%d"%(DB_name,min_start-margin_len,max_end+margin_len)
print tmp_seq[min_start-margin_len:max_end+margin_len].strip('N')
