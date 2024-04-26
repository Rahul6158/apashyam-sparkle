import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
import io

st.title("Scratch and Draw")

# Initialize canvas
canvas_width = 400
canvas_height = 400
canvas_image = Image.new('RGB', (canvas_width, canvas_height), (255, 255, 255))
draw = ImageDraw.Draw(canvas_image)

# Display canvas
st.image(canvas_image, caption='Draw on the canvas', width=400, use_column_width=False)

# Function to scratch on the canvas
def scratch_canvas(canvas_image, x, y):
    draw = ImageDraw.Draw(canvas_image)
    draw.rectangle([x-5, y-5, x+5, y+5], fill='black')

# Mouse events
is_scratching = False
last_x, last_y = None, None
mousedown = st.button('Scratch on the canvas')

if mousedown:
    is_scratching = True

if is_scratching:
    x, y = st.beta_columns([1, 1])
    x.write('X Coordinate:')
    y.write('Y Coordinate:')
    x_coord = x.number_input('X', 0, canvas_width, step=1)
    y_coord = y.number_input('Y', 0, canvas_height, step=1)
    
    if last_x is not None and last_y is not None:
        scratch_canvas(canvas_image, last_x, last_y)

    last_x, last_y = x_coord, y_coord

    scratch_canvas(canvas_image, x_coord, y_coord)
    st.image(canvas_image, caption='Draw on the canvas', width=400, use_column_width=False)
else:
    last_x, last_y = None, None
    is_scratching = False
