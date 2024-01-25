#!/bin/bash
this_env=${BASH_SOURCE[0]:-$0}
this_dir=$(cd $(dirname $this_env) && pwd -P)

# activate python virtual environment, if used
python_venv=$this_dir/venv/bin/activate
[ -f $python_venv ] && source $python_venv

# add your `hipo` installation to pkg-config's path
hipo_install_dir=$this_dir/install
export PKG_CONFIG_PATH=$hipo_install_dir/lib/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}}

# add your `hipo` installation to linker path
os=$(uname)
case $os in
  Linux)  export LD_LIBRARY_PATH=$hipo_install_dir/lib${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}       ;;
  Darwin) export DYLD_LIBRARY_PATH=$hipo_install_dir/lib${DYLD_LIBRARY_PATH:+:${DYLD_LIBRARY_PATH}} ;;
  *) echo "ERROR: linker path not appended, since uname returned '$os'" ;;
esac

# add hipo-cppy to PYTHONPATH
export PYTHONPATH=$this_dir/python${PYTHONPATH:+:${PYTHONPATH}}
