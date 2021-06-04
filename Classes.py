#Matthew Cradit 
#file for classes 
from io import DEFAULT_BUFFER_SIZE
from random import seed, randint
import pickle
import time

#seed for generating song lengths
seed(1)

'''
    This is a Class definition for the CD player interface
'''
class Player:
    #constructer 
    def __init__(self, name):
        self.file_name = name
        self.collection = []
        
        self.number_added = 0 
        self.number_deleted = 0

    #method for users 
    def menu(self, value):
        if value == '1':
            self.play()
        elif value == '2':
            self.add_album()
        elif value == '3':
            self.delete_album()
        elif value == 'x':
            pass 
        else:
            print("selection not recogized")

    #method for reading data using pickle  
    def read_file(self):
        
        with open(self.file_name, 'rb') as file_in:
            self.collection = pickle.load(file_in)

        
<<<<<<< HEAD
    #method for writing data using pickle 
=======
    #method for writing file with pickle, saves list of albums object
>>>>>>> my-comments
    def write_file(self):

        with open(self.file_name, 'wb') as file_out:
            pickle.dump(self.collection, file_out)

        
    '''
        Method for playing the album selected by user 
    '''
    def play(self):
        #display prompt 
        print("\nPlease select an Album to play\n")
        #select album from collection
        album_index = self.select()
        album = self.collection[album_index]
        #display album information
        print(f'\nTitle : {album.title}')
        print(f'Artist : {album.artist}')
        print(f'Released in : {album.release}\n')
        #play album 
        for tracks in album.tracks:
            print(f'now playing : {tracks.name}')
            time.sleep(tracks.time)

    
    '''
        Method for selecting an album to play 
    '''
    def select(self):
        #dsplay albums for selection
        for album in self.collection:
            print(f'{(self.collection.index(album) +1)} : {album.title} by {album.artist}')
        
        #get user input 
        selected = int(input("please select index of desired album :"))
        while (selected - 1) < 0 or selected  > len(self.collection):
            print('selection not recognized')
            selected = int(input("please select index of desired album :"))
        #play selected album 
        return (selected - 1)
        
    
    '''
        Method for adding album to collection 
    '''
    def add_album(self):
        #Album information
        print("please enter Album information")
        title = input("Title of album :")
        artist = input("Name of artist :")
        date = input("date of release: ")
        new_album = Album(title, artist, date)

        #track information
        another_track = 'y'
        while another_track != 'n' and another_track != 'N':
            track_name = input('Enter track name: ')
            new_track = Tracks(track_name)
            new_album.add_track(new_track)
            another_track = str(input('Would you like to add another (y/n) : '))
        #add new album to collection 
        self.collection.append(new_album)
        self.number_added += 1
        print(f'{new_album.title} by {new_album.artist} has been added to your collection!')

    
    #method for deleting alubm 
    def delete_album(self):
        #select album to delete
        print("\nSelect Album to be deleted")
        album_index = self.select()
        del_album = self.collection[album_index]
        try:
            
            print(f'{del_album.title} by {del_album.artist} has been removed from your collection!\n')
            self.collection.pop(album_index)
            self.number_deleted += 1
        except:
            print("Error album not found")

'''
    Album class definition, includes name of alubm, artist, and date released
'''
class Album:

    def __init__(self, title, artist, date) -> None:
        self.title = title
        self.artist = artist 
        self.release = date 
        self.tracks = []

    #method for adding tracks
    def add_track(self, new_track):
        self.tracks.append(new_track)
    
    
'''
    Class definition for Track objects
    takes name of track 
    and generates random number between 1 and 5 for song length
'''
class Tracks:
    #constructor
    def __init__(self, name) -> None:
        self.name = name 
        self.time = randint(1,5)
    
   


        
