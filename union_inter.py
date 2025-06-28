def union(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1.union(set2)
    return list(union_set)

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
union_result = union(list_a, list_b)
print(f"Union: {union_result}")

def intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection_set = set1.intersection(set2) 
    return list(intersection_set)

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
intersection_result = intersection(list_a, list_b)
print(f"Intersection: {intersection_result}")