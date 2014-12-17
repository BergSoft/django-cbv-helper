
from setuptools import setup, find_packages


version = __import__('cbv_helper').get_version()


def get_requires_list(filename):
    s = open(filename).read().split("\n")
    dependenses = []
    if len(s):
        for pkg in s:
            if pkg.strip() == '' or pkg.startswith("#"):
                continue
            if pkg.startswith("-e"):
                continue
                try:
                    p = pkg.split("#egg=")[1]
                    dependenses += [p, ]
                except:
                    continue
            else:
                dependenses += [pkg, ]
    return dependenses


setup(
    name = "django-cbv-helper",
    version = version,
    description = "Collect class based views for Django",
    keywords = "cbv, class based views",
    author = "Oleksandr Shtalinberg",
    author_email = "shtalinberg@mail.ru",
    url = "https://github.com/BergSoft/django-cbv-helper",
    license = "New BSD License",
    platforms = ["any"],
    classifiers = ["Development Status :: 4 - Beta",
                   "Environment :: Web Environment",
                   "Framework :: Django",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Topic :: Utilities"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)

