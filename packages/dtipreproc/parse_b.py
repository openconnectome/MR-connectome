#!/usr/bin/env python

# Copyright 2015 Open Connectome Project (http://openconnecto.me)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# b_format.py
# Created by Greg Kiar on 2015-05-07.
# Email: gkiar@jhu.edu
# Copyright (c) 2015. All rights reserved.



from argparse import ArgumentParser
from numpy import where, loadtxt, savetxt
import numpy as np
from os import system

def read_bvals(b_in):
	"""
	Parses b-values files provided by the scanner.
	
	The b-values received from the scanner indicate both the field intensity during the DTI scanning process as well as the index of the B0 volume. This function identifies both of these values.
	
	**Positional Arguments**
	
			B-values: [.b; ASCII file]
					- Ordered list of b-values from the scanner
	
	**Returns**
	
			B0 Index: [int]
					- Location of the first B0 volume
			B: [int]
					- Field intensity
			Multiple B0s: [int]
					- Acts as a flag indicating whether multiple B0 scans exist within the set.
	"""
	b = loadtxt(b_in)
	loc = where(b==0)
	if np.array(loc).size:
		b0 = int(loc[0][0])
	else:
		b0 = int(where(b==min(b))[0][0])
  
	bvalue = int(b[where(b!=0)[0][0]])
	lenb =  len(where(b==0)[0])
	if lenb > 1:
		lenb = 2
	else :
		lenb = 1

	system("echo 'b0=("+str(b0)+")'")
	system("echo 'First bvalue=("+str(bvalue)+")'")
	system("echo 'Multiple B0s (1=no; 2=yes)=("+str(lenb)+")'")

def format_bvec(b_in, b_out):	
	"""
	Parses b-vectors (or, gradient direction)  provided by the scanner.
	
	B-vectors can be provided in slightly different formats from different scanners, and this module parses them to ensure that downstream functions correctly perceive the information provided.
	
	**Positional Arguments**
	
			B-vectors: [(bvec), .grad; ASCII file]
					- Gradient directions of scanner corresponding to the b-values

	**Returns**

			Gradients: [(bvec); ASCII file]
					- Reformatted B-vectors file which is compatible with downstream processing algorithms
	"""
	b = loadtxt(b_in)
	if b.shape[1] < b.shape[0]:
		b = b.T
	savetxt(b_out, b,  fmt='%.18f')

def main():
  parser = ArgumentParser(description="")
  parser.add_argument("bval", action="store", help="The b-value file corresponding to the DTI image (.bval, .b)")
  parser.add_argument("bvec", action="store", help="The b-vector/gradient file corresponding to the DTI image (.bvec, .grad)")
  parser.add_argument("new_bvec", action="store", help="The new b-vector/gradient file (.grad)")

  result = parser.parse_args()
  read_bvals(result.bval)
  format_bvec(result.bvec, result.new_bvec)

if __name__ == "__main__":
    main()
