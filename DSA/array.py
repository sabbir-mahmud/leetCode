"""
1. Let us say your expense for every month are listed below,
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

"""

expenses = [2200, 2350, 2600, 2130, 2190]

print(f"extra spent compare to January --> {expenses[1] - expenses[0]}")
print(f"expense of first quarter --> ", expenses[0] + expenses[1] + expenses[2])

for i in expenses:
    if i == 2000:
        print("exactly 2000 dollars match found")
    else:
        print("exactly 2000 dollars not match")

# * Adding June month expense
expenses.append(1980)

# * Refund amount adjust with April month
expenses[3] -= 200


"""
2. You have a list of your favourite marvel super heros.
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

"""

heros = ["spider man", "thor", "hulk", "iron man", "captain america"]
print(f"Length of the list is --> {len(heros)}")

# * Add 'black panther' at the end of this list
heros.append("black panther")

# * Add 'black panther' after 'hulk'
heros.pop()
heros.insert(3, "black panther")
print(heros)

# * replace thor and hulk with doctor strange
heros[1:3] = ["doctor strange"]
print(heros)

# * Sort the heros list in alphabetical order
heros.sort()
print(heros)

"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

"""


def create_list():
    max_number = int(input("Enter number --> "))
    odds = []

    for i in range(1, max_number + 1):
        if i % 2 == 0:
            print(i)
            odds.append(i)

    print(odds)
    return


create_list()
