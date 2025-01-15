import logger

main_autopilot_started = {
    "log_info": "[AUTOPILOT STARTED]",
    "console": "\033[93m[AUTOPILOT STARTED]\033[0m"
    }

main_stopping_threads = {
    "log_info": "[STOPPING THREADS]",
    "console": "\033[93m[STOPPING THREADS]\033[0m"
    }

command_executor_done = {
    "log_info": "thread \'Command executor\', DONE.",
    "console": "thread \033[93mCommand executor\033[0m, DONE at {0}."
    }

command_executor_connected = {
    "log_info": "MSP connection is established: '{0}'",
    "console": "MSP connection is established: \033[92m{0}\033[0m"
    }

command_executor_executing_command = {
    "log_debug": "Executing command: {0}, Priority: {1}, Body: {2}",
    "console": "Executing command: {0}, Priority: {1}, Body: {2}"
    }

command_monitor_log = {
    "log_debug": "Monitoring: {0}",
    "console": "Monitoring: {0}"
    }

command_telemetry_log = {
    "log_debug": "Telemetry: {0}",
    "console": "Telemetry: {0}"
    }

command_monitor_current_rssi_and_battery = {
    "log_info": "RSSI: {0}, signal: {1}, battery voltage: {2}V",
    "console": "\033[93m[RSSI: {0}, signal: {1}, battery voltage: {2}V]\033[0m"
    }

command_telemetry_current_speed = {
    "log_info": "Current speed [{0} m/s]",
    "console": "current speed: - \033[93m[{0} m/s]\033[0m"
    }

command_telemetry_current_altitude = {
    "log_info": "Current altitude [{0} m]",
    "console": "current altitude: - \033[93m[{0} m]\033[0m"
    }

command_telemetry_autopilot_state = {
    "log_info": "Autopilot state: {0}",
    "console": "AUTOPILOT STATE: \033[95m{0}\033[0m"
    }

bee_state_changed_to = {
    "log_info": "Bee state changed to [{0}]",
    "console": "Bee state changed to [{0}]"
    }

initializing_autopilot = {
    "log_info": "Initializing autopilot",
    "console": "Initializing autopilot"
    }

command_deliver_we_are_going_forward = {
    "log_info": "[We are going forward for 2 sec]",
    "console": "[We are going forward for 2 sec]"
    }

command_deliver_we_are_delivering = {
    "log_info": "[We are delivering package]",
    "console": "[We are delivering package]"
    }

command_deliver_mission_completed = {
    "log_info": "[MISSION COMPLETED]",
    "console": "\033[93mMISSION COMPLETED\033[0m"
    }

telemetry_requestor_done = {
    "log_info": "thread \'Telemetry requestor\', DONE.",
    "console": "thread \033[93mTelemetry requestor\033[0m, DONE at {0}."
    }

empty_pilot_process_done = {
    "log_info": "thread \'Empty pilot process\', DONE.",
    "console": "thread \033[93mEmpty pilot process\033[0m, DONE at {0}."
    }

empty_pilot_process_connecting = {
    "log_info": "Empty pilot: attempting to connect with '{0}'",
    "console": "Empty pilot: attempting to connect with \033[91m{0}\033[0m"
    }

empty_pilot_process_connected = {
    "log_info": "Empty pilot: connected with '{0}'",
    "console": "Empty pilot: connected with \033[92m{0}\033[0m"
    }

telemetry_process_connecting = {
    "log_info": "Telemetry: attempting to connect with '{0}'",
    "console": "Telemetry: attempting to connect with \033[91m{0}\033[0m"
    }

telemetry_reconnection = {
    "log_info": "Telemetry: attempting to reconnect because of exception: '{0}'",
    "console": "Telemetry: attempting to reconnect because of exception: \033[91m{0}\033[0m"
    }

telemetry_process_connected = {
    "log_info": "Telemetry: connected with '{0}'",
    "console": "Telemetry: connected with \033[92m{0}\033[0m"
    }

fatal_error = {
    "log_fatal": "{0}"
    }

main_autopilot_finished = {
    "log_info": "[AUTOPILOT FINISHED]",
    "console": "\033[93m[AUTOPILOT FINISHED]\033[0m"
    }

def display(msg, params=[]):
    if msg.get('log_info'):
        logger.log_message(None, msg['log_info'].format(*params), 'info')
    if msg.get('log_debug'):
        logger.log_message(None, msg['log_debug'].format(*params), 'debug')
    if msg.get('log_fatal'):
        logger.log_message(None, msg['log_fatal'].format(*params), 'fatal')
    if msg.get('console'):
        print(msg['console'].format(*params))