#!/bin/bash
set -euo pipefail


# Download and extract Micromamba


# Set up environment variables
export MAMBA_ROOT_PREFIX="$PWD/micromamba"
export PATH="$PWD/bin:$PATH"

curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba

# Create the environment
./bin/micromamba create -y -n jupyterenv python=3.12 -c conda-forge

micromamba activate jupyterenv

pip install -r requirements-deploy.txt

jupyter lite build --output-dir dist

# Install dependencies via pip in the micromamba environment
# micromamba run -n jupyterenv python -m pip install -r requirements-deploy.txt

# Build JupyterLite
# micromamba run -n jupyterenv jupyter lite --version
# micromamba run -n jupyterenv jupyter lite build --contents content --output-dir dist
