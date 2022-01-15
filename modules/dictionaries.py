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
            'Input 0': 'ContactSensor', 'Input 0 counter': 'C_PulseMeter', 'Input 0 freq': 'C_FrequencyMeter', 
            'Input 1': 'ContactSensor', 'Input 1 counter': 'C_PulseMeter', 'Input 1 freq': 'C_FrequencyMeter',
            'Input 2': 'ContactSensor', 'Input 2 counter': 'C_PulseMeter', 'Input 2 freq': 'C_FrequencyMeter',
            'Input 3': 'ContactSensor', 'Input 3 counter': 'C_PulseMeter', 'Input 3 freq': 'C_FrequencyMeter',
            'Input 4': 'ContactSensor', 'Input 4 counter': 'C_PulseMeter', 'Input 4 freq': 'C_FrequencyMeter',
            'Input 5': 'ContactSensor', 'Input 5 counter': 'C_PulseMeter', 'Input 5 freq': 'C_FrequencyMeter',
            'Input 6': 'ContactSensor', 'Input 6 counter': 'C_PulseMeter', 'Input 6 freq': 'C_FrequencyMeter',
            'MCU Temperature': 'TemperatureSensor'
        },
        'visible': ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']
    },
    'leak': {
        'channels': {
            'K1': 'Valve', 'K2': 'Valve', 'Alarm': 'Switch',
            'F1': 'LeakSensor', 'F1 Counter': 'C_PulseMeter', 'F1 Freq': 'C_FrequencyMeter',
            'F2': 'LeakSensor', 'F2 Counter': 'C_PulseMeter', 'F2 Freq': 'C_FrequencyMeter',
            'F3': 'LeakSensor', 'F3 Counter': 'C_PulseMeter', 'F3 Freq': 'C_FrequencyMeter',
            'S1': 'ContactSensor', 'S1 Counter': 'C_PulseMeter', 'S1 Freq': 'C_FrequencyMeter',
            'S2': 'ContactSensor', 'S2 Counter': 'C_PulseMeter', 'S2 Freq': 'C_FrequencyMeter',
            'S3': 'ContactSensor', 'S3 Counter': 'C_PulseMeter', 'S3 Freq': 'C_FrequencyMeter',
            'P1 Counter': 'C_WaterMeter', 'P2 Counter': 'C_WaterMeter'
        },
        'visible': ['K1', 'K2', 'F1', 'F2', 'F3', 'Alarm']
    }
}

sh_service_types = {
    'C_FrequencyMeter': {
        'type': 'C_Frequency',
        'function': 'Input',
        'pollingTime': 1000
    },
    'C_PulseMeter': {
        'type': 'C_PulseCount',
        'function': 'Input',
        'pollingTime': 1000
    },
    'C_WaterMeter': {
        'type': 'C_CubicMeter',
        'function': 'Input',
        'pollingTime': 1000
    },
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
    'TemperatureSensor': {
        'type': 'CurrentTemperature',
        'function': 'Input',
        'pollingTime': 6000
    },
    'Valve': {
        'type': 'Active',
        'function': 'Coil',
        'pollingTime': 1000
    },
}
