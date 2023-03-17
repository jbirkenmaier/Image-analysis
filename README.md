# Image-analysis
This project uses the Pillow library to find out the number of light and dark pixels according to a threshold set by the user for all images in the directory of the form IMG_XXXX.XXX.

num_all_pictures(format) 
This function counts the number of pictures of the given format in the directory, returns an integer.
example: num_all_pictures('jpg') -> finds number of pictures with format jpg in the directory

find_first_picture(format)
This function finds the image with the lowest number and returns the ending as a list. For example out of a set (IMG_0001, IMG_0002, IMG_0003) it would return [0,0,0,1]
example: find_first_picture('png') -> finds the image of format png with the lowest ending number and returns ending as a list

find_last_picture(format))
This function finds the image of a given format with the highest number and returns the ending as a list. For example out of a set (IMG_0001, IMG_0002, IMG_0003) it would return [0,0,0,3]
example: find_last_picture('jpg') ->  finds the image of format jpg with the highest ending number and returns ending as a list

check_for_missing(format, start, end)
This function is used to check if there are pictures of a given format missing in between two given picture names. This becomes of importance when using analyze_all().
Former will only work if there are no picture names missing. The function takes the format, the starting name (as a list) and the ending name (as a list) and checks if there are names missing in between these two. It returns (bool, []). The boolean value is set to True if there are pictures missing and False if not. 
example: check_for_missing("jpg", [0,0,0,1], [0,0,0,5]) -> finds all pictures missing in between IMG_0001 and IMG_0005. It also checks if IMG_0001 and IMG_0005 exist and will add them to the list of missing pictures if they do.

lu.analyze_all("jpg",start)
analyze_all("jpg",start)
