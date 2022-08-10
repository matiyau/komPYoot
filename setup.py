import setuptools

with open('requirements.txt') as f:
    required = f.read().splitlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="komPYoot",  # Replace with your own username
    version="1.0.0",
    author="Nishad Mandlik",
    author_email="mandliksg@gmail.com",
    description="Python Interface for Komoot API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matiyau/komPYoot",
    project_urls={
        "Documentation": "https://komPYoot.rtfd.io",
        "Bug Tracker": "https://github.com/matiyau/komPYoot/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_reqs=required,
    python_requires=">=3.6",
)
