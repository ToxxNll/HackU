class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_el = sorted(candies,reverse=True)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_el[0]:
                candies[i] = True
            else: 
                candies[i] = False
        
        return candies
    
            