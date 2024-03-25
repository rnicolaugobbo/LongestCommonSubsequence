Simple function to find the longest common subsequence between two given strings, using dynamic programming.
This function has a runtime of 0(M * N), where M and N are the lengths of the two given strings. This is much more efficiente than a naive approach.
For a naive approach, we would need to generate every subsequence of each string and then check the longest generated subsequences to see if they match. If they don't, we need to keep checking smaller and smaller subsequences to see if they match.
The naive approach would have a runtime of 0(N ^ 2). Therefore, we greatly improved the efficiency of the algorithm using dynamic programming.
