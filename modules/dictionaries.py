wb_devices = {
    'WB-MRWL3': {
        'model_id': 'MRWL3',
        'type': 'relay',
        'sh_name': '3-channel Modbus Relay'
    },
    'WB-MR6C': {
        'model_id': 'WBMR6C',
        'type': 'relay',
        'sh_name': '6-channel Modbus Relay'
    },
    'WB-MWAC': {
        'model_id': 'WBMWAC',
        'type': 'leak',
        'sh_name': 'Leak protection'
    },
    'MSW v.3': {
        'model_id': 'WBMSW3',
        'type': 'sensors',
        'sh_name': '8 in 1 universal sensor'
    },
}

sh_custom = {
    'leak': {
        'custom_types': {'K1': 'Valve', 'K2': 'Valve', 'F1': 'LeakSensor', 'F2': 'LeakSensor', 'F3': 'LeakSensor'}
    }
}

sh_services_visible = [
    'K1', 'K2', 'K3', 'K4', 'K5', 'K6',
    'F1', 'F2', 'F3', 'Alarm'
]

wb_sh_reg_type_mathes = {
    'coil': 'Coil',
    'holding': 'Holding',
    'discrete': 'Discrete',
    'input': 'Input'
}

wb_sh_type_mathes = {
    'switch': 'Switch',
    'pushbutton': 'Switch',
    'temperature': 'TemperatureSensor',
    'rel_humidity': 'HumiditySensor',
    'concentration': 'AirQualitySensor',
    'concentration': 'CarbonDioxideSensor',
    'sound_level': 'C_NoiseSensor',
    'lux': 'LightSensor',
}

sh_characteristic_types = {
    'Switch': 'On',
    'LeakSensor': 'LeakDetected',
    'TemperatureSensor': 'CurrentTemperature',
    'HumiditySensor': 'CurrentRelativeHumidity',
    'AirQualitySensor': 'VOCDensity',
    'CarbonDioxideSensor': 'CarbonDioxideLevel',
    'C_NoiseSensor': 'C_CurrentNoiseLevel',
    'LightSensor': 'CurrentAmbientLightLevel',
    'MotionSensor': 'C_CurrentMotionLevel',
    'Valve': 'Active'
}
