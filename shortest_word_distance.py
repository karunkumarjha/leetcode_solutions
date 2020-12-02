"""
Problem Link: https://leetcode.com/problems/shortest-word-distance/
"""

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_indices = []
        word2_indices = []
        
        for index, word in enumerate(words):
            if word == word1:
                word1_indices.append(index)
            elif word == word2:
                word2_indices.append(index)
        
        if len(word1_indices)< len(word2_indices):
            shorter_array = word1_indices
            longer_array = word2_indices
        else:
            shorter_array = word2_indices
            longer_array = word1_indices
            
        return shortestDistanceHelper(shorter_array, longer_array)        
        
def shortestDistanceHelper(shorter_array, longer_array):
    min_distance = float('inf')
    
    for index in shorter_array:
        left, right = 0, len(longer_array)-1
        current_distance = float('inf')
        
        while left<=right:
            mid = left + (right-left)//2
            current_distance = min(current_distance, abs(longer_array[mid] - index))
            if index>longer_array[mid]:
                left = mid+1
            else:
                right = mid-1
                
        min_distance = min(min_distance, current_distance)
            
    return min_distance