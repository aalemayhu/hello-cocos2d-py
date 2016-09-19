# Modified from the cocos2d examples

from pyglet.gl import *
import cocos
from cocos.layer import *
from cocos.director import director

width = 1366
height = 768

class BlueLayer(cocos.layer.Layer):
    def __init__(self):
        super(BlueLayer, self).__init__()
        background = ColorLayer(128, 46, 101, 255)
        self.add(background, z = 0)

def main():
    director.init( width=width, height=height, resizable=False, fullscreen=True )
    director.window.set_caption('aspect ratio and fullscreen - see console for usage')
    scene = cocos.scene.Scene()
    scene.add(BlueLayer())
    director.run( scene )

if __name__ == '__main__':
    main()
