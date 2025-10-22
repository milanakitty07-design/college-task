# Задания от 24 сентября
# Студентка: Милана Каратеева
# Колледж: Алматинский экономический колледж, группа Web-3-5

# 1
print("#1")
lst = list(range(1, 11))
for i in lst:
    print(i)

# 2
print("#2")
nums = [3, 7, 2, 9, 5]
total = 0
for n in nums:
    total += n
print(total)

# 3
print("#3")
nums2 = [1, 4, 6, 9, 12, 15]
count = 0
for n in nums2:
    if n % 2 == 0:
        count += 1
print(count)

# 4
print("#4")
nums3 = [2, 8, 1, 6, 10]
max_val = nums3[0]
for n in nums3:
    if n > max_val:
        max_val = n
print(max_val)

# 5
print("#5")
nums4 = [1, 2, 3, 4, 6, 7]
found = False
for n in nums4:
    if n == 5:
        found = True
        break
print("Есть 5" if found else "Нет 5")


# 6
print("#6")
arr = [5, 2, 9, 1, 3]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(arr)

# 7
print("#7")
lst = [1, 2, 3, 4, 5]
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print(rev)

# 8
print("#8")
lst = [1, 2, 2, 3, 4, 4, 5]
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)
print(unique)

# 9
print("#9")
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
common = []
for x in a:
    if x in b:
        common.append(x)
print(common)

# 10
print("#10")
def shift_right(lst):
    if len(lst) == 0:
        return lst
    last = lst[-1]
    new_lst = [last]
    for i in range(len(lst)-1):
        new_lst.append(lst[i])
    return new_lst

print(shift_right([1, 2, 3, 4]))
