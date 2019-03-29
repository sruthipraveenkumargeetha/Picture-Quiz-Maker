import Image
import os
import random
def main():
	

	path ='/home/sruthi/Desktop/My Works/Picture-Quiz-Maker/images'
	files = os.listdir(path)
	index = random.randrange(0, len(files))
	filename=files[index]
	photoname="/home/sruthi/Desktop/My Works/Picture-Quiz-Maker/images/"+filename
	image = Image.open(photoname)
	new_image = image.resize((400, 400))
	new_image.save(photoname)
	new_image.show()





if __name__ =="__main__":
	main()
