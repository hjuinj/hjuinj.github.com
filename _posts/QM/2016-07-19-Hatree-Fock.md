---
title: "Hatree-Fock Notes"
layout: post
category : Scholastic
time : 23/07/2016
icon : psi
tags :
  - readings
  - notes
  - physics
  - chemistry
---
In computaional chemistry, the wavefunction of the entire molecular system is a function of all its electronic and nuclear coordinates. Due to the Born–Oppenheimer approximation, electronic and nuclear motion can be separated. This means, for a stationary frame of nuclear coordinates, the total wavefunction is the product of a wavefunction of the electronic coordinates multiplied by constant.The following mention of wavefunction will refer to this electronic wavefunction.

The wavefunction of the molecule is approximated by the product of individual **molecular orbital (MO) wavefunction** - a function of only one electron within the molecule. Thus a N-electron system will have N (filled) molecular orbitals:

<div style="text-align:center">
<b> Φ(n = 1,2,3....) </b> = ∏ Φ_n
</div>

In the Slater determinant, each element is a molecular orbital wavefunction. It is made up of all the molecular orbitals that are occupied by electrons. Hence for a N-electron system the determinant is NxN in dimension. The ith row is all the N possible wavefunctions the ith electron could reside in (can be the same MO, since each orbital accommodates two electrons).

The total energy Hamiltonian of a polyelectronic system can be split and attributed to three separable parts:
1. Each electron has its own kinetic and potential energy that depends on all the nuclei in the system. This is the **H_ii** part where "ii" means it is due to the same electron. (think of the Hamiltonian operator, where the potential energy part is made up of the summation of all the electrostatic potential from each nucleus)
2. Each *pair* of electrons experience electrostatic repulsion due to each other, denoted as **J_ij** where "ij" means it is interaction between different electrons.
3. Energy arising from spin correlation, or exchange interaction. Electron cannot reside in the same orbital if they have parallel spins. When two electrons have parallel spins, they cannot be in the same MO hence electron motions are not independent (that is even without considering part(2)). This is denoted **K_ij**, which is only non-zero when i and j have the same spin.

For a system of N electrons, there is N * **H_ii**. There are N*(N-1) * **J_ij**, similarly for **K_ij**, but some of these terms would be zero. Thus the energy Hamiltonian of the electronic wavefunction is the summation of these three terms. Bear in mind the total energy of the system would have an additional Columbic repulsion between all the nuclei, for the given nuclear arrangement it is a fixed constant added onto the three terms which all dynamically depends on the trajectory of the electrons.

---

The above formulation shows how the energy of a polyelectronic system is obtained when provided the MOs.

The MOs themselves are obtained in this way, using Hatree-Fock formulism.

The variation theorem states the energy of the **ground state** electronic configuration of a system will be at an minimum. Above, we have an expression of energy in terms of the MOs (Hamiltonian times wavefunction), we can find the MOs that minimises the energy with the additional requirement that MOs need to be orthonormal. This is a constraint minimisation problem. The Hatree-Fock formulation transforms this optimisation problem into the following format:

<div style="text-align:center">
 f̂ Φ = ϵ Φ  
 </div>

 This very Schrondinger-like equation says the molecular orbital wavefunction for a given electron acted upon by the Fock operator (the left-most symbol) equals the same wavefunction multiplied by a constant. The Fock operator encompasses the three energy contribution terms alluded to above. As you can see, the Fock opertor is a function of all the other MOs in the system. No analytical solution exists for this formulation. An iterative solution exists: the numerical solution involves starting with an initial guess for the set of MOs to describe all the electron and use them to obtain the Fock operators. Next, using the determined Fock operator, a better approximation of the MO wavefunctions can then be obtained, which are plugged back into obtain a new set of Fock operators. This iterative process continuous until some convergence condition is met. This is called the **self-consistent field** approach.  

---

Two levels of simplifications are added to the HF formulation to reduce the search space:

Firstly, each MO is constructed by a weighted combinations of atomic orbitals(obtained from solving for the hydrogen atom), abbreviated as LCAO:

<div style="text-align:center">
Φ = ∑ c_i * φ_i
</div>

The set of atomic orbitals being combined to become the molecular orbitals are referred to as the **basis set**. Combinations of M atomic orbitals yields M molecular orbitals, which *do not* necessarily need to be occupied by electrons. This means the functional form of the atomic orbitals would stay the same for every MO, the only difference is therefore only in the coefficients "c_i" terms in front of each atomic orbitals.

Secondly, Slater type orbitals (STO) simplifies the radial part of atomic orbital wavefuntions. Such simplification contains an empirical coefficient which is estimated by the Slater Rules.

To reformulate for the last time, obtaining MOs for a given molecular system becomes finding the "c_i"s that minimises the energy for each and every molecular orbital.
