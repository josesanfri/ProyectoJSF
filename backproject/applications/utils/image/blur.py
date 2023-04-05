# Third Party Imports
from PIL import Image, ImageFilter


# Functions
def blur_image(blur, image=None):
    
    if not image:
        print('Not image in params.\nblur_image()\n->\nblur_image(blur=int,file_path=str)')
        return

    try:
        name = image.split('/')[-1]

        with Image.open(image) as newImg:

            try:
                newImg.filter(ImageFilter.BoxBlur(radius=blur))

                newImg.save('./media/utils/image/filtered/Filtered_'+name, optimize=True, quality=50)
                return './media/utils/image/filtered/filtered_'+name
        
            except Exception as e:
                print('Error in save image\n'+str(e))
                return
    
    except Exception as e:
        print('Error in blur_image() :\nProblems with the image.\n'+str(e))
        return