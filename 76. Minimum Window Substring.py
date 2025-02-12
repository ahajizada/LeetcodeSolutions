from collections import Counter

class Solution(object):
    def minWindow(sself,s,t):
        if not s or not t:
            return ""
        
        # Frequency map of characters in t
        required = Counter(t)
        
        # Initialize pointers and data structures
        left, right = 0, 0
        formed = 0  # Counts how many unique characters satisfy their frequency requirement
        window_counts = {}
        min_length = float('inf')
        start_index = 0

        # Number of unique characters in t
        required_count = len(required)
        
        while right < len(s):
            # Add the current character to the window
            curr_char = s[right]
            window_counts[curr_char] = 1 + window_counts.get(curr_char, 0)

            # If the current character satisfies the frequency requirement
            if curr_char in required and window_counts[curr_char] == required[curr_char]:
                formed += 1

            # Try to shrink the window while it is valid
            while formed == required_count:
                # Update the minimum window size
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    start_index = left

                # Shrink the window
                char_to_remove = s[left]
                window_counts[char_to_remove] -= 1

                # If the character is in t and no longer satisfies the frequency requirement
                if char_to_remove in required and window_counts[char_to_remove] < required[char_to_remove]:
                    formed -= 1

                left += 1  # Move the left pointer

            # Expand the window
            right += 1

        # Return the minimum window substring or an empty string if no valid window exists
        return s[start_index:start_index + min_length] if min_length != float('inf') else ""
