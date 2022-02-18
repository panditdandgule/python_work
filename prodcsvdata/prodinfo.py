import csv

with open("products.csv",'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['pid','pname','price','qty'])
    n=int(input("Enter Number of products: "))
    for prod in range(n):
        pid=int(input("Enter product id: "))
        pname=input("Enter product name")
        price=int(input("Enter product price: "))
        qty=int(input("Enter product quantity:"))
        w.writerow([pid,pname,price,qty])
    print("Data written successfully")