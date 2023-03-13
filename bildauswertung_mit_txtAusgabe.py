from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import time 

option= int(input("Alle Bilder in diesem Ordner analysieren? -> 1 eingeben \n"
              "Eigene Anzahl an zu analysierenden Bildern in diesem Ordner festlegen -> 2 eingeben\n"))

file_counter = 0
time_per_picture = 1.5 #estimated time per picture in min
num_of_mistakes = 0

#find number of pictures to be analyzed

if option == 1:
    for element in os.listdir():
        file_object = os.path.isfile(element)
        if file_object == True  and element.endswith('.jpg'): #change to JPG
            file_counter+=1
    num_of_pix = file_counter
    print("Anzahl der zu analysierenden Bilder: %d\n"
          "Vorraussichtliche Dauer der Analyse: %.2f h\n" %(num_of_pix, num_of_pix*time_per_picture/60))
elif option == 2:
    num_of_pix = int(input("Anzahl der zu analysierenden Bilder: "))
    print("Vorraussichtliche Dauer der Analyse: %.2f h\n" %(num_of_pix*time_per_picture/60))
else:
    raise ValueError("Keine solche Option")


pic_num = 1 
pic_name=[0,0,0,1]

#find the first picture that should be analyzed, as the filenames might not always start with IMG_0001.jpg

