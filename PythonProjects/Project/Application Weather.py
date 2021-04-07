import tkinter as tk

HEIGHT = 700
WIDTH = 800

def test_funtion(entry):
    print('This is the entry: ' + entry)


root = tk.Tk()
root.title('Application Weather')

canavas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canavas.pack()

# background_image = tk.PhotoImage(file = r'C:/Users/ABC/PycharmProjects/PythonProjects/Project/landscape.png')
# background_label = tk.Label(root, image = background_image)
# background_label.place(relwidth = 1, relheight = 1)
# photo = tk.PhotoImage(file = "lanscape.png")
# label = tk.Label(root, image = photo)
# label.pack()


frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)#, bg = 'green')
entry.place(relwidth = 0.65, relheight = 1)#grid(row = 2, column = 2)#pack(side = 'left', fill = 'both')

button = tk.Button(frame, text = 'Get Weather',font = 40 , command =lambda: test_funtion(entry.get()))
button.place(relx = 0.7, relheight = 1, relwidth = 0.3)#pack(side = 'left', fill = 'x', expand = True) #grid(row = 0, column = 0)

lower_frame = tk.Frame(root, bg = '#80c1ff', bd = 10)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)#grid(row = 1, column = 1)#pack(side = 'left', fill = 'both')


root.mainloop()