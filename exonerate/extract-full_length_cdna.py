#!/usr/bin/python
import os
import sys
import gzip

filename_cigar = sys.argv[1]
filename_fasta = sys.argv[2]

h_seq = ''
seq_list = dict()
f_fasta = open(filename_fasta,'r')
for line in f_fasta:
    if( line.startswith('>') ):
        h_seq = line.strip().split()[0].lstrip('>')
        seq_list[h_seq] = []
    else:
        seq_list[h_seq].append( line.strip() )
f_fasta.close()

read2primer = dict()
f_cigar = open(filename_cigar,'r')
if( filename_cigar.endswith('.gz') ):
    f_cigar = gzip.open(filename_cigar,'rb')

for line in f_cigar:
    if( not line.startswith('cigar') ):
        continue
    tokens = line.strip().split()
    primer_name = tokens[1]
    primer_start = int(tokens[2])
    primer_end = int(tokens[3])
    primer_strand = tokens[4]
    read_name = tokens[5]
    read_start = int(tokens[6])
    read_end = int(tokens[7])
    read_strand = tokens[8]
    if( not read2primer.has_key(read_name) ):
        read2primer[read_name] = dict()
    read2primer[read_name][primer_name] = {'p_start':primer_start, 'p_end':primer_end, 'p_strand':primer_strand, 'r_start':read_start, 'r_end':read_end, 'r_strand':read_strand}
f_cigar.close()

def revcomp(tmp_seq):
    rv_list = []
    ncmp = {'A':'T','T':'A','G':'C','C':'G','N':'N','a':'t','t':'a','g':'c','c':'g','n':'n'}
    for n in tmp_seq[::-1]:
        rv_list.append( ncmp[n] )
    return ''.join(rv_list)

for read_name in read2primer.keys():
    primer_list = read2primer[read_name].keys()
    if( len(primer_list) < 2 ):
        continue
    
    F_primer_start = dict()
    R_primer_start = dict()
    F_primer_end = dict()
    R_primer_end = dict()
    for primer_name in primer_list:
        tmp = read2primer[read_name][primer_name]
        if( primer_name.find('FOR') >= 0 ):
            F_primer_start[primer_name] = tmp['r_start']
            F_primer_end[primer_name] = tmp['r_end']
        elif( primer_name.find('REV') >= 0 ):
            R_primer_start[primer_name] = tmp['r_start']
            R_primer_end[primer_name] = tmp['r_end']
     
    if( len(F_primer_start) == 0 or len(R_primer_start) == 0):
        continue
    F_primer_list = sorted(F_primer_start.keys(),key=F_primer_start.get)
    R_primer_list = sorted(R_primer_start.keys(),key=R_primer_start.get)
    forward_len = (R_primer_start[R_primer_list[-1]] - F_primer_start[F_primer_list[0]])
    reverse_len = (F_primer_start[F_primer_list[-1]] - R_primer_start[R_primer_list[0]])

    read_seq = ''.join(seq_list[read_name])
    if( forward_len > 0 and float(forward_len) / len(read_seq) > 0.9 ):
        tmp_start = F_primer_start[F_primer_list[0]]
        tmp_end = R_primer_start[R_primer_list[-1]]
        print ">%s|%s|%s|F|amplicon_len=%d|read_len=%d"%(read_name,F_primer_list[0],R_primer_list[-1],forward_len,len(read_seq))
        print read_seq[tmp_start:tmp_end+1]
    if( reverse_len > 0 and float(reverse_len)/len(read_seq) > 0.9 ):
        tmp_start = R_primer_start[R_primer_list[0]]
        tmp_end = F_primer_start[F_primer_list[-1]]
        print ">%s|%s|%s|R|amplicon_len=%d|read_len=%d"%(read_name,F_primer_list[-1],R_primer_list[0],reverse_len,len(read_seq))
        print read_seq[tmp_start:tmp_end+1]
