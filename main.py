#matthew cradit 
#project 0 main file

from data_collection_class import Data_collection_class
from Classes import Player
import file_handler
import time
import sys

#for execution time of program 
start_time = time.time()


def main():
    #check to see if there is a music collection 
    file_checker = file_handler.File_setup('collection_file.txt')
    file_checker.check_path_collection(0)

    #create player 
    player = Player('collection_file.txt')


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
    log_checker = file_handler.File_setup('project_0_logs.txt')
    log_checker.check_path_collection(1)
    #generate report
    data_collection.open_report()
    data_collection.calculate_average()

#non interative portion for testing purposes
def non_main():
    
    file_checker = file_handler.File_setup(sys.argv[1])
    file_checker.check_path_collection(sys.argv[2])


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        main()
    else:
        non_main()
