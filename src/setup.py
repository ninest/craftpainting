import setuptools

with open('../README.md') as readme_file:
  readme = readme_file.read()

setuptools.setup(
    name='craftpainting',
    version='0.0.1',
    packages=setuptools.find_packages(),
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
