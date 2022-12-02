def average_rgb(img_path, width, height): 
    '''''''''''''''''''''''''''''
    Find the mean or median RGB scores of an image. Inputs are:
    FileName: name of the file to be loaded
    ImgWidth: Number of pixels for image width
    ImgHeight:  Number of pixels for image height

    '''''''''''''''''''''''''''''
    import numpy as np
    from PIL import Image
    
    im = Image.open(FileName)
    r_list = []
    g_list = []
    b_list = []
    pixel_array = np.asarray(im)
    final_ret = FlatenImage(img_path, width, height)
    for n, dim in enumerate(pixel_array):
        
        for num, row in enumerate(dim):
            r, g, b = row
            r_list.append(r)
            g_list.append(g)
            b_list.append(b)
    
    r_median = np.median(r_list)
    g_median = np.median(g_list)
    b_median = np.median(b_list)
      
    return {"r": r_median, "g": g_median, "b": b_median, "array": final_ret}
    

import sys
import pprint
import logger
pp.PrettyPrinter(indent=2)
if __name__ == "__main__":
    if len(sys.argv) == 1:
        image = input('Image File Path: ')
        pp.pprint(average_rgb(image))
    elif len(sys.argv) == 2:
        pp.pprint(average_rgb(sys.argv[1]))
    else:
        logger.critical('Invalid call of script')        
