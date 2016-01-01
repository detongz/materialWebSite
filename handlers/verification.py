#!/usr/bin/python
# coding: utf-8

"""pil生成验证码"""

import random
import uuid
import os

from PIL import Image, ImageDraw, ImageFont, ImageFilter

NUM = [chr(i) for i in range(0x30, 0x39)]
UPPER = [chr(i) for i in range(0x41, 0x5a)]
LOWER = [chr(i) for i in range(0x61, 0x7a)]
LETTER = (NUM + UPPER + LOWER) * 2

PIC_SIZE = 100, 50  # width and high
BACKGROUND_COLOR = 242, 255, 255
FONT = os.path.dirname(__file__)[:-8] + 'static/fonts/PFCosmonutPro-Bold.ttf'
FONT_SIZE = 30
FONT_COLOR = 255, 199, 199
FONT_COLOR2 = 239, 161, 76
FONT_COLOR3 = 153, 153, 153
FONT_COLOR4 = 147, 255, 147

PIC_PATH = os.path.dirname(__file__)[:-8] + 'static/tmp/'
SUFFIX = '.png'

n_line = (1, 2)
point_chance = 2
width, height = PIC_SIZE


def get_code_and_position():
    return random.sample(LETTER, 4), sorted(random.sample(range(80), 4))


def get_verify_pic():
    image = Image.new('RGB', PIC_SIZE, BACKGROUND_COLOR)
    font = ImageFont.truetype(FONT, FONT_SIZE)
    draw = ImageDraw.Draw(image)
    code, position = get_code_and_position()
    draw.text((position[0], random.randint(0, 15)), code[0], font=font, fill=FONT_COLOR)
    draw.text((position[1], random.randint(0, 15)), code[1], font=font, fill=FONT_COLOR2)
    draw.text((position[2], random.randint(0, 15)), code[2], font=font, fill=FONT_COLOR3)
    draw.text((position[3], random.randint(0, 15)), code[3], font=font, fill=FONT_COLOR4)
    line_num = random.randint(*n_line)  # 干扰线条数

    chance = min(100, max(0, int(point_chance)))  # 大小限制在[0, 100]

    for w in xrange(width):
        for h in xrange(height):
            tmp = random.randint(0, 100)
            if tmp > 100 - chance:
                draw.point((w, h), fill=(271, 215, 271))
    for i in range(line_num):
        # 起始点
        begin = (random.randint(0, PIC_SIZE[0]), random.randint(0, PIC_SIZE[1]))
        # 结束点
        end = (random.randint(0, PIC_SIZE[0]), random.randint(0, PIC_SIZE[1]))
        draw.line([begin, end], fill=(170, 247, 86))

    pic_name = str(uuid.uuid1()) + SUFFIX
    image.save(PIC_PATH + pic_name, 'png')

    codestr = ''
    for c in code:
        codestr += c

    return codestr, pic_name


def remove_pics():
    cmd = 'rm ' + PIC_PATH + '*'
    os.system(cmd)


def remove_pic(one):
    cmd = 'rm ' + PIC_PATH + one
    os.system(cmd)


if __name__ == '__main__':
    print get_verify_pic()
