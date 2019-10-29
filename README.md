# fizbar

A quick demonstration of how to distribute, install, and load
package-associated data in Python.

## Installation

To install in "developer" mode, do:

```
pip install -e .
```
This will install it out of the development directory, and modifications to
the Python code will be immediately reflected in the installed script.

To install normally, do:

```
pip install .
```

## Execution

Either
```
fizbar
```

or

```
python -m fizbar
```

You should get output like this:

```
hello, world!
Running code from this directory: /Users/t/dev/py36/lib/python3.6/site-packages/fizbar

loading dist.dat from: /Users/t/dev/py36/lib/python3.6/site-packages/fizbar/dist.dat
dist.dat contains: (here is some package data)
```
