from setuptools import setup, find_packages

setup(
    name="analiz-pogody",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "analiz-pogody=analiz_pogody.cli:main",
        ],
    },
    description="Пакет для анализа погодных данных",
    author="Студент",
)
