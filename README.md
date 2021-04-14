# PySOTTO

A sorting visualiser in Python

## Todo

### UI/UX

- [x] Time of execution
- [x] Visualise like animation,frame by frame
- [ ] Distribute installers
- [ ] Screnshot option
- [ ] History of values min,max and size
- [ ] Menu bar

### Algorithms

- [x] Bubble Sort
- [x] Merge Sort
- [ ] Quick Sort

## Distribution

How to generate installer for your operating system. Follow below steps .

- `pip install pyinstaller`
- `pyinstaller sortingAlgos.py`
- Go to `dist/` directory in root folder of the project

  Read [pyinstaller manual](https://pyinstaller.readthedocs.io/en/stable/) for more details.

## known bugs

- clicking "Generate" button repeatedly,before last execution, does not delete previous canvas, it overwrites the canvas.
