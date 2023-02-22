ecfactory: A SageMath Library for Constructing Elliptic Curves
==============================================================


Overview
--------

The __ecfactory library__ is developed by the [SCIPR Lab](http://www.scipr-lab.org/) project and contributors (see [AUTHORS](AUTHORS) file) and is released under the MIT License (see [LICENSE](LICENSE) file). The library implements algorithms to construct elliptic curves with certain desired properties; specifically, it provides the following functionality.

1. [Complex Multiplication method](/ecfactory/complex_multiplication)
2. [Cocks-Pinch method](/ecfactory/cocks_pinch)
3. [Dupont-Enge-Morain method](/ecfactory/dupont_enge_morain)
4. [Solver for Pell equations](/ecfactory/pell_equation_solver)
5. [Miyaji-Nakabayashi-Takano curves](/ecfactory/mnt_curves)
6. [Barreto-Naehrig curves](/ecfactory/bn_curves)
7. [Elliptic-curve chains](/ecfactory/ec_chain) (via the Cocks-Pinch method)
8. [Elliptic-curve cycles](/ecfactory/mnt_cycles) (via MNT curves)

Each of the above is packaged as a Python module in a corresponding subfolder under the [ecfactory folder](/ecfactory).

Throughout, a curve _E_ is specified as a tuple (_q_,_t_,_r_,_k_,_D_) where:
_q_ is the prime size of the base field;
_t_ is the trace of Frobenius;
_r_ is the prime size of the subgroup (which can be the size of the entire group);
_k_ is the embedding degree; and
_D_ is the (negative) fundamental discriminant.
From the tuple (_q_,_t_,_r_,_k_,_D_), the curve equation can be found using the _Complex Multiplication method_.

Requirements
------------

The library requires a working [SageMath](http://www.sagemath.org) installation, and has been tested on SageMath version 6.8, 7.2 and 9.7.

Installation
-----------

To install, use sage pip:

	$ git clone https://github.com/scipr-lab/ecfactory.git && cd ecfactory && sage -pip install .
	
To import and use the library, write

```python
import ecfactory
```

Methods can now be invoked as

```python
ecfactory.module_name.method_name
```
	
For example,

```python
ecfactory.dupont_enge_morain.run(50,5)
```

To import only one module, write

```python
import ecfactory.module_name as other_name
```
	
Methods can now be invoked more concisely as

```python
other_name.method_name
```
	
For example,

```python
import ecfactory.dupont_enge_morain as dem
dem.run(50,5)
```

Tutorials
---------

Each subfolder contains a readme, code examples, and unit tests. The methods are described in the readme, and the code examples show how to run the relevant methods. Many of the algorithms and tests are probabilistic, and the random seed can be set using `set_random_seed(s)`.

Additionally, the `utils` module contains global functions that filter the curves found by all algorithms. See the [utils folder](ecfactory/utils) for more details.