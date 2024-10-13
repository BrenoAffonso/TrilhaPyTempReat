import tkinter as tk

root=tk.Tk()
root.title('Test1')

def addToList():
    text=entry.get()
    if text:
        textList.insert(tk.END, text)
        entry.delete(0, tk.END)

def addToList():
    text=entry.get()
    if text:
        textList.insert(tk.END, text)
        entry.delete(0, tk.END)

def addToList2():
    text=entry2.get()
    if text:
        textList2.insert(tk.END, text)
        entry2.delete(0, tk.END)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame2=tk.Frame(root)
frame2.grid(row=0, column=1, sticky='nsew')

frame2.columnconfigure(0,weight=1)
frame2.rowconfigure(1, weight=1)

entry2=tk.Entry(frame2)
entry2.grid(row=0, column=0, sticky='ew')

entry2.bind("<Return>", lambda event: addToList2())

entryBtn2= tk.Button(frame2, text='Add', command=addToList2)
entryBtn2.grid(row=0, column=1)

textList2=tk.Listbox(frame2)
textList2.grid(row=1, column=0, columnspan=2, sticky='nsew')

frame=tk.Frame(root)
frame.grid(row=0, column=0, sticky='nsew')

frame.columnconfigure(0,weight=1)
frame.rowconfigure(1, weight=1)

entry=tk.Entry(frame)
entry.grid(row=0, column=0, sticky='ew')

entry.bind("<Return>", lambda event: addToList())

entryBtn= tk.Button(frame, text='Add', command=addToList)
entryBtn.grid(row=0, column=1)

textList=tk.Listbox(frame)
textList.grid(row=1, column=0, columnspan=2, sticky='nsew')

root.mainloop()