# Importing useful modules
import os
import pickle
import PySimpleGUI as sg
from threading import Thread

# setting a theme
sg.ChangeLookAndFeel('DarkBlue')


# Creating a class for GUI of program
class Gui:
    # Creating constructor of class
    def __init__(self):
        # defining layout of our GUI which is setting row wise
        self.layout: list = [
            # First row of GUI
            [sg.FolderBrowse('Browse', size=(12, 1), pad=(15, 5), font=("Bahnschrift SemiBold Condensed", 13), button_color="light blue"),
             sg.Button('Re-Index', size=(12, 1), key="_INDEX_", pad=(15, 5), font=("Bahnschrift SemiBold Condensed", 13), button_color="light blue", mouseover_colors='sky blue'),
             sg.Button('Search', size=(12, 1), bind_return_key=True, key="_SEARCH_", pad=(15, 5), font=("Bahnschrift SemiBold Condensed", 13), button_color="light blue", mouseover_colors='sky blue'),
             sg.Button('Close', size=(12, 1), key="_CLOSE_", pad=(15, 5), font=("Bahnschrift SemiBold Condensed", 13), button_color="light blue", mouseover_colors='sky blue')],
            # Second row of GUI
            [sg.Radio('Contains', size=(8, 1), group_id='choice', key="CONTAINS", default=True, pad=(5, 5), font=("Bahnschrift SemiBold Condensed", 13), background_color="#232733"),
             sg.Radio('StartsWith', size=(10, 1), group_id='choice', key="STARTSWITH", pad=(110, 5), font=("Bahnschrift SemiBold Condensed", 13), background_color="#232733"),
             sg.Radio('EndsWith', size=(8, 1), group_id='choice', key="ENDSWITH", pad=(0, 5), font=("Bahnschrift SemiBold Condensed", 13), background_color="#232733")],
            # Third row of GUI
            [sg.Text('Search Term', size=(11, 1), font=("Bahnschrift Light Condensed", 13), background_color="#232733"),
             sg.Input(size=(42, 1), focus=True, key="TERM", font="Cambria 13", background_color="#151f2b", border_width=2)],
            # Forth row of GUI
            [sg.Text('Root Path', size=(11, 1), font=("Bahnschrift Light Condensed", 13), background_color="#232733"),
             sg.Input('/..', size=(42, 1), key="PATH", font="Cambria 13", background_color="#151f2b", border_width=2)],
            # Fifth and last row of GUI which is output window
            [sg.Output(size=(67, 23), background_color="#20242e", font=("Bahnschrift Light Condensed", 12), pad=(2, 10), text_color="#8cff4e", sbar_background_color="#37435b", sbar_trough_color="#011627")]]

        # Setting attributes of GUI
        self.window: object = sg.Window('File Searcher', self.layout, element_justification='left', alpha_channel=1, transparent_color='DarkBlue', no_titlebar=True, background_color="#232733")


# Creating SearchEngine class for searching the result
class SearchEngine:
    # Defining constructor of class SearchEngine
    def __init__(self):
        self.file_index: list = []  # directory listing returned by os.walk()
        self.results: list = []  # search results returned from search method
        self.matches: int = 0  # count of records matched
        self.records: int = 0  # count of records searched

    def create_new_index(self, values: dict):
        # Create a new index of the root; then save to self.file_index and to pickle file
        root_path: str = values['PATH']
        self.file_index: list = [(root, files) for root, dirs, files in os.walk(root_path) if files]
        # save index to file
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\File Searcher\\file_index.pkl', 'wb') as f:
            pickle.dump(self.file_index, f)

    def load_existing_index(self):
        # Load an existing index into the program'
        try:
            with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\File Searcher\\file_index.pkl', 'rb') as f:
                self.file_index = pickle.load(f)
        except:
            self.file_index = []

    def search(self, values: dict):
        # Search for the term based on teh type in the index; the types of search include: contains, startswith, endswith; save the results to file
        self.results.clear()
        self.matches: int = 0
        self.records: int = 0
        term = values['TERM']

        # search for matches and count results
        for path, files in self.file_index:
            for file in files:
                self.records += 1
                if (values['CONTAINS'] and term.lower() in file.lower() or
                        values['STARTSWITH'] and file.lower().startswith(term.lower()) or
                        values['ENDSWITH'] and file.lower().endswith(term.lower())):

                    result = path.replace('\\', '/') + '/' + file
                    self.results.append(result)
                    self.matches += 1
                else:
                    continue

        # save results to file
        with open('A:\\My Projects\\Android Subsystem for Windows (Python)\\File Searcher\\search_results.txt', 'w') as f:
            for row in self.results:
                f.write(row + '\n')


# Creating The main loop for the program
def main():
    g: object = Gui()
    s: object = SearchEngine()
    s.load_existing_index()  # load if exists, otherwise return empty list

    while True:
        event, values = g.window.Read()
        if event is None:
            break
        if event == sg.WIN_CLOSED or event == '_CLOSE_':
            break
        if event == '_INDEX_':
            s.create_new_index(values)
            print()
            print(">> New index created")
            print()
        if event == '_SEARCH_':
            s.search(values)

            # print the results to output element
            print()
            for result in s.results:
                print(result)

            print()
            print(">> Searched {:,d} records and found {:,d} matches".format(s.records, s.matches))
            print(">> Results saved in working directory as search_results.txt.")

def threading_main():
    t1 = Thread(target=main)
    t1.start()

# Starting point of program
if __name__ == '__main__':
    threading_main()
