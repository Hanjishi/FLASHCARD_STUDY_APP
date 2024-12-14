def binangkal_recipe():
    oil = "as needed"
    all_purpose_flour = 1 #cup
    powdered_milk = 0.5 #cup 
    baking_powder = 0.5 #teaspoon
    sugar = 0.5 #cup 
    evaporated_milk = 0.25 #cup
    melted_butter = 0.25 #cup 
    egg = 1 #whole egg
    
    print("Gathering the following ingredients:\nOil, All Purpose Flour, Powdered Milk, Baking Powder, \nSugar, Evaporated Milk, Melted Butter, Egg")
    
    dry_mixture = {
        "all_purpose_flour": all_purpose_flour,
        "powdered_milk": powdered_milk,
        "baking_powder": baking_powder,
    }
    
    print("\nMixing Dry Mixture from the ingredients...")
    
    wet_mixture = {
        "sugar": sugar,
        "evaporated_milk": evaporated_milk,
        "melted_butter": melted_butter,
        "egg": egg,
    }
    
    print("Mixing Wet Mixture from the Ingredients...")
    print("Mixing both Mixtures to create the dough for the recipe...")
    
    mixture = {**dry_mixture, **wet_mixture}
    is_smooth_and_sticky = False
    while not is_smooth_and_sticky:
        is_smooth_and_sticky = True
        
    binangkal_balls = ["ball coated with sesame seeds" for ingredients in range(5)]
    
    print("\nHeating oil in a pan")
    
    fried_binangkal = []
    for ball in binangkal_balls:
        is_golden_brown = False
        while not is_golden_brown:
            print(f"Frying {ball}...")
            is_golden_brown = True
        fried_binangkal.append(ball)
        
    print("\nBinangkal is ready to be served!")
    return fried_binangkal

binangkal_recipe()