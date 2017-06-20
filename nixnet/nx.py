from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

class Session(object):

    def __init__(
            self,
            database_name,
            cluster_name,
            list,
            interface,
            mode):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesession/"
        # What about http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesessionbyref/
        # Store sessionRef as a member variable
        raise NotImplementedError("Placeholder")


    def __exit__(self):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxclear/"
        raise NotImplementedError("Placeholder")


    def read_frame(
            self,
            timeout):
        """
        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        raise NotImplementedError("Placeholder")


def create_session_by_ref(
        number_of_database_ref,
        array_of_database_ref,
        interface,
        mode,
        session_ref):
    raise NotImplementedError("Placeholder")


def get_sub_property(
        session_ref,
        active_index,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def get_sub_property_size(
        session_ref,
        active_index,
        property_id,
        property_size):
    raise NotImplementedError("Placeholder")


def set_sub_property(
        session_ref,
        active_index,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def read_signal_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer):
    raise NotImplementedError("Placeholder")


def read_signal_waveform(
        session_ref,
        timeout,
        start_time,
        delta_time,
        value_buffer,
        size_of_value_buffer,
        number_of_values_returned):
    raise NotImplementedError("Placeholder")


def read_signal_xy(
        session_ref,
        time_limit,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer,
        num_pairs_buffer,
        size_of_num_pairs_buffer):
    raise NotImplementedError("Placeholder")


def read_state(
        session_ref,
        state_id,
        state_size,
        state_value,
        fault):
    raise NotImplementedError("Placeholder")


def write_frame(
        session_ref,
        buffer,
        number_of_bytes_for_frames,
        timeout):
    raise NotImplementedError("Placeholder")


def write_signal_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer):
    raise NotImplementedError("Placeholder")


def write_state(
        session_ref,
        state_id,
        state_size,
        state_value):
    raise NotImplementedError("Placeholder")


def write_signal_waveform(
        session_ref,
        timeout,
        value_buffer,
        size_of_value_buffer):
    raise NotImplementedError("Placeholder")


def write_signal_xy(
        session_ref,
        timeout,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer,
        num_pairs_buffer,
        size_of_num_pairs_buffer):
    raise NotImplementedError("Placeholder")


def convert_frames_to_signals_single_point(
        session_ref,
        frame_buffer,
        number_of_bytes_for_frames,
        value_buffer,
        size_of_value_buffer,
        timestamp_buffer,
        size_of_timestamp_buffer):
    raise NotImplementedError("Placeholder")


def convert_signals_to_frames_single_point(
        session_ref,
        value_buffer,
        size_of_value_buffer,
        buffer,
        size_of_buffer,
        number_of_bytes_returned):
    raise NotImplementedError("Placeholder")


def blink(
        interface_ref,
        modifier):
    raise NotImplementedError("Placeholder")


def clear(
        session_ref):
    raise NotImplementedError("Placeholder")


def connect_terminals(
        session_ref,
        source,
        destination):
    raise NotImplementedError("Placeholder")


def disconnect_terminals(
        session_ref,
        source,
        destination):
    raise NotImplementedError("Placeholder")


def flush(
        session_ref):
    raise NotImplementedError("Placeholder")


def start(
        session_ref,
        scope):
    raise NotImplementedError("Placeholder")


def stop(
        session_ref,
        scope):
    raise NotImplementedError("Placeholder")


def status_to_string(
        status,
        sizeof_string,
        status_description):
    raise NotImplementedError("Placeholder")


def system_open(
        system_ref):
    raise NotImplementedError("Placeholder")


def system_close(
        system_ref):
    raise NotImplementedError("Placeholder")


def wait(
        session_ref,
        condition,
        param_in,
        timeout,
        param_out):
    raise NotImplementedError("Placeholder")