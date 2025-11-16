# Control Block Diagram
![](docs/Control_Block_Diagram.png)

[**Overview**](#overview)
| [**Quickstart**](#getting-started)
| [**Examples**](#examples)
| [**Installation**](#installation)

## Overview
The control-block-diagram package is a Python Toolbox for drawing block diagrams. It is build
upon [Pylatex](https://jeltef.github.io/PyLaTeX/current/), and therefore, can generate Latex
files, PDF files, and high-resolution raster images (PNG/JPEG/WebP). It allows you to construct typical control block diagrams with the
usual building blocks, i.e., PI-Controllers, Adders, Multiplier. It is also possible to
define own blocks. 

## Getting Started

The easiest way to get started with the ControlBlockDiagram Toolbox is to play around with the Hands On Jupyter Notebook. There the most important functions are explained and demonstrated with simple examples.

[Hands On Jupyter Notebook](https://github.com/upb-lea/control-block-diagram/blob/main/examples/Control_Block_Diagram_Hands_On.ipynb)

A basic routine is as simple as:
```py
from control_block_diagram import ControllerDiagram
from control_block_diagram import Point, Box, Connection


if __name__ == '__main__':
    doc = ControllerDiagram()
    
    box_control = Box(Point(0, 0), text='Control')
    box_block = Box(box_control.position.add_x(3), text='Block')
    box_diagram = Box(box_block.position.add_x(3), text='Diagram')

    Connection.connect(box_control.output, box_block.input)
    Connection.connect(box_block.output, box_diagram.input)
    
    doc.save('pdf')
    doc.show()
```

To export image assets simply switch the file type, e.g. `doc.save('png')` or `doc.save('pdf', 'webp')`.
You can pass `image_dpi=<value>` when creating `ControllerDiagram` to control the resolution that is used for the rasterized outputs.
Run your scripts via `uv run python your_script.py` so that `uv` automatically provisions the environment without needing a separate `requirements.txt`.

The output of this code is:
![](docs/Control_Block.png)

## Examples
There are some examples in the examples folder:

* [Flux Observer](https://github.com/upb-lea/control-block-diagram/blob/main/examples/flux_observer.py)
* [FPGA Board](https://github.com/upb-lea/control-block-diagram/blob/main/examples/fpga_example.py)
* [Induction Motor Controller](https://github.com/upb-lea/control-block-diagram/blob/main/examples/induction_motor_controller.py)
* [Model Predictive Controller](https://github.com/upb-lea/control-block-diagram/blob/main/examples/model_predictive_controller.py)

## Installation

This project is configured for [uv](https://github.com/astral-sh/uv), so you just run commands through `uv run` and it will create/manage the virtual environment automatically based on `pyproject.toml`.

Typical workflow:

```
git clone git@github.com:upb-lea/control-block-diagram.git
cd control-block-diagram
uv run python examples/simple_gain.py          # run an example
uv run python -m compileall control_block_diagram  # lightweight validation
```

If you prefer to install the package globally you can still do `pip install control-block-diagram`, but `uv run` is the recommended path for both development and first-time exploration.

You also need a latex compiler such as pdfLaTex to create a PDF file.  For example, you can get this from the latex distribution [MiKTeX](https://miktex.org/).
