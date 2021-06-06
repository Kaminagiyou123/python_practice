import re
email='jose@gmail.com'
parts=email.split("@")
name=parts[0]
domain=parts[1]


price="Price: $189,989.50"
expression="Price: \$([0-9,]+\.[0-9])"
matches=re.search(expression,price)


print(matches.group(0))
print(matches.group(1))
price_without_comma=matches.group(1).replace(',','')
price_number=float(price_without_comma)
print(price_number)