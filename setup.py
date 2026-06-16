from setuptools import setup, find_packages

setup(
    name='regolith-properties',
    version='0.1.0',
    author='Curiefuel',
    author_email='hello@curiefuel.com',
    description='Lunar and Martian regolith thermal and mechanical property database with uncertainty bounds. Built by Curiefuel for surface nuclear power system design.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/curiefuel/regolith-properties',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'numpy>=1.24.0',
        'scipy>=1.10.0',
        'matplotlib>=3.7.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
