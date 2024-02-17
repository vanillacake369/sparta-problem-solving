def solution(phone_book):
    
    hashMap = {}
    for nums in phone_book: # O(N)
        hashMap[hash(nums)] = nums

    for nums in phone_book:
        arr = ""
        for num in nums:
            arr += num

            if hash(arr) in hashMap and arr != nums:
                return False
    
    return True