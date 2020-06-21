import setuptools

with open('../README.md') as readme_file:
  readme = readme_file.read()

setuptools.setup(
    name='craftpainting',
    version='0.0.3',
    packages=setuptools.find_packages(),
    entry_points={
      'console_scripts': [
        'craftpainting = craftpainting.__main__:main'
      ]
    },
    license='MIT',
    url='https://github.com/ninest/craftpainting',
    project_urls={
        "Bug Tracker": "https://github.com/ninest/craftpainting/issues",
        "Documentation": "https://github.com/ninest/craftpainting",
        "Source Code": "https://github.com/ninest/craftpainting",
    },
    long_description_content_type="text/markdown",
    description='Create Minecraft-like paintings',
    long_description=readme,
)

'''
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
'''