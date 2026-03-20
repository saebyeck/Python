price = int(input("상품의 가격:"))
if price > 20000:
    shipping_cost = 0
else :
    shipping_cost = 3000

print("배송비 =",shipping_cost)