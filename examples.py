import luminance as lu

print(lu.num_all_pictures('jpg'))
print(lu.find_first_picture('jpg')) 
print(lu.find_last_picture('jpg'))
start=lu.find_first_picture('jpg')
print(lu.check_for_missing("jpg", [0,0,0,1], [0,0,0,5]))
print(lu.analyze_all("jpg",start))
