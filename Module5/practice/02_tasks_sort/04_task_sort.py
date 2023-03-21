# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3


def sort_choice(nums, reverse=False, my_abs=False) -> None:
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                rule_sort = nums[j] > nums[m]
                if my_abs:
                    rule_sort = abs(nums[j]) > abs(nums[m])
            else:
                rule_sort = nums[j] < nums[m]
                if my_abs:
                    rule_sort = abs(nums[j]) < abs(nums[m])
            if rule_sort:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

sort_choice(numbers, True, True)

summ = 0
print(numbers)
for num in numbers[:5]:
    print(num)
    summ+=num

print(f'Сумма больших чисел по модулю {summ}')
