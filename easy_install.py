"""
Simple "open this script and run it" installer for dnppy.
"""

__author__ = 'Jwely'

# set up dependencies for active python directory, includes installation of pip
import install_dependencies
install_dependencies.main()

# uses pip to install this local copy of the repo
import pip
pip.main(["install", "--upgrade", "../dnppy"])
