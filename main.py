from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  #
co11 = "#f2f4f2"


# Create Window

window = Tk()
window.title("")
window.geometry('380x500')
window.configure(background=co1)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")

#######################Frames###################################

frame_Up = Frame(window, width=380, height=50, bg=co1, relief='flat')
frame_Up.grid(row=0, column=0, columnspan=2)

frame_Down = Frame(window, width=380, height=400, bg=co1, relief='flat')
frame_Down.grid(row=2, column=0, pady=10)

frame_Result = Frame(window, width=364, height=50, bg=co3, relief='flat')
frame_Result.grid(row=1, column=0, pady=10)

#####################Divide Frame################################

frames_Actives = Frame(frame_Down,width=180, height=370, bg=co9, relief='flat')
frames_Actives.grid(row=0, column=0, pady=0, padx= 5)

frames_Passive = Frame(frame_Down, width=180, height=370, bg=co9, relief='flat')
frames_Passive.grid(row=0, column=1, pady=0)

#####################Logo##########################################

#Open Image

app_img = Image.open('money.png')
app_img = app_img.resize((50,50))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frame_Up, image=app_img, width=900, compound=LEFT, padx=5, relief=FLAT, anchor=NW,bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_ = Label(frame_Up,text="Wealth Calculator",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Ivy 12'),bg=co1, fg=co4 )
app_.place(x=50, y=0)

l_row = Label(frame_Up, width=380, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
l_row.place(x=0, y=47)


##############################ACTIVES####################################

#Function for equity

def calculate():
    #Actives:
    active1 = e_house_value.get()
    active2 = e_value_properties.get()
    active3 = e_value_vehicles.get()
    active4 = e_value_investments.get()
    active5 = e_others_actives.get()

    #Passives
    passive1 = e_value_mortgage.get()
    passive2 = e_value_car.get()
    passive3 = e_value_student.get()
    passive4 = e_value_debts.get()

    if active1 == '' or active2 == '' or active3 == '' or active4 == '' or active5 == '' or passive1 == '' or passive2 == '' or passive3 == '' or passive4 == '':

            print('Entra algum valor')

            return
    else:
        Total_actives = float(active1) + float(active2) + float(active3) + float(active4) + float(active5)
        Total_passives = float(passive1) + float(passive2) + float(passive3) + float(passive4)

        # NET
        Net = Total_actives - Total_passives

        l_result['text'] = '${:,.2f}'.format(Net)







l_name = Label(frames_Actives,  text='Entry Actives', padx=10, width=35, height=1, anchor=NW, font=('Verdana 11 '), bg=co2, fg=co1)
l_name.place(x=0, y=0)

# Home Value

l_house = Label(frames_Actives, text='House Value', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_house.place(x=10, y=40)

e_house_value = Entry(frames_Actives, width=10, font=('Ivy 12 '), justify='center', relief="solid")
e_house_value.place(x=10, y=65)

# Properties

l_properties = Label(frames_Actives, text='Properties', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_properties.place(x=10, y=105)

e_value_properties = Entry(frames_Actives, width=10, font=('Ivy 12 '), justify='center', relief="solid")
e_value_properties.place(x=10, y=125)

# Vehicles

l_vehicles = Label(frames_Actives, text="Vehicles", height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_vehicles.place(x=10, y=165)

e_value_vehicles = Entry(frames_Actives, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_value_vehicles.place(x=10, y=195)

# Investments and Savings

l_Investments = Label(frames_Actives, text='Investments', height=1, anchor=E, font=('Verdana 9'), bg=co9, fg=co0)
l_Investments.place(x=10, y= 230)

e_value_investments = Entry(frames_Actives, width=10, font=('Ivy 12 '), justify='center', relief='solid')
e_value_investments.place(x=10, y=255)

####################################Others Actives######################################

l_actives = Label(frames_Actives, text="Outros ativos", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_actives.place(x=10, y=295)

e_others_actives = Entry(frames_Actives,width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_others_actives.place(x=10, y=315)

# Entrando Passivos -------------------------------------------------------

l_nome = Label(frames_Passive, text="Entry Passives",padx=10, width=35, height=1,anchor=NW, font=('Verdana 11 '), bg=co5, fg=co1)
l_nome.place(x=0, y=0)

# Mortgage ($)
l_mortgage = Label(frames_Passive, text="Mortgage", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_mortgage.place(x=10, y=40)

e_value_mortgage = Entry(frames_Passive, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_value_mortgage.place(x=10, y=65)


#  Car Loans
l_car = Label(frames_Passive, text="Car Loans", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_car.place(x=10, y=105)

e_value_car = Entry(frames_Passive, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_value_car.place(x=10, y=125)


# Student Loans
l_student = Label(frames_Passive, text="Student Loans", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_student.place(x=10, y=165)

e_value_student = Entry(frames_Passive, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_value_student.place(x=10, y=195)


# Other Debts
l_debts = Label(frames_Passive, text="Other Debts", height=1,anchor=E, font=('Verdana 9 '), bg=co9, fg=co0)
l_debts.place(x=10, y=230)

e_value_debts = Entry(frames_Passive, width=10, font=('Ivy 12 '), justify='center',relief="solid")
e_value_debts.place(x=10, y=255)

#Result

l_result = Label(frame_Result, text="$ {:,.2f}".format(00), padx=10, width=15, height=1, anchor=NE, font=('Verdana 25 bold'), bg=co3, fg=co1)
l_result.place(x=0, y=7)

button_calculate = Button(frames_Passive, command=calculate, width=12, anchor=CENTER, text="Calculate".upper(), overrelief=RIDGE,  font=('ivy 9 bold '),bg=co1, fg=co0 )
button_calculate.place(x=10, y=310)



window.mainloop()