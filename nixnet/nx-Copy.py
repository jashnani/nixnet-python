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
        # Store sessionRef as a member variable
        raise NotImplementedError("Placeholder")


    # What about http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxcreatesessionbyref/


    def __exit__(self):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxclear/"
        raise NotImplementedError("Placeholder")


    def convert_signals_to_frames_single_point(
            self,
            value_buffer,
            size_of_value_buffer,
            buffer,
            size_of_buffer,
            number_of_bytes_returned):
        """
        Valid modes
        - nxMode_SignalConversionSinglePoint
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxconvertsignalstoframessinglepoint/
        """
        raise NotImplementedError("Placeholder")


    def convert_frames_to_signals_single_point(
            self,
            frame_buffer,
            number_of_bytes_for_frames,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer):
        """
        Valid modes
        - nxMode_SignalConversionSinglePoint
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxconvertframestosignalssinglepoint/
        """
        raise NotImplementedError("Placeholder")


    def connect_terminals(
            self,
            source,
            destination):
        """
        Seems like there is a fixed list of terminals.  Use an enum?
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxconnectterminals/
        """
        raise NotImplementedError("Placeholder")


    def disconnect_terminals(
            self,
            source,
            destination):
        """
        Seems like there is a fixed list of terminals.  Use an enum?
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxdisconnectterminals/
        """
        raise NotImplementedError("Placeholder")


    def flush(self):
        """
        Clears the read or write buffers for non-singlepoint and non-conversion modes
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxflush/
        """
        raise NotImplementedError("Placeholder")


    def start(
            self,
            scope):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxstart/"
        raise NotImplementedError("Placeholder")


    def stop(
            self,
            scope):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxstop/"
        raise NotImplementedError("Placeholder")


    def wait(
            self,
            condition,
            param_in,
            timeout,
            param_out):
        """
        Function per wait mode like LV?
         paramIn/ParamOut seem to be unused for the supported wait modes
         http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwait/
        """
        raise NotImplementedError("Placeholder")


    def read_frame(
            self,
            buffer,
            size_of_buffer,
            timeout,
            number_of_bytes_returned):
        """
        Valid modes
        - Frame Input Stream Mode
        - Frame Input Queued Mode
        - Frame Input Single-Point Mode
        Frame: one or more
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadframe/
        """
        raise NotImplementedError("Placeholder")


    def read_signal_single_point(
            self,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer):
        """
        Valid modes
        - Single Input Single-Point
         Timestamps
        - Optional in C API
        - Timestamp per data point
        Should we expose this as [(timestamp, data)]?
         Special behavior for trigger signals.  Should we expose these in any special way? Either in the signal name or in the data?
         http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadsignalsinglepoint/
        """
        raise NotImplementedError("Placeholder")


    def read_signal_waveform(
            self,
            timeout,
            start_time,
            delta_time,
            value_buffer,
            size_of_value_buffer,
            number_of_values_returned):
        """
        Valid modes
        - Signal Input Waveform Mode
         http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadsignalwaveform/
        """
        raise NotImplementedError("Placeholder")


    def read_signal_xy(
            self,
            time_limit,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer):
        """
        Valid modes
        - Signal Input XY Mode
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadsignalxy/
        """
        raise NotImplementedError("Placeholder")


    def read_state(
            self,
            state_id,
            state_size,
            state_value,
            fault):
        """
        Valid Modes
        - All (but Conversion?)
         Reported format is dependent on State.  Make this a function per state? That is what LV does.
         How is fault different than return code?  Should both just throw?  If its non-fatal, how do we report it to the user?
        http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxreadstate/
        """
        raise NotImplementedError("Placeholder")


    def write_frame(
            self,
            buffer,
            number_of_bytes_for_frames,
            timeout):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwriteframe/"
        raise NotImplementedError("Placeholder")


    def write_signal_single_point(
            self,
            value_buffer,
            size_of_value_buffer):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwritesignalsinglepoint/"
        raise NotImplementedError("Placeholder")


    def write_state(
            self,
            state_id,
            state_size,
            state_value):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwritestate/"
        raise NotImplementedError("Placeholder")


    def write_signal_waveform(
            session_ref,
            timeout,
            value_buffer,
            size_of_value_buffer):
        "http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwritesignalwaveform/"
        raise NotImplementedError("Placeholder")


    def write_signal_xy(
            self,
            timeout,
            value_buffer,
            size_of_value_buffer,
            timestamp_buffer,
            size_of_timestamp_buffer,
            num_pairs_buffer,
            size_of_num_pairs_buffer):
        """
        Timestamps aren't currently supported
         http://zone.ni.com/reference/en-XX/help/372841N-01/nixnet/nxwritesignalxy/
        """
        raise NotImplementedError("Placeholder")


def get_property(
        session_ref,
        property_id,
        property_size,
        property_value):
    raise NotImplementedError("Placeholder")


def get_property_size(
        session_ref,
        property_id,
        property_size):
    raise NotImplementedError("Placeholder")


def set_property(
        session_ref,
        property_id,
        property_size,
        property_value):
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


def blink(
        interface_ref,
        modifier):
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
