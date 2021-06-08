import pickle
from pathlib import Path
from Classes import Album, Tracks

class File_setup:

    def __init__(self, file_name):
        self.path = Path('.')
        self.file_name = file_name
        self.dir_name = Path('~/matthew-project0-production/project_data')
        self.target_path = self.dir_name / self.file_name
        self.collection = []
        
    def write_file(self):

            with open(self.target_path, 'wb') as file_out:
                pickle.dump(self.collection, file_out)
        
    #check to see if music collection exists 
    def check_path_collection(self, option):
        
        #check if dir is present
        print(self.dir_name)
        
        if (self.dir_name.exists()):
            pass
        else:
            self.dir_name.mkdir()
            

        check_path = self.target_path.resolve()

        if check_path.exists():
            if option == 0:
                print('Loading music collection')
        else:
            #create file for default music 
            check_path.touch()
            if option == 0:
                self.load_default()
            else:
                self.collection.append((0,0,0,0))
                self.write_file()
    #write file
    

    #create default collection
    def load_default(self):

        album_1 = Album('Speaking in Tounges', 'Talking heads', 1983)
        tracks_1 = ['Burning Down the House', 
                    'Making Flippy Floppy',
                    'Girlfriend Is Better',
                    'Slippery People',
                    'Swamp',
                    'This Must Be the Place (Naive Melody)',]
        #album_1.add_tracks((Tracks(track) for track in tracks_1))
        for track in tracks_1:
            album_1.add_track(Tracks(track))

        self.collection.append(album_1)

        album_2 = Album('Malibu', 'Anderson .Paak', 2016)
        tracks_2 = ['The Bird',
                    'Heart dont Stand a Chance',
                    'The Season | Carry Me',
                    'Put Me Thru',
                    'Come Down']
        #album_2.add_tracks((Tracks(track) for track in tracks_2))
        for track in tracks_2:
            album_2.add_track(Tracks(track))

        self.collection.append(album_2)

        album_3 = Album('Wide Awake!', 'Parquet Courts', 2018)
        tracks_3 = ['Total Football',
                    'Violence',
                    'Almost Had to Start a Fight/In and Out of Patience',
                    'Wide Awake']
        #album_3.add_track((Tracks(track) for track in tracks_3))
        for track in tracks_3:
            album_3.add_track(Tracks(track))

        self.collection.append(album_3)

        self.write_file()

