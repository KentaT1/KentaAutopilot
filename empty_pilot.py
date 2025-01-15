import time
import autopilot
import messages
import router
import definitions as vars

def empty_pilot_process(stop_command):
    while autopilot.state['connection'] == False and not stop_command.is_set():
        try:
            time.sleep(7)
            messages.display(messages.empty_pilot_process_connecting, [vars.companion_computer])
        except Exception as e:
            messages.display(messages.fatal_error, [e])
            pass
    
    if not stop_command.is_set():
        messages.display(messages.empty_pilot_process_connected, [vars.companion_computer])

    while not stop_command.is_set():
        try:
            if autopilot.state['bee_state'] in ['READY']:
                if autopilot.state['delivered'] == False:
                    if float(autopilot.state['altitude']) != 0.0:
                        router.put_command(router.Command(1,'DELIVER',{}))
            time.sleep(2)
        except:
            pass

    stopped_time = time.strftime("%H:%M:%S, %Y, %d %B", time.localtime())
    messages.display(messages.empty_pilot_process_done, [stopped_time])