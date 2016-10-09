---
title: "Recent Reads #1"
layout: post
category : Scholastic
tags :
    - casual reading
    - science
    - notes
---

My placement at UCB Celltech has finally come to an end yesterday. With that I came home with a huge pile of papers that I glanced over during the year for personal gain (mainly at the beginning as I switched to electronic papers later on).

As I probably need to throw most of them away when I move house, it is a good idea to review some of the valuable ones before I do so.

- [Computer-based de novo design of drug-like molecules](www.nature.com/nrd/journal/v4/n8/full/nrd1799.html)

  *De Novo* Deisgn : "The design of bioactive compounds by incremental construction of a ligand model within a model of the receptor or enzyme active site, the structure of which is known from X-ray or NMR data."

  The procedure requires three main components. First, to assemble chemical fragments in synthetically tractable fashion. Second, to score the overall interactions between the assembled structure and the therapeutic target. Lastly, to ensure enough representitive strucutres have been tested for good coverage of the relevant chemical space. The last is the hardest.

  Determination of the shape of the binding site allows significant reduction in chemical space seraching.Optimisation on the ligand mainly consist of bettering the hydrogen bond complementarity between the recpetor and the ligand (usually grid-based search). This allows pharmacophores to be places to complement the residue interactions. Then a scheme is needed to link them together into one piece. These ligand poses then are scored by approximating the binding free energy using either explicit force-field, empirical scorin functions or knowledge-based methods (database on frequency of atom-pair interactions e.g. Superstar).   On top of binding affinity, other properties of the ligand needs to be assessed such as ADMET and structural alerts. These are collectively known as secondary target constraints and they are weighted in the score.

  The linking scheme between all these fragments/pharamcophores requires enumeration of different combintaions where all enumerations cannot be explictly run. Tree search algorithm or Monte Carlo or even machine learning schemes can be used to join them together.

  Automated de Novo design can be used as in idea generator as new chemotypes for chemists and can complement experimental techqniues like HTS or in silico screening. One major problem with which is of course its inability to consider protein motion/flexibility.



- [De Novo Fragment Design for Drug Discovery and Chemical Biology](onlinelibrary.wiley.com/doi/10.1002/anie.201508055/abstract)

  An example ligand based de novo design on the death associated protein kinase target. Using DOGS to perfrom virtual synthesis and scaffold hopping with a known drug as the template. A structurally very different chemcial entity to the template though with similar pharamcophores profile was ranked the highest and synthesised with X-ray structure solved to show binding at ATP site.

- [A Simple Statistical Parameter for Use in Evaluation and Validation of High Throughput Screening Assays.](jbx.sagepub.com/content/4/2/67.long)

  Introduced the Z-factor, a measure of assay quality to allow cross-campaign comparison of HTS resutls. Using the readings for the controls to define the assay window, The Z-factor uses the ratio of SD and means between the control and sample defining the capability of hit identification for a given assay. A Z'-factor was also devised which only involves comparing the same statistical quantity of only the +ve and -ve controls, allowing a determination of quality of the assay. Z' evaluates overall assay quality and Z reflects the quality of a configured assay.

- [Reporting data from high-throughput screening of small-molecule libraries](www.nature.com/nchembio/journal/v3/n8/full/nchembio0807-438.html)

  Proposed standard for high HTS screen results ought to be reported. See table 1.

- [An overview of molecular fingerprint similarity search in virtual screening](www.tandfonline.com/doi/abs/10.1517/17460441.2016.1117070)

  Topological and circular fingerprints enumerates all the bonding pathes of a molecule (up to a number of bond cut-off). These pathes are hashed into bit-strings. For a given compound, the bit strings corresponding to the chemical fragments it contained are combined together. Topological encodes the linear bonding paths of the molecular, circular fingerprint expands out radially.

  Structural key fingerprints have a pre-defined sets of functional groups and a bit string can be generated based on the presence and absence of these functional environments for a given molecule.

  Pharmacophore fingerprints encodes combinations of chemcial environemnts in the moelcular and their distance of sepration into bits that are joined.

  All these schemes can yield molecules encoded by a series of zeros and ones. So two molecules can be compared by different distance measures. A comprehensive table of different fingerprint distance measure is [here](http://www.daylight.com/dayhtml/doc/theory/theory.finger.html)

  Some usages in the context of viertual screening: 1). measure compound deck diversity 2). prioritise compounds based on similarity to a template molecule 3). measure activity probability based on similarity to template compound


