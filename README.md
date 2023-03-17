# Image-analysis
This project uses the Pillow library to find out the number of light and dark pixels according to a threshold set by the user for all images in the directory of the form IMG_XXXX.XXX <br />

num_all_pictures(format) <br />
This function counts the number of pictures of the given format in the directory, returns an integer.<br />
example:<br /> 
num_all_pictures('jpg') <br />
-> finds number of pictures with format jpg in the directory<br />

find_first_picture(format)<br />
This function finds the image with the lowest number and returns it as a list. For example out of a set (IMG_0001, IMG_0002, IMG_0003) it would return [0,0,0,1]<br />
example:<br /> 
find_first_picture('png') <br /> 
-> finds the image of format png with the lowest ending number and returns it as a list<br />

find_last_picture(format))<br />
This function finds the image of a given format with the highest number and returns it as a list. For example out of a set (IMG_0001, IMG_0002, IMG_0003) it would return [0,0,0,3]<br />
example: <br />
find_last_picture('jpg') <br />
->  finds the image of format jpg with the highest ending number and returns ending as a list<br />

check_for_missing(format, start, end)<br />
This function is used to check if there are pictures of a given format missing in between two given picture names. This becomes of importance when using analyze_all().
Former will only work if there are no picture names missing. The function takes the format, the starting name (as a list) and the ending name (as a list) and checks if there are names missing in between these two. It returns (bool, []). The boolean value is set to True if there are pictures missing and False if not. <br />
example: <br />
check_for_missing("jpg", [0,0,0,1], [0,0,0,5]) <br />
-> finds all pictures missing in between IMG_0001 and IMG_0005. It also checks if IMG_0001 and IMG_0005 exist and will add them to the list of missing pictures if they do.<br />

analyze_all(format, start, averaging_range=1, brightness = 0, threshold=127.5)<br />
This function takes a threshold between 0 and 255 (127.5 is set by default) and from the RGB-Values of the pixels it calculates if the pixel is above or under that threshold. For all pictures in the directory it counts how many pixels are above (pixel is counted as white) or below (pixel is counted as black) the threshold and returns three lists. Each first, every second, every third element and so on in every list belongs to one picture ([black_pixels], [white_pixels], [total_pixels]).<br />
example:<br />
analyze_all('jpg', [0,0,0,1], averaging_range=1, brightness = 0, threshold=127.5) 
<br />-> analyses all pictures of format IMG_XXXX.jpg, starting with [0,0,0,1]
