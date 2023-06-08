# Helps define a constant in Python
# From Section 6.3: Defining Constants
# Python Cookbook (2 Ed) by Alex Martelli et al.
#
# Usage:
# import const
# const.magic = 23 # First binding is fine
# const.magic = 88 # Second binding raises const.ConstError
#
# Adapted by Augusto Manzano for Python 3.6.4
#

class _const:

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__: 
      # if self.__dict__.has_key(name):
            raise self.ConstError("Can't rebind const(%s)" % name)
          # raise self.ConstError, "Can't rebind const(%s)" % name
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()
