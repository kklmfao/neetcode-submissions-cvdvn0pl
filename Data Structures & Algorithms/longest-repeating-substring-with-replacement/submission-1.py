class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_window = 0
        l, r = 0, 0
        n = len(s)
        hash_map = {}
        l_changed, r_changed = False, True

        while r < n:
            right_char = s[r] # Getting the current char the right pointer is pointing at
            left_char = s[l] # Getting the current char the left pointer is pointing at
            current_substr_len = r - l + 1 # Calculate the current substr length bounded by the 2 pointers

            if r_changed: # Add a check if the last loop the r is pointing at the same or not, If not same update the map
                if right_char in hash_map: # Check if the char is already in the hashmap or not, If yes just increment it
                    hash_map[right_char] += 1
                else: # If not create an entry and set the count as 1
                    hash_map[right_char] = 1

            # Check how many chars we need to replace in order to create a repeating character substr
            # And we are always replacing all other chars with the most frequent chars appeared in the substr
            most_char, most_count = None, -1
            for c, cnt in hash_map.items(): # O(24) for worst case, since we only got 24 uppercase english characters
                if cnt > most_count:
                    most_count = cnt
                    most_char = c

            # No. of chars need to be replaced = substr len - frequency of the most frequent char
            no_of_chars_to_be_replaced = current_substr_len - most_count
            print(f"Replace Cnt in Substr({l},{r}): {no_of_chars_to_be_replaced}. Most frequent char: {most_char}({most_count}). Curr window length: {current_substr_len}. Max: {max_window}")

            # Check if it exceeds our k or not. 
            if no_of_chars_to_be_replaced > k: # If yes, we shrink the window
                hash_map[left_char] -= 1 # Decrement the count of the left pointer pointed char 
                                         # since we are going to shrink the window by moving the left pointer to the right by one
                                         # So the char is excluded from the window

                if hash_map[left_char] == 0: # Optional: Remove the entry of chars that count is equal to 0 from hashmap
                    del hash_map[left_char]
                
                l += 1

                l_changed = True
                r_changed = False
            else: # If not, we save the current substr length and continue searching
                max_window = max(current_substr_len, max_window)
                r += 1

                l_changed = False
                r_changed = True

        return max_window