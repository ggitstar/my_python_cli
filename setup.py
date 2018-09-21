from setuptools import setup, find_packages  
  
setup(  
    name='git_empty_dir',  
    version='1.0',  
    packages=find_packages(),  
    #install_requires=['cliff'],  
    entry_points={  
        'console_scripts':  
            'git-empty-dir = git_empty_init.main:main'  
    },  
    zip_safe=False,  
    classifiers=[  
          'Environment :: Console',  
          'Intended Audience :: Developers',  
          'Operating System :: MacOS :: MacOS X',  
          'Programming Language :: Python',  
          'Programming Language :: Python :: 2.7',  
    ],  
)  