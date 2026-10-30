list_spending = [1200, 3600, 2100, 800, 2300, 1000, 8600]

sum_spending = sum(list_spending)
avg_spending = sum_spending / len(list_spending)

spending_tuple = (min(list_spending), max(list_spending), sum_spending)

print(spending_tuple)
print(avg_spending)