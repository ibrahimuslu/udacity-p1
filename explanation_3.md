I would like to emphasize that the most educative problem is this one. I really enjoyed while trying to solve this. I have used almost all data structures learned in this problem
1. The complexity analysis of Huffman Encoding 
    - encoding algorithm is starting with creating a huffman tree. The tree algorithm has O(n) complexity
    after that the algorithm is going through each char in the given string and finds the binary representation of huffman code so it O(n*n/2) because max depth of huffman tree is n/2
    - decoding algorithm need the huffman tree created before and so no need to create again but decoding still needs to loop over the string given and need loop over the tree so it is O(n*n/2)
2. space complexity analysis of Huffman algorithm
    - tree queue used for the algorithm. A(n)