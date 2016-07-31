---
title: "Hatree-Fock"
layout: post
category : Resources
time : 23/07/2016
tags :
  - readings
---
The wavefunction of the entire system is a function with all the electronic coordinates as variables for a stationary system of nuclear coordinates.

For a given nuclear coordinates arrangement, the wavefunction is a function of the electron coordinates.

Firstly, the joint wavefunction for the molecule is approxmiated by the product of individual molecular orbital wavefunction only depended upon each nuclear coordinate.
<https://en.wikipedia.org/wiki/Slater_determinant>
A molecular orbital wavefunction is a better description of the environment a electron expreiences within a molecule. The overall system of the molecule is often described (approximated) by the product of the molecular orbital wavefunctions for each individual electron:

***Φ*** = ∏ Φ_n

In the Slater determinant, each element is a molecular orbital wavefunction. It is made up of all the molecular orbitals that are occupied by electrons. Hence for a N-electron system the determinant is NxN in dimention. The ith row is all the N possible wavefunctions the ith electron could reside in (can be the same MO, since each orbital accomodates two electrons).

The energy Hamiltonian of a polyelectronic system is attributed to three separable parts:
1. Each occupied molecular orbital has the kinetic and potential energy from all the nuclei. This is the **H_ii** part where "ii" means it is due to the same electron. (think of the Hamiltonian operator, where the potential energy part is made up of the summation of all the electrostatic potential from each nucleus)
2. Each *pair* of electrons experience electrostatic repulsion due to each other, denoted as **J_ij** where "ij" means it is interaction between different electrons.
3. Energy arising from spin correlation, or exchange interaction. Electron cannot reside in the same orbital if they have parallel spins. When two electrons have parallel spins, they cannot be in the same MO hence electron motions are not independent (that is even without considering part(2)). This is denoted **K_ij**, which is only non-zero when i and j are in the same spin.

For a system of N electrons, there is N * **H_ii**. There are N*(N-1) * **J_ij**, similarly for **K_ij**, but some of these terms would be zero. The total energy of the system would have a additional Columbic interaction between all Nuclei, for the given nuclear arrangement it is a fixed constant added onto the three terms which all dynamically depends on the trjectory of the electrons.

---

The above formulation shows how the energy of a polyelectronic system is obtained from provided the MOs.

The MOs are obtained in this way.
The variation theorem states the *ground state* electronic configuration of a system will be an energy minimum. We have an expression of energy in terms of the MOs, we can find the MOs that minimises the energy with the additional requirement that MOs need to be orthonormal. This is a constraint minimisation problem. The Hatree-Fock formulation transforms this optimisation problem into the following format:

 f̂ Φ = ϵ Φ  

 This very Schrondinger-like equation says the wavefunction of a molecular orbital where a electron resides acted upon by the Fock operator (on the left) equals the same wavefunction multiplied by a constant. The Fock operator encompasses the three energy contribution terms alluded to above. As you can see, the Fock opertor is a function of the MOs for all the other electrons in the system. No analytical solution exists for this. The numerical solution involves starting with an initial guess for the set of MOs and use them to obtain the Fock operators. Using the derived Fock operators, a better approximation of the MO wavefunctions can then be obtained, which are again plugged in to obtain a new set of Fock operators. This iterative process continuous until some convergence condition is met. This is called the **self-consistent field** approach.  

Two levels of simplifications are added to the HF formulation to reduce the search space.

Firstly, molecular orbitals are constructed by weighted combinations of atomic orbitals(obtained from solving for the hydrogen atom), abbreviated as LCAO:

Φ = ∑ c_i * φ_i

The set of atomic orbitals chosen to become the molecular orbitals are referred to as the **basis set**. Combinations of N atomic orbitals yields N molecular orbitals, which do not necessarily need to be occupied by electrons. The difference between these molecular orbitals are therefore only in the coefficients "c_i" terms in front of the atomic orbitals.

Secondly, Slater type orbitals (STO) simplifies the radial part of atomic orbital wavefuntions. Such simplification contains an empirical coefficient which is estimated by the Slater Rules. Finding the solution becomes getting the "c_i"s that minimises the energy for each and every molecular orbital.
