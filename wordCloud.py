from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

# importing sample dataset from same folder
text = open("sampleWords.txt", "r").read()


# for random custom colour generation that sets hue, saturation and lightness. This creates a word cloud with different shades of red.
def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h = 360
    s = 90
    l = int(100.0 * float(random_state.randint(60, 180)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)


def createWordCloud(string):
    # breaking the mask image in pixels
    maskImageArray = np.array(Image.open("love.jpg"))
    cloud = WordCloud(background_color="black", max_words=2000, color_func=random_color_func,
                      mask=maskImageArray, stopwords=set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("wordCloud.png")


createWordCloud(text)
