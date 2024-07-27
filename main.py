import pygame as pg
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import random
import math
from subprocess import call
pg.mixer.init()

begin_sound=pg.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\HeatleyBros - HeatleyBros II - 01 8 Bit Beginning.mp3")
click_sound=pg.mixer.Sound("E:\SEMESTER 8\Computer Graphics\lab\Mouse-Click-00-c-FesliyanStudios.com.mp3")


def load_texture(texture_path):
    # Load the image file using Pygame
    image = pg.image.load(texture_path)
    image_data = pg.image.tostring(image, "RGBA", 1)

    # Create an OpenGL texture object
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Apply the image data to the texture
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id


def draw_rect_2(x1,y1,x2,y2,x3,x4):
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_QUADS)

    glColor4f(0.95, 0.8, 0.8, 0.3)#shade on head pink
    glVertex2f(x1, y1)
    glVertex2f(x2, y1)
    glVertex2f(x3, y2)
    glVertex2f(x4, y2)
    
    glEnd()
    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING) 

def draw_rect_3(x1,y1,x2,y2,x3,y3,x4,y4):
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_QUADS)

    glColor4f(0.95, 0.8, 0.8, 0.3)#shades on side pink
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glVertex2f(x4, y4)
    
    glEnd()
    glDisable(GL_BLEND)
    glEnable(GL_LIGHTING) 

def draw_rect(x1,y1,x2,y2,texture_id):
    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glBegin(GL_QUADS)

    glColor3f(1, 1, 1)
    glTexCoord2f(0, 1)
    glVertex2f(x1, y1)  
    glTexCoord2f(0, 0)
    glVertex2f(x1, y2)  
    glTexCoord2f(1, 0)
    glVertex2f(x2, y2)   
    glTexCoord2f(1, 1)
    glVertex2f(x2, y1) 
    
    glEnd()
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING) 


def draw_sphere(radius,x_center,y_center,angle, slices, stacks, texture_id):
    phi_step = math.pi / stacks
    theta_step = 2 * math.pi / slices
    glDisable(GL_LIGHTING)
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTranslatef(x_center, y_center, 0.0)  

    #glRotatef(angle, 0.0, 1.0, 0.0)  # Rotate around the z-axis (0.0, 0.0, 1.0)


    for i in range(stacks):
        phi = i * phi_step
        phi_next = (i + 1) * phi_step

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            theta = j * theta_step

            x = x_center+radius * math.sin(phi) * math.cos(theta)
            y = y_center+radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(phi)

            x_next =x_center +radius * math.sin(phi_next) * math.cos(theta)
            y_next = y_center+radius * math.sin(phi_next) * math.sin(theta)
            z_next = radius * math.cos(phi_next)

            glTexCoord2f(1 - (theta / (2 * math.pi)), phi / math.pi)
            glVertex3f(x, y, z)

            glTexCoord2f(1 - (theta / (2 * math.pi)), phi_next / math.pi)
            glVertex3f(x_next, y_next, z_next)

        glEnd()
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)  


       
def DrawCircleWithTexture(radius, segments, x, y,z,texture_id):
    """
    Parameters:
    radius (float): The radius of the circle.
    segments (int): The number of segments to use to approximate the circle.
    x (float): The x-coordinate of the center of the circle.
    y (float): The y-coordinate of the center of the circle.
    z (float): The z-coordinate of the center of the circle.
    texture_id (int): The OpenGL texture ID.
    """
    glDisable(GL_LIGHTING)
    angle = 0
    step = 2 * 3.14159 / segments

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    

    glBegin(GL_TRIANGLE_FAN)
    #glColor3f(1, 1, 1)
    #glVertex3f(x, y, z)

    for i in range(segments + 1):
        #glColor3f(1.0, 1.0, 0.5)  # Pastel yellow 
        glTexCoord2f((math.cos(angle) + 1) / 2, (math.sin(angle) + 1) / 2)
        glVertex3f(x + radius * math.cos(angle), y + radius * math.sin(angle), z)
        angle += step
    glEnd()
    glDisable(GL_BLEND)
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING) 
    

