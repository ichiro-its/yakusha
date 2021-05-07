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

import json
from rclpy.node import MsgType

import kumo_json.data_types as dtypes


def fiter_type(value: any, data_type: str) -> any:
    if dtypes.is_integer(data_type) or dtypes.is_unsigned_integer(data_type):
        return int(value)
    elif dtypes.is_float(data_type):
        return float(value)
    elif dtypes.is_byte(data_type):
        return value.decode('ISO-8859-1')
    elif 'msg' in str(type(value)):
        return msg_to_dict(value)

    return value


def msg_to_dict(msg: MsgType) -> dict:
    fields = msg.get_fields_and_field_types()

    msg_dict = {}
    for field, data_type in fields.items():
        if not hasattr(msg, field):
            continue

        value = getattr(msg, field)

        if dtypes.is_array(data_type):
            value = [fiter_type(element, dtypes.get_sequence_item_type(data_type))
                     for element in value]
        else:
            value = fiter_type(value, data_type)

        msg_dict[field] = value

    return msg_dict


def msg_to_json(msg: MsgType) -> str:
    msg_dict = msg_to_dict(msg)

    return json.dumps(msg_dict)
