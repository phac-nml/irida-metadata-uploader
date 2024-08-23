import setuptools

# Use the readme file as the long description on PyPi
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='iridametadatauploader',
    version='0.0.1',
    description='IRIDA Metadata Uploader: upload metadata to IRIDA system',
    url='https://github.com/phac-nml/irida-metadata-uploader',
    author='Darian Hole',
    author_email='darian.hole@phac-aspc.gc.ca',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # license specified on github
    license='Apache-2.0',
    keywords="IRIDA NGS metadata uploader",
    install_requires=['argparse',
                      'configparser',
                      'pandas',
                      'iridauploader'
                      ],
    entry_points={
        'console_scripts': [
            'irida-metadata-uploader=upload_metadata:main'
        ],
    },
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    # urllib3 v2.0 requires >=3.7
    python_requires='>=3.7',
)