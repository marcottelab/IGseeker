#!/usr/bin/python
import os
import sys

seq_in_total = 0
seq_in_cluster = 0
seq_nohit = 0
count_cluster = 0
sum_identity = 0

filename_uc = sys.argv[1]

cluster_size_list = []
f_uc = open(filename_uc,'r')
for line in f_uc:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    if( tokens[0] == 'N' ):
        seq_nohit += 1
    if( tokens[0] == 'D' ):
        cluster_size = int(tokens[2])
        if( cluster_size == 1 ):
            seq_in_total += 1
        else:
            identity = float(tokens[7])
            sum_identity += identity
            count_cluster += 1
            seq_in_total += cluster_size
            seq_in_cluster += cluster_size
            cluster_size_list.append(cluster_size)
f_uc.close()

print "Total sequences: %d"%seq_in_total
print "Sequences in clusters: %d"%seq_in_cluster
print "Sequences without clusters: %d"%seq_nohit
print "Clusters: %d (id_pct %.2f)"%(count_cluster, sum_identity/count_cluster)
print "Top 5 cluster_size: %s"%(','.join(["%d"%x for x in sorted(cluster_size_list,reverse=True)[:5]]))
