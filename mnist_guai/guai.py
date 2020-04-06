import pygame
from pygame.locals import *
import random
from sklearn.externals import joblib
from skimage import color, io
from skimage.transform import resize
import matplotlib.image as mpimg
import os 


MODEL = joblib.load('mnist_guai/log_reg.pkl')


def prediction(model, img):
    #resize img
    img = resize(img, (28,28))
    #print(resized_img.reshape(-1).shape)

    prediction = model.predict([img.reshape(-1)])

    return prediction



pygame.init()


#colors 
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0, 0, 0)
colors = [BLACK, WHITE]

# Defines the display size with a width and height of 600, 600
width, height = 600, 600
size = (width, height)
 
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
# Draws the screen using the size
 
pygame.display.set_caption("mnist guai")
# Displays the title at the top of the draw screen
 

 
 
keep_going = True
# The program continues until you close the window and type exit() in the shell
 
#radius = radius + 20    
radius = 30
 
#pen_size = pen_size + 5   
pen_size = 100  # This variable is not used
 
mousedown = False   # we have not started drawing yet
keep_going = True   # The program continues unti you close the window and type exit() in the shell
 
# MAIN LOOPwhile keep_going != False:   # this can be done more pythonic
while keep_going:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
        
        if event.type == pygame.KEYDOWN and event.key == K_s:
            ID = random.randint(1,10000)
            img_path = f"mnist_guai/screenshots/window{ID}.png"
            img = pygame.image.save(screen, img_path)
            read_img = io.imread(img_path, as_gray=True)
            print(f'loaded {img_path}')
            pred = prediction(MODEL, read_img)
            print(pred)
            
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            screen.fill(BLACK)

        if event.type == pygame.KEYDOWN and event.key == K_d:
            #delete unnecessary files
            folder = 'mnist_guai/screenshots'
            for file_name in os.listdir(folder):
                file_path = os.path.join(folder, file_name)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                     print('Failed to delete %s. Reason: %s' % (file_path, e))
 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousedown = True
             
        if event.type == pygame.MOUSEBUTTONUP:
            mousedown = False
     
    if mousedown: # start drawing
        spot = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1:
            button_color = colors[1]
        elif pygame.mouse.get_pressed()[2] == 1:
            button_color = colors[0]
        
 
 
        pygame.draw.circle(screen, button_color, spot, radius)
    
 
    pygame.display.update()
 
pygame.quit()

