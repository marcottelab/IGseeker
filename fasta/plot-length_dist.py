#!/usr/bin/python
import os
import sys

filename_fasta = sys.argv[1]

seq_len = dict()

h_fasta = ''
f_fasta = open(filename_fasta,'r')
for line in f_fasta:
    if( line.startswith('>') ):
        h_fasta = line.strip()
        seq_len[h_fasta] =  0
    else:
        seq_len[h_fasta] += len(line.strip())
f_fasta.close()

import matplotlib.pyplot as plt

seq_len_sorted_list = sorted(seq_len.values())
bin_list = range(200,400,2)
fig = plt.figure(figsize=(12,9))
ax1 = fig.add_subplot(1,2,1)
ax1.hist(seq_len_sorted_list, bins=bin_list)
ax1.set_xlabel("Read length (bp)")
ax1.set_ylabel("Frequency")
ax1.set_title(filename_fasta)
ax1.grid()

cum_len_list = []
count_total = 0
count_lt200 = 0
count_gt400 = 0
len_95pct = 0
count_95pct = int(len(seq_len_sorted_list)*0.95)
for tmp_len in sorted(seq_len_sorted_list, reverse=True):
    count_total += 1
    cum_len_list.append( count_total )
    if( tmp_len < 200 ):
        count_lt200 += 1
    if( tmp_len > 400 ):
        count_gt400 += 1
    if( count_total > count_95pct and len_95pct == 0 ):
        len_95pct = tmp_len

print "< 200 bp :",count_lt200
print "> 400 bp :",count_gt400

ax2 = fig.add_subplot(1,2,2)
ax2.plot(seq_len_sorted_list[::-1], cum_len_list)
ax2.set_xlim(seq_len_sorted_list[-1], seq_len_sorted_list[0])
ax2.set_xlabel("Read length (bp)")
ax2.set_ylabel("Cumulated number of reads")
ax2.set_title("N=%d,median=%d,min=%d,max=%d"%(count_total,seq_len_sorted_list[int(count_total*0.5)],seq_len_sorted_list[0],seq_len_sorted_list[-1]))
ax2.vlines(len_95pct,0,count_total)
ax2.hlines(count_95pct,0,max(seq_len_sorted_list))
ax2.text(len_95pct-20, count_95pct-0.05*count_total, "95 percent cutoff length: %d"%len_95pct)
ax2.grid()

tmp_list = sorted(seq_len.values())
print tmp_list[:10]
print max(seq_len.values())
print min(seq_len.values())
#plt.savefig("%s.V_length_dist.png"%species)
plt.show()
