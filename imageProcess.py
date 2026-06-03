import os
from PIL import Image

def checkIfImageExistsOrNot(path):
    if os.path.exists(path.strip()):
        return True
    else:
        return False
    
def resizeImageandChangeQuality(imagePath, width, height, quality):
    if imagePath.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp")):
        img = Image.open(imagePath)
        resizedImage = img.resize((width, height))
        resizedImage.save('C:\\Users\\Ameya\\Desktop\\resized' + extension,optimise=True, quality=quality)
        print("Image file is present at location")
    else:
        print("Please provide valid image file extension.")

def cropImage(imagePath, left, top, right, bottom):
    if imagePath.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp")):
        img = Image.open(imagePath)
        croppedImage = img.crop((left, top, right, bottom))
        croppedImage.save('C:\\Users\\Ameya\\Desktop\\cropped' + extension,optimise=True, quality=100)
        print("Image file is present at location")
    else:
        print("Please provide valid image file extension.")


path = input("Enter the path to image file (Select the files with extension: .png, .jpg, .jpeg, .gif, .tiff, .bmp): ")

fileExists = checkIfImageExistsOrNot(path)

if fileExists == True:
    filename, extension = os.path.splitext(path)
    imageProcess = int(input("Enter the number for the process to run:\n\t1. Resize the image and change its quality\n\t2. Resize the image\n\t3. Compress the image\n\t4. Crop the image\nPlease enter the number for the process to do on image: "))

    match imageProcess:
        case 1:
            width = int(input("Please enter the width of image in pixels: "))
            height = int(input("Please enter the height of image in pixels: "))
            quality = int(input("Please enter the quality of image: \n\t 1. High quality\n\t 2. Medium quality\n\t 3. Low quality\nPlease enter your response: "))
            match quality:
                case 1:
                    quality = 100
                case 2:
                    quality = 50
                case 3:
                    quality = 30
                case _:
                    quality = 100

            resizeImageandChangeQuality(path, width, height, quality)
        
        case 2:
            width = int(input("Please enter the width of image in pixels: "))
            height = int(input("Please enter the height of image in pixels: "))

            resizeImageandChangeQuality(path, width, height, 100)
        
        case 3:
            quality = int(input("Please enter the quality of image: \n\t 1. High quality\n\t 2. Medium quality\n\t 3. Low quality\nPlease enter your response: "))
            match quality:
                case 1:
                    quality = 100
                case 2:
                    quality = 50
                case 3:
                    quality = 30
                case _:
                    quality = 100

            (width, height) = Image.open(path).size
            resizeImageandChangeQuality(path, width, height, quality)
        
        case 4:
            left = int(input("Please enter the left coordinate: "))
            top = int(input("Please enter the top coordinate: "))
            right = int(input("Please enter the right coordinate: "))
            bottom = int(input("Please enter the bottom coordinate: "))

            cropImage(path, left, top, right, bottom)

        case _:
            print("Invalid response.")
else:
    print("Image file does not exist")