from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Book_Ticket():
    def __init__(self, master, F):
        self.master = master
        master.title("M&H Travels")
        self.photo = PhotoImage(file="y.png")
        self.w = self.photo.width()
        self.h = self.photo.height()
        master.geometry("%dx%d+50+30" % (self.w, self.h))
        master.maxsize(self.w, self.h)
        self.cv = Canvas(master, width=self.w, height=self.h)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.photo, anchor='nw')
        self.btn1 = Button(self.cv, text="Book ticket Now", fg="yellow",
                           bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=10, command= lambda: F.Screen2(True))
        self.btn1.place(relx=0.5, rely=0.8, anchor=CENTER)
        self.btn1.config(width=15, height=3)


class Person:
    def __init__(self, lstofname=[]):#INHERITANCE
        self._lstofname = lstofname



class Pilot(Person): #PILOT AND STAFF COMPOSING IN Flight class
    def __init__(self,lst):
        super().__init__(lst)

    def get_pilot(self):
        x=""
        for i in self._lstofname:
            x=str(x+" "+i)
        return x


class Staff(Person):
    def __init__(self,lst):
        super().__init__(lst)

    def get_staff(self):
        x=""
        for i in self._lstofname:
            x=str(x+" "+i)
        return x




class seat: #SEAT CLASS COMPOSING IN FLIGHT CLASS

    def __init__(self, fl_no, seats_avai):
        self.flight_no = fl_no
        self.seats_avai = seats_avai

    def get_seat(self):
        print(self.flight_no)
        print(self.seats_avai)


class flight: #composing pilot , staff and seats
    def __init__(self, source="", des="", date="", fl_no=0, seats_avai=0, lstofPilot=[], lstofstaff=[], price=""):
        self.date = date
        self.source = source
        self.destination = des
        self.price = price

        self._SEAT = seat(fl_no, seats_avai)
        self.pilot = Pilot(lstofPilot)
        self.staff = Staff(lstofstaff)
    def printing(self):
        print(self.source, self.destination, self.date)
        self._SEAT.get_seat()
        self.pilot.get_pilot()
        self.staff.get_staff()
        print(self.price)
