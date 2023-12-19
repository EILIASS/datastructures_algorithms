def bubble_sort(nums):
    # Create a copy of the list to avoid changing the original
    nums = list(nums)
    
    # Repeat the process n-1 times
    for _ in range(len(nums) - 1):
        # Iterate over the array (except the last element)
        for i in range(len(nums) - 1):
            # Compare the numbers
            if nums[i] > nums[i+1]:
                # Swap the two elements
                nums[i], nums[i+1] = nums[i+1], nums[i]
    
    # Return the sorted list
    return nums

# Test avec l'exemple fourni
test_input = [4, 2, 6, 3, 4, 6, 2, 1]
expected_output = [1, 2, 2, 3, 4, 4, 6, 6]

print('Input:', test_input)
print('Expected output:', expected_output)

result = bubble_sort(test_input)
print('Actual output:', result)

# Vérifiez si le résultat correspond à la sortie attendue
print('Match:', result == expected_output)

print(result == expected_output)

# Insertion Sort

def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums  

test_input1 = [4, 2, 6, 3, 4, 6, 2, 1]
expected_output1 = [1, 2, 2, 3, 4, 4, 6, 6]

print('Input:', test_input1)
print('Expected output:', expected_output1)
result1 = insertion_sort(test_input1)
print('Actual output:', result1)
print('Match:', result1 == expected_output1)


def merge_sort(nums):
    # Terminating condition (list of 0 or 1 elements)
    if len(nums) <= 1:
        return nums
    
    # Get the midpoint
    mid = len(nums) // 2
    
    # Split the list into two halves
    left = nums[:mid]
    right = nums[mid:]
    
    # Solve the problem for each half recursively
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    
    # Combine the results of the two halves
    sorted_nums =  merge(left_sorted, right_sorted)
    
    return sorted_nums

def merge(nums1, nums2, depth=0):
    print('  '*depth, 'merge:', nums1, nums2)
    i, j, merged = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]
        
def merge_sort(nums, depth=0):
    print('  '*depth, 'merge_sort:', nums)
    if len(nums) < 2: 
        return nums
    mid = len(nums) // 2
    return merge(merge_sort(nums[:mid], depth+1), 
                 merge_sort(nums[mid:], depth+1), 
                 depth+1)

test_input1 = expected_output2 = merge_sort([5, -12, 2, 6, 1, 23, 7, 7, -12])

print('Input:', test_input1)
print('Expected output:', expected_output2)
result2 = merge_sort(test_input1)
print('Actual output:', result2)
print('Match:', result2 == expected_output2)

def quicksort(nums, start=0, end=None):
    # print('quicksort', nums, start, end)
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    
    if start < end:
        pivot = partition(nums, start, end)
        quicksort(nums, start, pivot-1)
        quicksort(nums, pivot+1, end)

    return nums

def partition(nums, start=0, end=None):
    # print('partition', nums, start, end)
    if end is None:
        end = len(nums) - 1
    
    # Initialize right and left pointers
    l, r = start, end-1
    
    # Iterate while they're apart
    while r > l:
        # print('  ', nums, l, r)
        # Increment left pointer if number is less or equal to pivot
        if nums[l] <= nums[end]:
            l += 1
        
        # Decrement right pointer if number is greater than pivot
        elif nums[r] > nums[end]:
            r -= 1
        
        # Two out-of-place elements found, swap them
        else:
            nums[l], nums[r] = nums[r], nums[l]
    # print('  ', nums, l, r)
    # Place the pivot between the two parts
    if nums[l] > nums[end]:
        nums[l], nums[end] = nums[end], nums[l]
        return l
    else:
        return end
    
l1 = [1, 5, 6, 2, 0, 11, 3]
pivot = partition(l1)
print(l1, pivot)

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)
    
nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

print(notebooks)

def compare_likes(nb1, nb2):
    if nb1.likes > nb2.likes:
        return 'lesser'
    elif nb1.likes == nb2.likes:
        return 'equal'
    elif nb1.likes < nb2.likes:
        return 'greater'
    
def default_compare(x, y):
    if x < y:
        return 'less'
    elif x == y:
        return 'equal'
    else:
        return 'greater'

def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare), 
                 merge_sort(objs[mid:], compare), 
                 compare)

def merge(left, right, compare):
    i, j, merged = 0, 0, []
    while i < len(left) and j < len(right):
        result = compare(left[i], right[j])
        if result == 'lesser' or result == 'equal':
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]
sorted_notebooks = merge_sort(notebooks, compare_likes)

print(sorted_notebooks)


def compare_titles(nb1, nb2):
    if nb1.title < nb2.title:
        return 'lesser'
    elif nb1.title == nb2.title:
        return 'equal'
    elif nb1.title > nb2.title:
        return 'greater'
def merge_sort(objs, compare=default_compare):
    if len(objs) < 2:
        return objs
    mid = len(objs) // 2
    return merge(merge_sort(objs[:mid], compare), 
                merge_sort(objs[mid:], compare), 
                compare)

print(merge_sort(notebooks, compare_titles))
