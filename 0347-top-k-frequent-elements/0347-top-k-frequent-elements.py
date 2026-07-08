class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        # Step 1: Har number ki frequency count karo
        for item in nums:
            freq[item] = freq.get(item, 0) + 1

        # Step 2: Frequency ke according sort karo
        sorted_items = sorted(freq, key=freq.get, reverse=True)

        # Step 3: Top k elements return karo
        return sorted_items[:k]