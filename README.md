# `hipo-cppyy`
Example reading HIPO with [`cppyy` Python bindings](https://cppyy.readthedocs.io/en/latest/)
to the [C++ HIPO API](https://github.com/gavalian/hipo)

## Setup: Install the Dependencies

### 🔶 `hipo`: C++ HIPO API
<https://github.com/gavalian/hipo>
Download the latest release of HIPO (set by the `--branch` option), and install it to a local directory `./install`; [click here for the list](https://github.com/gavalian/hipo/tags) of HIPO releases, since the version used in this example will be out of date someday:
```bash
git clone https://github.com/gavalian/hipo.git --branch 4.0.1
cmake -S hipo -B hipo/build -DCMAKE_INSTALL_PREFIX=$(pwd)/install
cmake --build hipo/build
cmake --install hipo/build
```

### 🔶 Python Virtual Environment
Before installing Python packages, it's good practice to create a Python virtual environment, otherwise these next
steps will install the Python packages at the system level.

Doing this is optional, but if you work with a lot of Python code, it may be a good idea.

Various guides are available online, for example: <https://docs.python.org/3/library/venv.html>

Following this guide, we can create a local virtual environment in `./venv`:
```bash
python -m venv ./venv
```
Then activate it:
```bash
source venv/bin/activate
```

### 🔶 Python Packages
Whether or not you are using a Python virtual environment or Python from the system level (run `which python` to check), install the required Python packages:
```
pip install -r requirements.txt
```

## Run the Example

### Set your Environment
If you have installed `hipo` to `./install`, you may just run:
```bash
source environ.sh
```
If not, check `environ.sh` to see what environment variables are set, and set them yourself according to your installation.

Sourcing `environ.sh` will also activate your Python virtual environment, if it's in `./venv`.

### Try the Example
Running with no arguments will print the usage guide:
```bash
python ./example.py
```
It will draw the momentum distribution of pions, and the plot will be saved as `plot.png`.

If you want to see the plots interactively, run with `python -i`:
```bash
python -i ./example.py [ARGS]...
```
Then in the prompt, run:
```python
plt.show()
```
(you may also add this line to the Python script)
