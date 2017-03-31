"""
Possible properies

 * background-color
 * axes
  * color
  * visible
  * label
    * color
  * ticklabel
    * color
  * x/y/z
    * color
    * visible
    * label
      * color
    * ticklabel
      * color

Run:
python -m ipyvolume.style
to update the json style (needed for the js side)
"""
from . import utils
import copy

styles = {}
_defaults = {
    'axes': {
        'visible': True,
        'label': {
            'color': 'black'
        },
        'ticklabel': {
            'color': 'black'
        }
    },
    'box': {
        'visible': True,
    },
}


def create(name, properties):
    style = copy.deepcopy(_defaults)
    utils.dict_deep_update(style, properties)
    styles[name] = style
    return style


default = light = create("light", {
    'background-color': 'white',
    'axes': {
        'color': 'black',
    }
})

dark = create("dark", {
    'background-color': 'black',
    'axes': {
        'color': 'white',
        'label': {
            'color': 'white'
        },
        'ticklabel': {
            'color': 'white'
        },
    }
})

demo = create("demo", {
    'background-color': 'white',
    'box': {
        'color': 'pink',
        'visible': True,
    },
    'axes': {
        'color': 'black',
        'visible': True,
        'x': {
            'color': '#f00',
            'label': {
                'color': '#0f0'
            },
            'ticklabel': {
                'color': '#00f'
            },
        },
        'y': {
            'color': '#0f0',
            'label': {
                'color': '#00f'
            },
            'ticklabel': {
                'color': '#f00'
            }
        },
        'z': {
                'color': '#00f',
                'label': {
                    'color': '#f00'
                },
                'ticklabel': {
                    'color': '#0f0'
                }
        }
    }
})

minimal = {
    'background-color': 'white',
    'box': {
        'visible': False,
    },
    'axes': {
        'visible': False,
        'color': 'black'
    }
}

if __name__ == "__main__":
    import os
    source = __file__
    dest = os.path.join(os.path.dirname(source), "../js/data/style.json")
    print(source, dest)
    need_update = (not os.path.exists(dest)) or (os.path.getmtime(source) > os.path.getmtime(dest))
    if need_update:
        import json
        print(styles)
        with open(dest, "w") as f:
            json.dump(styles, f, indent=2)
        print("wrote json")
