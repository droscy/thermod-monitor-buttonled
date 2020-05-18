# -*- coding: utf-8 -*-
"""Setup script for Thermod ButtonLED monitor.

@author:     Simone Rossetto
@copyright:  2018 Simone Rossetto
@license:    GNU General Public License v3
@contact:    simros85@gmail.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup

__updated__ = '2020-05-11'

def get_version():
    main_ns = {}
    version_str = None
    
    with open('thermod-monitor-buttonled','rt') as script:
        for line in script:
            if line.find('__version__') == 0:
                version_str = '# -*- coding: utf-8 -*-\n{}'.format(line)
                break
    
    exec(version_str, main_ns)
    return main_ns['__version__']

def get_readme():
    with open('README.md', 'r') as readme:
        txt = readme.read()
    return txt

setup(name='thermod-monitor-buttonled',
      version=get_version(),
      description='Thermod monitor for Raspberry Pi with one Button and one RGB LED',
      author='Simone Rossetto',
      author_email='simros85@gmail.com',
      long_description=get_readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/droscy/thermod-monitor-buttonled',
      license = 'GPL-3.0+',
      classifiers=['Programming Language :: Python :: 3',
                   'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                   'Environment :: Console'],
      scripts=['thermod-monitor-buttonled'],
      python_requires='>=3.5',
      install_requires=['thermod >=1.0.0, <2.0.0',
                        'requests >=2.4.3',
                        'gpiozero >=1.3.0'])

# vim: fileencoding=utf-8 tabstop=4 shiftwidth=4 expandtab
