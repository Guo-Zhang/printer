# --*-- coding: utf-8 --*--

from distutils.core import setup
import py2exe

setup(console=["printer.py"])

setup(console=["helloworld.py"],
      data_files=[("base",
                   [
                       "base/base0.jpg",
                       "base/base1.jpg",
                       "base/base2.jpg",
                       "base/base3.jpg",
                       "base/base4.jpg",
                    ]),
                  ]
)