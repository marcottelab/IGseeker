#!/usr/bin/python
import os
import sys

filename_uc = sys.argv[1]

id_size = dict()
id_count = dict()

total_size = 0
f_uc = open(filename_uc,'r')
for line in f_uc:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    if( tokens[0] == 'D' ):
        cluster_size = int(tokens[2])
        cluster_id = float(tokens[7])

        if( not id_size.has_key(cluster_id) ):
            id_size[cluster_id] = 0
            id_count[cluster_id] = 0
        id_size[cluster_id] += cluster_size
        id_count[cluster_id] += 1
        total_size += cluster_size
f_uc.close()

print "Total: ",total_size
import matplotlib.pyplot as plt 

id_list = sorted(id_size.keys(), reverse=True)
sum_coverage = 0
sum_cluster = 0
cutoff_95pct = 0
sum_coverage_list = []
sum_cluster_list = []
for tmp_id in id_list:
    sum_coverage += id_size[tmp_id]
    sum_cluster += id_count[tmp_id]
    sum_coverage_list.append( sum_coverage )
    sum_cluster_list.append(sum_cluster)
    if( total_size*0.95 < sum_coverage and cutoff_95pct == 0 ):
        print "95% cutoff: ",tmp_id
        cutoff_95pct = tmp_id

fig = plt.figure(figsize=(12,6))

ax1 = fig.add_subplot(1,2,1)
ax1.plot(id_list, [float(x)/total_size for x in sum_coverage_list])
ax1.set_xlim(100,90)
ax1.set_xlabel("%id of clusters")
ax1.set_ylabel("Relative number of sequences (coverage)")
ax1.set_title(filename_uc)
ax1.hlines(0.95,100,90,color='red',lw=2)
ax1.vlines(cutoff_95pct,0,1,color='red',lw=2)
ax1.text(99,0.95,"95% coverage")
ax1.text(cutoff_95pct-0.1,0.90,"id=%.1f"%(cutoff_95pct)+" %")
ax1.grid()

ax2 = fig.add_subplot(1,2,2)
ax2.plot(id_list, sum_cluster_list)
ax2.set_xlim(100,90)
ax2.vlines(cutoff_95pct,0,max(sum_cluster_list),color='red',lw=2)
ax2.set_xlabel("%id of clusters")
ax2.set_ylabel("Cumulative number of clusters")
ax2.grid()
#ax1.hist([x*id_size[x] for x in id_size.keys()], normed=1, cumulative=True)

#plt.show()
plt.savefig('%s.usearch_id_dist.png'%filename_uc)
