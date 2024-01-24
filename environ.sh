#!/bin/bash
this_env=${BASH_SOURCE[0]:-$0}
this_dir=$(cd $(dirname $this_env) && pwd -P)

### add your `hipo` installation to pkg-config's path
hipo_install_dir=$this_dir/install
export PKG_CONFIG_PATH=$hipo_install_dir/lib/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}}

### add hipo-cppy to PYTHONPATH
export PYTHONPATH=$this_dir/python${PYTHONPATH:+:${PYTHONPATH}}
