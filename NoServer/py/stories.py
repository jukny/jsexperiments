import os
import sys
from json import dumps
import yaml


def def_story(caps):
    data = []
    try:
        with open(caps+'/captions.yml') as f:
            data = yaml.load(f)
    except yaml.YAMLError as ye:
        print(ye)
        exit(1)
    path = caps+'/captions.js'
    div = ['<div style="background: rgb(153, 153, 255)">', '<div style="background: rgb(153, 204, 255)">']
    story = []
    images = []
    if data!=None:
        for image, captions in data.items():
            rows = []
            images.append("{}/{}".format(caps.replace("\\", "/"), image))
            try:
                for count,row in enumerate(captions):
                    i = count % 2
                    rows.append(div[i] + row + '</div>')
                story.append(rows)
            except TypeError:
                pass
    with open(path, "w") as out:
        out.write("images = " + dumps(images, indent=4))
        out.write('\n')
        out.write("story = ")
    with open(path, 'a') as out:
        out.write(dumps(story, indent=4))
        


if __name__ == "__main__":
    caps = sys.argv[1]
    def_story(caps)