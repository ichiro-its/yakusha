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

from std_msgs.msg import Float32

from kumo_json import msg_to_json, json_to_msg


def test_float32_msg():
    msg = Float32()
    msg.data = 3.14

    parsed_msg = json_to_msg(msg_to_json(msg), Float32())

    assert parsed_msg.data == msg.data


def test_float32_msg_from_json():
    msg_json = '{ "data": 3.14 }'

    parsed_msg = json_to_msg(msg_json, Float32())

    assert parsed_msg.data == 3.14


def test_float32_msg_from_json_integer():
    msg_json = '{ "data": 50 }'

    parsed_msg = json_to_msg(msg_json, Float32())

    assert parsed_msg.data == 50.0
