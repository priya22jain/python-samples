weight = float(input("Weight : "))
weight_type = input("(K)g or (L)bs : ")
if weight_type == "K" or weight_type == "k":    # weight_type.upper() == "K"
    print("Weight in Lbs: " + str(weight * 2.20462))
elif weight_type == "L" or weight_type == "l":
    print("Weight in Kg: " + str(weight * 0.453592))
else:
    print("Wrong weight type")