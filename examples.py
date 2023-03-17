import luminance as lu

#Remember to place pictures of the form 'IMG_xxxx' in your directory 
#The function 'analyze_all()' will only work for continuos naming of the pictures. For example IMG_0001, IMG_0003 ... will not work because there is IMG_0002 missing
#You can use 'check_for_missing()' to make sure there are no pictures missing

print(lu.num_all_pictures('jpg'))
print(lu.find_first_picture('jpg')) 
print(lu.find_last_picture('jpg'))
start=lu.find_first_picture('jpg')
print(lu.check_for_missing("jpg", [0,0,0,1], [0,0,0,5]))
print(lu.analyze_all("jpg",start))
