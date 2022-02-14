import TControl as tc
import can
import time
motor_ID = 2

try:
    bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
except:
    print("Failed to open CAN bus.")
else:
    v_des = 0.0
    i_des = 0.0
    Kp = 10.0
    Kd = 1.0

    tc.power_on(bus, motor_ID)
    tc.zero(bus, motor_ID)

    end_time = time.time() + 10.0

    while time.time() < end_time:
        msg = bus.recv(timeout=1)
        if msg is not None:
            print(tc.parse_MIT_message(msg))
        tc.power_on(bus, motor_ID)
        time.sleep(0.01)

    # while time.time() < end_time:
    #     msg = bus.recv(timeout=2)
    #     if msg is not None:
    #         print(tc.parse_MIT_message(msg))
    #     tc.MIT_controller(bus, motor_ID, 0.0, v_des, Kp, Kd, i_des)
    #     time.sleep(2)
    #     msg = bus.recv(timeout=2)
    #     if msg is not None:
    #         print(tc.parse_MIT_message(msg))
    #     tc.MIT_controller(bus, motor_ID, 3.14, v_des, Kp, Kd, i_des)
    #     time.sleep(2)



    tc.power_off(bus, motor_ID)