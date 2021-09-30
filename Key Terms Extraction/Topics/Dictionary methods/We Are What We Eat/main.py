# the list "meals" is already defined
# your code here
out = 0
for meal in meals:
    out += int(meal.get("kcal"))
print(out)
