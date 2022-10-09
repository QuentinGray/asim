# Creating a program that stores songs with user input metadata, can then print out lists of similarity from the metadata, like same key music, same bpm, same genre, etc

# import needed modules
import csv
import copy

# Welcome user to the program

print("Welcome to my music management system, called ASIM(Analyse and Store Important Music Data)")

inventorySongs = []
inventoryNum = 0

while True:
    if inventorySongs:
        print("Songs in Database:")
        for song in inventorySongs:
            print(f"{song[inventoryNum]} Tracks in Library")

    inventoryNum = inventoryNum + 1
    #Input data
    s_band = input("What is the bands name? ")
    s_title = input("What is the songs name? ")
    s_genre = input("What is the songs genre? ")
    s_key = input("What key is this song? ")
    s_bpm = input("What is the bpm? ")
    # define stored song dictionary
    song = {
    "track" : inventoryNum,
    "band" : s_band,
    "songtitle" : s_title,
    "genre" : s_genre,
    "key" : s_key,
    "bpm" : s_bpm
}
    print(f"Adding the following track to the library: {song[s_band]} - {song[s_title]}") 

    inventorySongs.append(song)
    # Take stored information and give you the option to organize lists by types (bpm / key / genre)



#Currently only takes input and prints that back to you in a continious loop
#going off labs page 6


