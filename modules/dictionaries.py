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
    },
    'WB-MAP3E fw2': {
        'model_id': 'MAP3E',
        'type': 'power_meter',
    },
    'WB-MAP12E fw2': {
        'model_id': 'MAP12',
        'type': 'power_meter',
    }
}

wb_device_options = {
    'relay': {
        'channels': {
            'Switch': ['K1', 'K2', 'K3', 'K4', 'K5', 'K6'],
            'ContactSensor': ['Input 0', 'Input 1', 'Input 2', 'Input 3', 'Input 4', 'Input 5', 'Input 6'],
            'C_PulseMeter': ['Input 0 counter', 'Input 1 counter', 'Input 2 counter', 'Input 3 counter', 'Input 4 counter', 'Input 5 counter', 'Input 6 counter'],
            'C_FrequencyMeter': ['Input 0 freq', 'Input 1 freq', 'Input 2 freq', 'Input 3 freq', 'Input 4 freq', 'Input 5 freq', 'Input 6 freq']
        },
        'visible': ['K1', 'K2', 'K3', 'K4', 'K5', 'K6']
    },
    'leak': {
        'channels': {
            'Switch': ['Alarm'],
            'Valve': ['K1', 'K2'],
            'LeakSensor': ['F1', 'F2', 'F3'],
            'C_PulseMeter': ['F1 Counter', 'F2 Counter', 'F3 Counter', 'S1 Counter', 'S2 Counter', 'S3 Counter'],
            'C_FrequencyMeter': ['F1 Freq', 'F2 Freq', 'F3 Freq', 'S1 Freq', 'S2 Freq', 'S3 Freq'],
            'C_WaterMeter': ['P1 Counter', 'P2 Counter'],
            'ContactSensor': ['S1', 'S2', 'S3']
        },
        'visible': ['K1', 'K2', 'F1', 'F2', 'F3', 'Alarm']
    },
    'power_meter': {
        'channels': {
            'C_VoltMeter': ['Urms L1', 'Upeak L1', 'Urms L2', 'Upeak L2', 'Urms L3', 'Upeak L3'],
            'C_AmpereMeter': ['Irms L1', 'Ipeak L1', 'Irms L2', 'Ipeak L2', 'Irms L3', 'Ipeak L3',
                              'Ch 1 Irms L1', 'Ch 1 Ipeak L1', 'Ch 1 Irms L2', 'Ch 1 Ipeak L2', 'Ch 1 Irms L3', 'Ch 1 Ipeak L3',
                              'Ch 2 Irms L1', 'Ch 2 Ipeak L1', 'Ch 2 Irms L2', 'Ch 2 Ipeak L2', 'Ch 2 Irms L3', 'Ch 2 Ipeak L3',
                              'Ch 3 Irms L1', 'Ch 3 Ipeak L1', 'Ch 3 Irms L2', 'Ch 3 Ipeak L2', 'Ch 3 Irms L3', 'Ch 3 Ipeak L3'
                              'Ch 4 Irms L1', 'Ch 4 Ipeak L1', 'Ch 4 Irms L2', 'Ch 4 Ipeak L2', 'Ch 4 Irms L3', 'Ch 4 Ipeak L3'],
            'C_WattMeter': ['P L1', 'P L2', 'P L3', 'Total P',
                            'Ch 1 P L1', 'Ch 1 P L2', 'Ch 1 P L3', 'Ch 1 Total P',
                            'Ch 2 P L1', 'Ch 2 P L2', 'Ch 2 P L3', 'Ch 2 Total P',
                            'Ch 3 P L1', 'Ch 3 P L2', 'Ch 3 P L3', 'Ch 3 Total P',
                            'Ch 4 P L1', 'Ch 4 P L2', 'Ch 4 P L3', 'Ch 4 Total P'],
            'C_KilowattHourMeter': ['AP energy L1', 'AP energy L2', 'AP energy L3', 'Total AP energy',
                                    'Ch 1 AP energy L1', 'Ch 1 AP energy L2', 'Ch 1 AP energy L3', 'Ch 1 Total AP energy',
                                    'Ch 2 AP energy L1', 'Ch 2 AP energy L2', 'Ch 2 AP energy L3', 'Ch 2 Total AP energy',
                                    'Ch 3 AP energy L1', 'Ch 3 AP energy L2', 'Ch 3 AP energy L3', 'Ch 3 Total AP energy',
                                    'Ch 4 AP energy L1', 'Ch 4 AP energy L2', 'Ch 4 AP energy L3', 'Ch 4 Total AP energy']
        },
        'visible': ['Urms L1', 'Irms L1', 'P L1', 'Total P', 'AP energy L1', 'Total AP energy',
                    'Ch 1 Irms L1', 'Ch 1 P L1', 'Ch 1 Total P', 'Ch 1 AP energy L1', 'Ch 1 Total AP energy']
    }
}

sh_service_types = {
    'C_AmpereMeter': {
        'type': 'C_Ampere',
        'function': 'Input',
        'pollingTime': 10000
    },
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
    'C_VoltMeter': {
        'type': 'C_Volt',
        'function': 'Input',
        'pollingTime': 10000
    },
    'C_WaterMeter': {
        'type': 'C_CubicMeter',
        'function': 'Input',
        'pollingTime': 1000
    },
    'C_WattMeter': {
        'type': 'C_Watt',
        'function': 'Input',
        'pollingTime': 10000
    },
    'C_KilowattHourMeter': {
        'type': 'C_KilowattHour',
        'function': 'Input',
        'pollingTime': 60000
    },
    'ContactSensor': {
        'type': 'ContactSensorState',
        'function': 'Coil',
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