- [Molecular Similarity in Medicinal Chemistry](pubs.acs.org/doi/abs/10.1021/jm401411z)

  Similarity property pricinple : similar compounds should have similar property. "molecular similarity values are rarely of interest per se. Rather, they are used as a basis for correlating similarity, however assessed, with compounddependent properties such as biological activity"

  Many levels of similarity: physicochemical similarity, topological similarity, shape similarity, biological similarity, local similarity...

  Pharmacophore models in drug design focuses only on selected atoms, groups, or functionalities that are known or hypothesized to be responsible for activity. This represents a local view of similarity.

  Use of similarity should be exercised with caution. Its applicability varies based depending on the combination of compound class, similarity matric, molecular representation.  The absolute magnitude of similarity is not as meaningful as relative magnitude of similarity.


- [Data Mining of Protein-Binding Profiling Data Identifies Structural Modifications that Distinguish Selective and Promiscuous Compounds](pubs.acs.org/doi/abs/10.1021/ci3002606)

  Utilised binding assay data on a set of compounds against 100 sequence-unrelated proteins where the compounds are divided into three main classes : natural proudct, commerical synthesised cpds and diverse synthesised compounds. The goal was to find structural motifs that distinguish highly specific and promiscuous binders.

  Pair-wise cpd structural similarity was defined by MACCS fingerprint with Tanimoto metric. A structure-promiscuity index difference (SPID) was divised for compound pairs that measures the relation between the number of proteins bound by the two molecules and their structural similarity. Compounds that bound many proteins and compounds that were very specific were selected to have the SPID calculated. This way chemical motifs that could lead to promiscuity issues can be identified.

  "It was concluded that small structural changes in synthetic compounds from academic groups showed greater promiscuity difference than do synthetic compounds from commercial sources. Natural products showed the lowest drastic changes in promiscuity due to small structural  modifications."

- [Chemography of Natural Product Space](dl.kums.ac.ir/bitstream/Hannan/172114/1/2015%20Volume%2081%20Issue%206%20April%20(3).pdf)

  Reduced a series of pharamcophoric features into 2 dimensions using generative topological mapping, a non-linear dimensional reduction scheme to visualise chemical space. Observed natural products and drug/lead moleculers have very similar profiles. Infere this method can be used to measure functional similarities between these two classes.

- [Linked open drug data for pharmaceutical research and development](https://jcheminf.springeropen.com/articles/10.1186/1758-2946-3-19)

  Aim to allow sharing of interlinked *data* at very detailed levels with the visual of revolutionise global data sharing, integration and analysis. Each single piece of data is represented by a URL. The data object is composed of subject-predicate-object triples within a resource description framework, allowing individual data pieces be linked into a network. Linked data sets include databases such as ChEMBL and Drugbank. Used by Open PHACTS under the IMI.

- [Detection of secondary binding sites in proteins using fragment screening](www.pnas.org/content/112/52/15910.short)

  "Indeed, given the significant size of most proteins it could be argued that it would be inefficient for evolution not to have resulted in multiple binding sites that could be used to regulate function. Furthermore, drug molecules that target such sites can offer an orthogonal mechanism for modulating the biological activity of a target protein and may have improved selectivity and resistance profiles. ... ligands targeting these sites can provide a mechanism for activating enzymes, something that is unlikely to be achievable by binding to the catalytic site."

  Frgament screening solving X-ray structure on 2 dozen proteins revealed on average more than 2 secondary fragment binding sites. The functional relevance for such sites were by and large unknown.

  Orthologs of the screened proteins were minded to see whether the residues in those defined sites are evolutionarily conserved. They were.  An atom mobility index was devised which indicate how rigid regions of the proteins are. These secondary sites were quite rigid (also used B-factor). Other physicochemical properties were test, e.g. such sites are also quite buried and thus polar. All three points point to these site exibiting function.
