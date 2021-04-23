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


def dict_to_msg(msg_dict: dict, msg: MsgType) -> MsgType:
    fields = msg.get_fields_and_field_types()

    for field, data_type in fields.items():
        if not hasattr(msg, field):
            continue

        value = msg_dict.get(field)

        if dtypes.is_array(data_type):
            sequence_data_type = data_type[data_type.find('<')+1:data_type.find('>')]
            for index, item in enumerate(value):
                value[index] = dtypes.filter_type(sequence_data_type, item)
        else:
            value = dtypes.filter_type(data_type, value)

        setattr(msg, field, value)

    return msg


def json_to_msg(msg_json: str, msg: MsgType) -> MsgType:
    msg_dict = json.loads(msg_json, strict=False)

    return dict_to_msg(msg_dict, msg)
