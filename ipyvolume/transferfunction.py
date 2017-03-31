import ipywidgets as widgets
from traitlets import Unicode
from traittypes import Array
import traitlets
import numpy as np
import matplotlib

from .serialize import array_serialization

N = 1024
x = np.linspace(0, 1, N, endpoint=True)


if 0:
    def array_from_json(value, obj=None):
        if value is not None:
            return np.asarray(value['values'], dtype=np.float64)

    def array_to_json(a, obj=None):
        if a is not None:
            a = a.astype(np.float64)
            return dict(values=a.tolist(), type=str(a.dtype))
        else:
            return dict(values=a, type=None)

    array_serialization = dict(to_json=array_to_json, from_json=array_from_json)


@widgets.register('ipyvolume.transferfunction.TransferFunction')
class TransferFunction(widgets.DOMWidget):
    _view_name = Unicode('TransferFunctionView').tag(sync=True)
    _view_module = Unicode('ipyvolume').tag(sync=True)
    style = Unicode("height: 32px; width: 100%;").tag(sync=True)
    rgba = Array().tag(sync=True, **array_serialization)


class TransferFunctionJsBumps(TransferFunction):
    _model_name = Unicode('TransferFunctionJsBumpsModel').tag(sync=True)
    _model_module = Unicode('ipyvolume').tag(sync=True)
    levels = traitlets.List(traitlets.CFloat, default_value=[0.1, 0.5, 0.8]).tag(sync=True)
    opacities = traitlets.List(traitlets.CFloat, default_value=[0.01, 0.05, 0.1]).tag(sync=True)
    widths = traitlets.List(traitlets.CFloat, default_value=[0.1, 0.1, 0.1]).tag(sync=True)

    def control(self):
        import ipywidgets
        return ipywidgets.VBox()
        l1 = ipywidgets.FloatSlider(min=0, max=1, step=0.001, value=self.level1)
        l2 = ipywidgets.FloatSlider(min=0, max=1, step=0.001, value=self.level2)
        l3 = ipywidgets.FloatSlider(min=0, max=1, step=0.001, value=self.level3)
        o1 = ipywidgets.FloatSlider(min=0, max=.2, step=0.001, value=self.opacity1)
        o2 = ipywidgets.FloatSlider(min=0, max=.2, step=0.001, value=self.opacity2)
        o3 = ipywidgets.FloatSlider(min=0, max=.2, step=0.001, value=self.opacity2)
        ipywidgets.jslink((self, 'level1'), (l1, 'value'))
        ipywidgets.jslink((self, 'level2'), (l2, 'value'))
        ipywidgets.jslink((self, 'level3'), (l3, 'value'))
        ipywidgets.jslink((self, 'opacity1'), (o1, 'value'))
        ipywidgets.jslink((self, 'opacity2'), (o2, 'value'))
        ipywidgets.jslink((self, 'opacity3'), (o3, 'value'))
        return ipywidgets.VBox(
            [ipywidgets.HBox([ipywidgets.Label(value="levels:"), l1, l2, l3]),
             ipywidgets.HBox([ipywidgets.Label(value="opacities:"), o1, o2, o3])]
        )


class TransferFunctionWidgetJs3(TransferFunction):
    _model_name = Unicode('TransferFunctionWidgetJs3Model').tag(sync=True)
    _model_module = Unicode('ipyvolume').tag(sync=True)
    level1 = traitlets.Float(0.1).tag(sync=True)
    level2 = traitlets.Float(0.5).tag(sync=True)
    level3 = traitlets.Float(0.8).tag(sync=True)
    opacity1 = traitlets.Float(0.01).tag(sync=True)
    opacity2 = traitlets.Float(0.05).tag(sync=True)
    opacity3 = traitlets.Float(0.1).tag(sync=True)
    width1 = traitlets.Float(0.1).tag(sync=True)
    width2 = traitlets.Float(0.1).tag(sync=True)
    width3 = traitlets.Float(0.1).tag(sync=True)

    def control(self):
        import ipywidgets
        l1 = ipywidgets.FloatSlider(min=0, max=1, step=0.001, value=self.level1)
        l2 = ipywidgets.FloatSlider(min=0, max=1, step=0.001, value=self.level2)
        l3 = ipywidgets.FloatSlider(min=0, max=1, step=0.001, value=self.level3)
        o1 = ipywidgets.FloatSlider(min=0, max=.2, step=0.001, value=self.opacity1)
        o2 = ipywidgets.FloatSlider(min=0, max=.2, step=0.001, value=self.opacity2)
        o3 = ipywidgets.FloatSlider(min=0, max=.2, step=0.001, value=self.opacity2)
        ipywidgets.jslink((self, 'level1'), (l1, 'value'))
        ipywidgets.jslink((self, 'level2'), (l2, 'value'))
        ipywidgets.jslink((self, 'level3'), (l3, 'value'))
        ipywidgets.jslink((self, 'opacity1'), (o1, 'value'))
        ipywidgets.jslink((self, 'opacity2'), (o2, 'value'))
        ipywidgets.jslink((self, 'opacity3'), (o3, 'value'))
        return ipywidgets.VBox(
            [ipywidgets.HBox([ipywidgets.Label(value="levels:"), l1, l2, l3]),
             ipywidgets.HBox([ipywidgets.Label(value="opacities:"), o1, o2, o3])]
        )


