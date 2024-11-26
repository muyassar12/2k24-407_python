def main():
    print("""
 ___________________________________________________
|                                                   |
|   #  #  #   #####  #       ####   ###   #     #   |
|   #  #  #   #      #      #      #   #  ##   ##   |
|   #  #  #   ####   #      #      #   #  # # # #   |
|   #  #  #   #      #      #      #   #  #  #  #   |
|    ## ##    #####  #####   ####   ###   #     #   |
|___________________________________________________|           
""")
    data = True
    while (data == True):
        
        obj = Order()
        print("""
--------------------------
||  Choose the car type ||
--------------------------
""")
        obj.print_car_tyes()
        obj.get_name_car_type()
        obj.get_name_car_model()
        
        obj.get_name_car_color()
        
        data = obj.result()
        if data == False:
            print("""
 _______________________________________________________________
|                                                               |
|     #####    ###    ###   ####          ####   #   #  #####   |
|    #        #   #  #   #  #    #        #   #  #   #  #       |
|    #  ###   #   #  #   #  #    #        ####    # #   #####   |
|    #     #  #   #  #   #  #    #        #   #    #    #       |
|     #####    ###    ###   ####          ####     #    #####   |
|_______________________________________________________________|

""")
    
    
    
class Order:
    #its my "car database"
    #Car types, models and price data
    __dic = {
        "Sedan" : {
            1 : ("Toyota Camry", 30000),
            2 : ("Honda Accord", 32000),
            3 : ("BMW 3 Series", 50000),
        },
    
        "Hatchback" : {
            1 : ("Volkswagen Golf", 27000),
            2 : ("Honda Civic Hatchback", 27500),
            3 : ("Mazda3 Hatchback", 30000),
        },
    
        "Coupe" : {
            1 : ("Ford Mustang", 45000),
            2 : ("Chevrolet Camaro", 47000),
            3 : ("BMW 4 Series Coupe", 57000),
        },
        
        "Minivan" : {
            1 : ("Honda Odyssey", 44000),
            2 : ("Toyota Sienna", 46000),
            3 : ("Chrysler Pacifica", 48000),
        },
        
        "SUV" : {
            1 : ("Toyota RAV4", 35000),
            2 : ("Honda CR-V", 34000),
            3 : ("Ford Explorer", 47000),
        }  
    }
    
    #Car colors data with percantage
    __dic_color = {
        1 : ("White", 0),
        2 : ("Black", 4.6),
        3 : ("Red", 5.2),
        4 : ("Yellow", 4.5),
        5 : ("Green", 5.8),
    }
    
    def __init__(self) -> None:
        self._cars_type = [] 
        self._cars_model = []
        self._cars_color = []
        self.__summ = 0
        
    
    #Append all car types to list
    def __set_car_type_to_list(self):
        for i, j in self.__dic.items() :
            self._cars_type.append(i)
            
        
        return self._cars_type
    
    
    #get or print car models with order and append car models and price to list
    def get_car_models(self, type: str):
        print()
        print("""
--------------------------
||  Choose the car model ||
--------------------------
""")
        for type_name, values in self.__dic.items():
            if type_name == type:
                for model_num, value in values.items():
                    self._cars_model.append(value)
                    print(model_num, "\b.", value[0], ":", value[1], "$")
    
    
    #get or print car colors with order and append car colors and percentage to list
    def get_car_color(self):
        print()
        print("""
--------------------------
||  Choose the car color ||
--------------------------
""")
        for i, j in self.__dic_color.items():
            self._cars_color.append(j)
            print(i, "\b.", j[0], " : ", j[1],"%")
            
            
    #print "enter number" string and check this 
    def print_input(self):
        try:
            enter_data = int(input("\nEnter number: "))

            return enter_data
        
        except:
            pass
            
    
    #print car all car types with order        
    def print_car_tyes(self):
        cars = self.__set_car_type_to_list()
        
        for j in range(1, len(cars)+1):
            print(f"{j}. {cars[j-1]}")
    
    
    #check enter number and print car models
    def get_name_car_type(self):
        data = self.print_input()
        # print(self._cars_type)
        if data is None or data>len(self._cars_type) or 0>=data:
            print("Enter the correct number!!!")
            self.again_type()            
        else:
            for j in range(1, len(self._cars_type)+1):
                if data == j:
                    self.get_car_models(self._cars_type[j-1])
                    
                    
    #check enter number and add price to summ
    def get_name_car_model(self):
        
        data = self.print_input()
        if data is None or data>len(self._cars_model) or 0>=data:
            print("\nEnter the correct number!!!")
            self.again_model()
        else:
            self.__summ+=self._cars_model[data-1][1]
            self.get_car_color()
            
    
    #check enter number and add percentage price to summ
    def get_name_car_color(self):
        
        data = self.print_input()
        # print(data)
        
        if data is None or data>len(self._cars_color) or 0>=data:
            print("\nEnter the correct number!!!")
            self.again_color()
        else:
            self.__summ+=self.__summ*self._cars_color[data-1][1]/100
   
    
    def again_model(self):
        answer = input("\nDo you want to enter it again (yes/no):")
        if answer == "yes" or answer == "YES" or answer == "Yes":
            self.get_name_car_model()
        elif answer == "No" or answer == "NO" or answer == "no":
            exit()
        else: 
            self.again_model()
    
    
    def again_type(self):
        answer = input("\nDo you want to enter it again (yes/no):")
        if answer == "yes" or answer == "YES" or answer == "Yes":
            self.get_name_car_type()
        elif answer == "No" or answer == "NO" or answer == "no":
            exit()
        else: 
            self.again_type()
    
    
    def again_color(self):
        answer = input("\nDo you want to enter it again (yes/no):")
        if answer == "yes" or answer == "YES" or answer == "Yes":
            self.get_name_car_color()
        elif answer == "No" or answer == "NO" or answer == "no":
            exit()
        else: 
            self.again_color()
    
    #result methods for print price and asking
    #print method
    def result(self):
        print(f"""
----------------------------------------
||  Your order Price:  {self.__summ } $ ||
----------------------------------------
""")
        print("Your order Price: ", self.__summ, "$")
        return self.result_print()
    
    
    #asking method
    def result_print(self):
        answer = input("\nDo you want any order (yes/no): ")
        
        if answer == "yes" or answer == "YES" or answer == "Yes":
            return True
        elif answer == "No" or answer == "NO" or answer == "no":
            return False
        else: 
            self.result_print()
    


if __name__ == "__main__":
    main()
    
    
    
    