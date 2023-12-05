# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 22:04:37 2023

@author: leo
Sourdough Calculator
"""
import argparse
# Parse arguments
def getopts():
    
    # Arg for slecting which type of lookup
    parser = argparse.ArgumentParser()
    # Arg for number of servings
    parser.add_argument('Servings',type=int, nargs='?',default=8, help="Servings: Input Number > 0")
    # Arg for hydration
    parser.add_argument('Hydration',type=int, nargs='?',default=70, help="Hydration (%): Input Number > 0")
    # Arg for amount of starter
    parser.add_argument('Starter',type=int, nargs='?',default=100, help="Starter (g): Input Number > 0")

    # parse command line
    opts = parser.parse_args()
    Servings = opts.Servings
    Hydration = opts.Hydration
    Starter = opts.Starter

    # Error Checks
    if Servings < 1:
        raise ValueError("Servings: Input Number > 0")
    if Hydration < 1:
        raise ValueError("Hydration(%): Input Number > 0")
    if Starter < 1:
        raise ValueError("Starter(g): Input Number > 0")
    
    return [Servings,Hydration,Starter]
def main():
    Servings,Hydration,AmountOfStarter = getopts()
    CaloriesPerServing = 260
    FlourPerServing = CaloriesPerServing/4
    AmountOfFlour = Servings*FlourPerServing-(AmountOfStarter/2)
    AmountOfWater = Hydration/100*AmountOfFlour-(AmountOfStarter/2)
    AmountOfSalt = AmountOfFlour*.02
    Sourness = AmountOfStarter/AmountOfFlour
    
    print("In order to make dough for",Servings,"people, you need the following:")
    print("Flour:",AmountOfFlour,"Grams")
    print("Water:",AmountOfWater,"Grams")
    print("Salt:",AmountOfSalt,"Grams")
    print("Starter:",AmountOfStarter,"Grams")
    if Sourness < .05:
        print("This is a very sour loaf, if you want a more mellow loaf, consider increasing the amount of starter")
    elif Sourness < .1:
        print("This is a sour loaf, if you want a more mellow loaf, consider increasing the amount of starter, if you would like a more sour loaf, consider decreasing the amount of starter you use")
    elif Sourness < .2:
        print("This is a medium sourness loaf, if you want a more mellow loaf, consider increasing the amount of starter, if you would like a more sour loaf, consider decreasing the amount of starter you use")
    else:
        print("This is a mellow loaf, if you'd like a more sour loaf, consider decreasing the amount of starter")

main()