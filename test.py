# import tkinter as tk


# # Define the data points
# data = [20, 15, 10, 7, 5, 4, 3, 2, 1, 1, 0]

# root = tk.Tk()
# root.title("Bar Graph")

# c_width = 400  # Define it's width
# c_height = 350  # Define it's height
# c = tk.Canvas(root, width=c_width, height=c_height, bg='white')
# c.pack()

# # The variables below size the bar graph
# y_stretch = 15  # The highest y = max_data_value * y_stretch
# y_gap = 20  # The gap between lower canvas edge and x axis
# x_stretch = 10  # Stretch x wide enough to fit the variables
# x_width = 20  # The width of the x-axis
# x_gap = 20  # The gap between left canvas edge and y axis

# # A quick for loop to calculate the rectangle
# for x, y in enumerate(data):

#     # coordinates of each bar

#     # Bottom left coordinate
#     x0 = x * x_stretch + x * x_width + x_gap

#     # Top left coordinates
#     y0 = c_height - (y * y_stretch + y_gap)

#     # Bottom right coordinates
#     x1 = x * x_stretch + x * x_width + x_width + x_gap

#     # Top right coordinates
#     y1 = c_height - y_gap

#     # Draw the bar
#     c.create_rectangle(x0, y0, x1, y1, fill="red")

#     # Put the y value above the bar
#     c.create_text(x0 + 2, y0, anchor=tk.SW, text=str(y))

# root.mainloop()

#Import the required library

import tkinter as tk
from tkinter import ttk


LARGEFONT =("Verdana", 35)

class tkinterApp(tk.Tk):
  
  # __init__ function for class tkinterApp
  def __init__(self, *args, **kwargs):
    
    # __init__ function for class Tk
    tk.Tk.__init__(self, *args, **kwargs)
    
    # creating a container
    container = tk.Frame(self)
    container.pack(side = "top", fill = "both", expand = True)

    container.grid_rowconfigure(0, weight = 1)
    container.grid_columnconfigure(0, weight = 1)

    # initializing frames to an empty array
    self.frames = {}

    # iterating through a tuple consisting
    # of the different page layouts
    for F in (StartPage, Page1, Page2):

      frame = F(container, self)

      # initializing frame of that object from
      # startpage, page1, page2 respectively with
      # for loop
      self.frames[F] = frame

      frame.grid(row = 0, column = 0, sticky ="nsew")

    self.show_frame(StartPage)

  # to display the current frame passed as
  # parameter
  def show_frame(self, cont):
    frame = self.frames[cont]
    frame.tkraise()

# first window frame startpage

class StartPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    
    # label of frame Layout 2
    label = ttk.Label(self, text ="Startpage", font = LARGEFONT)
    
    # putting the grid in its place by using
    # grid
    label.grid(row = 0, column = 4, padx = 10, pady = 10)

    button1 = ttk.Button(self, text ="Page 1",
    command = lambda : controller.show_frame(Page1))
  
    # putting the button in its place by
    # using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)

    ## button to show frame 2 with text layout2
    button2 = ttk.Button(self, text ="Page 2",
    command = lambda : controller.show_frame(Page2))
  
    # putting the button in its place by
    # using grid
    button2.grid(row = 2, column = 1, padx = 10, pady = 10)

    


# second window frame page1
class Page1(tk.Frame):
  
  def __init__(self, parent, controller):
    
    tk.Frame.__init__(self, parent)
    label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
    label.grid(row = 0, column = 4, padx = 10, pady = 10)

    # button to show frame 2 with text
    # layout2
    button1 = ttk.Button(self, text ="StartPage",
              command = lambda : controller.show_frame(StartPage))
  
    # putting the button in its place
    # by using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)

    # button to show frame 2 with text
    # layout2
    button2 = ttk.Button(self, text ="Page 2",
              command = lambda : controller.show_frame(Page2))
  
    # putting the button in its place by
    # using grid
    button2.grid(row = 2, column = 1, padx = 10, pady = 10)




# third window frame page2
class Page2(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
    label.grid(row = 0, column = 4, padx = 10, pady = 10)

    # button to show frame 2 with text
    # layout2
    button1 = ttk.Button(self, text ="Page 1",
              command = lambda : controller.show_frame(Page1))
  
    # putting the button in its place by
    # using grid
    button1.grid(row = 1, column = 1, padx = 10, pady = 10)

    # button to show frame 3 with text
    # layout3
    button2 = ttk.Button(self, text ="Startpage",
              command = lambda : controller.show_frame(StartPage))
  
    # putting the button in its place by
    # using grid
    button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
