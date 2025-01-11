"""
Exercise: Array DataStructure
    Let us say your expense for every month are listed below,
    January - 2200
    February - 2350
    March - 2600
    April - 2130
    May - 2190
    Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this


    You have a list of your favourite marvel super heros.
    heros=['spider man','thor','hulk','iron man','captain america']
    Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
    so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
    Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

    Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

"""

# Exercise 01: Monthly Expenses

monthly_expenses = [2200, 2350, 2600, 2130, 2190]

# 1. Extra dollars spent in February compared to January
extra_feb = monthly_expenses[1] - monthly_expenses[0]
print(f"Extra spent in Feb compared to Jan: {extra_feb} dollars")

# 2. Total expenses in the first quarter (Jan-Mar)
q1_expenses = sum(monthly_expenses[:3])
print(f"Total expenses in Q1: {q1_expenses} dollars")

# 3. Check if exactly $2000 was spent in any month
if 2000 in monthly_expenses:
    print("Found a month with exactly $2000 spent")
else:
    print("No month with exactly $2000 spent")

# 4. Add June expenses of $1980
monthly_expenses.append(1980)
print(f"Expenses after adding June: {monthly_expenses}")

# 5. Refund of $200 for an April purchase
monthly_expenses[3] -= 200
print(f"Expenses after April refund: {monthly_expenses}")

# Exercise 02: Heroes List

heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# 1. Length of the heroes list
print(f"Number of heroes: {len(heroes)}")

# 2. Add 'black panther' at the end of the list
heroes.append("black panther")
print(f"Heroes after adding 'black panther': {heroes}")

# 3. Move 'black panther' to be after 'hulk'
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(f"Heroes after rearranging: {heroes}")

# 4. Replace 'thor' and 'hulk' with 'doctor strange'
heroes[1:3] = ["doctor strange"]
print(f"Heroes after replacement: {heroes}")

# 5. Sort the heroes alphabetically
heroes.sort()
print(f"Heroes sorted alphabetically: {heroes}")

# Exercise 03: Odd Numbers List

# Generate a list of odd numbers up to a user-defined maximum
max_num = int(input("Enter the max number: "))
odd_numbers = [i for i in range(1, max_num + 1) if i % 2 != 0]
print(f"Odd numbers up to {max_num}: {odd_numbers}")
