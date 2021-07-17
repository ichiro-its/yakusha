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
from yakusha.msg import Numbers


def test_numbers_msg():
    msg = Numbers()

    msg.floats.float32 = 3.1415
    msg.floats.float64 = -3.14159265359
    msg.non_floats.integers.int8 = 100
    msg.non_floats.integers.int16 = -10000
    msg.non_floats.integers.int32 = 1000000000
    msg.non_floats.integers.int64 = -1000000000000
    msg.non_floats.unsigned_integers.uint8 = 200
    msg.non_floats.unsigned_integers.uint16 = 20000
    msg.non_floats.unsigned_integers.uint32 = 2000000000
    msg.non_floats.unsigned_integers.uint64 = 2000000000000

    parsed_msg = json_to_msg(msg_to_json(msg), Numbers())

    parsed_floats = parsed_msg.floats
    floats = msg.floats

    assert parsed_floats.float32 == floats.float32
    assert parsed_floats.float64 == floats.float64

    parsed_integers = parsed_msg.non_floats.integers
    integers = msg.non_floats.integers

    assert parsed_integers.int8 == integers.int8
    assert parsed_integers.int16 == integers.int16
    assert parsed_integers.int32 == integers.int32
    assert parsed_integers.int64 == integers.int64

    parsed_unsigned_integers = parsed_msg.non_floats.unsigned_integers
    unsigned_integers = msg.non_floats.unsigned_integers

    assert parsed_unsigned_integers.uint8 == unsigned_integers.uint8
    assert parsed_unsigned_integers.uint16 == unsigned_integers.uint16
    assert parsed_unsigned_integers.uint32 == unsigned_integers.uint32
    assert parsed_unsigned_integers.uint64 == unsigned_integers.uint64


def test_numbers_msg_from_json():
    msg_json = '''{
                    "floats": {
                      "float32": 3.1415,
                      "float64": -3.14159265359
                    },
                    "non_floats": {
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
                  }'''

    parsed_msg = json_to_msg(msg_json, Numbers())

    assert parsed_msg.floats.float32 == 3.1415
    assert parsed_msg.floats.float64 == -3.14159265359
    assert parsed_msg.non_floats.integers.int8 == 100
    assert parsed_msg.non_floats.integers.int16 == -10000
    assert parsed_msg.non_floats.integers.int32 == 1000000000
    assert parsed_msg.non_floats.integers.int64 == -1000000000000
    assert parsed_msg.non_floats.unsigned_integers.uint8 == 200
    assert parsed_msg.non_floats.unsigned_integers.uint16 == 20000
    assert parsed_msg.non_floats.unsigned_integers.uint32 == 2000000000
    assert parsed_msg.non_floats.unsigned_integers.uint64 == 2000000000000
