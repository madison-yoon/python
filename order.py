file_name = "order.txt"

product_list = []
ea_list = []
price_list = []


with open(file_name, 'r', encoding="utf-8") as file:
    header = file.readline().strip().split(",")
    for e in file:
        produst_list = e.strip().split(",")
        ea, price = map(int, [produst_list[1], produst_list[2].replace("원", "")])
        if 0 < price < 10000 and 0 < ea:
            product_list.append(produst_list[0])
            ea_list.append(ea)
            price_list.append(price)


print("정제 후 데이터")
print(product_list)
print(ea_list)
print(price_list)
print()
print()

def total_sales_func():
    total_sales = 0
    print("----------------------------")
    for i in range(len(product_list)):
        ea_total = ea_list[i] * price_list[i]
        total_sales += ea_list[i] * price_list[i]
        print(f"{product_list[i]} {ea_list[i]}잔 총 {ea_total}원")
    print(f"전체 매출 : {total_sales}원")
    print("----------------------------")
total_sales_func()