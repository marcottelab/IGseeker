#!/usr/bin/python
import os
import sys

# 1=Type, 2=ClusterNr, 3=SeqLength or ClusterSize, 4=PctId, 5=Strand, 6=QueryStart, 7=SeedStart, 8=Alignment, 9=QueryLabel, 10=TargetLabel
# Record types (field 1): L=LibSeed, S=NewSeed, H=Hit, R=Reject, D=LibCluster, C=NewCluster, N=NoHit

filename_uc = sys.argv[1]

type_list = []
count_hit = 0
count_new = 0
count_cluster = 0
f_uc = open(filename_uc,'r')
for line in f_uc:
    if( line.startswith('#') ):
        continue
    tokens = line.strip().split("\t")
    type_list.append(tokens[0])
    if( tokens[0] == 'D' ):
        count_cluster += 1
        cluster_size = int(tokens[2])
        pct_id = float(tokens[7])
        query_id = tokens[8].split(',')[0]
        #print query_id, pct_id, cluster_size
    elif( tokens[0] == 'N' ):
        count_new += 1
    elif( tokens[0] == 'H' ):
        count_hit += 1
f_uc.close()

print "Total sequences: ",count_hit+count_new
print "Number of clusters: ",count_cluster
print "Sequences in cluster: %d (%.2f pct)"%(count_hit, float(count_hit)/(count_hit+count_new))
print "Sequences without cluster: %d (%.2f pct)"%(count_new, float(count_new)/(count_hit+count_new))
