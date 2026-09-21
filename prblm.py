#Part B - Fill in the blanks
sales = [250, 480, 120]

for sale in sales:
    print(sale)

sales = [250, 480, 120, 700]
big_count = 0

for sale in sales:
    if sale > 400:
        big_count = big_count + 1

print("Big sales:", big_count)


def sale_size(amount):
    if amount >= 400:
        return "Big Sale"
    elif amount > 200:
        return "Normal sale"
    else:
        return "Small sale"


print(sale_size(700))
print(sale_size(250))
print(sale_size(90))


def bill_amount(price, quantity):
    return price * quantity


print(bill_amount(120, 3))

#C1:
# Shop Details
shop = {
    "name" : "Everest Snacks",
    "owner" : "Asha",
    "opened_date" : 2019,
    "daily_rent" : 850.5
}
print(shop["opened_date"])
print(shop["daily_rent"])
print(shop["name"])
shop["flour_price"] = "120"
print(shop)
shop["flour_price"] = int(shop["flour_price"]) + 30
print(shop)

#c2:

sales = [250, 480, 120, 700, 350, 480, 90]
count = 0
for sale in sales:
    count = count + 1
print("Numbers of sales:", count)
total = sum(sales)
print("Total sales:", total)
print("Average:", total/len(sales))
print("Minimum sales:", min(sales))
print("Maximum sales:", max(sales))

print("First sales:", sales[0:3])
print("Last sales:", sales[-1])

sales.append(300)

print("Sales after one new sale", sales)

# sales = [250, 480, 120, 700, 350, 480, 90, 300]

sales.remove(480)

print("Sales after 480 cancel:", sales)

#c3 - Label every sale
big_count = 0
for sale in sales:
    if sale >= 400:
        print("Big Sale")
        big_count = big_count + 1
    elif sale >200:
        print("Normal Sale")
    else:
        print("Small Sale")
print("Total big sales:", big_count)


#C4 - Use your functions
bill_amount_c1 = bill_amount(3, 120)
bill_amount_c2 = bill_amount(2,250)
print(bill_amount_c1)
print(bill_amount_c2)
print(sale_size(bill_amount_c1))
print(sale_size(bill_amount_c2))


#c5 - Customer records

customer = [
    {"name" : "Asha", "item" : "Momo", "amount" : 250},
    {"name" : "Bikash", "item" : "Chowmein", "amount":480},
    {"name" : "Nima", "item" : "Tea", "amount" : 90},
    {"name" : "Sita", "item" : "Momo", "amount" : 700}
]

print(customer[0]["name"], "bought", customer[0]["item"], "for", customer[0]["amount"],".")

total_collected = 0
count_customer = 0

for i in customer:
    total_collected = total_collected + i["amount"]
    if i["amount"] >= 400:
        count_customer = count_customer + 1
print("Total collected money:", total_collected)
print("Big customer: ",count_customer)

#C6 - Location and menu
location = (27.7172, 85.3240)
print(location[0:1])

count_item = 0
item_bought = {"Momo", "Chowmein", "Tea", "Momo"}
for i in item_bought:
    count_item = count_item + 1
print("Different items sold:", count_item)
