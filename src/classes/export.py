# export class to convert txt file of subtitle string to csv file

class export():
    def __init__(self, inputfile, removeperps=True, exportfile="") -> None:
        self.inputfile = inputfile
        self.removepersp = removeperps
        self.exportfile = exportfile

    

    def save_to_csv(self):
        pass