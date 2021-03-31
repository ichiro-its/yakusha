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

from kumo_json import msg_to_json, json_to_msg
from std_msgs.msg import ColorRGBA


def test_color_rgba_msg():
    msg = ColorRGBA()

    msg.r = 0.0
    msg.g = 64.0
    msg.b = 128.0
    msg.a = 255.0

    parsed_msg = json_to_msg(msg_to_json(msg), ColorRGBA())

    assert parsed_msg.r == msg.r
    assert parsed_msg.g == msg.g
    assert parsed_msg.b == msg.b
    assert parsed_msg.a == msg.a


def test_color_rgba_msg_from_json():
    msg_json = '''{
                    "r": 0.0,
                    "g": 64.0,
                    "b": 128.0,
                    "a": 255.0
                  }'''

    parsed_msg = json_to_msg(msg_json, ColorRGBA())

    assert parsed_msg.r == 0.0
    assert parsed_msg.g == 64.0
    assert parsed_msg.b == 128.0
    assert parsed_msg.a == 255.0
