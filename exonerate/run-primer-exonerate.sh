#!/bin/bash
BIN_EXONERATE="/home/taejoon/src64/exonerate-2.2.0-x86_64/bin/exonerate"

PRIMER_FILE="../primers.fasta"

DATANAME="GH_BoneMarrowPlasma_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="GH_LymphPlasma_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="GH_SpleenPlasma_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VH_BoneMarrowPlasma_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VH_LymphGerm_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VH_LymphPlasma_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VH_PeriBloodMono_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VH_SpleenGerm_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VH_SpleenPlasma_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VL_LymphGerm_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VL_PeriBloodMono_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"

DATANAME="VL_SpleenGerm_mouse23"
SEQ_FILE=$DATANAME".fna"
$BIN_EXONERATE -q $PRIMER_FILE -t $SEQ_FILE --showcigar T --showvulgar F --showalignment F --showsugar F > "primers.$DATANAME.exonerate_cigar"
