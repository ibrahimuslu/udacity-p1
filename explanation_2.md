1. Time complexity analysis of finding files in a directory
    - If we take n as the directory number parameter then the complexity is n times(*) - since the algorithm visits every directory once and because of using systems find function omitting that - max depth(md) of the folders and the all file number(fn) of whole folders so it is sth O(n*md*fd)
2. Space complexity analysis of finding files in a directory
    - the max depth of the recursion and the found files name size A(nd)