def main():
    pg.init()
    begin_sound.play()

    display=(800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]),0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glClearColor(1.0, 0.95, 0.95, 1.0) 

    angle = 0  

   #sphere
    texture_id = load_texture("E:\SEMESTER 8\Computer Graphics\lab\sunset.jpg") 
    #play
    texture_id2 =load_texture("E:\SEMESTER 8\Computer Graphics\lab\play1.png")
    #angrybirds logo
    texture_id3 =load_texture("E:\SEMESTER 8\Computer Graphics\lab\logo3.png")

    #bird
    texture_id4 =load_texture("E:\SEMESTER 8\Computer Graphics\lab\pinkbird.png")
  
    

    #sparkles
    texture_id_s1 =load_texture("E:\SEMESTER 8\Computer Graphics\lab\sparkles.png")
    texture_id_s2 =load_texture("E:\SEMESTER 8\Computer Graphics\lab\sparlkesmany.png")
    texture_id_s3 =load_texture("E:\SEMESTER 8\Computer Graphics\lab\—Pngtree—lens flare white sparkling light_8415861.png")
    



    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            elif event.type == pg.MOUSEBUTTONDOWN:
              mouse_x, mouse_y = pg.mouse.get_pos()
              print("Mouse position:", mouse_x, mouse_y)
                # Convert mouse coordinates to OpenGL coordinates
              opengl_mouse_x = (mouse_x / display[0]) * 2 - 1
              opengl_mouse_y = -(mouse_y / display[1]) * 2 + 1
              print("OpenGL mouse position:", opengl_mouse_x, opengl_mouse_y)
                # Check if the mouse click position is within the rectangle
                #x2   x1         y2  y1         
              if -0.185 <= opengl_mouse_x <= 0.177 and -0.54 <= opengl_mouse_y <= -0.48:
                 pg.quit()
                 call(["python","game.py"])
                 print("rectangle")
                 

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_rect_2(-3,3,-1,0,0,0.5)
        draw_rect_2(3,3,1,0,0,0.5)

        draw_rect_3(3,0.7,3,0,0,0,0.5,0)
        draw_rect_3(-3,0.7,-3,0,0,0,0.5,0)

        draw_rect_2(-3,-3,-1,0,0,0.5)
        draw_rect_2(3,-3,1,0,0,0.5)

        glColor3f(1,1,1)


        glPushMatrix()
        glRotatef(angle, 1, 0, 0)  
        draw_sphere(1.5,0,0,45,32,50,texture_id)
        glPopMatrix()

        #play

        draw_rect(-0.7,-0.8,0.7,-1.3,texture_id2)

        #logo

        draw_rect(-2,1.5,2,0.5,texture_id3)

        #sparkles      

        for _ in range(5):
            x_s = random.uniform(-2.9, -1.5)
            y_s = random.uniform(-2.5, 2.5)
            DrawCircleWithTexture(0.1,36,x_s,y_s,0,texture_id_s3)

        for _ in range(5):
            x_s = random.uniform(-2.9, -1.5)
            y_s = random.uniform(-2.5, 2.5)
            DrawCircleWithTexture(0.1,36,x_s,y_s,0,texture_id_s2)

        for _ in range(5):
            x_s = random.uniform(-2.9, -1.5)
            y_s = random.uniform(-2.5, 2.5)
            DrawCircleWithTexture(0.1,36,x_s,y_s,0,texture_id_s3)

    


        for _ in range(5):
            x_s1 = random.uniform(2.9, 1.5)
            y_s1 = random.uniform(-2.5, 2.5)
            DrawCircleWithTexture(0.1,36,x_s1,y_s1,0,texture_id_s3)

        for _ in range(5):
            x_s1 = random.uniform(2.9, 1.5)
            y_s1 = random.uniform(-2.5, 2.5)
            DrawCircleWithTexture(0.1,36,x_s1,y_s1,0,texture_id_s2)

        for _ in range(5):
            x_s1 = random.uniform(2.9, 1.5)
            y_s1 = random.uniform(-2.5, 2.5)
            DrawCircleWithTexture(0.1,36,x_s1,y_s1,0,texture_id_s3)

        
        #bird on top

        DrawCircleWithTexture(0.4,35,0,1.7,0,texture_id4)

        pg.display.flip()
        pg.time.wait(100)
        
        angle += 2  

main()
