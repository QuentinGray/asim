# Creating a program that stores songs with user input metadata, can then print out lists of similarity from the metadata, like same key music, same bpm, same genre, etc

# import needed modules
import csv
import copy

# Welcome user to the program

print("Welcome to my music management system, called ASIM(Analyse and Store Important Music Data)")

while True:
    #Input data
    s_band = input("What is the bands name? ")
    s_title = input("What is the songs name? ")
    s_genre = input("What is the songs genre? ")
    s_key = input("What key is this song? ")
    s_bpm = input("What is the bpm? ")
    # define stored song dictionary
    storedsongs = {
        "band" : s_band,
        "songtitle" : s_title,
        "genre" : s_genre,
        "key" : s_key,
        "bpm" : s_bpm
    }
    # Take stored information and give you the option to organize lists by types (bpm / key / genre)


    for key, value in storedsongs.items():
        print(f"{key} : {value}")


#Currently only takes input and prints that back to you in a continious loop
#going off labs page 6


