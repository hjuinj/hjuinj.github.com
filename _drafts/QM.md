---
title: "Computational Chemistry"
layout: post
category : Profession
tags : [notes]
---

additions, insertions and deletions will be done as my understanding of the topic progresses. This serves as a test-ground for me to elucidate my understanding in computational chemistry as well as a sand-box for formatting maths-heavy documents in markdown. Hence **I do NOT guarantee the validity of the following document nor is it my attempt of a rigorous piece of work**

Maths equations markdown reminder
<http://www.statpower.net/Content/310/R%20Stuff/SampleMarkdown.html>
markdown cheatshet
<https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet>

$$\int_0^{2\pi} \sin x~dx$$

From this, one can begin to see why when compared to MM methods, QM calculations are deemed a lot more expensive. In order to simulation a system requires evaluation of the system evolution over time. For each time step, a MM approach only requires the evaluation of the analytical function composing of the different energy contributions (torsion, electrostatic, etc), but a QM calculation would need to iteratively solve for the new MOs for the changed nuclei coordinates before the energy evaluations.


For an atomic orbital calculation, these are typically the orbitals for a hydrogenic atom (an atom with only one electron, but the appropriate nuclear charge). For a molecular orbital or crystalline calculation, the initial approximate one-electron wave functions are typically a linear combination of atomic orbitals (LCAO).



## Basis Sets
The adaptation of Gaussian orbital over Slater type orbital (STO) is due to its efficiency in computation. Such orbital has a general form of:
                                    $$x^ay^bz^c exp(-\alpha  r^2) $$
The exponential format allows orbital joining (multiplication) very cheap to calculate.

Depending on the powers a,b,c which can take on values of 1 or 0. When all of them equal to zero, it is a zeroth-order Gaussian that resembles the formalism of s-type atomic orbitals. When one of the three is one it is a first-order Gaussian, resembling p-type orbitals.

Often a linear combinations of GTOs are used to approximate STOs. Fitting is done via minimising least square error for example. After optimisation, in the linear combination, the coefficient in front of each GTO and the $\alpha$ is often fixed when calculating the final MO form. In addition, the $\alpha$ term is fixed for s and p type orbitals This is again for computational cost.

The notation "STO-3G" therefore means each Slater type orbital is approximated by 4 Gaussian orbitals. For *ab initio*, 3 is the bare minimum. Reminder of the hierarchy, MOs are approxmiate by LCAO, AOs are approximated by STO, and STOs are approximated by GTOs.


*Minimal basis set* includes all the filled orbitals in each atom.
