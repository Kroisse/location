lat = [18.0, 64.0] 
lng = [-124.0, -66.0]

loc = []
locs = []

i=0.0

arrLat = []
for x in range(int((lat[1]-lat[0])*10)):
    arrLat.append(lat[0]+x*0.1)  
    
arrLng = []
for x in range(int((lng[1]-lng[0])*10)):
    arrLng.append(lng[0]+x*0.1)    


locs = [(x, y) for x in arrLat for y in arrLng if x != y]  

for i, loc in enumerate(reversed(locs)):
    print i + 1, loc
