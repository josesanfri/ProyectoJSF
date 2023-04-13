# Third Party Imports
from PIL import Image

# Functions
def compress_image(image=None, resize=None, quality=70):
    
    if not image:
        print('Not image in params.\ncompress_image()\n->\ncompress_image(file_path, *quality)')
        return

    try:

        with Image.open(image).convert('RGBA') as newImg:
    
            if resize:
                try:
                    newImg = newImg.resize((resize))
                except Exception as e:
                    print('Error in sizes or image\nSizes must be like [50,50]\n\n'+str(e))
                    return

            try:
            
                newImg.save('./media/utils/image/compressed/Compressed_'+image.split('/')[-1], optimize=True, quality=quality)
                return './media/utils/image/compressed/Compressed_'+image.split('/')[-1]

            except Exception as e:
                print('Error on save image:\n'+str(e))
                return
        
    
    except Exception as e:
        print('Error in compress_image() :\nProblems with the image.\n'+str(e))
        return
    