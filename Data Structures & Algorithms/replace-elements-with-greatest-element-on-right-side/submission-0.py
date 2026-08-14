class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        output = [0] * length
        output[length - 1] = -1
        for i in range(length - 1): 
            current_max = -1
            for j in range(i + 1, length):
                if arr[j] > current_max:
                    current_max = arr[j]
            output[i] = current_max
        return output
