# `hipo-cppyy`
Example reading HIPO with [`cppyy` Python bindings](https://cppyy.readthedocs.io/en/latest/)
to the [C++ HIPO API](https://github.com/gavalian/hipo)

## Setup: Install the Dependencies

Before doing anything, clone this repository
```bash
git clone https://github.com/c-dilks/hipo-cppyy.git
```
Then `cd` into it, since most of the following instructions assume you are working from within it
```bash
cd hipo-cppyy
```
(you may prefer not to work in the `hipo-cppyy` directory, so modify the following commands as needed).

### 🔶 `hipo`: C++ HIPO API
<https://github.com/gavalian/hipo>

Download the latest release of HIPO (set by the `--branch` option), and install it to a local directory `./install`; [click here for the list](https://github.com/gavalian/hipo/tags) of HIPO releases, since the version used in this example will be out of date someday:
```bash
git clone https://github.com/gavalian/hipo.git --branch 4.0.1 --recurse-submodules
cmake -S hipo -B hipo/build -DCMAKE_INSTALL_PREFIX=$(pwd)/install -DCMAKE_C_COMPILER=$(which gcc)   # -DCMAKE_C_COMPILER is needed, if on ifarm
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
python3 -m venv ./venv
```
Then activate it:
```bash
source venv/bin/activate
```

### 🔶 Python Packages
Whether or not you are using a Python virtual environment or Python from the system level (run `which python3` to check), install the required Python packages:
```
python3 -m pip install pkgconfig cppyy matplotlib PyQt5
```

| Package      | Description                                           |
| ---          | ---                                                   |
| `pkgconfig`  | Python wrapper for `pkg-config` dependency resolution |
| `cppyy`      | Automated C++ / Python bindings                       |
| `matplotlib` | Data visualization                                    |
| `PyQt5`      | Supports `matplotlib` usage                           |

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
python3 ./example.py
```
It will draw the momentum distribution of pions, and the plot will be saved as `plot.png`.

See the script [`example.py`](example.py) for more details.
