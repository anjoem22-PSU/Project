from PIL import Image

def from_path(path):
    im = Image.open(path)
    pixels = im.load()
    
    ret_arr = []
    
    for y in range(im.size[0]):
        ret_arr.append([])
        for x in range(im.size[1]):
            pixel = pixels[x,y]
            if pixel == (255,255,255,255):
                ret_arr[y].append(0)
            else:
                ret_arr[y].append(1)
        
    return ret_arr