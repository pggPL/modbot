from setuptools import setup, find_packages

setup(
    name="ModBot",
    version="0.1",
    description="Discord bot for email moderation",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Cezary Botta, Paweł Gadziński, Mateusz Scharmach, Ignacy Stępniewski",
    author_email="pawelgadzinski@gmail.com, c.botta2003@gmail.com , mateusz.scharmach@gmail.com, ignacy2038@gmail.com",
    url="https://github.com/pggPL/modbot",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        # Lista zależności, np. 'requests', 'numpy >= 1.11.1', itp.
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    
    entry_points={
        'console_scripts': [
            'modbot = modbot.__main__:main',
        ],
    },
)