# class payment:
#     def __init__(self,cr=""):
class passanger:
    count=0

    def __init__(self, n="", f="", ad="", cn="", nic=""):
        self.name1 = n
        self.father = f
        self.adress = ad
        self.contact = cn
        self.nic = nic
        self.name_ = StringVar()
        self.father_ = StringVar()
        self.contact_ = StringVar()
        self.address_ = StringVar()
        self.nic_ = StringVar()
        self.cardno = StringVar()
        self.cardexp = StringVar()




    def Screen2(self, dis= False, home=False ,dishome=False):
        global root2

        if dis == True and home == True and dishome == True:
            root5.destroy()
        elif dis == True and home == True:
            root4.destroy()
        elif dis == True:
            root.destroy()

        else:
            root3.destroy()
        root2 = Tk()
        root2.geometry("1280x720")
        root2.title("M&H Travels")
        root2.wm_iconbitmap('py.ico')
        self.photo = PhotoImage(file="11.png")
        self.w = self.photo.width()
        self.h = self.photo.height()
        root2.geometry("%dx%d+50+30" % (self.w, self.h))
        root2.maxsize(self.w, self.h)
        self.cv = Canvas(root2, width=self.w, height=self.h)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.photo, anchor='nw')

        self.btn2 = Button(self.cv, text="Book Ticket", fg="yellow",
                           bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=7, command= lambda: self.book_Ticket(True))
        self.btn2.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn2.config(width=10, height=2)

        self.btn3 = Button(self.cv, text="Check your Booked ticket", fg="yellow",
                           bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=7,command=lambda : self.check_book(True))
        self.btn3.place(relx=0.5, rely=0.64, anchor=CENTER)
        self.btn3.config(width=22, height=2)
        root2.mainloop()

    def book_Ticket(self, dis2=False):
        global root3
        if dis2 == True:
            root2.destroy()
        else:
            root4.destroy()

        root3 = Tk()
        root3.title("M&H Travels")
        root3.wm_iconbitmap('py.ico')
        self.photo = PhotoImage(file="11.png")
        self.w = self.photo.width()
        self.h = self.photo.height()
        root3.geometry("%dx%d+50+30" % (self.w, self.h))
        root3.maxsize(self.w, self.h)
        self.cv = Canvas(root3, width=self.w, height=self.h)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.photo, anchor='nw')
        ######################################################
        heading_label = Label(root3, text="BOOK YOUR SEAT!!", fg='Yellow', bg="black", font="comicsans 27 bold").place(
            relx=0.5, rely=0.2, anchor='n')
        f1 = Frame(root3, width=200, height=150,borderwidth=7, relief=RIDGE,background="black")
        f1.place(relx=0.5, rely=0.5, anchor=CENTER)
        Label(f1, text="Source", fg='Yellow', bg="black", font="comicsans 16 bold",justify="left"
              ).grid(row=0,column=0,sticky="W")
        # Label(root3, text="Source", fg='Yellow', bg="black", font="comicsans 13 bold", borderwidth=5,padx=150,relief=SUNKEN).place(relx=0.5, rely=0.5,anchor=CENTER)
        ### initialize var


        self.source_combo=StringVar()
        self.desti_combo=StringVar()
        self.date_combo=StringVar()
        self.class_combo=StringVar()
        self.time_combo = StringVar()
        self.seat_combo = StringVar()



        ttk.Combobox(f1, height=11, width=17, values=["Lahore"],
                     textvariable = self.source_combo).grid(row=0,column=2)
        Label(f1, text="Destination", fg='Yellow', bg="black", font="comicsans 16 bold", borderwidth=2, relief=SUNKEN
              ).grid(row=1, column=0,sticky="W")
        ttk.Combobox(f1, height=11, width=17, values=["Karachi","Dubai","America","Saudia","Islamabad","Australia"],
                     textvariable = self.desti_combo).grid(row=1, column=2)
        Label(f1, text="Avaliable Dates", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2, relief=SUNKEN
              ).grid(row=2, column=0,sticky="W")
        ttk.Combobox(f1, height=11, width=17, values=["1/2/2020", "2/2/2020 ", "3/2/2020"],
                     textvariable= self.date_combo).grid(row=2, column=2)

        Label(f1, text="Class", fg='Yellow', bg="black", font="comicsans 16 bold", borderwidth=2,
              relief=SUNKEN
              ).grid(row=3, column=0,sticky="W")
        ttk.Combobox(f1, height=11, width=17, values=["Businuss", "Economy","Premium"],
                     textvariable=self.class_combo).grid(row=3, column=2)
        Label(f1, text="Avaliable time", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
              relief=SUNKEN
              ).grid(row=4, column=0,sticky="W")
        ttk.Combobox(f1, height=11, width=17, values=["7:00pm", "1:00pm ", "6:00pm","3:00pm"],
                     textvariable=self.time_combo).grid(row=4, column=2,)

        Label(f1, text="Seats", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
              relief=SUNKEN
              ).grid(row=5, column=0, sticky="W")
        ttk.Combobox(f1, height=11, width=17, values=["1", "2 ", "3", "4"],
                     textvariable=self.seat_combo).grid(row=5, column=2, )


        Button(root3,text="CONFIRM",fg="yellow",bg="black",font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=7, command= lambda: self.Search(lstofFlights,dis3=True,)).place(relx=0.5, rely=0.8, anchor='s')


        Button(root3,text="Back",fg="yellow",bg="black",font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=7, command= lambda: self.Screen2()).place(relx=0.5, rely=0.9, anchor='s')


    def Search(self, lst=[], dis3=False):
        global root4
        for flightOBJ in lst:
            if flightOBJ.source == self.source_combo.get() and flightOBJ.destination == self.desti_combo.get():
                if dis3 == True:
                    root3.destroy()
                else:
                    pass #yahan msg box banan hai yad se


                self.userFlight = flightOBJ

                root4 = Tk()
                root4.title("M&H Travels")
                root4.wm_iconbitmap('py.ico')
                self.photo = PhotoImage(file="12.png")
                self.w = self.photo.width()
                self.h = self.photo.height()
                root4.geometry("%dx%d+50+30" % (self.w, self.h))
                root4.maxsize(self.w, self.h)
                self.cv = Canvas(root4, width=self.w, height=self.h)
                self.cv.pack(side='top', fill='both', expand='yes')
                self.cv.create_image(0, 0, image=self.photo, anchor='nw')
                # print(self.source_combo.get(),self.desti_combo.get(),self.date_combo.get(),self.time_combo.get(),
                #       self.class_combo.get())
                heading_label = Label(root4, text="Fill your Billing details!!", fg='Yellow', bg="black",
                                      font="comicsans 27 bold",relief=SUNKEN,borderwidth=7).place(
                    relx=0.5, rely=0.14, anchor='n')
                f2 = Frame(root4, width=400, height=300, borderwidth=7, relief=SUNKEN, background="black")
                f2.place(relx=0.15, rely=0.6, anchor=CENTER)
                self.y=flightOBJ.pilot.get_pilot()
                self.st = flightOBJ.staff.get_staff()
                Label(f2, text=f"This is your booked ticket details\n Source: {self.source_combo.get()}\nDestination: {self.desti_combo.get()}\n Departure date: {self.date_combo.get()}\n Time: {self.time_combo.get()}\nSeat Class: {self.class_combo.get()}\n Pilot: {self.y}\n Staff: {self.st}\n Price: {flightOBJ.price}\n", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=0, column=0,sticky="W")



                f3 = Frame(root4, width=200, height=150, borderwidth=10, relief=SUNKEN, background="black")
                f3.place(relx=0.5, rely=0.6, anchor=CENTER)
                Label(f3, text="First Name", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=0, column=0, sticky="W")
                Label(f3, text="Last Name", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=1, column=0, sticky="W")
                Label(f3, text="Contact No", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=2, column=0, sticky="W")
                Label(f3, text="Address", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=3, column=0, sticky="W")
                Label(f3, text="Your NIC", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=4, column=0, sticky="W")
                Label(f3, text="Card No", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=5, column=0, sticky="W")
                Label(f3, text="Expiration", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                      relief=SUNKEN
                      ).grid(row=6, column=0, sticky="W")

                Button(root4, text="Book", fg="yellow", bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
                       borderwidth=7, command=self.msgwindow).place(relx=0.5, rely=0.87,anchor='s')

                Button(root4,text="Back",fg="yellow",bg="black",font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=7, command= lambda: self.book_Ticket()).place(relx=0.5, rely=0.97, anchor='s')
                Button(root4, text="Go to Home Page", fg="yellow", bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
                       borderwidth=7, command=lambda: self.Screen2(True,True)).place(relx=0.2, rely=0.98, anchor='s')
                self.name_ = StringVar()
                self.father_ = StringVar()
                self.contact_ = StringVar()
                self.address_ = StringVar()
                self.nic_ = StringVar()
                self.cardno = StringVar()
                self.cardexp = StringVar()


                self.userInput= Entry(f3, textvariable=self.name_,width=30).grid(row=0, column=1)
                self.fatInput = Entry(f3, textvariable=self.father_,width=30).grid(row=1, column=1)
                self.conInput= Entry(f3, textvariable=self.contact_,width=30).grid(row=2, column=1)
                self.adInput = Entry(f3, textvariable=self.address_,width=30).grid(row=3, column=1)
                self.nicInput = Entry(f3, textvariable=self.nic_,width=30).grid(row=4, column=1)
                self.cardInput = Entry(f3, textvariable=self.cardno, width=30).grid(row=5, column=1)
                self.exInput = Entry(f3, textvariable=self.cardexp, width=30).grid(row=6, column=1)
    def check_book(self,dis=False):
        global label1
        global root5
        if dis==True:
            root2.destroy()


        root5 = Tk()
        root5.title("M&H Travels")
        root5.wm_iconbitmap('py.ico')
        self.photo = PhotoImage(file="11.png")
        self.w = self.photo.width()
        self.h = self.photo.height()
        root5.geometry("%dx%d+50+30" % (self.w, self.h))
        root5.maxsize(self.w, self.h)
        self.cv = Canvas(root5, width=self.w, height=self.h)
        self.cv.pack(side='top', fill='both', expand='yes')
        self.cv.create_image(0, 0, image=self.photo, anchor='nw')
        ######################################################
        heading_label = Label(root5, text="This is you Booking details", fg='Yellow', bg="black", font="comicsans 27 bold").place(
            relx=0.5, rely=0.2, anchor='n')

        self.f9 = Frame(root5, width=200, height=150, borderwidth=7, relief=RIDGE, background="black")
        self.f9.place(relx=0.5, rely=0.5, anchor=CENTER)
        Button(root5, text="Back", fg="yellow", bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
               borderwidth=7, command=lambda: self.Screen2(True, True, True)).place(relx=0.5, rely=0.97, anchor='s')

        ps = passanger(self.name_.get(), self.father_.get(), self.address_.get(), self.contact_.get(), self.nic_.get())
        passanger.count+=1

        if ps.name1 != "":

            label1 = Label(self.f9, text=f"Flight No{self.userFlight._SEAT.flight_no} \n Name:{ps.name1}\n Source: {self.source_combo.get()}\nDestination: {self.desti_combo.get()}\n Departure date: {self.date_combo.get()}\n Time: {self.time_combo.get()}\nSeat Class: {self.class_combo.get()}\n Price: {self.userFlight.price}\n Seats:{self.seat_combo.get()} \n", fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                relief=SUNKEN).grid(row=0, column=0, sticky="W")


        else:
            Label(self.f9,
                  text="No Booking Detail available Go and Book your ticket now ",
                  fg='Yellow', bg="black", font="comicsans 16 bold ", borderwidth=2,
                  relief=SUNKEN).grid(row=0, column=0, sticky="W")

        self.btn1 = Button(root5, text="Cancel ticket", fg="yellow",
                           bg="black", font="comicsans 19 bold italic", relief=SUNKEN,
                           borderwidth=7, command=self.remove_)
        self.btn1.place(relx=0.34, rely=0.93, anchor=CENTER)

    def remove_(self):
        list = self.f9.grid_slaves()
        for i in list:
            i.destroy()
        print("Your ticket has successfully Cancel")
        my_w = Tk()
        my_w.geometry("500x500")  # Size of the window
        my_w.eval("tk::PlaceWindow %s center" % my_w.winfo_toplevel())
        my_w.withdraw()
        messagebox.showinfo("Cancel Ticket ", "Your Ticket has successfully Canceled")
        my_w.destroy()
        my_w.mainloop()







    def msgwindow(self):
        with open("input1.txt", 'a') as inFile1:#address without space
            inFile1.write(f"{self.name_.get()} {self.source_combo.get()} {self.desti_combo.get()} {self.userFlight._SEAT.flight_no} {self.date_combo.get()} {self.time_combo.get()} {self.class_combo.get()} {self.userFlight.price} {self.seat_combo.get()}\n")


        my_w = Tk()
        my_w.geometry("500x500")  # Size of the window
        my_w.eval("tk::PlaceWindow %s center" % my_w.winfo_toplevel())
        my_w.withdraw()
        if messagebox.askyesno("Confirm ", "Do you want to confirm your Purchase") == TRUE:
            self.x = int(self.userFlight._SEAT.seats_avai) - int(self.seat_combo.get())
            inFile = open("input.txt", "r+")
            outFile = open("output.txt", "w")
            f_NO= str(self.userFlight._SEAT.flight_no)
            seat_NO= str(self.userFlight._SEAT.seats_avai)
            count = 0
            for line in inFile:
                lstofWords = line.strip().split()
                count=0


                for words in lstofWords:
                    don= False
                    if don==False:
                        start = seat_NO == words
                    if seat_NO == words:
                        start = True

                        outFile.write(str(self.x) + " ")


                    else:
                        count+=1
                        outFile.write(words+" ")

                outFile.write('\n')




                    # else:
                    #     outFile.write(words+" ")


##                if f_NO == line[0]:
##                    z = str(line[4])
##                    for linee in inFile:
##                        print(linee.replace(z, str(self.x)))
##                        inFile.replace(z, str(self.x))


            inFile.close()
            outFile.close()

            messagebox.showinfo("Success ", "Purchase has successfully Done")

        else:
            print("Ticket is not booked")

        # my_w.deiconify()
        my_w.destroy()
        my_w.mainloop()







## pehle , lstofFlight pass karani ha search ke func mein


def main():
    global root
    global lstofFlights
    root = Tk()
    root.wm_iconbitmap('py.ico')
    inFile = open("output.txt", "r")
    lstofFlights = []

    for line in inFile:
        lstofWords = line.strip().split()
        lstofFlights.append(flight(lstofWords[1], lstofWords[2], lstofWords[3], int(lstofWords[0]), int(lstofWords[4]), [lstofWords[5], lstofWords[6]],
                                    [lstofWords[7], lstofWords[8]], lstofWords[9]))

    for e in lstofFlights:
        print(e.printing())
    inFile.close()
    passangerOBJ = passanger()
    call_airline = Book_Ticket(root, passangerOBJ)

    root.mainloop()


main()










