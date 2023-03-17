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

lu.check_for_missing(format, start, end)
This function is used to check if there are pictures of a given format missing in between two given picture names. This becomes of importance when using analyze_all().
Former will only work if there are no picture names are missing.
example

lu.analyze_all("jpg",start)
