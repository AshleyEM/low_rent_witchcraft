from PIL import Image

# posterize(): apply a posterize filter to an image. Better results if threshold > 300
# detect_edges(): apply an edge detection filter to an image

def posterize(img, threshold): 
    px = img.load() # access pixels of image file
    new_img = Image.new(mode="RGB", size=img.size, color=(0,0,0)) # new blank image
    # iterate through [x,y] pixel coords of original image
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            val = px[x,y][0] + px[x,y][1] + px[x,y][2] # brightness (value) of pixel
            if val > threshold:
                new_img.load()[x,y] = (255,255,255) # set pixel to white
    new_img.show()

def detect_edges(img, threshold): 
    px = img.load() # access pixels of image file
    new_img = Image.new(mode="RGB", size=img.size, color=(255,255,255)) # new blank image 
    # iterate through [x,y] pixel coords of original image
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            val1 = px[x,y][0] + px[x,y][1] + px[x,y][2] # value of first pixel (r+g+b)
            val2 = px[x-1,y-1][0] + px[x-1,y-1][1] + px[x-1,y-1][2] # value of previous pixel (r+g+b)
            if abs(val1 - val2) > threshold: # if contrast between pixels exceeds threshold
                new_img.load()[x,y] = (0,0,0) # set pixel to black
    new_img.show()


posterize(Image.open('portrait.png'), 350)
detect_edges(Image.open('palace2.png'), 20)