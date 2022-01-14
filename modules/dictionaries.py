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
    # 'WB-MIR v2': {
    #     'model_id': 'WBMIR3',
    #     'type': 'sensor',
    # },
}

sh_custom = {
    'leak': {
        'custom_types': {'K1': 'Valve', 'K2': 'Valve', 'F1': 'LeakSensor', 'F2': 'LeakSensor', 'F3': 'LeakSensor', 'S1': 'ContactSensor', 'S2': 'ContactSensor', 'S3': 'ContactSensor'},
        'custom_reg_types': {'discrete': 'Input'}
    },
    'relay': {
        'custom_types': {'Input 0': 'ContactSensor', 'Input 1': 'ContactSensor', 'Input 2': 'ContactSensor', 'Input 3': 'ContactSensor', 'Input 4': 'ContactSensor', 'Input 5': 'ContactSensor', 'Input 6': 'ContactSensor'},
        'custom_reg_types': {'discrete': 'Input'}
    }
}

sh_services_visible = [
    'K1', 'K2', 'K3', 'K4', 'K5', 'K6',
    'F1', 'F2', 'F3', 'Alarm', 'S1', 'S2', 'S3'
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
    'lux': 'LightSensor'
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
    'Valve': 'Active',
    'ContactSensor': 'ContactSensorState'
}
