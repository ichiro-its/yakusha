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

from yakusha_interfaces.msg import NonFloats

from yakusha import msg_to_json, json_to_msg


def test_non_floats_msg():
    msg = NonFloats()

    msg.integers.int8 = 100
    msg.integers.int16 = -10000
    msg.integers.int32 = 1000000000
    msg.integers.int64 = -1000000000000
    msg.unsigned_integers.uint8 = 200
    msg.unsigned_integers.uint16 = 20000
    msg.unsigned_integers.uint32 = 2000000000
    msg.unsigned_integers.uint64 = 2000000000000

    parsed_msg = json_to_msg(msg_to_json(msg), NonFloats())

    assert parsed_msg.integers.int8 == msg.integers.int8
    assert parsed_msg.integers.int16 == msg.integers.int16
    assert parsed_msg.integers.int32 == msg.integers.int32
    assert parsed_msg.integers.int64 == msg.integers.int64
    assert parsed_msg.unsigned_integers.uint8 == msg.unsigned_integers.uint8
    assert parsed_msg.unsigned_integers.uint16 == msg.unsigned_integers.uint16
    assert parsed_msg.unsigned_integers.uint32 == msg.unsigned_integers.uint32
    assert parsed_msg.unsigned_integers.uint64 == msg.unsigned_integers.uint64


def test_non_floats_msg_from_json():
    msg_json = '''{
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
                  }'''

    parsed_msg = json_to_msg(msg_json, NonFloats())

    assert parsed_msg.integers.int8 == 100
    assert parsed_msg.integers.int16 == -10000
    assert parsed_msg.integers.int32 == 1000000000
    assert parsed_msg.integers.int64 == -1000000000000
    assert parsed_msg.unsigned_integers.uint8 == 200
    assert parsed_msg.unsigned_integers.uint16 == 20000
    assert parsed_msg.unsigned_integers.uint32 == 2000000000
    assert parsed_msg.unsigned_integers.uint64 == 2000000000000
