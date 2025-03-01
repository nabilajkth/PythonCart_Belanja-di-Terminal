'''
=================================================
Graded Challenge 2

Nama  : Nabila Sulistiowati
Batch : CODA-RMT-003

Berikut adalah program sederhana untuk shopping cart yang dapat menambah, menghapus, menampilkan serta melihat jumlah total belanja.

=================================================
'''


'''
Fungsi untuk menampilkan tampilan menu Shopping Cart
'''

def menu_display():
    print("\n==== Shopping Cart Menu ====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Show Items in Cart")
    print("4. View Total Purchase")
    print("5. Exit")
    print("---------------------------------")


'''
Fungsi ini untuk menambahkan nama item ke keranjang dan harga item

'''
def add_item(cart):
    name = input("Enter the Item Name:").strip()
    price = input("Enter the Item Price: ")

    # Validasi harga
    if price.isdigit() or (price.replace('.', '',1).isdigit() and price.count('.')==1):
        price = float(price)
        if price > 0:
            cart[name] = price
            print(f"The item '{name}' has been successfully added to the cart")
        else:
            print("The item price must be greater than 0")
    else:
        print("The price must be a valid number")


'''
Fungsi ini untuk menghapus item dari keranjang
'''
def remove_item(cart):
    name = input("Enter the name of the item you want to remove: ").strip()
    if name in cart:
        del cart[name]
        print(f"The item ‘{name}’ has been successfully removed from the cart")
    else:
        print(f"The item ‘{name}’ was not found")


'''
Fungsi ini untuk menampilkan item yang ada di keranjang
'''
def show_cart(cart):
    if not cart:
        print("The shopping cart is empty")
    else:
        print("\nMy cart:")
        for name, price in cart.items():
            print(f"- {name}: Rp{price:.2f}")


'''
Fungsi ini untuk menghitung total belanja dari keranjang
'''
def calculate_total(cart):
    total = sum(cart.values())
    print(f"\nTotal purchase: Rp{total:.2f}")


'''
Fungsi ini merupakan fungsi utama untuk menjalankan program Shopping Cart
'''
def main():
    cart = {}
    while True:
        menu_display()
        choice = input("Option: ")

        # Validasi pilihan menu
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                add_item(cart)
            elif choice == 2:
                remove_item(cart)
            elif choice == 3:
                show_cart(cart)
            elif choice == 4:
                calculate_total(cart)
            elif choice == 5:
                print("Thank you for shopping. See ya!")
                break
            else:
                print("Invalid menu option. Please choose between 1 and 5")
        else:
            print("Invalid input. Please enter a number between 1 and 5")

'''
Untuk menjalankan program Shopping Cart
'''
if __name__ == "__main__":
    main()
