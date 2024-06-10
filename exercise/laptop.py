print("================Computer Bazar===============")
print("1. Dell(Rs:20000) 2.Toshiba(Rs:30000) 3. Mac(Rs:50000)")
dell_price=0
toshiba_price=0
mac_price=0
product_name=''
quantity=0

option=int(input("Enter the option:"))
if option==1:
    quantity=int(input("Enter the quantity:"))
    dell_price=20000*quantity
    product_name="Dell"
elif option==2:
    quantity=int(input("Enter the quantity:"))
    toshiba_price=30000*quantity
    product_name="Toshiba"
elif option==3:
    quantity=int(input("Enter the quantity:"))
    mac_price=50000*quantity
    product_name="Mac"
else:
    print("Invalid option")
    exit()


delivery_charge=0
print("1. Home Delivery(Rs:1000) 2. Store Pickup(Free)")
del_option=int(input("Enter the delivery option:"))
if del_option==1:
    delivery_charge=1000

plastic_charge=0
bag_charge=0
gift_wrap_charge=0

print("1. Plastic Bag(Rs:500) 2. Paper Bag(Rs:1000) 3. Gift Wrap(Rs:5000) 4. No Bag")
bag_option=int(input("Enter the bag option:"))
if bag_option==1:
    plastic_charge=500
elif bag_option==2:
    bag_charge=1000
elif bag_option==3:
    gift_wrap_charge=5000

total = dell_price+toshiba_price+mac_price
tax_amount=0
print("Location: 1.KTM(13% tax) 2. Lalitpur(0 tax) 3. Bhaktapur(0 tax)")
locaiton = int(input("Enter the location:"))
if locaiton==1:
    tax_amount = total*0.13

grand_total = total+delivery_charge+plastic_charge+bag_charge+gift_wrap_charge+tax_amount
print("=================Invoice====================")
print("Product Name:",product_name)
print("Quantity:",quantity)
print("Total:",total)
print("Delivery Charge:",delivery_charge)
print("Plastic Charge:",plastic_charge)
print("Bag Charge:",bag_charge)
print("Gift Wrap Charge:",gift_wrap_charge)
print("Tax Amount:",tax_amount)
print("Grand Total:",grand_total)
