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

import json
from rclpy.node import MsgType
from rosidl_parser.definition import NamespacedType
from rosidl_runtime_py.convert import get_message_slot_types
from rosidl_runtime_py.import_message import import_message_from_namespaced_type

import kumo_json.data_types as dtypes


def filter_type(data_type: str, value: any, attribute: any) -> any:
    if dtypes.is_integer(data_type) or dtypes.is_unsigned_integer(data_type):
        value = int(value)
    elif dtypes.is_float(data_type):
        value = float(value)
    elif dtypes.is_byte(data_type):
        value = value.encode('ISO-8859-1')
    elif 'msg' in str(attribute):
        value = dict_to_msg(value, attribute)

    return value


def dict_to_msg(msg_dict: dict, msg: MsgType) -> MsgType:
    fields = msg.get_fields_and_field_types()

    for field, data_type in fields.items():
        if not hasattr(msg, field):
            continue

        value = msg_dict.get(field)

        if dtypes.is_array(data_type):
            rosidl_type = get_message_slot_types(msg)[field]
            if isinstance(rosidl_type.value_type, NamespacedType):
                field_elem_type = import_message_from_namespaced_type(rosidl_type.value_type)
                for n in range(len(value)):
                    submsg = field_elem_type()
                    value[n] = filter_type(None, value[n], submsg)
            else:
                sequence_item_type = dtypes.get_sequence_item_type(data_type)
                for index, item in enumerate(value):
                    value[index] = filter_type(sequence_item_type, item, getattr(msg, field))
        else:
            value = filter_type(data_type, value, getattr(msg, field))

        setattr(msg, field, value)

    return msg


def json_to_msg(msg_json: str, msg: MsgType) -> MsgType:
    msg_dict = json.loads(msg_json, strict=False)

    return dict_to_msg(msg_dict, msg)
