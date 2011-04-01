#!/bin/bash
BIN_EXONERATE="/home/taejoon/src/exonerate/current/bin/exonerate"
PRIMER_FILE="../primers.fasta"

for SEQ_FILE in $(ls *fna)
do
  DATANAME=${SEQ_FILE%".fna"}
  echo $DATANAME, $SEQ_FILE
  $BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "exonerate/primers.$DATANAME.exonerate_cigar"
done
