#Harrison Pierce
##Final q4


from tkinter import *

class Info(Frame):

    #Initializer 
    def __init__(self):

        self.window = Tk() #Create frame

        self.new_frame = Frame(self.window, width=500, height=50,padx = 50, pady=30)
        self.new_frame.grid(row = 5, sticky="nsew")       

        #My information
        self.name = '\tHarrison Pierce\n\t143 Salem End Rd\n\tFramingham, MA'

        self.l1 = Label(self.new_frame, text='\n\n\n') #add labels

        #set the elements in grid
        self.l1.grid(row = 0, column = 1)
        self.show_info_button = Button(self.new_frame, text="Show Info", command = self.show_info)
        self.show_info_button.grid(row = 8, column = 1, padx = 30, pady = 30)

        self.quit = Button(self.new_frame, text = 'Quit', command =self.quit_window)
        self.quit.grid(row = 8, column = 4, padx = 30, pady = 30)

        #keep window open
        self.window.mainloop();

    def show_info(self):

       self.l1['text'] = self.name

    def quit_window(self):

        #close the windoww when quit is pressed
        self.window.destroy()

ob = Info() #call info