# Low Rent Witchcraft

Python scripts I made in my shed.


## Edgy Pixels (edgy_pixels.py)
![](edgypixels.png)

Given an image file, apply an **edge detection** filter or a **posterization** filter. 
Generates a new image, doesn't overwrite the original image file.
Uses the Pillow Python library.

**posterize(image file, threshold)**: reduce the brightness levels down to 2 values (black and white)

**detect_edge(image file, threshold)**: create sketchy outlines based on the contrast between pixels

EXAMPLE: `detect_edge(Image.open('mcr_lead_singer.png'), 40)`

## Reddit Sources (reddit_sources.py)


It's universally known that [Redditors use reliable sources for their arguments](https://www.youtube.com/watch?v=r7l0Rq9E8MY&list=LL&index=3).

This script scrapes the front page of a given subreddit and extracts external domain urls linked in comments and posts.
Then it returns a dictionary of each domain and their count.

EXAMPLE: `reddit_sources("worldnews")`

