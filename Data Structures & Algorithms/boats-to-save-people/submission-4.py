class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        people_sort = sorted(people)
        l, r = 0, len(people_sort) - 1
        num_of_boats = 0
        while l <= r:
            sum = people_sort[l] + people_sort[r]
            if sum <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            num_of_boats += 1
        return num_of_boats
