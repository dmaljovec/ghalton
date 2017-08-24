# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_ghalton_wrapper')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_ghalton_wrapper')
    _ghalton_wrapper = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ghalton_wrapper', [dirname(__file__)])
        except ImportError:
            import _ghalton_wrapper
            return _ghalton_wrapper
        try:
            _mod = imp.load_module('_ghalton_wrapper', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _ghalton_wrapper = swig_import_helper()
    del swig_import_helper
else:
    import _ghalton_wrapper
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SizeError(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SizeError, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SizeError, name)
    __repr__ = _swig_repr

    def __init__(self, inMessage):
        this = _ghalton_wrapper.new_SizeError(inMessage)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def what(self):
        return _ghalton_wrapper.SizeError_what(self)
    __swig_destroy__ = _ghalton_wrapper.delete_SizeError
    __del__ = lambda self: None
SizeError_swigregister = _ghalton_wrapper.SizeError_swigregister
SizeError_swigregister(SizeError)

class GeneralizedHalton(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GeneralizedHalton, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GeneralizedHalton, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _ghalton_wrapper.new_GeneralizedHalton(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ghalton_wrapper.delete_GeneralizedHalton
    __del__ = lambda self: None

    def get(self, inCount=1):
        return _ghalton_wrapper.GeneralizedHalton_get(self, inCount)

    def reset(self):
        return _ghalton_wrapper.GeneralizedHalton_reset(self)

    def seed(self, *args):
        return _ghalton_wrapper.GeneralizedHalton_seed(self, *args)
GeneralizedHalton_swigregister = _ghalton_wrapper.GeneralizedHalton_swigregister
GeneralizedHalton_swigregister(GeneralizedHalton)

class Halton(GeneralizedHalton):
    __swig_setmethods__ = {}
    for _s in [GeneralizedHalton]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Halton, name, value)
    __swig_getmethods__ = {}
    for _s in [GeneralizedHalton]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Halton, name)
    __repr__ = _swig_repr

    def __init__(self, inDim):
        this = _ghalton_wrapper.new_Halton(inDim)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _ghalton_wrapper.delete_Halton
    __del__ = lambda self: None
Halton_swigregister = _ghalton_wrapper.Halton_swigregister
Halton_swigregister(Halton)

# This file is compatible with both classic and new-style classes.


