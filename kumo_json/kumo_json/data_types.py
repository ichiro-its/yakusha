# Copyright (c) 2021 ICHIRO ITS
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


def is_integer(data_type: str) -> bool:
    return data_type in ['int8', 'int16', 'int32', 'int64']


def is_unsigned_integer(data_type: str) -> bool:
    return data_type in ['uint8', 'uint16', 'uint32', 'uint64']


def is_float(data_type: str) -> bool:
    return data_type in ['float', 'double']


def is_byte(data_type: str) -> bool:
    return data_type == 'octet'


def is_array(data_type: str) -> bool:
    return data_type.startswith('sequence')


def filter_type(data_type: str, value: any) -> any:
    if is_integer(data_type) or is_unsigned_integer(data_type):
        value = int(value)
    elif is_float(data_type):
        value = float(value)
    elif is_byte(data_type):
        value = str.encode(value)

    return value


def get_sequence_item_type(data_type: str) -> str:
    opening_tag_index = data_type.find('<') + 1

    for index, char in enumerate(data_type):
        if char in [',', '>']:
            closing_tag_index = index
            break

    return data_type[opening_tag_index:closing_tag_index]
