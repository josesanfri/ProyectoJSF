# Third Party Imports
from PIL import Image


# Functions
def formatter_image(image=None, format='webp'):
    
    if not image:
        print('Not image in params.\nformatter_image()\n->\nformatter_image(file_path, *quality)')
        return

    try:
        name = "".join(image.split('/')[-1].split('.')[0])
    
        with Image.open(image) as newImg:
    
            try:
                newImg.save('./media/utils/image/formatted/Formated_'+name+'.'+format, optimize=True, quality=100)
                return './media/utils/image/formatted/Formated_'+name+'.'+format
        
            except Exception as e:
                print('Error in save image\n'+str(e))
                return
    
    except Exception as e:
        print('Error in formatter_image() :\nProblems with the image.\n'+str(e))
        return


    

def restaurant_formatter_image ( image=None , format="webp" ):

    from PIL import Image
    from io import BytesIO 
    try:
        filename = "%s.webp" % image.name.split('.')[0]
        image = Image.open(image)
        
        # for PNG images discarding the alpha channel and fill it with some color
        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, '#fff')
            background.paste(image, image.split()[-1])
            image = background
        image_io = BytesIO()
        return (image , image_io , filename)

        # image.save(image_io, format='webp', quality=90)
    except Exception as err:
        print(" Fallo en my_formatter_image : ",err)