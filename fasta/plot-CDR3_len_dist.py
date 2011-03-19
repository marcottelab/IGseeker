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
bin_list = range(0,30)
fig = plt.figure(figsize=(12,9))
ax1 = fig.add_subplot(1,2,1)
ax1.hist(seq_len_sorted_list, bins=bin_list)
ax1.set_xlabel("Length (aa)")
ax1.set_ylabel("Frequency")
ax1.set_title(filename_fasta)
ax1.grid()

cum_len_list = []
count_total = 0
count_lt5 = 0
count_gt30 = 0
len_95pct = 0
count_95pct = int(len(seq_len_sorted_list)*0.95)
for tmp_len in sorted(seq_len_sorted_list, reverse=True):
    count_total += 1
    cum_len_list.append( count_total )
    if( tmp_len < 5 ):
        count_lt5 += 1
    if( tmp_len > 30 ):
        count_gt30 += 1
    if( count_total > count_95pct and len_95pct == 0 ):
        len_95pct = tmp_len

print "< 5 aa :",count_lt5
print "> 30 aa :",count_gt30

ax2 = fig.add_subplot(1,2,2)
ax2.plot(seq_len_sorted_list[::-1], cum_len_list)
#ax2.set_xlim(seq_len_sorted_list[-1], seq_len_sorted_list[0])
ax2.set_xlabel("Length (a.a.)")
ax2.set_ylabel("Cumulated number of CDR3")
median_len = seq_len_sorted_list[int(count_total*0.5)]
q25_len = seq_len_sorted_list[int(count_total*0.25)]
q75_len = seq_len_sorted_list[int(count_total*0.75)]
#ax2.set_title("N=%d,median=%d,min=%d,max=%d"%(count_total,seq_len_sorted_list[int(count_total*0.5)],seq_len_sorted_list[0],seq_len_sorted_list[-1]))
iqr = q75_len - q25_len
ax2.set_title("N=%d,median=%d,1.5xIQR:%.1f-%.1f"%(count_total,median_len,q25_len-iqr*1.5,q75_len+iqr*1.5))
ax2.vlines(len_95pct,0,count_total)
ax2.hlines(count_95pct,0,max(seq_len_sorted_list))
ax2.text(median_len, count_95pct-0.05*count_total, "95pct covered: %d"%len_95pct)
ax2.set_xlim(30,0)
ax2.grid()

#tmp_list = sorted(seq_len.values())
#print tmp_list[:10]
#print max(seq_len.values())
#print min(seq_len.values())

plt.savefig("%s.CDR3_len_dist.png"%filename_fasta)
