#! python
import os
import sys
from json import dumps
from stories import def_story
import yaml


def files(path):
    with open('template.html', 'r') as template_file:
        template = template_file.read()
    name = path.replace('\\','/').split('/')[-1]
    template = template.replace('##name##', name)
    p = path.replace('\\','/')
    with open(name.replace(' ','') + ".html", 'w+') as output:
        output.write(template)
    try:
        with open(f'{path}/captions.yml', 'r') as y:
            caps = yaml.load(y)
        image_list = list(caps.keys())
    except FileNotFoundError:
        print(f'No captions file found, creating with empty captions')
        image_list = [ i for i in os.listdir(path) if i.endswith(('.jpg', '.gif')) ]
        with open(f'{path}/captions.yml', 'w') as y:
            y.write(yaml.dump({k:[] for k in image_list}))
        caps = {}
    except yaml.YAMLError as e:
        print(e)
        exit(1)
    with open(f'{p}/captions.js', "w") as y:
        y.write('captions = ' + dumps([caps.get(i) or [] for i in image_list], indent=2))
    images = 'images = [\n'
    for image in image_list:
        images += f'"{p}/{image}",\n'
    images += ']'
    with open(f'{p}/images.js', "w") as i:
        i.write(images)


if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        print("Usage: images <path>")
        sys.exit()
    files(path)
