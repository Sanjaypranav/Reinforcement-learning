# Description: This is a simple example of how to use the gym environment
import gym                                          
import numpy as np                                  
import random
                   
# used to help with visualizing in Colab                 
from IPython.display import display, clear_output   
from time import sleep

# create Taxi environment
env = gym.make('Taxi-v3', render_mode="rgb_array")
# create a new instance of taxi, and get the initial state
state = env.reset()

print(f"Initial state: {state}")


import os
os.environ['SDL_VIDEODRIVER']='dummy'
import pygame
pygame.display.set_mode((640,480))

num_steps = 99
for s in range(num_steps+1):

    clear_output(wait=True) 

    print(f"step: {s} out of {num_steps}")

    # sample a random action from the list of available actions
    action = env.action_space.sample()

    # perform this action on the environment
    env.step(action)

    # print the new state
    img =env.render()

    sleep(0.2)

# end this instance of the taxi environment
pygame.quit()

import matplotlib.pyplot as plt

print(img.shape)


plt.imshow(img)
plt.imsave(fname='Data/img/ex1/taxi.png', arr=img)

