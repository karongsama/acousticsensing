import time
import numpy as np
from skimage import io
import plotly.graph_objects as go
import os
import cv2

path=r"D:\coding\AcousticSensing\Data\NewCylinder\CTpic\ctpicture_up"
vol=io.imread(os.path.join(path, '*.tif'))
# vol = io.imread("D://coding//AcousticSensing//Data//NewCylinder//CTpic//ctpicture_up.tif")
volume=vol.T
volume=volume.T
r,c=volume[0].shape
# print(vol.shape)
frames=10

# 显示volume的第一张图片
# io.imshow(vol[10])
# io.show()
# io.imshow(volume[1000])
# io.show()

fig = go.Figure(frames=[go.Frame(data=go.Surface(
    z=(1.0 - k * 0.1) * np.ones((r, c)),
    surfacecolor=np.flipud(volume[frames - 1 - k]),
    cmin=0, cmax=200
    ),
    name=str(k) # you need to name the frame for the animation to behave properly
    )
    for k in range(frames)
    ]
)

fig.add_trace(go.Surface(
    z=1.0 * np.ones((r, c)),
    surfacecolor=np.flipud(volume[frames-1]),
    colorscale='Gray',
    cmin=0, cmax=200,
    colorbar=dict(thickness=20, ticklen=4)
))

def frame_args(duration):
    return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }

sliders = [
            {
                "pad": {"b": 10, "t": 60},
                "len": 0.9,
                "x": 0.1,
                "y": 0,
                "steps": [
                    {
                        "args": [[f.name], frame_args(0)],
                        "label": str(k),
                        "method": "animate",
                    }
                    for k, f in enumerate(fig.frames)
                ],
            }
        ]

# Layout
fig.update_layout(
         title='Slices in volumetric data',
         width=2000,
         height=2000,
         scene=dict(
                    zaxis=dict(range=[-0.1, 1.0], autorange=False),
                    aspectratio=dict(x=1, y=1, z=1),
                    ),
         updatemenus = [
            {
                "buttons": [
                    {
                        "args": [None, frame_args(50)],
                        "label": "&#9654;", # play symbol
                        "method": "animate",
                    },
                    {
                        "args": [[None], frame_args(0)],
                        "label": "&#9724;", # pause symbol
                        "method": "animate",
                    },
                ],
                "direction": "left",
                "pad": {"r": 10, "t": 70},
                "type": "buttons",
                "x": 0.1,
                "y": 0,
            }
         ],
         sliders=sliders
)

fig.show()