# `hipo-cppyy`
Example reading HIPO with [`cppyy` Python bindings](https://cppyy.readthedocs.io/en/latest/)
to the [C++ HIPO API](https://github.com/gavalian/hipo)

## Setup: Install the Dependencies

### 🔶 `hipo`: C++ HIPO API
<https://github.com/gavalian/hipo>
- If you don't have it, obtain it from GitHub and build it locally
- In the following example, we download the latest release of HIPO (set by the `--branch` option), and install it to a local directory `./install`; [click here for the list](https://github.com/gavalian/hipo/tags) of HIPO releases, since this example will be out of date someday:
```bash
git clone https://github.com/gavalian/hipo.git --branch 4.0.1
cmake -S hipo -B hipo/build -DCMAKE_INSTALL_PREFIX=$(pwd)/install
cmake --build hipo/build
cmake --install hipo/build
```

### 🔶 Python Virtual Environment
Before installing Python packages, it's good practice to create a Python virtual environment, otherwise these next
steps will install the Python packages at the system level.

Doing this is optional, but if you work with a lot of Python code, it may be a good idea

Various guides are available online, for example: <https://docs.python.org/3/library/venv.html>

Following this guide, we can create a local virtual environment in `./venv`:
```bash
python -m venv ./venv
```
Then you need to activate it (which you will need to do every time you want to use this virtual environment)
```bash
source venv/bin/activate
```
With anything, there are better ways to do this, such as
[`virtualenvwrapper`](https://pypi.org/project/virtualenvwrapper/), but this is enough to get started.

### 🔶 Python Packages
Whether or not you are using your Python virtual environment or Python from the system level (run `which python` to check), install the required Python packages:
```
pip install -r requirements.txt
```
> [!TIP]
> Edit the [`requirements.txt`](requirements.txt) file, in case you want to use newer versions of the packages


## Run the Example

### Set your Environment
If you have installed `hipo` to `./install`, you may just run:
```bash
source environ.sh
```
If not, check `environ.sh` to see what environment variables are set, and set them yourself according to your installation.

Also, don't forget to activate your Python virtual environment, if you are using one (or if you opened a new
shell after following the above setup guide)

### Try the Example
Running with no arguments will print the usage guide:
```bash
./example.py
```
Run in interactive mode (`python -i`) to see the plots (or add lines to the code to save them as an image):
```bash
python -i example.py
```
