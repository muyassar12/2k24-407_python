class PurchaseCompletion:
    def complete_purchase(self, car, color):
        while True:
            confirm = input("Sotib olishni tasdiqlaysizmi? (ha/yo'q): ").lower()
            if confirm == "ha":
                print(f"\nXaridingiz uchun rahmat! Siz ${car.price} evaziga {color} rangli {car.model} sotib oldingiz.")
                break
            elif confirm == "yo'q":
                print("\nXarid bekor qilindi.")
                break
            else:
                print("Iltimos, 'ha' yoki 'yo'q' deb javob bering.")
