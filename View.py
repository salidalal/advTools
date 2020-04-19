import logic
import tkinter as tk

def search():
    logic.main(e1.get(), e2.get() )


master = tk.Tk()
tk.Label(master,
         text="Please insert tweeter user:").grid(row=0)
tk.Label(master,
         text="Please insert key word:").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master,
          text='Search', command=search).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()




