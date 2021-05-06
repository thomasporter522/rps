# RPS
 
I consider generalizations of Rock, Paper, Scissors, which consist of a set of outcomes, and an irreflexive, antisymmetric, trichotomous binary relation. In other words, for each pair of distinct outcomes, a choice of which outcome wins. I only consider games without extraneous outcomes. An outcome A is extraneous if there is another outcome B such that B beats everything A beats. If an outcome is extraneous then the optimal stragey never chooses it. 

The program iterates through {0,1}-valued matrices, describing the relation. It eliminates games with extraneous outcomes, and eliminates games that are equivalent to previous found games, under permutation of outcomes. 
