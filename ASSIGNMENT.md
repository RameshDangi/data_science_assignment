# First week ending assignment

For problems 1 to 10, discuss what you would use. Some need more than one.

1. Print every sale amount in today's list.
2. Show `Free delivery` when the bill is 1000 or more, and `Delivery charge` otherwise.
3. You need the same big / normal / small rule in three different programs.
4. Print each of the 7 sales together with its label.
5. Count how many sales were above 400.
6. Given one amount, give back its label.
7. Print the numbers 1 to 10.
8. Add 13 percent VAT to any price.
9. Print a pass or fail line for all 30 students in a class.
10. Decide whether one student with 38 marks passed.

For problems 11 to 18, write which of a list, a tuple, a dictionary or a set you would use.

11. Today's seven sale amounts.
12. The latitude and longitude of the shop.
13. One customer's name, item and amount.
14. The different items sold today, ignoring repeats.
15. The names of all students in your class, in roll number order.
16. The twelve month names.
17. One student's name, roll number, marks and course.
18. The cities your customers came from, when you only want to know how many different cities.

Commit: `Add Part A answers`

## Part B - Fill in the blanks

The shop's rule: a sale of 400 or more is a big sale, 200 to 399 is a normal sale, and below 200 is a small sale.

Copy each block into your file and replace every `____`. Run it and check the output.

**B1**

```python
sales = [250, 480, 120]

for sale in ____:
    print(____)
```


Output: `250`, `480`, `120`

**B2**

```python
sales = [250, 480, 120, 700]
big_count = 0

for sale in sales:
    if ____:
        big_count = ____

print("Big sales:", big_count)
```

Output: `Big sales: 2`

**B3**

```python
def sale_size(amount):
    if amount >= 400:
        return ____
    elif ____:
        return "Normal sale"
    else:
        return ____


print(sale_size(700))
print(sale_size(250))
print(sale_size(90))
```

Output: `Big sale`, `Normal sale`, `Small sale`

**B4**

```python
def bill_amount(price, quantity):
    return ____


print(bill_amount(120, 3))
```

Output: `360`

Commit: `Fill in the blanks`

## Part C - Write it yourself

Commit after each problem: `Add C1`, `Add C2`, and so on.

**C1 - Shop details**

The shop is called Everest Snacks. The owner is Asha. It opened in 2019. The daily rent is 850.5 rupees. It is open today. Store each fact in its own well-named variable and print them.

Print the type of the opening year, the daily rent and the shop name.

Your supplier sent today's flour price as `"120"`. The price is going up by 30, but you cannot add 30 to text. Fix the value and print the new price.

**C2 - Today's sales**

Today's seven sales were 250, 480, 120, 700, 350, 480 and 90 rupees. Keep them together in one list.

Print how many sales there were, the total, the smallest, the largest and the average.

The morning shift was the first three sales. Print only those. Print the last sale without counting the positions yourself.

Then two corrections arrive. A customer paid 300 after closing time. One 480 sale was cancelled. Update the list, then print the list and the new total.

**C3 - Label every sale**

Using the shop's rule from Part B, go through your updated list and print every sale with its label. Do not write seven separate print lines.

Count how many big sales there were and print the count.

**C4 - Use your functions**

Use `sale_size` and `bill_amount` from Part B for two customers. One buys 3 plates at 120 rupees each. One buys 2 plates at 250 rupees each. Print each bill with its label.

**C5 - Customer records**

Store each customer as a record with a name, an item and an amount. Today's customers were Asha with momo for 250, Bikash with chowmein for 480, Nima with tea for 90, and Sita with momo for 700. Keep all four records in one list.

Print a sentence for each customer, such as `Asha bought Momo for 250`.

While you go through them, add up the total collected and count the customers who paid 400 or more. Print both.

**C6 - Location and menu**

The shop location is 27.7172 and 85.3240. This never changes, so store it in a way that cannot be changed by mistake. Print the first number.

Two customers bought the same item today. Store the four item names in a way that keeps only the different ones, and print how many different items you sold.

## Check your answers

- Total 2470, smallest 90, largest 700, average 352.857...
- Updated list `[250, 120, 700, 350, 480, 90, 300]`, new total 2290
- Big sales today: 2
- Bills 360 (Normal sale) and 500 (Big sale)
- Total collected 1520, big customers 2
- Different items sold: 3
