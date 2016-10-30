---
title: "Recent Reads #2"
layout: post
category : Scholastic
tags :
    - casual reading
    - science
    - notes
---
- [Evidence for a limit to human lifespan](www.nature.com/nature/journal/v538/n7624/full/nature19793.html)

  The general trend for average age of population has been steadily growing for since 1960s. By mapping the rate of change in gain in age, they found in the past 30 years, the major contributor to that trend is reduced old-age mortaility, i.e. the most dramatic increase in number is in people who now live upto around 100. However, no significant increase in people living above that has been observed. In addition, they found, starting from the 20th century, the largest gain in number of years have increased from 85 quite steadily. However, it has plateaued at 100 for a longer time than previous plateaus. They then collated the number of people who lived to older than 110 (supercentenarians) and their ages of death starting from 1970. The trend shows increase in maximum age has ceased after 1995. By fitting a Poisson to the data, it was found that the probability of an individual exceeding 125 in any given year is less than 1 in 10,000. Although they do acknowledge the datasets is quite small, the increase and decline could just be fluctuations (the data shown would suggest the maximum age has in fact more rapidly decresed after 1995 than it has increased). Thus they "suggest that the maximum lifespan of humans is fixed and subject to natural constraints" and they postulate there is species-specific limits set by these longevity-assurance systems encoded in the genome.

- [MoS<sub>2</sub> transistors with 1-nanometer gate lengths](science.sciencemag.org/content/354/6308/99.full)

  Silicon as channel material has gate length limit ~5nm is due to short channel effect. "Direct source-to-drain tunneling and the loss of gate electrostatic control on the channel severely degrade the Off state leakage currents". Transition metal dichalcogenides (TMDs) as alternative as low in-plane dielectric constant enhances the electronstatic control. MoS<sub>2</sub> achieves 100-fold better leakage property than Si due to higher effective mass along the direction of transport. Althougth at the same time the On state (ballistic) current is lower. TCAD simulation run to explain superior behaviour. Also shown achieving the thinner the semicondutor layer the better distringuished the off state. Manufacutring such thin layer is challenging.


- [SambVca 2. A Web Tool for Analyzing Catalytic Pockets with Topographic Steric Maps](pubs.acs.org/doi/full/10.1021/acs.organomet.6b00371)

  Use "descriptors to quantitatively correlate properties of the catalytic pocket to how it behaves experimentally." Two types of desciprotrs, electronic of steric effect.

  Topographic steric map: grid based system applied to geometry optimised metal complex. A center point is chosen for the complex and the substrate that will be displaced is removed. A sphere of given radius cutoff is defined around the center point and this space is divided up into voxels. The occupance of each voxel is defined by whether or not atoms' VdW radii were within the voxel center. The map is a 2-d representation with occupancy along one axis(z) represented by colours of intensity.

  Choice of the radius cutoff is as below: "Considering that typical metal–ligand bond distances are within 2.0–2.5 Å, a value of 3.5 Å to define the first coordination sphere around the metal is expected to account for the space roughly comprising the van der Waals volume occupied by the atoms coordinated to the metal."

- [MDcons: Intermolecular contact maps as a tool to analyze the interface of protein complexes from molecular dynamics trajectories](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/1471-2105-15-S5-S1)

  Illucidated the differences in binding affinity of the PPIs. Using 2000 frames from a 100 ns simulation, the conservation of inter-residue contact points are plotted on a 2-D plot. Color gradient is able to show which interactions are the main contributors to the binding energy and can indicate regions of new interactions not exist in the crystal structure.

- [Ranking multiple docking solutions based on the conservation of inter-residue contacts](onlinelibrary.wiley.com/doi/10.1002/prot.24314/full)

  Critical Assessment of PRedicted Interactions (CAPRI), a community-wide blind docking experiment - ranking the native-like solution high amongst the ensemble of solutions (decoys), assumes unbiased sampling of the conformational space. For a given pose, the number of times each contact site has been seen in other poses have been tallied then normalised. The overall score for a given pose is the sum of all these tallies. Works better emsembles of docking poses generated from multiple docking programs as the noise of wrong docking poses destructively interfere with each other and the right contacts constructively interfere and make the signal stronger.

