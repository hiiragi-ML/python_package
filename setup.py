from setuptools import setup, find_packages

setup(
    name="samplelib",
    version="1.2",
    description="Pythonディレクトリ構成のテスト用",
    author="hiiragi-ML",
    author_email="hiiragisatoru1221@gmail.com",
    url="https://github.com/hiiragi-ML/python_package",
    packages=find_packages(),
    entry_points="""
      [console_scripts]
      samplelib = samplelib.cli:execute
    """,
    install_requires=open('requirements.txt').read().splitlines(),
)
