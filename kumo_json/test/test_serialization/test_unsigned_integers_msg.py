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

from kumo_json_interfaces.msg import UnsignedIntegers

from kumo_json import msg_to_json, json_to_msg


def test_unsigned_integers_msg():
    msg = UnsignedIntegers()
    msg.uint8 = 200
    msg.uint16 = 20000
    msg.uint32 = 2000000000
    msg.uint64 = 2000000000000

    parsed_msg = json_to_msg(msg_to_json(msg), UnsignedIntegers())

    assert parsed_msg.uint8 == msg.uint8
    assert parsed_msg.uint16 == msg.uint16
    assert parsed_msg.uint32 == msg.uint32
    assert parsed_msg.uint64 == msg.uint64


def test_unsigned_integers_msg_from_json():
    msg_json = '''{
                    "uint8": 200,
                    "uint16": 20000,
                    "uint32": 2000000000,
                    "uint64": 2000000000000
                  }'''

    parsed_msg = json_to_msg(msg_json, UnsignedIntegers())

    assert parsed_msg.uint8 == 200
    assert parsed_msg.uint16 == 20000
    assert parsed_msg.uint32 == 2000000000
    assert parsed_msg.uint64 == 2000000000000


def test_unsigned_integers_msg_from_json_float():
    msg_json = '''{
                    "uint8": 3.14,
                    "uint16": 5000.1,
                    "uint32": 3.14,
                    "uint64": 0.0001
                  }'''

    parsed_msg = json_to_msg(msg_json, UnsignedIntegers())

    assert parsed_msg.uint8 == 3
    assert parsed_msg.uint16 == 5000
    assert parsed_msg.uint32 == 3
    assert parsed_msg.uint64 == 0
