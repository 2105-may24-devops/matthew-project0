#matthew cradit 
#project 0 main file

from data_collection_class import Data_collection_class
from Classes import Player
import file_setup
import blessed
import time
import sys

#for execution time of program 
start_time = time.time()



""" term = blessed.Terminal()

print(term.home + term.clear + term.move_y(term.height // 2))


print(term.black_on_darkkhaki(term.center('Welcome to the music player interface') 
                            + term.center('Press any key to continue')))

with term.cbreak():
    inp = term.inkey()

print(term.move_down(2) + 'You pressed ' + term.bold(repr(inp))) """

#check to see if there is a music collection 
file_checker = file_setup.File_setup('collection_file')
file_checker.check_path_collection(0)

#create player 
player = Player('collection_file')


#load current collection 
player.read_file()
#variable for selection 
fin = 'y'

while fin != 'n' and fin != 'N':
    print("\nMusic player menu.\n")
    print("Please select one of the following")
    print("1) select album to play")
    print("2) Add new album")
    print("3) Delete Album")
    print("x) to exit")
    value = input("\nslection :")
    player.menu(value)

    fin = input('would you like to continue? (Y/N) :')

player.write_file()

print('\nCollection Saved.\nThank you for Listening!\n')

#time of program execution 
total_time = time.time() - start_time

data_collection = Data_collection_class(total_time, 
                                        len(player.collection), 
                                        player.number_added, 
                                        player.number_deleted)

#check if a log file exist 
log_checker = file_setup.File_setup('project_0_logs')
log_checker.check_path_collection(1)
#generate report
data_collection.open_report()
data_collection.calculate_average()
