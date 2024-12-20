import setuptools
from setuptools import setup, find_packages
from pathlib import Path

setup(
    name='SGtSNEpiPy',
    version='1.1.5',
    description='SGtSNEpiPy is a Python interface to SG-t-SNE-П, a powerful tool for visualizing large, sparse, stochastic graphs.',
    author=['Chenshuhao Qin','Yihua Zhong'],
    author_email="cq27@duke.edu, yz737@duke.edu,",
    classifiers=[
                'Programming Language :: Python',
                'Intended Audience :: Developers',
                 ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'juliacall >= 0.9.13',
    ]
)