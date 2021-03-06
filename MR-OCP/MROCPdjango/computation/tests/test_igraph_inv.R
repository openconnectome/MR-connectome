# test_igraph_inv.R
# Created by Disa Mhembere on 2013-12-31.
# Email: disa@jhu.edu
# Copyright (c) 2013. All rights reserved.

require(igraph)
require(argparse)
 
parser <- ArgumentParser(description="Run same invariants as MROCP on igraphs")
parser$add_argument("gfn", help="The graph file name")
parser$add_argument("-f", "--graph_format", default="gml", help="The graph format e.g gml, graphml, pajek, dot etc..")
 
result <- parser$parse_args()
 
if (!file.exists(result$gfn)){
    stop(paste("File", result$gfn, "does not exist!!\n"))
}

g <- igraph::read.graph(result$gfn, format=result$graph_format) # Throws an exception if the graph format is unknown

begin <- proc.time()[3] 

# Degree
cat("Processing Degree Vector...\n")
system.time( igraph::degree(g, mode="total") )

# Scan Stat 1
cat("Processing Scan Statistic...\n")
system.time( igraph::scan1(g) )

# Clustering Coefficient
cat("Processing Transitivity (i.e. Clustering Coefficient) ...\n")
system.time( igraph::transitivity(g, "local") )

# Triangles
cat("Processing Triangle count ...\n")
system.time( igraph::adjacent.triangles(g) )

# Eigendecomposition
cat("Spectral decomposition ...\n")
if (igraph::vcount(g) >= 102){
  eigs <- 100
} else {
  eigs <- igraph::vcount(g)-2
}

system.time( igraph::adjacency.spectral.embedding(g, eigs ))

cat("Total time for the 5 invariants = ", (proc.time()[3]-begin), " ...\n")
