# Importing all packages
from tkinter import *
import tkinter
from tkinter.ttk import *
from PIL import Image
from tkinter.filedialog import askopenfilename, asksaveasfilename
from model import *

print('GUI SYSTEM STARTED...')

def OpenFile():
        try:
            a = askopenfilename()
            print(a)
            value, classes = main(a)
            image = Image.open(a)
            # plotting image
            file = image.convert('RGB')
            plt.figure("Result")
            plt.imshow(np.array(file))
            plt.title(f'Severity scale: {value} , Stage : {classes}')
            plt.show()
            print('Thanks for using the system !')
        except Exception as error:
            print("File not selected ! Exiting..., Please try again")

#-----------------------------------------------------------------------------------------

#GUI

root = Tk()
root.geometry('700x300')
root.title("Diabetic retionopathy detection")
root.configure(bg='blanched almond')
label1 = tkinter.Label(root, text="DR detection", font=('Arial', 30),bg="blanched almond")
label1.grid(padx=20, pady=10, row=0, column=0)
scale=tkinter.Label(text="Scale: Severity of DR",bg="white",font=('Arial', 12,'bold'))
scale.grid(row=1,column=0,sticky='W',padx=20)
instru=tkinter.Label(text='\n0: No DR\n\n 1: Mild\n\n 2: Moderate\n\n 3: Severe\n\n 4: Proliferative',bg="blanched almond",font=('Arial', 12))
instru.grid(row=2,column=0, sticky = 'W',padx=20)

l1=tkinter.Label(text="Upload the fundus image to get results",bg="white",font=('Arial', 10))
l1.grid(row=1,column=3)

button1 = tkinter.Button(root, text="Upload Image",bg="midnight blue",fg='white',command=OpenFile)
button1.grid(row=2, column=3)

root.mainloop()
