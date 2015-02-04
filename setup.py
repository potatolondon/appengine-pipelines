#!/usr/bin/env python
"""Setup specs for packaging, distributing, and installing Pipeline lib."""

import setuptools

# To debug, set DISTUTILS_DEBUG env var to anything.
setuptools.setup(
    name="GoogleAppEnginePipeline-Potatoified",
    version="1.9.15.1",
    packages=setuptools.find_packages(),
    author="Google App Engine",
    author_email="https://github.com/potatolondon/appengine-pipelines.git",
    keywords="google app engine pipeline data processing",
    url="https://github.com/potatolondon/appengine-pipelines.git",
    license="Apache License 2.0",
    description=("Enable asynchronous pipeline style data processing on "
                 "App Engine"),
    zip_safe=True,
    include_package_data=True,
    # Exclude these files from installation.
    exclude_package_data={"": ["README"]},
    install_requires=[
      "GoogleAppEngineCloudStorageClient >= 1.9.15"
      ]
)
