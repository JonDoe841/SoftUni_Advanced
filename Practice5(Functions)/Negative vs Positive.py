def nums_sums(*args):
    n_nums = sum(num for num in args if num < 0)
    p_nums = sum(num for num in args if num > 0)

    return n_nums, p_nums

nums = map(int, input().split())
neg_sum, p_sum = nums_sums(*nums)
print(neg_sum)
print(p_sum)
if abs(neg_sum) > p_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")