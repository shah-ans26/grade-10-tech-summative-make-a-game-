from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from playsound import playsound
from perlin_noise import PerlinNoise
import math
app = Ursina()
player = FirstPersonController()
Sky()

noise = PerlinNoise(octaves=3, seed=42)
boxes = []

block_count = 20
noise = PerlinNoise(octaves=3, seed=42)

boxes = []
for i in range(40):     
    for j in range(40):
        scale = 20 
        y_val = noise([j / scale, i / scale]) * 6
        
        y_val = floor(y_val) 

        box = Button( color=color.white,model='cube',position=(j, y_val, i),texture='grass',parent=scene,origin_y=0.5)
        
        boxes.append(box)
    
def input(key):
  global block_count
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        if block_count >= 1:
          new = Button(color=color.white, model='cube', position=box.position + mouse.normal,texture='grass.png', parent=scene, origin_y=0.5)
          boxes.append(new)
          block_count -= 1
        else:
          print("you dont have any blocks left")
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)
        block_count += 1

def update():
  print(player.position)
  
    
bottom_counter = Text(text=str(block_count),parent=camera.ui,origin=(0, -1),position=(0, -0.45),scale=4,color=color.lime)

def update():
    global block_count
    bottom_counter.text = str(int(block_count))

app.fullscreen = True
app.run()
