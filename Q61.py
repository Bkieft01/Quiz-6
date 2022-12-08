#Brenna Kieft
import dbm
photo_category=dbm.open("categories","p")

#photo_category[animals.png]="a picture of my dog"
#photo_category[myself.png]="a selfie"
#photo_category[saintmarys.png]="Lemans hall"

photo_category[notredame.png]="a picture of the dome"
photo_category[saintmarys.png]="a picture of the lake"
photo_category[winter.png]="a picture of the snow"

for item in photo_category:
    print (item, photo_category[item])
    
