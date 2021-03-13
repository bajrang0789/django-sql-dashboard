from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="django-sql-dashboard",
    description="Django app for building dashboards using raw SQL queries",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/django-sql-dashboard",
    project_urls={
        "Issues": "https://github.com/simonw/django-sql-dashboard/issues",
        "CI": "https://github.com/simonw/django-sql-dashboard/actions",
        "Changelog": "https://github.com/simonw/django-sql-dashboard/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["django_sql_dashboard"],
    install_requires=["Django"],
    extras_require={"test": ["pytest", "pytest-django", "pytest-pythonpath"]},
    tests_require=["django-sql-dashboard[test]"],
    python_requires=">=3.6",
)
