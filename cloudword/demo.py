# - * - coding: utf - 8 -*-
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
import chardet
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)
def readfile(filename):
    text1 = open(filename).read()
    type = chardet.detect(text1)
    text = text1.decode(type["encoding"])
    return text
def dealwithword(backgrooundfile,text,savefile):
    # 背景
    alice_mask = np.array(Image.open(backgrooundfile))
    # 分词
    wordlist = jieba.cut(text, cut_all=True)
    word_space_split = ' '.join(wordlist)
    wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
                   font_path="C:\\Windows\\Fonts\\STFANGSO.ttf").generate(word_space_split)
    # 保存
    wc.to_file(savefile)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():

    filename=path.join(d, '../11-15/duanzi.json')
    backgrooundfile=path.join(d, "love.jpg")
    savefile=path.join(d, "alice.png")
    text=readfile(filename)
    dealwithword(backgrooundfile,text,savefile)

if __name__ == '__main__':
    main()