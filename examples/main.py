# coding=utf-8

from kivy.app import App
from kivyspinepy3 import SpineAsset

class SpineApp(App):
    def build(self):
        asset = SpineAsset(filename="data/dragon")
        asset.animate("flying")
        return asset

if __name__ == "__main__":
    SpineApp().run()
