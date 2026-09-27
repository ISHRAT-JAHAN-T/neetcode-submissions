class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Step 1: Count characters in s1
        s1_count = {}

        for char in s1:
            if char not in s1_count:
                s1_count[char] = 1
            else:
                s1_count[char] += 1

        # Step 2: Count first window of s2
        window = {}

        for i in range(len(s1)):
            char = s2[i]

            if char not in window:
                window[char] = 1
            else:
                window[char] += 1

        # Step 3: Check first window
        if window == s1_count:
            return True

        # Step 4: Slide the window
        left = 0

        for right in range(len(s1), len(s2)):

            # Add new character from right
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Remove old character from left
            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1

            # Check if counts match
            if window == s1_count:
                return True

        return False
        