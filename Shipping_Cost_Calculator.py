#Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter package weight in kgs: "))
rate = float(input("Enter shipping rate per kgs: "))

## Calculate shipping cost
shipping_cost = weight*rate

## Display result
print(f"Shipping cost: ${shipping_cost}")
