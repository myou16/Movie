def movies():
    print("This program calculates the total price of the movie tickets.")
    weather=input("Is it raining? Enter yes or no: ")
    if weather.lower()=="no":
    
        total=0
        ppl=eval(input("How many ppl are in your group?: "))
        for i in range(ppl):
            age=eval(input("Enter age of person: "))
            if age<12:
                price=0
            elif age<60:
                price=12
                ID=input("Do you have a special ID? Respond with student, nurse, veteran, or none: ")
                if ID.lower()=="student":
                    price=price*.7
                elif ID.lower()=="nurse":
                    price=price*.65
                elif ID.lower()=="veteran":
                    price=price*.5
                else:
                    price=12
            elif age>60:
                price=7
                ID=input("Do you have a special ID? Respond with student, nurse, veteran, or none: ")
                if ID.lower()=="student":
                    price=price*.7
                elif ID.lower()=="nurse":
                    price=price*.65
                elif ID.lower()=="veteran":
                    price=price*.5
                else:
                    price=7

            total+=price
        print("The total cost of the tickets is","{0:.2f}".format(total),end=" dollars.\n")

    else:
        print("Sorry, it is raining today and the theater is closed.")


    print("Thanks for coming to the movies!")

movies()
            

    
            
                
                
           




