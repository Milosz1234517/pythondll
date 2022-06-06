import ctypes
import os

ctypes.windll.kernel32.SetDllDirectoryW(None)

lib_path = os.path.join(os.path.dirname(__file__), 'native.dll')
inter = ctypes.cdll.LoadLibrary(lib_path)
inter.interpolation.argtypes = (ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_float)
inter.interpolation.restype = ctypes.c_float


def calculateInterpolation(x, f, val):
    n = len(x)
    array_type = ctypes.c_float * n
    result = inter.interpolation(array_type(*x), array_type(*f), ctypes.c_int(n), ctypes.c_float(val))
    return result
