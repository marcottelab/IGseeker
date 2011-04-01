#!/usr/bin/python
import os
import sys
import gzip

min_seq_len = 200
max_seq_len = 450

filename_fasta = sys.argv[1]
filename_base = filename_fasta.replace('.gz','').replace('.fna','')

seq_len = dict()

h_fasta = ''
f_fasta = open(filename_fasta,'r')
if( filename_fasta.endswith('.gz') ):
    f_fasta = gzip.open(filename_fasta,'rb')
for line in f_fasta:
    if( line.startswith('>') ):
        h_fasta = line.strip()
        seq_len[h_fasta] =  0
    else:
        seq_len[h_fasta] += len(line.strip())
f_fasta.close()

lt_min_seq = 0
gt_max_seq = 0
seq_len_list = []
for seq_id in seq_len.keys():
    if( seq_len[seq_id] < min_seq_len ):
        #seq_len_list.append( min_seq_len )
        lt_min_seq += 1
    elif( seq_len[seq_id] > max_seq_len ):
        #seq_len_list.append( max_seq_len )
        gt_max_seq += 1
    else:
        seq_len_list.append( seq_len[seq_id] )

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(9,5))
bin_list = range(200,450,2)
ax1 = fig.add_subplot(1,2,1)
n, bins, patches = ax1.hist(seq_len_list, bins=bin_list)
ax1.set_xlabel("Read length (bp)")
ax1.set_ylabel("Frequency")
ax1.set_title(filename_base)
ax1.text(min_seq_len,n[0],"<%d: %d"%(min_seq_len,lt_min_seq))
ax1.text(max_seq_len,n[-1],"<%d: %d"%(max_seq_len,gt_max_seq))
ax1.grid()

count_total = 0
cum_len_list = []
seq_len_sorted = sorted(seq_len.values(),reverse=True)
for tmp_len in sorted(seq_len.values(),reverse=True):
    count_total += 1
    cum_len_list.append( count_total )
seq_len_median = seq_len_sorted[int(count_total*0.5)]

ax2 = fig.add_subplot(1,2,2)
ax2.plot(seq_len_sorted, cum_len_list)
ax2.set_xlabel("Read length (bp)")
ax2.set_ylabel("Cumulated number of reads")
ax2.set_title("N=%d,median=%d,<%d=%d,>%d=%d"%(count_total,seq_len_median,min_seq_len,lt_min_seq,max_seq_len,gt_max_seq), size=9)
ax2.grid()

plt.savefig("%s.len_dist.png"%filename_base)
#plt.show()
