import serial
import time
import autopilot
import definitions as vars
import msp_helper as msp

command_delays =  {
    'go_forward': 2,
    'deliver': 1
}

command_target_ids = {
    'MSP_ANALOG': msp.MSP_ANALOG,
    'MSP_ALTITUDE': msp.MSP_ALTITUDE,
    'MSP_RC': msp.MSP_RC
}

serial_port = {}

def wait_for_execution(target, delay=0):
    if delay == 0:
        delay = command_delays.get(target)
    time.sleep(delay)

def get_target_id(target):
    return int(command_target_ids.get(target))
    
def connect():
    global serial_port
    serial_port = serial.Serial(
        vars.companion_computer, 
        vars.companion_baud_rate, 
        timeout=1)

def disconnect():
    serial_port.close()

def reboot():
    disconnect()
    time.sleep(1)
    connect()

def set_row_rc(roll, pitch, yaw, throttle, servo_aux):
    # ROLL/PITCH/THROTTLE/YAW/AUX1/AUX2/AUX3/AUX4
    data = [roll, 
            pitch, 
            throttle, 
            yaw, 0, 
            servo_aux, 0, 0]
    msp.send_msp_command(serial_port, msp.MSP_SET_RAW_RC, data)
    
    msp_command_id, payload = msp.read_msp_response(serial_port)
    if msp_command_id != msp.MSP_SET_RAW_RC:
        return False
    return True

def copter_init():
    # connect()
    
    return set_row_rc(
        vars.default_roll,
        vars.default_pitch, 
        vars.default_yaw, 
        vars.default_throttle, 
        vars.default_servo_aux2)

def telemetry(target):
    msp_target_command_id = get_target_id(target)
    msp.send_msp_request(serial_port, msp_target_command_id)
    time.sleep(0.1)
    msp_command_id, payload = msp.read_msp_response(serial_port)
    if msp_command_id == msp_target_command_id:
        return payload

    return {}

def prepare_go_forward(throttle):
    set_row_rc(
        vars.default_roll,
        vars.default_pitch, 
        vars.default_yaw, 
        int(throttle), 
        vars.default_servo_aux2)  

def go_forward():
    set_row_rc(
        vars.default_roll,
        vars.default_pitch + 20, 
        vars.default_yaw, 
        int(autopilot.state['throttle']), 
        vars.default_servo_aux2) 

    wait_for_execution('go_forward')

    set_row_rc(
        vars.default_roll,
        vars.default_pitch, 
        vars.default_yaw, 
        int(autopilot.state['throttle']), 
        vars.default_servo_aux2) 
    
    wait_for_execution('go_forward')

    return True

def deliver(): 
    set_row_rc(
        vars.default_roll,
        vars.default_pitch, 
        vars.default_yaw, 
        int(autopilot.state['throttle']), 
        2000) # 2000 to open the servo-device (to deliver the bomb)

    wait_for_execution('deliver')
    return True