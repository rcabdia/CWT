import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cwt-seismology",  # Replace with your own username
    version="0.0.1",
    author="rcabdia",
    author_email="rcabdia@roa.es",
    description="Wavelet transform for seismic signal detection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rcabdia/CWT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License, Version 3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
