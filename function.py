#!/usr/bin/env python3

choice = int(input("Enter Channel Number: "))

def channel_sorter(chan):
    if chan >0 and chan <= 10:
        print("you want the basic package")

    elif chan <= 50:
        print("you want to premium pachage")

    elif chan <= 300:
        print("You want the extras package")

    else:
        print ("that value is not correct")

channel_sorter(choice)

