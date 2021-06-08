import datetime
import pickle

class Data_collection_class:

    def __init__(self, session_time , collection_size, number_added, number_deleted) -> None:
        self.session_time = session_time
        self.number_of_albums = collection_size
        self.number_added = number_added
        self.number_deleted = number_deleted
        self.report_file = './project_data/project_0_report.txt'
        self.log_file = './project_data/project_0_logs.txt'
        self.log_data = []
        self.today = datetime.date.today()

    #load log file 
    def open_report(self):
        with open(self.log_file, 'rb') as file_in:
            self.log_data = pickle.load(file_in)

    #write files 
    def write_files(self, ave_albums, ave_added, ave_del, ave_time):
        date = self.today.strftime('%Y - %m - %d') 
        with open(self.report_file, 'a+') as file_out:
            file_out.write(f'Date : {date} \n\n')
            file_out.write(f'Average size of collection : {ave_albums}\n')
            file_out.write(f'Average albums added       : {ave_added}\n')
            file_out.write(f'Average albums deleted     : {ave_del}\n')
            file_out.write(f'Average session time       : {ave_time} \n\n')

        with open(self.log_file, 'wb') as file_out:
            pickle.dump(self.log_data, file_out)

    
        
    
    #calulate values to update report
    def calculate_average(self):
        #create new entry for log
        entry = (self.number_of_albums, 
                self.number_added,
                self.number_deleted,
                self.session_time )

        self.log_data.append(entry)
        
        #generate totals for averages
        albums_total, added_total, deleted_total, time_total = 0, 0, 0, 0

        for item in self.log_data:
            albums_total += item[0]
            added_total += item[1]
            deleted_total += item[2]
            time_total += item[3]
        #calculate averages
        sessions = len(self.log_data)
        average_albums = albums_total / sessions
        average_added = added_total / sessions
        average_deleted = deleted_total / sessions
        average_time = time_total / sessions 

        self.write_files(average_albums, average_added, average_deleted, average_time)
