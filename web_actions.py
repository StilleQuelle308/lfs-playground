import json

import utils
from tinkerforge_remote_switch import switch_light_off
from tinkerforge_remote_switch import switch_light_on
from extract_counter import do_work


def do(path):
    if str(path) == '/light_on_do':
        utils.log_info("Turning the light on...")
        switch_light_on()
        return 'Light turned on.'
    elif str(path) == '/light_off_do':
        utils.log_info("Turning the light off...")
        switch_light_off()
        return 'Light turned off'
    elif str(path).startswith('/crop_frame_do'):
        param_dict = extract_params(path)
        write_json("crop_frame_" + param_dict['mode'], param_dict)
        utils.log_info("Crop position received for: " + param_dict['mode'])
        return 'Setting crop frame.'
    elif str(path) == '/read_meter_do':
        utils.log_info("Reading meter ans sending mail...")
        do_work(True)
        return 'Meter read.'
    else:
        return 'No such command.'


def write_json(name, data):
    file_name = name + ".json"
    with open(file_name, 'w') as file:
        json.dump(data, file)


def extract_params(path):
    result = {}
    query_string = path.split("?", 2)
    pairs = query_string[1].split("&")
    for pair in pairs:
        params = pair.split("=", 2)
        result[params[0]] = params[1]
    return result


# For testing purposes
if __name__ == '__main__':
    parameters = extract_params("/crop_frame_do?mode=counter&posx1=100&posx2=200&posy1=300&posy2=400")
    for key, value in parameters.items():
        print(key + " = " + value)
