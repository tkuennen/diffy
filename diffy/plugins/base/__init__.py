"""
.. module: diffy.plugins.base
    :platform: Unix
    :copyright: (c) 2018 by Netflix Inc., see AUTHORS for more
    :license: Apache, see LICENSE for more details.

.. moduleauthor:: Kevin Glisson <kglisson@netflix.com>
"""
from __future__ import absolute_import, print_function

from diffy.plugins.base.manager import PluginManager
from diffy.plugins.base.v1 import *  # noqa

plugins = PluginManager()
register = plugins.register
unregister = plugins.unregister