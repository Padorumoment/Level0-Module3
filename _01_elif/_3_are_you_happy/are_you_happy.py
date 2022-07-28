from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    b1 = simpledialog.askstring('', 'Are you happy?')
    if(b1 == 'yes'):
        messagebox.showinfo('', "Keep doing what you're doing")
    elif(b1 == 'no'):
        b2 = simpledialog.askstring('', 'Do you want to be happy?')
    if (b2 == 'no'):
        messagebox.showinfo('', "Keep doing what you're doing")
    elif (b2 == 'yes'):
        messagebox.showinfo('', 'Change something')

    pass
