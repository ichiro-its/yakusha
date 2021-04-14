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

from kumo_json_interfaces.msg import Arrays

from kumo_json import data_types as dtypes, msg_to_json, json_to_msg


def test_array_msg():
    msg = Arrays()
    msg.int8_array = [1, 2, 3]
    msg.bool_array = [True, False, True]
    msg.string_array = ["hello", "world", "!"]

    parsed_msg = json_to_msg(msg_to_json(msg), Arrays())

    assert parsed_msg.int8_array == msg.int8_array
    assert parsed_msg.bool_array == msg.bool_array
    assert parsed_msg.string_array == msg.string_array


def test_array_msg_from_json():
    msg_json = '''{
                    "int8_array": [1, 2, 3],
                    "bool_array": [true, false, true],
                    "string_array": ["hello", "world", "!"]
                  }'''

    parsed_msg = json_to_msg(msg_json, Arrays())

    assert list(parsed_msg.int8_array) == [1, 2, 3]
    assert list(parsed_msg.bool_array) == [True, False, True]
    assert list(parsed_msg.string_array) == ["hello", "world", "!"]


def test_array_msg_from_json_overflowed_value():
    msg_json = '''{
                    "int8_array": [-200, 200],
                    "bool_array": [true, false, true],
                    "string_array": ["hello", "world", "!"]
                  }'''

    parsed_msg = json_to_msg(msg_json, Arrays())

    assert list(parsed_msg.int8_array) == [dtypes.MIN_INT8, dtypes.MAX_INT8]
