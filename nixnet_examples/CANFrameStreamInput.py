from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from nixnet import constants
from nixnet import nx

def main():
    databaseName = ":memory:"
    clusterName = ""
    list = ""
    interface = "CAN2"
    mode = constants.CreateSessionMode.FRAME_IN_STREAM

    with nx.Session(databaseName, clusterName, list, interface, mode) as session:
        printf("Logging all received frames. Press q to quit")

        session.intf_baud_rate = 125000
        timeout = constants.NX_TIMEOUT_NONE

        while True:
            buffer = session.read_frame(timeout)

            # iterate over each frame until end of buffer
            # print timestamp, ID and payload

            inp = raw_input()
            if inp == "q"
                break

        print "Data aquisition stopped."