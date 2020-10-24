import os
import time
import pexpect


def test_sr():
    file_send = "file_test.txt"
    file_receive = "file_test_rcv.txt"

    receiver = pexpect.spawn(f"python3 file_receiver.py sr {file_receive}")
    sender = pexpect.spawn(f"python3 file_sender.py sr {file_send}")

    # wait for 1 sec, then terminate receiver
    time.sleep(1)
    receiver.sendcontrol('c')
    receiver.close()
    sender.close()

    # compare output
    output = os.popen(f"md5 {file_send} {file_receive}").read()

    file_send_checksum = output.split("\n")[0].split()[-1]
    file_receive_checksum = output.split("\n")[1].split()[-1]

    assert file_send_checksum == file_receive_checksum


def test_gbn():
    file_send = "file_test.txt"
    file_receive = "file_test_rcv.txt"

    receiver = pexpect.spawn(f"python3 file_receiver.py gbn {file_receive}")
    sender = pexpect.spawn(f"python3 file_sender.py gbn {file_send}")

    # wait for 1 sec, then terminate receiver
    time.sleep(1)
    receiver.sendcontrol('c')
    receiver.close()
    sender.close()

    # compare output
    output = os.popen(f"md5 {file_send} {file_receive}").read()

    file_send_checksum = output.split("\n")[0].split()[-1]
    file_receive_checksum = output.split("\n")[1].split()[-1]

    assert file_send_checksum == file_receive_checksum