# Copyright (c) 2021 Ichiro ITS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

MIN_INT8 = -(2 ** 7)
MIN_INT16 = -(2 ** 15)
MIN_INT32 = -(2 ** 31)
MIN_INT64 = -(2 ** 63)

MAX_INT8 = (2 ** 7) - 1
MAX_INT16 = (2 ** 15) - 1
MAX_INT32 = (2 ** 31) - 1
MAX_INT64 = (2 ** 63) - 1

MAX_UINT8 = (2 ** 8) - 1
MAX_UINT16 = (2 ** 16) - 1
MAX_UINT32 = (2 ** 32) - 1
MAX_UINT64 = (2 ** 64) - 1


def clamp(value: any, min_value: any, max_value: any) -> any:
    return max(min(value, max_value), min_value)


def is_integer(data_type: str) -> bool:
    return data_type in ['int8', 'int16', 'int32', 'int64']


def filter_integer(data_type: str, value: any) -> int:
    value = int(value)

    if data_type == 'int8':
        value = clamp(value, MIN_INT8, MAX_INT8)
    elif data_type == 'int16':
        value = clamp(value, MIN_INT16, MAX_INT16)
    elif data_type == 'int32':
        value = clamp(value, MIN_INT32, MAX_INT32)
    elif data_type == 'int64':
        value = clamp(value, MIN_INT64, MAX_INT64)

    return value


def is_unsigned_integer(data_type: str) -> bool:
    return data_type in ['uint8', 'uint16', 'uint32', 'uint64']


def filter_unsigned_integer(data_type: str, value: any) -> int:
    value = int(value)

    if data_type == 'uint8':
        value = clamp(value, 0, MAX_UINT8)
    elif data_type == 'uint16':
        value = clamp(value, 0, MAX_UINT16)
    elif data_type == 'uint32':
        value = clamp(value, 0, MAX_UINT32)
    elif data_type == 'uint64':
        value = clamp(value, 0, MAX_UINT64)

    return value


def is_float(data_type: str) -> bool:
    return data_type in ['float', 'double']


def is_array(data_type: str) -> bool:
    return data_type.startswith('sequence')


def filter_type(data_type: str, value: any) -> any:
    if is_integer(data_type):
        value = filter_integer(data_type, value)
    elif is_unsigned_integer(data_type):
        value = filter_unsigned_integer(data_type, value)
    elif is_float(data_type):
        value = float(value)

    return value
