xNCO
====
The NetCDF Operators (NCO) written in Python using Xarray and Dask.

## Motivation

NCO has long been among the most commonly used tools in the climate scientist's toolbox. However, there are certain limitations to the original NCO library that challenge its applicability in the big-data age. A few of those challenges are:

1. Written in low-level C language which makes maintenance and development challenging
2. Unable to provide out-of-core processing
3. Parallelization is limited to OpenMP threading and not across many machines

## What is xNCO

Currently, xNCO is just meant as a proof of concept. The goal here is just to show how it is possible to reproduce the core NCO operations using Xarray and to demonstrate possible performance improvement (or lack there of) that arise by using dask for out-of-core distributed computations. It only has a small fraction of the functionality that the full NCO package has.

## LICENSE
MIT. See License.txt.