- [Analysis of Iterative Screening with Stepwise Compound Selection Based on Novartis In-house HTS Data](pubs.acs.org/doi/full/10.1021/acschembio.6b00029)

  Aim to reduce the cost of hit discovery by iterative screening of subsets of the total HTS deck, ending up with less compound screened in total. The interative screening algorithm: "(1) ranking of compounds based on retrospective activity data, (2) selection/triaging of hits, and (3) expanding from hits to close analogs based on chemical and biological similarity metrics." Begin with a well selected subset of compound with well-characterised MoA, then selecting a small proportion with high activity, finding the analogs of these compounds that has not been tested to be further screened. The matrics of assessment of the performance of this strategy is the rank distribution of the selected compund w.r.t all the other compounds (this is only availble in such retrospective study) and the chemical diversity by counting Murcko scaffolds.

  Test 34 assays where a total of over 1.3 M compounds were screened. On average "screening only 1% of the collection provides ∼7500 top-quality hits for further optimization".

  Considerations: Used both ECFP4 and HTS-FP (biological similarity) thus finding structural similarity and at the same time allow scaffold hopping. Performed better for cell-free assays compared to cell-based assays due to disregard of physicochemical properties at the moment. Found the amount of highly active scaffolds plateaus for further iterations. Compared the algorithm with randomly selection sets at iterations to carry forward and found stat-sig difference in performances. Explored effect on the performance of alogrithm by changing the parameters, such as the propertion of highest active compounds to be used for next iteration, the cut-offs for similarity criteria.

- [Building Force Fields: An Automatic, Systematic, and Reproducible Approach](pubs.acs.org/doi/pdf/10.1021/jz500737m)

    Came up withe a tool called ForceBalance. Experimented on parameter fitting of the TIP3P and TIP4P water models. Beginning with TIP3P and TIP4P's paramters (the functional forms are unchanged), iterative runs of MD simulations are performed to minimise the RMSE difference between the MD prediction and experimental value (experimental values also includes ab initio QM calculations). It was observed that the newly generated params better aggreed with experiments, which makes sense as this corresponds to fitting training data. But they also observed improved predictions on other properties not included in the experimental data fed into the training model, such as O−O radial distribution function, self-diffusion coefficient and shear viscosity. Regularisation was constraint posed to not have the trained value to be too far away from the initial start (this would not work then the starting point is stochastic). They argued for this particular case of water model, the amount of availble data is huge which would prevent overfitting, this again would not be true for other cases I think.

- [Voyages to the (un)known: adaptive design of bioactive compounds](www.sciencedirect.com/science/article/pii/S016777990800259X)

  Enlist two techniques to perform structural enumeration in a de novo design cycle.

  Evolutional Algorithm: seen before, intuitive. Can have random mutation of new terminal groups or/and combination of parental properties. Usually uses existing QSAR models rather than computing free energy.

  Particle Swarm Optimisation: "During its search, a particle remembers the best solution it has found so far in its personal memory. This point in search space exerts an attracting force on the particle, that is, in subsequent search steps, the particle has the tendency to revisit known territory that featured good solutions. In addition, particles influence each others’ search direction by communicating about search successes. Every particle knows the best search point that has been explored by the entire swarm so far. Similar to the personal memory, this so-called ‘social memory’ has an attracting force on a particle. This behavior is supposed to make the swarm preferably explore promising regions of the search space while ignoring less attractive territory"

- [An integrated encyclopedia of DNA elements in the human genome](www.nature.com/nature/journal/v489/n7414/pdf/nature11247.pdf)

  "The Encyclopedia of DNA Elements (ENCODE) project aims to delineate all functional elements encoded in the human genome". Intergration of results type from different types of experiments and cell types. This is a highly cited consortium. Anotated functional elements to 82% of the human genome. The range and the magnitude of the work is immense, although at the moment I cannot fully appriciate the true importance of this piece of work.
