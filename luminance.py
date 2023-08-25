from PIL import Image
import numpy as np
import os

def picture_raise(pic_ending):
    pic_ending[3]+=1
    if pic_ending[3] == 10:
        pic_ending[3] = 0
        pic_ending[2]+=1
    if pic_ending[2] == 10:
        pic_ending[2] = 0
        pic_ending[1] +=1
    if pic_ending[1] == 10:
        pic_ending[1]=0
        pic_ending[0] +=1
    return pic_ending

def num_all_pictures(format):
    file_counter=0
    for element in os.listdir():
        file_object = os.path.isfile(element)
        if file_object == True  and element.endswith('.%s'%format):
            file_counter+=1
    num_of_pix = file_counter
    return num_of_pix

def find_first_picture(format):
    pic_name=[0,0,0,1]
    while True:
        try:
            Image.open('IMG_%d%d%d%d.%s'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3], format))
            break
        except:
            picture_raise(pic_name)
        if (pic_name[0]== 9 and pic_name[1]== 9 and pic_name[2]== 9 and pic_name[3]== 9):
            return([])
            break 
    return ([pic_name[0], pic_name[1], pic_name[2], pic_name[3]])

def find_last_picture(format):
    pic_name=[0,0,0,1]
    last_pic=[]
    while True:
        try:
            Image.open('IMG_%d%d%d%d.%s'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3], format))
            print("opened")
            last_pic=pic_name[:]
        except:
            pass
        
        if (pic_name[0]== 9 and pic_name[1]== 9 and pic_name[2]== 9 and pic_name[3]== 9):
            break 
       # print(last_pic)
        picture_raise(pic_name)
    return (last_pic)


def check_for_missing(format, start_pic, end_pic):
    missing_bool=False
    missing_pic=[]
    pic_name = []
    for element in start_pic:
        pic_name.append(element)
    while(True):
        try:
            Image.open('IMG_%d%d%d%d.%s'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3], format))
            #print("available: IMG_%d%d%d%d.%s"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3], format))
            
        except:
            missing_bool=True
            missing_pic.append([pic_name[0],pic_name[1],pic_name[2],pic_name[3]])

        if (pic_name[0]==end_pic[0] and pic_name[1]==end_pic[1] and pic_name[2]==end_pic[2] and pic_name[3]==end_pic[3]):
            break

        picture_raise(pic_name)
    return(missing_bool, missing_pic)

def analyze_all(format, start_picture, averaging_range=1, brightness = 0, threshold=127.5):
    pic_name=start_picture[:]
    pic_num=1
    total_num_pictures=num_all_pictures(format)
    #if total num < pic num => exception
    white_pixels=[]
    black_pixels=[]
    total_pixels=[]
    while True:

        x,y=0,0
        numB=0
        numW=0

            
        if pic_num <= total_num_pictures:  
            im = Image.open('IMG_%d%d%d%d.JPG'%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
            pix = im.load()
            size_of_picture = im.size[0]*im.size[1]
            x0=0
            while y <= im.size[1]-averaging_range: 
                while x <= im.size[0]-averaging_range: 
                    j=0
                    cx=[]
                    cy=[]
                    cxy=[]
                    while j < averaging_range:
                        cx.append(pix[x+j,y])
                        cy.append(pix[x,y+j])
                        cxy.append(pix[x+j,y+j])
                        j+=1

                    av=[]
                    kx0=kx1=kx2=ky0=ky1=ky2=kxy0=kxy1=kxy2=0
                    for tupel in cx:
                        kx0+=tupel[0]/averaging_range #R
                        kx1+=tupel[1]/averaging_range #G
                        kx2+=tupel[2]/averaging_range #B in cx direction , summing up and then dividing the values (Like an average) 
                    for tupel in cy:
                        ky0+=tupel[0]/averaging_range
                        ky1+=tupel[1]/averaging_range
                        ky2+=tupel[2]/averaging_range
                    for tupel in cxy:
                        kxy0+=tupel[0]/averaging_range
                        kxy1+=tupel[1]/averaging_range
                        kxy2+=tupel[2]/averaging_range

                    av.append(int((int(kx0)+int(ky0)+int(kxy0)+brightness)/3)) #R average
                    av.append(int((int(kx1)+int(ky1)+int(kxy1)+brightness)/3)) #G average 
                    av.append(int((int(kx2)+int(ky2)+int(kxy2)+brightness)/3)) #B average

                    j=0
                    k=0

                    Y =0.2126*av[0]+0.7152*av[1]+0.0722*av[2] #formula for relative luminance 

                    if Y >  threshold:
                        col=255 #White
                        numW+=1 
                        
                    else:
                        col=0 #Black
                        numB+=1

                    x+=averaging_range
                    
                y+=averaging_range
                x=0
            black_pixels.append(numB) 
            white_pixels.append(numW)
            tot_num_pix = numB + numW
            total_pixels.append(tot_num_pix)

            #if the size of the picture is not equal to the total ammount of counted pixels, something went wrong. I didnt want to raise exception here for now

            #if im.size[0]*im.size[1] != tot_num_pix:
            #    print("Fehler bei Bild IMG_%d%d%d%d.JPG"%(pic_name[0], pic_name[1], pic_name[2], pic_name[3]))
            #    print("Tatsächliche Bildgroesse: %d"%(size_of_picture))
            #    num_of_mistakes+=1
            #    print(tot_num_pix)

            #calculate the next filename
            picture_raise(pic_name)
            pic_num+=1
            im.close()

        else:
            end_time = time.time()
            break #end of while loop
    return(black_pixels, white_pixels, total_pixels)
