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
from yakusha.msg import Integers


def test_integers_msg():
    msg = Integers()

    msg.int8 = 100
    msg.int16 = 10000
    msg.int32 = 1000000000
    msg.int64 = 1000000000000

    parsed_msg = json_to_msg(msg_to_json(msg), Integers())

    assert parsed_msg.int8 == msg.int8
    assert parsed_msg.int16 == msg.int16
    assert parsed_msg.int32 == msg.int32
    assert parsed_msg.int64 == msg.int64


def test_integers_msg_negative():
    msg = Integers()

    msg.int8 = -100
    msg.int16 = -10000
    msg.int32 = -1000000000
    msg.int64 = -1000000000000

    parsed_msg = json_to_msg(msg_to_json(msg), Integers())

    assert parsed_msg.int8 == msg.int8
    assert parsed_msg.int16 == msg.int16
    assert parsed_msg.int32 == msg.int32
    assert parsed_msg.int64 == msg.int64


def test_integers_msg_from_json():
    msg_json = '''{
                    "int8": 100,
                    "int16": 10000,
                    "int32": 1000000000,
                    "int64": 1000000000000
                  }'''

    parsed_msg = json_to_msg(msg_json, Integers())

    assert parsed_msg.int8 == 100
    assert parsed_msg.int16 == 10000
    assert parsed_msg.int32 == 1000000000
    assert parsed_msg.int64 == 1000000000000


def test_integers_msg_from_json_negative():
    msg_json = '''{
                    "int8": -100,
                    "int16": -10000,
                    "int32": -1000000000,
                    "int64": -1000000000000
                  }'''

    parsed_msg = json_to_msg(msg_json, Integers())

    assert parsed_msg.int8 == -100
    assert parsed_msg.int16 == -10000
    assert parsed_msg.int32 == -1000000000
    assert parsed_msg.int64 == -1000000000000


def test_integers_msg_from_json_float():
    msg_json = '''{
                    "int8": 3.14,
                    "int16": 5000.1,
                    "int32": -3.14,
                    "int64": 0.0001
                  }'''

    parsed_msg = json_to_msg(msg_json, Integers())

    assert parsed_msg.int8 == 3
    assert parsed_msg.int16 == 5000
    assert parsed_msg.int32 == -3
    assert parsed_msg.int64 == 0
