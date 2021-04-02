from PIL import Image
import os

change_png = False # do not change, else files will break

if change_png :
    Im_path = '/home/leo/Images/autres'
    for file in os.listdir (Im_path) :
        print (file)
        if file.endswith ('.jpg') or file.endswith('.jpeg') :
            file_name = os.path.splitext(file)[0]
            os.rename(f'{Im_path}/{file}', f'{Im_path}/{file_name}.png')


file = '/home/leo/Images/autres/beanos.jpeg'

imA = Image.open (file)
imA.thumbnail((300, 300))
imA.show ()