# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 09:19:42 2016
#Utiliser soit la webcam soit la caméra IP à l'adresse indiquée.
@author: Nug
"""

# Import the modules needed to run the script.
import sys, os
import cv2
import numpy as np
from threading import Thread
import threading
import time


cap=0
c=False
CamIpOn=False
WebCamOn=False

def Attente():
    bc= cv2.VideoCapture("http://10.17.155.25:8080/enabletorch")
    time.sleep(2)
    bc= cv2.VideoCapture("http://10.17.155.25:8080/disabletorch")
    print "je sleep"
    global c
    c=False
    return
    

def boucle():
     while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        img = frame
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        corners = cv2.goodFeaturesToTrack(gray,25,0.01,10)
        corners = np.int0(corners)
        #print corners
        
        for i in corners:
            x,y = i.ravel()
            cv2.circle(img,(x,y),3,255,-1)
    
        cv2.imshow('img',img)
        
        a= np.mean(frame)
        
        if (a<60 and c==False and CamIpOn==True and WebCamOn==False ):
            print "Threada<90"
            
            global c
            c=True
            
            Attente()
            
               
     
    
        print a
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # When everything done, release the capture
     cap.release()
     cv2.destroyAllWindows()


def CamIP():
    
    global CamIpOn
    CamIpOn=True
    
    global WebCamOn
    WebCamOn=False
    
#    s1 = threading.BoundedSemaphore(value=0)
#    
#    class lightBitch(Thread):
#        def __init__(self, s1):
#            self.s1 = s1
#            
#        def run():
#               
#                print "Je sleep !"
#                bc= cv2.VideoCapture("http://10.17.155.25:8080/enabletorch")
#                time.sleep(2)
#                bc= cv2.VideoCapture("http://10.17.155.25:8080/disabletorch")
#                s1.release()
    
    global cap
    cap = cv2.VideoCapture("http://10.17.155.25:8080//videofeed?something.mjpeg")
    
    #bc= cv2.VideoCapture("http://10.17.155.25:8080/disabletorch")
    
    if cap.isOpened(): # try to get the first frame
        rval, frame = cap.read()
    else:
        rval = False
        
#    def light():
#        time.sleep(2)
#        bc= cv2.VideoCapture("http://10.17.155.25:8080/disabletorch")
#        return
           
    b=False
    
    #np.savetxt('dst.txt', dst)
    boucle()

def Webcam():
    global WebCamOn
    WebCamOn=True
    
    global CamIpOn
    CamIpOn=False
    
    global cap
    cap= cv2.VideoCapture(0)
    boucle()
    return
   

# Main definition - constants
menu_actions  = {}  
 
# =======================
#     MENUS FUNCTIONS
# =======================
 
# Main menu
def main_menu():
    os.system('clear')
    
    print "Projet CESAR\n"
    print "Type de caméra"
    print "1. Webcam"
    print "2. Caméra IP"
    print "\n0. Quitter"
    choice = raw_input(" >>  ")
    exec_menu(choice)
 
    return
 
# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Menu 1
def menu1():
    print "Choix de la Webcam\n"
    print "9. Back"
    print "0. Quit"
    Webcam()
    choice = raw_input(" >>  ")
    
    exec_menu(choice)
    
    return
 
 
# Menu 2
def menu2():
    print "Choix de la caméra IP\n"
    print "9. Back"
    print "0. Quit"
    CamIP()
    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
# Back to main menu
def back():
    menu_actions['main_menu']()
 
# Exit program
def exit():
    sys.exit()
 
# =======================
#    MENUS DEFINITIONS
# =======================
 
# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '9': back,
    '0': exit,
}
 
# =======================
#      MAIN PROGRAM
# =======================
 
# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
