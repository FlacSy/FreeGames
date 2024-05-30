from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-freegames',
    version='1.0.0',
    description='A Python library for scraping and extracting information about game discounts.',
    url='https://github.com/FlacSy/FreeGames',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='FlacSy',
    author_email='flacsy.x@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords=['FreeGames', 'Free Games', 'Free Games API'],
    packages=find_packages(),
    install_requires=['requests', 'bs4'],
)
