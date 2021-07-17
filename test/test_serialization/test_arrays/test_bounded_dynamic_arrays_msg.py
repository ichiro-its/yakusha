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
from yakusha.msg import BoundedDynamicArrays

from array import array


def test_bounded_dynamic_array_msg():
    msg = BoundedDynamicArrays()
    msg.int8_bounded_dynamic_array = [1, 2, 3]
    msg.uint8_bounded_dynamic_array = [1, 2, 3]
    msg.float32_bounded_dynamic_array = [-3.1415, 3.1415]
    msg.bool_bounded_dynamic_array = [True, False, True]
    msg.string_bounded_dynamic_array = ["hello", "world", "!"]

    parsed_msg = json_to_msg(msg_to_json(msg), BoundedDynamicArrays())

    assert parsed_msg.int8_bounded_dynamic_array == msg.int8_bounded_dynamic_array
    assert parsed_msg.uint8_bounded_dynamic_array == msg.uint8_bounded_dynamic_array
    assert parsed_msg.float32_bounded_dynamic_array == msg.float32_bounded_dynamic_array
    assert parsed_msg.bool_bounded_dynamic_array == msg.bool_bounded_dynamic_array
    assert parsed_msg.string_bounded_dynamic_array == msg.string_bounded_dynamic_array


def test_bounded_dynamic_array_msg_from_json():
    msg_json = '''{
                    "int8_bounded_dynamic_array": [1, 2, 3],
                    "uint8_bounded_dynamic_array": [1, 2, 3],
                    "float32_bounded_dynamic_array": [-3.1415, 3.1415],
                    "bool_bounded_dynamic_array": [true, false, true],
                    "string_bounded_dynamic_array": ["hello", "world", "!"]
                  }'''

    parsed_msg = json_to_msg(msg_json, BoundedDynamicArrays())

    assert parsed_msg.int8_bounded_dynamic_array == array('b', [1, 2, 3])
    assert parsed_msg.uint8_bounded_dynamic_array == array('B', [1, 2, 3])
    assert parsed_msg.float32_bounded_dynamic_array == array('f', [-3.1415, 3.1415])
    assert parsed_msg.bool_bounded_dynamic_array == [True, False, True]
    assert parsed_msg.string_bounded_dynamic_array == ["hello", "world", "!"]
