import sys

productlist=[]
productdict={}

def take_user_inputs():
    pid = int(input('Enter Product Id : '))
    pnam = str(input('Enter Product Name : '))
    pqty = int(input('Enter Product Qty : '))
    prc = float(input('Enter Product Price : '))
    return (pid,pnam,pqty,prc)



def product_add(tup):
    productlist.append(tup)

def display():
    print(productlist)

def prod_quantity():

    for qnt in productlist:
        productdict[qnt.pnam].append(qnt.pqty)
    return productdict

while True:
    choice=int(input("Enter choice 1.add 2. display 3. quantity 4.Exit"))

    if choice==1:
        prod=take_user_inputs()
        product_add(prod)
    elif choice==2:
        display()
    elif choice==3:
        print("Product Quantity: ",prod_quantity())
    elif choice==4:
        sys.exit()

