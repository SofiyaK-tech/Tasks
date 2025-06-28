def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    n = len(merged)

    if n % 2 == 0:  
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        return (mid1 + mid2) / 2
    else: 
        return merged[n // 2]

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

median = find_median_sorted_arrays(list1, list2)
print(f"The median is: {median}")

list3 = [1, 2, 3]
list4 = [4, 5]

median2 = find_median_sorted_arrays(list3, list4)
print(f"The median is: {median2}")