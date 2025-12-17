from setuptools import setup
with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
AUTHOR_NAME = "Pranava adithyaa"
SRC_REPO = 'src' 
LIST_OF_REQUIRMENTS =  ['streamlit']
setup(
    name="SRC_REPO",
    author=AUTHOR_NAME,
    version="0.0.1",
    author_email="pranavaadithyaa15@gmail.com',
    description="A small example package for recommender system",
    long_description=long_description,\
    long_description=_content_type="text/markdown",
    package_data={SRC_REPO},
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIRMENTS,
) 
