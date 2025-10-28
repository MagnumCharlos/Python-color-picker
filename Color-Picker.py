from pynput.mouse import Controller
import getpixelcolor
import tkinter as tk
from tkinter import Canvas



i = input()
mouse = Controller()
pos = []
pos = mouse.position
x = pos[0]
y = pos[1]
print(x, y)

rgb_color = getpixelcolor.pixel(x, y)

print(getpixelcolor.pixel(x, y))

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb  # Convert (R, G, B) to Hex

hex_color = rgb_to_hex(rgb_color)



# Create a window
root = tk.Tk()
canvas = Canvas(root, width=300, height=300)
canvas.pack()


canvas.create_rectangle(0, 0, 300, 300, fill=hex_color)




text = tk.Text(root, height=8)
text.pack(padx=10, pady=10, expand=True,fill=tk.BOTH)

text.insert(
    index='1.0', 
    chars= f"rgb = {rgb_color}, hex = {hex_color}"
)




# Run the application
root.mainloop()
