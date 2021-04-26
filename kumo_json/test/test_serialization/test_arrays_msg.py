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

from kumo_json_interfaces.msg import Arrays

from kumo_json import msg_to_json, json_to_msg

from array import array


def test_array_msg():
    msg = Arrays()
    msg.int8_array = [1, 2, 3]
    msg.uint8_array = [1, 2, 3]
    msg.float32_array = [-3.1415, 3.1415]
    msg.bool_array = [True, False, True]
    msg.string_array = ["hello", "world", "!"]
    msg.byte_array = [b'\x01', b'\x10', b'\x11']

    parsed_msg = json_to_msg(msg_to_json(msg), Arrays())

    assert parsed_msg.int8_array == msg.int8_array
    assert parsed_msg.uint8_array == msg.uint8_array
    assert parsed_msg.float32_array == msg.float32_array
    assert parsed_msg.bool_array == msg.bool_array
    assert parsed_msg.string_array == msg.string_array
    assert parsed_msg.byte_array == msg.byte_array


def test_array_msg_from_json():
    msg_json = '''{
                    "int8_array": [1, 2, 3],
                    "uint8_array": [1, 2, 3],
                    "float32_array": [-3.1415, 3.1415],
                    "bool_array": [true, false, true],
                    "string_array": ["hello", "world", "!"],
                    "byte_array": ["\u0001", "\u0010", "\u0011"]
                  }'''

    parsed_msg = json_to_msg(msg_json, Arrays())

    assert parsed_msg.int8_array == array('b', [1, 2, 3])
    assert parsed_msg.uint8_array == array('B', [1, 2, 3])
    assert parsed_msg.float32_array == array('f', [-3.1415, 3.1415])
    assert parsed_msg.bool_array == [True, False, True]
    assert parsed_msg.string_array == ["hello", "world", "!"]
    assert parsed_msg.byte_array == [b'\x01', b'\x10', b'\x11']
