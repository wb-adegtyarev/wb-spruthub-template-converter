wb_devices = {
    'WB-MRWL3': {
        'model_id': 'MRWL3',
        'type': 'relay',
    },
    'WB-MR6C': {
        'model_id': 'WBMR6C',
        'type': 'relay',
    },
    'WB-MWAC': {
        'model_id': 'WBMWAC',
        'type': 'leak',
    }
}

wb_device_options = {
    'relay': {
        'channels': {
            'K1': 'Switch', 'K2': 'Switch', 'K3': 'Switch', 'K4': 'Switch', 'K5': 'Switch', 'K6': 'Switch',
            'Input 0': 'ContactSensor', 'Input 1': 'ContactSensor', 'Input 2': 'ContactSensor', 'Input 3': 'ContactSensor', 'Input 4': 'ContactSensor', 'Input 5': 'ContactSensor', 'Input 6': 'ContactSensor', 'MCU Temperature': 'TemperatureSensor'
        },
        'visible': ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']
    },
    'leak': {
        'channels': {
            'K1': 'Valve', 'K2': 'Valve', 'F1': 'LeakSensor', 'F2': 'LeakSensor', 'F3': 'LeakSensor', 'S1': 'ContactSensor', 'S2': 'ContactSensor', 'S3': 'ContactSensor'
        },
        'visible': ['K1', 'K2', 'F1', 'F2', 'F3']
    }
}

sh_service_types = {
    'ContactSensor': {
        'type': 'ContactSensorState',
        'function': 'Input',
        'pollingTime': 100
    },
    'LeakSensor': {
        'type': 'LeakDetected',
        'function': 'Input',
        'pollingTime': 1000
    },
    'Switch': {
        'type': 'On',
        'function': 'Coil',
        'pollingTime': 1000
    },
    'Valve': {
        'type': 'Active',
        'function': 'Coil',
        'pollingTime': 1000
    },
    'TemperatureSensor': {
        'type': 'CurrentTemperature',
        'function': 'Input',
        'pollingTime': 6000
    },
}
