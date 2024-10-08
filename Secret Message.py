from tkinter import *    #importing all classes, functions and constants from tkinter
from tkinter import messagebox   #imports standard dialog boxes which displays simple pop-up messages to user
import base64 #this is used for encoding and decoding data.
import os  #provides functions for interacting with the operating system

def decrypt():  #this function is designed to handle decryption using Base64. 
    password=code.get()  #retrieves the password entered by the user and then stores it in variable named password

    #if the password entered by the user is 1234 then the text will be decrypted
    if password == "1234":   
        s3=Toplevel(s)   #creates a new window that will have the decrypted text
        s3.title("Decryption")  #title of the new window
        s3.geometry("400x200")  #size of the new window
        s3.configure(bg="#00bd56")  #changes the background color of the new window to green

        #retrieves the text that needs to be decrypted from tkinter.Text widget and starts decrypting from line 1, character 0 (1,0) and goes to the end of the text
        msg=text.get(1.0, END)  
        decode_msg=msg.encode("ascii")  #converting the retrived msg from text widget into bytes encoded in ASCII format
        base64_bytes=base64.b64decode(decode_msg) #decoding the Base64-encoded msg into its original byte form
        decrypt=base64_bytes.decode("ascii")  #converting decoded byte msg back into ASCII string (decrypted msg)


        Label(s3,text="Decrypt", font="arial",fg="white",bg="#00bd56").place(x=10,y=0) #adding a decrypt label to the new window and setting its font, color, position
        text2 = Text(s3, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0) #creating a new text widget. This will show the decrypted message.
                                                                                       #provides a groove borded around the text and wraps the text by word. 

        text2.place(x=10, y=40, width=380, height=150) #positioning the text widget within the window and setting its size

        text2.insert(END,decrypt) #inserts the decrypted msg into text2 widget at the end of the text field, displaying it to the user

    elif password=="":
        messagebox.showerror("encryption","Input Password") #if the user didn't input any password, then this error msg will display

    elif password !="1234":
        messagebox.showerror("encryption", "Invalid Password") #if the password inputted by the user is wrong, then this error msg will pop up

def encrypt():  #this function is designed to handle encryption using Base64
    password=code.get() #retrieves the password entered by the user by the user and stores it in a variable named password. 

    if password == "1234":   #if the password entered by the user is 1234 then the text will be encrypted
        s2=Toplevel(s)  #creates a new window that will have the encrypted text 
        s2.title("Encryption")  #title of the new window
        s2.geometry("400x200")  #size of the new window
        s2.configure(bg="#ed3833")  #changes the background color of the new window to red

        msg=text.get(1.0, END)  #retrieves the text that needs to be encrypted from the tkinter.Text widget and starts encrypting from line 1, character 0 and goes to the end of the text 
        encode_msg=msg.encode("ascii") #converting the retrieved msg from text widget into bytes using ASCII encoding
        base64_bytes=base64.b64encode(encode_msg)  #encodes the ASCII-encoded msg into Base64 format. Base64 is used to encode binary data into text format.
        encrypt=base64_bytes.decode("ascii") #decodes the Base64-encoded bytes back into an ASCII string


        Label(s2,text="Encrypt", font="arial",fg="white",bg="#ed3833").place(x=10,y=0) #adding an encrypt label to the new window and setting its font, color and position
        text2 = Text(s2, font="Rpbote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0) #creating a new text widget. This one will show the encrypted msg.
                                                                                       #provides a groove border around the text and wraps the text by word.
        text2.place(x=10, y=40, width=380, height=150)  #positioning the text widget within the window and setting its size. 

        text2.insert(END,encrypt) #insets the encrypted msg into text2 widget at the end of the text field, displaying it to the user

    elif password=="":
        messagebox.showerror("encryption","Input Password") #if the user didn't input any password, then this error msg will display

    elif password !="1234":
        messagebox.showerror("encryption", "Invalid Password") #if the password inputted by the user is wrong, then this error msg will pop up

def main_screen():

    global s  #declaring s as a global variable, allowing it to be accessible in encryption and decryption functions
    global code #declaring code as a global variable, this will store the secret key entered by the user
    global text #declaring text as a global variable, this text refers to the text widget where the user enters the msg to either be decrypted or encrypted
    
    s = Tk()  #initializing the main window of the application 
    s.geometry("375x398")  #setting the size of the window to 375x398 pixels
    s.title("Secret Message App")  #setting the title of the window to "Secret Message"

    def reset():  #reset function 
        code.set("")  #this clears the value of the code field that stores the secret key
        text.delete(1.0, END)  #deletes all the text in the Text widget
    
    Label(text = "Enter text for Encryption and Decryption", fg = "black", font=("arial", 13)).place(x=10,y=10)  #label that tells the user to enter text. setting its font, size and position 
    text = Text(font="calbri", bg = "white", relief = GROOVE, wrap=WORD, bd = 0)  #this is created so that the user can input the msg. setting the font and background color. No border is applied
    text.place(x=10,y=50, width=355,height=100) #

    Label(text = "Enter Secret Key for Encryption and Decryption", fg="black", font=("calibri",13)).place(x=10,y=170) #creates an entry widget where the user can input the secret key

    code=StringVar() #stores the secret key entered by the user
    Entry(textvariable=code, width=19, bd=0, font=("arial",20), show = "*").place(x=10, y=200) #binds the entry widget to code variable allowing the variable to store the secret key. * is used to mask the password.

    #Encrypt Button triggers the encrypt() function. Decrypt Button triggers the decrypt() function. Reset button triggers the reset() function. 
    Button(text = "Encrypt", height = "2", width = 23, bg = "#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text = "Decrypt", height = "2", width=23, bg="#00bd56", fg="white", bd=0,command=decrypt).place(x=200, y=250)
    Button(text="Reset", height="2",width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    
    #starts the tkinter main event loop, constantly listening for user input and this remains running until the window is closed. 
    s.mainloop()
 
main_screen()
