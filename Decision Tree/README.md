* Classification & Regression Trees
* Leaves Represent class label
* Branches reresent conjuctions
* Based on Recursive partitioning
* it is Greedy algorithm
* ID3 | C4.5 | CART | CHAID Chi-square automatic interaction detection |MARS
* CHAID - Performs multi-level splits when computing classification trees
* MARS - extends decision trees to handle numerical data better
* Algorithms for constructing decision trees usually work top-down : 
* Gini impurity | Information gain
* Gini Impurity : Used by CART  -> Measure the quality of split
   * Gini impurity is a measure of how often a randomly chosen element from the set would be incorrectly labeled 
   * If we have CC total classes and p(i) is the probability of picking a datapoint with class i, 
     then the Gini Impurity is calculated as submation [p(i)∗(1−p(i))]
* Information Gain -is based on the concept of entropy and information content from information theory.
* How can we quantify the quality of a split? describes I G
