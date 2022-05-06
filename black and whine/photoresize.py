from PIL import Image

ERR="Error"
ERRF="A file with this name does not exist"
def options():
    L1=True
    while L1:
        try:
            input_image_path=str(input("Enter the file storage path:")); L2=True
        except:
            print(ERR); L2=False
        while L2:
            try:
                output_image_path=str(input("Enter the path where to save the new file:")); L3=True
            except:
                print(ERR); L3=False
            while L3:
                resize_image(input_image_path,
                 output_image_path)
                    
        
            
def resize_image(input_image_path,
                 output_image_path):
    try:
        original_image = Image.open(input_image_path)
    except:
        print(ERRF)
        options()
    width, height = original_image.size
    print('The original image size is {wide} wide x {height} '
          'high'.format(wide=width, height=height))
    
    W=int(int(width)*0.75)
    H=int(int(height)*0.75)
    newsize=(W, H)

    recolored_image = original_image.convert('L')
    resized_image = recolored_image.resize(newsize)
    width, height = resized_image.size
    print('The resized image size is {wide} wide x {height} '
          'high'.format(wide=W, height=H))
    resized_image.show()
    resized_image.save(output_image_path +'\\resizedBW.jpg')
    print('File saved:',output_image_path +'\\resizedBW.jpg'+'\n')
    options()

options()
