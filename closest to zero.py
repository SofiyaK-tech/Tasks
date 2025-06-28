def find_closest_sum_to_zero(numbers):  
    if len(numbers) < 2:
        return None

    numbers.sort()  
    left = 0
    right = len(numbers) - 1
    min_sum = float('inf')  
    result_pair = (None, None)

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result_pair = (numbers[left], numbers[right])

        if current_sum < 0:
            left += 1  
        elif current_sum > 0:
            right -= 1  
        else:
            
            return (numbers[left], numbers[right])

    return result_pair

a = [1, 60, -10, 70, -80, 85]
pair = find_closest_sum_to_zero(a)
if pair:
    print(f"The two elements whose sum is closest to zero are: {pair[0]} and {pair[1]}")
else:
    print("The list must contain at least two elements.")

b = [-5, -2, 1, 3, 7]
pair_2 = find_closest_sum_to_zero(b)
if pair_2:
    print(f"The two elements whose sum is closest to zero are: {pair_2[0]} and {pair_2[1]}")
else:
    print("The list must contain at least two elements.")
