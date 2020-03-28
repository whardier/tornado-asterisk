#!/usr/bin/env python3

try:
    # Use setuptools if available, for install_requires (among other things).
    import setuptools
    from setuptools import setup
except ImportError:
    setuptools = None
    from distutils.core import setup

kwargs = {}

# "Safe" version read
with open("tornado_asterisk/__init__.py") as f:
    ns = {}
    exec(f.read(), ns)
    kwargs["version"] = ns["version"]

with open("README.rst") as f:
    kwargs["long_description"] = f.read()

if setuptools is not None:
    python_requires = ">= 3.8"
    kwargs["python_requires"] = python_requires

setup(
    name="tornado_asterisk",
    packages=["tornado_asterisk"],
    author="Shane R. Spencer",
    author_email="spencersr@gmail.com",
    url="https://github.com/whardier/tornado-asterisk",
    license="MIT",
    project_urls={
        'Funding': 'https://github.com/sponsors/whardier',
        'Source': 'https://github.com/whardier/tornado-asterisk',
    },
    description=(
	"Tornado Asterisk AMI/ARI/AGI Client"
    ),
    install_requires=[
        "tornado>=6.0",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 1 - Planning",
        "Topic :: Communications :: Telephony",
        "Intended Audience :: Telecommunications Industry",
        "Framework :: Tornado",
        "Framework :: Tornado :: 6.0",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    **kwargs
)
