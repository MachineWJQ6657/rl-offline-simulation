# setup.py: install script for offsim4rl
"""
to install offsim4rl and its dependencies for development work,
run this cmd from the root directory:
    pip install -e .
"""
import setuptools

setuptools.setup(
    name="offsim4rl",
    version="0.1",
    url="https://www.github.com/microsoft/rl-offline-simulation",
    include_package_data=True,
    packages=setuptools.find_packages(include=['offsim4rl']),
    install_requires=[
        "gym==0.26.2",
        "h5py>=3.8.0",
        "joblib>=1.2.0",
        "matplotlib>=3.6.0",
        "seaborn>=0.12.0",
        "tensorboardX>=2.6",
        "torch>=1.13.1",
        "tqdm>=4.65.0"
    ],
    extras_require={
        'agents': [
            # Forked version of the spinup library, with simplified dependencies.
            # "spinup @ git+https://github.com/sebastko/spinningup-simple-install.git#egg=spinup"
        ]
    }
)
