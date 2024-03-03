import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-MLFlow"
AUTHOR_USER_NAME = "yashar1908"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "yash.209302170@muj.manipal.edu"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for a CNN App",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages = setuptools.find_packages(where="src")
)