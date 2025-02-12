class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        # Array to store count of remainders when divided by 60
        remainder_count = [0] * 60
        count = 0

        # Iterate through the list of time (song durations)
        for t in time:
            remainder = t % 60

            # If remainder is 0, it can pair with another song with remainder 0
            if remainder == 0:
                count += remainder_count[0]
            else:
                # It can pair with remainder (60 - remainder)
                count += remainder_count[60 - remainder]

            # Increment the count of the current remainder
            remainder_count[remainder] += 1

        return count

# Example usage:
songs = [40, 20, 60]
solution = Solution()
print(solution.numPairsDivisibleBy60(songs))  # Output: 1

        