while True:
    try:
        Image.open('IMG_%d%d%d%d.JPG'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
        break
    except:
        print("not available: IMG_%d%d%d%d.JPG"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
        pic_name[3]+=1
        if pic_name[3] == 10:
            pic_name[3] = 0
            pic_name[2]+=1
        if pic_name[2] == 10:
            pic_name[2] = 0
            pic_name[1] +=1
        if pic_name[1] == 10:
            pic_name[1]=0
            pic_name[0] +=1

start_picture = [pic_name[0], pic_name[1], pic_name[2], pic_name[3]]

#check if there is no pictures missing, otherwise the program will raise an error at some point during analyzing process

for element in os.listdir():
        file_object = os.path.isfile(element)
        if file_object == True  and element.endswith('.jpg'): #change to JPG
            try:
                Image.open('IMG_%d%d%d%d.JPG'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
                print("available: IMG_%d%d%d%d.JPG"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
                pic_name[3]+=1 
                if pic_name[3] == 10:
                    pic_name[3] = 0
                    pic_name[2]+=1
                if pic_name[2] == 10:
                    pic_name[2] = 0
                    pic_name[1] +=1
                if pic_name[1] == 10:
                    pic_name[1]=0
                    pic_name[0] +=1
            except:
                raise ValueError('IMG_%d%d%d%d.JPG seems to be missing'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
        
#now we must reset to start_picture to run the rest of the program

for i in range(len(pic_name)):
    pic_name[i]=start_picture[i]

#print out the name of the first picture, to check
    
print("Erstes Bild ist IMG_%d%d%d%d.JPG"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))

white_pixels=[]
black_pixels=[]
total_pixels=[]
white_pixels_perc = []
black_pixels_perc = []

line = 1

#create a csv file to store the data

with open('picture_data.csv', "a+") as datafile:
    datafile.write("bildnummer" + ", "+ "schwarz" + ", " + "weiss"+ ", " + "gesamt" + "\n") #Ausgabe in den CSV - File

#go through all the files and analyse them

    start_time=time.time()
    estimated_end_time=start_time+num_of_pix*time_per_picture*60
    
while True:

    x,y=0,0
    numB=0
    numW=0

        
    if pic_num <= num_of_pix:  
        im = Image.open('IMG_%d%d%d%d.JPG'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
        print("Bild IMG_%d%d%d%d.JPG"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
        pix = im.load()
        print(im.size) # Get the width and hight of the image for iterating over
        size_of_picture = im.size[0]*im.size[1]
        ar=1 #averaging range: ar=20 pixel -> To make the pixel range bigger or smaller change this number
        x0=0

        while y <= im.size[1]-ar: ## <
            while x <= im.size[0]-ar: ## <
                j=0
                cx=[]
                cy=[]
                cxy=[]
                while j < ar:
                    cx.append(pix[x+j,y])
                    cy.append(pix[x,y+j])
                    cxy.append(pix[x+j,y+j])
                    j+=1

                #averaging range: ar=number of pixel that we are averaging over 
                av=[]
                kx0=kx1=kx2=ky0=ky1=ky2=kxy0=kxy1=kxy2=0
                for tupel in cx:
                    kx0+=tupel[0]/ar #R
                    kx1+=tupel[1]/ar #G
                    kx2+=tupel[2]/ar #B in cx direction , summing up and then dividing the values (Like an average) 
                for tupel in cy:
                    ky0+=tupel[0]/ar
                    ky1+=tupel[1]/ar
                    ky2+=tupel[2]/ar
                for tupel in cxy:
                    kxy0+=tupel[0]/ar
                    kxy1+=tupel[1]/ar
                    kxy2+=tupel[2]/ar

                b=0 #to change brightness of the pictures set b non zero
                av.append(int((int(kx0)+int(ky0)+int(kxy0)+b)/3)) #R average
                av.append(int((int(kx1)+int(ky1)+int(kxy1)+b)/3)) #G average 
                av.append(int((int(kx2)+int(ky2)+int(kxy2)+b)/3)) #B average

                j=0
                k=0

                thresh = 127.5 #set the Threshold (255 max)
                Y =0.2126*av[0]+0.7152*av[1]+0.0722*av[2] #formula for relative luminance 

                if Y >  thresh:
                    col=255 #White
                    numW+=1 
                    
                else:
                    col=0 #Black
                    numB+=1

                x+=ar
                
            y+=ar
            x=0
        print("Schwarz: %d , Weiss: %d" %(numB, numW))
        black_pixels.append(numB) 
        white_pixels.append(numW)
        tot_num_pix = numB + numW
        total_pixels.append(tot_num_pix)

        #if the size of the picture is not equal to the total ammount of counted pixels, something went wrong. I didnt want to raise exception here for now

        if im.size[0]*im.size[1] != tot_num_pix:
            print("Fehler bei Bild IMG_%d%d%d%d.JPG"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
            print("Tatsächliche Bildgroesse: %d"%(size_of_picture))
            num_of_mistakes+=1
            print(tot_num_pix)

        #write the results into the csv file

        with open('picture_data.csv', "a+") as datafile:
            datafile.write("%d"%line + ", "+str(f'{numB}') + ", " + str(f'{numW}')+ ", " + str(f'{tot_num_pix}' + "\n")) 
            line+=1

        print("Fertig, voraussichtlich verbleibende Zeit: %.2f h bzw. %.2f min \n" % ((estimated_end_time-time.time())/3600, (estimated_end_time-time.time())/60))

        #calculate the next filename

        pic_name[3]+=1 
        if pic_name[3] == 10:
            pic_name[3] = 0
            pic_name[2]+=1
        if pic_name[2] == 10:
            pic_name[2] = 0
            pic_name[1] +=1
        if pic_name[1] == 10:
            pic_name[1]=0
            pic_name[0] +=1
        
        pic_num+=1
        im.close()

    else:
        end_time = time.time()
        print("Die benötigte Zeit für %d Bilder war %.2f min bzw. %.2f h \n"
              "Die vorausgesagte Zeit betrug: %.2f min bzw. %.2f h\n"
              "Es gab %d Fehler\n"%(num_of_pix, (end_time-start_time)/60,(end_time-start_time)/3600, time_per_picture*num_of_pix, time_per_picture*num_of_pix/60, num_of_mistakes))
                
        break #end of while loop

#PLOTTING

#To divide two lists through each other we need to create a zip object, we need to do this to get the percantages

zipped_white_total=zip(white_pixels,total_pixels)
zipped_black_total=zip(black_pixels,total_pixels)

for i, j in zipped_white_total:
     white_pixels_perc.append(i/j*100)
for i, j in zipped_black_total:
    black_pixels_perc.append(i/j*100)

pic_space = np.linspace(1,num_of_pix,num=num_of_pix) #This delivers a linspace with natural numbers from 1 to the total number of pictures 

plt.plot(pic_space, white_pixels, '+', markersize = 3.5, label = "Total number of white Pixels")
plt.xlabel('Bildnummer')
plt.ylabel('Anzahl weißer Pixel')
plt.legend()
plt.show()

plt.plot(pic_space, black_pixels, '+', markersize = 3.5, label = "Total number of black Pixels")
plt.xlabel('Bildnummer')
plt.ylabel('Anzahl schwarzer Pixel')
plt.show()

plt.plot(pic_space, white_pixels_perc, '+', markersize = 3.5, label = "white pixels / total pixels")
plt.xlabel('Bildnummer')
plt.ylabel('Weiße Pixel in %')
plt.legend()
plt.show()

plt.plot(pic_space, black_pixels_perc, '+', markersize = 3.5, label = "black pixels / total pixels")
plt.xlabel('Bildnummer')
plt.ylabel('Schwarze Pixel in %')
plt.legend()
plt.show()