class TransferFunctionWidget3(TransferFunction):
    level1 = traitlets.Float(0.1).tag(sync=True)
    level2 = traitlets.Float(0.5).tag(sync=True)
    level3 = traitlets.Float(0.8).tag(sync=True)
    opacity1 = traitlets.Float(0.4).tag(sync=True)
    opacity2 = traitlets.Float(0.1).tag(sync=True)
    opacity3 = traitlets.Float(0.1).tag(sync=True)
    width1 = traitlets.Float(0.1).tag(sync=True)
    width2 = traitlets.Float(0.1).tag(sync=True)
    width3 = traitlets.Float(0.1).tag(sync=True)

    def __init__(self, *args, **kwargs):
        super(TransferFunctionWidget3, self).__init__(*args, **kwargs)
        N = range(1, 4)
        self.observe(self.recompute_rgba,
                     ["level%d" % k for k in N]
                     + ["opacity%d" % k for k in N]
                     + ["width%d" % k for k in N]
                     )
        self.recompute_rgba()

    def recompute_rgba(self, *_ignore):
        rgba = np.zeros((1024, 4))
        N = range(1, 4)
        levels = [getattr(self, "level%d" % k) for k in N]
        opacities = [getattr(self, "opacity%d" % k) for k in N]
        widths = [getattr(self, "width%d" % k) for k in N]
        #print(levels, opacities, widths)
        colors = [np.array(matplotlib.colors.colorConverter.to_rgb(name)) for name in ["red", "green", "blue"]]
        # TODO: vectorize
        for i in range(rgba.shape[0]):
            position = i / (1023.)
            intensity = 0.
            #self.rgba[i, 0, :] = 0
            for j in range(3):
                intensity = np.exp(-((position-levels[j]) / widths[j])**2)
                rgba[i, 0:3] += colors[j] * opacities[j] * intensity
                rgba[i, 3] += opacities[j] * intensity
            rgba[i, 0:3] /= rgba[i, 0:3].max()
        rgba = np.clip(rgba, 0, 1)
        self.rgba = rgba
        #self._notify_trait("rgba", old_value, self.rgba)

    def control(self):
        import ipywidgets
        l1 = ipywidgets.FloatSlider(min=0, max=1, value=self.level1)
        l2 = ipywidgets.FloatSlider(min=0, max=1, value=self.level2)
        l3 = ipywidgets.FloatSlider(min=0, max=1, value=self.level3)
        o1 = ipywidgets.FloatSlider(min=0, max=0.2, step=0.001, value=self.opacity1)
        o2 = ipywidgets.FloatSlider(min=0, max=0.2, step=0.001, value=self.opacity2)
        o3 = ipywidgets.FloatSlider(min=0, max=0.2, step=0.001, value=self.opacity2)
        ipywidgets.jslink((self, 'level1'), (l1, 'value'))
        ipywidgets.jslink((self, 'level2'), (l2, 'value'))
        ipywidgets.jslink((self, 'level3'), (l3, 'value'))
        ipywidgets.jslink((self, 'opacity1'), (o1, 'value'))
        ipywidgets.jslink((self, 'opacity2'), (o2, 'value'))
        ipywidgets.jslink((self, 'opacity3'), (o3, 'value'))
        return ipywidgets.VBox(
            [ipywidgets.HBox([ipywidgets.Label(value="levels:"), l1, l2, l3]), ipywidgets.HBox([ipywidgets.Label(value="opacities:"), o1, o2, o3])]
        )
