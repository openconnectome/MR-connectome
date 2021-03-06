#!/usr/bin/env python

# Copyright 2014 Open Connectome Project (http://openconnecto.me)
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

# test_mrocp_inv.py
# Created by Disa Mhembere on 2013-12-31.
# Email: disa@jhu.edu

import argparse
from computation.utils.loadAdjMatrix import loadAnyMat
from computation.composite.invariants import compute
from time import time

def main():
  parser = argparse.ArgumentParser(description="Run MROCP invariants individually for timing purposes")

  parser.add_argument("gfn", action="store", help="The name of the graph on disk")
  result = parser.parse_args()

  g = loadAnyMat(result.gfn)

  begin = time()

  # TODO optimize invariants

  # Deg
  print "Individual run ...\n Processing Degree vector ..."
  b = time()
  compute({"deg":True, "G":g, "graph_fn":result.gfn}, save=False)
  print "Time for degree vector = %.4f"% (time()-b)

  # SS
  print "Processing Scan Statistic ..."
  b = time()
  compute({"ss1":True, "G":g, "graph_fn":result.gfn}, save=False)
  print "Time for scan 1 vector = %.4f"% (time()-b)

  # CC
  print "Processing Clustering Coefficient (Transitivity)"
  b = time()
  compute({"cc":True, "G":g, "graph_fn":result.gfn}, save=False)
  print "Time for Clustering Coefficient vector = %.4f"% (time()-b)

  # TRI
  b = time()
  compute({"tri":True, "G":g, "graph_fn":result.gfn}, save=False)
  print "Time for triangle vector = %.4f" % (time()-b)

  print "Total time for non-daisy-chained invariant = %.4f" % (time()-begin) # minus all the populate_invariants

  print "\n*** Daisy-chain run ... ***\n"

  begin = time()
  compute({"deg":True, "ss1":True, "cc":True, "tri":True, "G":g, "graph_fn":result.gfn}, save=False)
  print "Total time for daisy-chained invariant = %.4f" % (time()-begin) # minus all the populate_invariants

if __name__ == "__main__":
  main()