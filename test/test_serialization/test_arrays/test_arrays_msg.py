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

from yakusha import msg_to_json, json_to_msg
from yakusha.msg import Arrays, NonFloats, NonNumbers

from array import array


def test_array_msg():
    msg = Arrays()
    msg.int8_array = [1, 2, 3]
    msg.uint8_array = [1, 2, 3]
    msg.float32_array = [-3.1415, 3.1415]
    msg.bool_array = [True, False, True]
    msg.string_array = ["hello", "world", "!"]
    msg.byte_array = [b'\x01', b'\x10', b'\x11']

    non_floats_msg = NonFloats()
    non_floats_msg.integers.int8 = 100
    non_floats_msg.integers.int16 = -10000
    non_floats_msg.integers.int32 = 1000000000
    non_floats_msg.integers.int64 = -1000000000000
    non_floats_msg.unsigned_integers.uint8 = 200
    non_floats_msg.unsigned_integers.uint16 = 20000
    non_floats_msg.unsigned_integers.uint32 = 2000000000
    non_floats_msg.unsigned_integers.uint64 = 2000000000000

    msg.non_floats_array = [non_floats_msg, non_floats_msg]

    non_numbers_msg = NonNumbers()
    non_numbers_msg.boolean = True
    non_numbers_msg.string = "hello"
    non_numbers_msg.byte = b'\x01'

    msg.non_numbers_array = [non_numbers_msg, non_numbers_msg]

    parsed_msg = json_to_msg(msg_to_json(msg), Arrays())

    assert parsed_msg.int8_array == msg.int8_array
    assert parsed_msg.uint8_array == msg.uint8_array
    assert parsed_msg.float32_array == msg.float32_array
    assert parsed_msg.bool_array == msg.bool_array
    assert parsed_msg.string_array == msg.string_array
    assert parsed_msg.byte_array == msg.byte_array
    assert parsed_msg.non_floats_array == msg.non_floats_array
    assert parsed_msg.non_numbers_array == msg.non_numbers_array


def test_array_msg_from_json():
    msg_json = '''{
                    "int8_array": [1, 2, 3],
                    "uint8_array": [1, 2, 3],
                    "float32_array": [-3.1415, 3.1415],
                    "bool_array": [true, false, true],
                    "string_array": ["hello", "world", "!"],
                    "byte_array": ["\u0001", "\u0010", "\u0011"],
                    "non_floats_array": [
                        {
                            "integers": {
                            "int8": 100,
                            "int16": -10000,
                            "int32": 1000000000,
                            "int64": -1000000000000
                            },
                            "unsigned_integers": {
                            "uint8": 200,
                            "uint16": 20000,
                            "uint32": 2000000000,
                            "uint64": 2000000000000
                            }
                        },
                        {
                            "integers": {
                            "int8": 100,
                            "int16": -10000,
                            "int32": 1000000000,
                            "int64": -1000000000000
                            },
                            "unsigned_integers": {
                            "uint8": 200,
                            "uint16": 20000,
                            "uint32": 2000000000,
                            "uint64": 2000000000000
                            }
                        }
                    ],
                    "non_numbers_array": [
                        {
                            "boolean": true,
                            "string": "hello",
                            "byte": "\u0001"
                        },
                        {
                            "boolean": true,
                            "string": "hello",
                            "byte": "\u0001"
                        }
                    ]
                  }'''

    parsed_msg = json_to_msg(msg_json, Arrays())

    non_floats_msg = NonFloats()
    non_floats_msg.integers.int8 = 100
    non_floats_msg.integers.int16 = -10000
    non_floats_msg.integers.int32 = 1000000000
    non_floats_msg.integers.int64 = -1000000000000
    non_floats_msg.unsigned_integers.uint8 = 200
    non_floats_msg.unsigned_integers.uint16 = 20000
    non_floats_msg.unsigned_integers.uint32 = 2000000000
    non_floats_msg.unsigned_integers.uint64 = 2000000000000

    non_numbers_msg = NonNumbers()
    non_numbers_msg.boolean = True
    non_numbers_msg.string = "hello"
    non_numbers_msg.byte = b'\x01'

    assert parsed_msg.int8_array == array('b', [1, 2, 3])
    assert parsed_msg.uint8_array == array('B', [1, 2, 3])
    assert parsed_msg.float32_array == array('f', [-3.1415, 3.1415])
    assert parsed_msg.bool_array == [True, False, True]
    assert parsed_msg.string_array == ["hello", "world", "!"]
    assert parsed_msg.byte_array == [b'\x01', b'\x10', b'\x11']
    assert parsed_msg.non_floats_array == [non_floats_msg, non_floats_msg]
    assert parsed_msg.non_numbers_array == [non_numbers_msg, non_numbers_msg]
