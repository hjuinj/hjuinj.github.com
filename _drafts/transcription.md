---
title: "Genome Transcription Lecture 1"
author: "hjuinj"
date: "27 October 2015"
output: html_document
---

Transcription governs what type of cell a cell becomes. A subset of the entire genome is replicated by a particular cell 

Replication stand alone compare to transcription followed by translation

The two questions:

1. How does RNA choose the origin of transcription
2. How frequent is the transcription


RNA polymerase is far more processive and slower and more fidel, it does not need a primer template junction like DNA polymerase does

#One Gene Methods

##Incorporation Assay:(how active, precessive the polymerase is)
radioactive rNTP

Gel electrophoresis:
- Denaturing gel, urea and heat, prevents folding of single straned RNA
- Termination place imprecise, oftren cuts DNA templates so the RNA will run to the end of the template so all terminate at the same place


##Primer extension assay (mapping starting site of transcription):
- A DNA primer on the non-template strand that is somewhere within the region of the RNA copy, radioactivly labelled
- Anneal to the RNA and extends using reverse transcriptase
- The DNA primer that extends to the start of the RNA transcript can be run on acrylamide gel to give almost single nuleotide resolution of the starting position (place of initiation and length of the DNA).


##Real time PCR: (show how abundant/how expressed a gene is)
incorporate a dye into double stranded DNA and see the color intensity of the product grow over time, at the start the rate of increase of color is proportional to the abundance of the starting template for PCR to occur. 


#Global Gene 

##RNA Seq: (the expression of RNA)
- Isolate RNA (from cell) as starting template for reverse transcriptase
- Make cDNA (complementary DNA, starting with hexmer primers) 
- Allow few rounds of replication of DNA and generate reads for deep sequencing (Bioinformatics course part II)
- Maps how frequent genes are transcribed by the number of reads that fall into bins
- ONLY Measures steady state RNA levels, RNAs have different half-lives. 

##Global-run-on Seq (RNA transcription rate)
- Go back to isolate nuclei, looking at a frame in time where RNA polymerases are still on their respective DNA template for trascription
- Incorporating a brominated version of UTP, and theses Br-UTPs are incorporated into the RNA currently being synethsized. 
- Isolate the RNA by immunopercipitation (special anti-body that recognize the labelled bromo URPs) and do deep sequencing


<!-- ![Summary](/assets/img/Genomics/L1_SequencingMethodsSummary.png) -->