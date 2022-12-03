class Solution:
    def frequencySort(self, s: str) -> str:
        
        ans_str = ''
        # Find unique characters
        characters = set(s)
        
        counts = []
        # Count their frequency
        for i in characters:
            counts.append([i,s.count(i)])
        
		# Sort characters according to their frequency
        counts = sorted(counts, key= lambda x: x[1], reverse = True)
        
		# Generate answer string by multiplying frequency count with the character
        for i,j in counts:
            ans_str += i*j
        
        return ans_str