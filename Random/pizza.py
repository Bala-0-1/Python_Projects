print("Last slice algo. :)")
print("It only accepts 'yes' and 'no'.Be careful with your choice.")
var = input("Did you buy the pizza ? ")
if var == 'yes':
    print("Go ahead")
if var == 'no':
    var = input("Did you buy the pizza last time ?")
    if var == 'yes':
        print("Eat it.")
    else:
        while True:
            var = input("Do you care what people think ?")
            if var == 'no':
                print("Eat it.")
                break
            else:
                var = input("have you had less than or equal to 2 silces ?")
                if var == 'yes':
                    print("Eat it.")
                    break
                else:
                    var = input("Did you ask ?")
                    if var == 'yes':
                        var = input("Does anyone else want it ?")
                        if var == 'no':
                            print("Eat it . ")
                        else:
                            var = input("Yes . ")
                            continue
                    else:
                        continue
                            
        
    