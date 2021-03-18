# Spine Widget

`SpineAsset` is a Kivy widget that load and animate [Spine](http://esotericsoftware.com/) assets.

![Simple example](https://github.com/SGGames/kivy-spine-python3/master/screenshot.png)

Fork from: https://github.com/kivy-garden/garden.spine
- Support python 3
- kivy 2

Warning: this has been done during a sprint, many part are not functionnal such as:
- Only json export works
- Color per vertex
- Some models don't work (officials from the SpineTrial packages don't work, or the goblins example)

## Installation

    pip install spine
    pip install kivy-spine-python3
	
    python setup.py install
## Usage

```python
from kivy.app import App
from kivyspinepy3 import SpineAsset

class SpineApp(App):
    def build(self):
        asset = SpineAsset(filename="data/dragon", valign="bottom")
        # print all possible animations
        print asset.animations
        asset.animate("flying")
        return asset

if __name__ == "__main__":
    SpineApp().run()
```

## Examples

See `examples` directory for an asset viewer (you can control the animation to apply, and load a different asset)

![Asset browser](https://github.com/SGGames/kivy-spine-python3/master/screenshot2.png)
