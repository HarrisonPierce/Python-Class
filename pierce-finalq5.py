##Harrison Pierce
##Final question 5

##Program displays a window for a auto shop and lets user check options
##displays total price


import tkinter

#create class for joes automotive
class JoesAutomotive:

    #constuctor
    def __init__(self, parent):

        self.main_window = parent  #main_window refrence        
        self.top_frame = tkinter.Frame(self.main_window) #top frame
        self.main_window.title("Joe's Automotive") #window title name
        self.bottom_frame = tkinter.Frame(self.main_window) #bottom frame

        #objects for oil, lube, radiator, flush, inspection, muffler and tire
        self.oil = tkinter.IntVar()
        self.lube = tkinter.IntVar()
        self.rad = tkinter.IntVar()
        self.trans = tkinter.IntVar()
        self.insp = tkinter.IntVar()
        self.muff = tkinter.IntVar()
        self.tire = tkinter.IntVar()

        #Check boxes for all services for each variable
        self.oilb = tkinter.Checkbutton(self.top_frame, text="Oil Change - $30", variable=self.oil, onvalue = 30)

        self.lubeb = tkinter.Checkbutton(self.top_frame,text= "Lube Job - $20", variable=self.lube, onvalue = 20)

        self.radb = tkinter.Checkbutton(self.top_frame, text= "Radiator Flush - $40", variable=self.rad, onvalue = 40)

        self.transb = tkinter.Checkbutton(self.top_frame,text= "Transmission Flush - $100", variable=self.trans, onvalue = 100)

        self.inspectb = tkinter.Checkbutton(self.top_frame,text= "Inspection - $35", variable=self.insp, onvalue = 35)

        self.muffb = tkinter.Checkbutton(self.top_frame,text= "Muffler Replacement - $200", variable=self.muff, onvalue = 200)

        self.tireb = tkinter.Checkbutton(self.top_frame, text= "Tire Rotation - $20", variable=self.tire, onvalue = 20)

        #"Display Charges" button
        self.display_button = tkinter.Button(self.bottom_frame, text= "Display Charges", command=self.display_charge)

        #Create button to quit program
        self.quit_button=tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        #Create the label to display the charge.
        self.total_l = tkinter.Label(self.bottom_frame, text="$0.00")
        self.top_frame.pack()
        self.bottom_frame.pack()

        #Pack check boxes
        self.oilb.pack()
        self.lubeb.pack()
        self.radb.pack()
        self.transb.pack()
        self.inspectb.pack()
        self.muffb.pack()
        self.tireb.pack()

        self.display_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.total_l.pack(side='left')
        #pack the display and quit buttons


    #define the method to calculate the charge
    #show user the charge in the label
    def display_charge(self):

        self.total_l.config(text="${}.00".format(sum(map(tkinter.IntVar.get, 
        [self.oil, self.lube, self.rad, self.trans, self.insp, self.muff,self.tire]))))

#here we call calculation function
if __name__ == "__main__":

        #Tkinter object
        root = tkinter.Tk()

        #Object for JoesAutomotive class
        gui = JoesAutomotive(root)
        root.mainloop()