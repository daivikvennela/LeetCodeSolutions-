class Solution(object){
    def mergeAlternately(self, word1, word2):
    # using two different pointers tracking and appending both words by switching off 
    i , j = 0, 0 
    # using list since strings are immutable and provide ineffecient time complexity 
    s = []
    while (i < len(word1) and j < len(word2)):
        s.append(word1[i])
        s.append(word2[j])
        i += 1
        j += 2
    s.append(word1[i:]) 
    s.append(word2[j:])

    return "".join(s)
    







}