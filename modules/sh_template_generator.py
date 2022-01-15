from . import dictionaries as dicts


class ShTemplateGenerator:

    wb_device_name = ''
    wb_device_type = ''

    def init(self, wb_device_name):
        self.wb_device_name = wb_device_name
        self.wb_device_type = self.get_device_type()

    def is_enum_parameter(self, wb_parameter):
        result = False
        for index, value in enumerate(wb_parameter):
            if value == 'enum':
                result = True
                break

        return result

    def is_value_parameter(self, wb_parameter):
        result = False
        for index, value in enumerate(wb_parameter):
            if value == 'min' or value == 'max':
                result = True
                break

        return result

    def is_visible_service(self, channel_name):
        result = False
        wb_device_options = dicts.wb_device_options
        wb_device_type = self.wb_device_type

        if wb_device_type in wb_device_options:
            if 'visible' in wb_device_options[wb_device_type]:
                if channel_name in wb_device_options[wb_device_type]['visible']:
                    result = True

        return result

    def get_wb_parameter_type(self, wb_parameter):
        result = 'unknown'

        if self.is_enum_parameter(wb_parameter):
            result = 'enum'

        if self.is_value_parameter(wb_parameter):
            result = 'value'

        return result

    def get_model_id(self):
        name = self.wb_device_name

        if name in dicts.wb_devices:
            result = dicts.wb_devices[name]['model_id']
        else:
            result = ''

        return result

    def get_device_type(self):
        name = self.wb_device_name

        if name in dicts.wb_devices:
            result = dicts.wb_devices[name]['type']
        else:
            result = 'unknown'

        return result

    def get_sh_option_values(self, wb_enum, wb_enum_titles):
        result = []

        for index, value in enumerate(wb_enum):
            option_value = {
                'value': value,
                'name': wb_enum_titles[index]
            }
            result.append(option_value)

        return result

    def get_services(self, wb_device_channels):
        services = []

        for index, value in enumerate(wb_device_channels):
            service = self.get_service(value)

            if service:
                services.append(service)

        return services

    def get_service(self, wb_channel):
        service = {}
        service_scale = ''

        channel_name = wb_channel['name']

        wb_device_options = dicts.wb_device_options
        sh_service_types = dicts.sh_service_types
        wb_device_type = self.wb_device_type

        if wb_device_type in wb_device_options:

            wb_device_options_channels = wb_device_options[wb_device_type]['channels']

            if channel_name in wb_device_options_channels:
                service_type = wb_device_options_channels[channel_name]
                characteristics_type = sh_service_types[service_type]['type']
                characteristics_function = sh_service_types[service_type]['function']
                characteristics_polling_time = sh_service_types[service_type]['pollingTime']

                service_char_address = wb_channel['address']

                if 'scale' in wb_channel:
                    service_scale = wb_channel['scale']

                if service_type:
                    service['name'] = channel_name
                    service['visible'] = self.is_visible_service(channel_name)
                    service['type'] = service_type
                    service['characteristics'] = []
                    service['characteristics'].append({})
                    service['characteristics'][0]['type'] = characteristics_type
                    service['characteristics'][0]['link'] = {}
                    service['characteristics'][0]['link']['address'] = service_char_address
                    service['characteristics'][0]['link']['function'] = characteristics_function
                    service['characteristics'][0]['link']['pollingTime'] = characteristics_polling_time

                    if service_scale:
                        service['characteristics'][0]['link']['scale'] = service_scale

        return service

    def get_section(self, section_id):
        section = {}

        section['manufacturer'] = 'WirenBoard'
        section['model'] = self.wb_device_name
        section['serial'] = section_id
        section['services'] = []
        section['options'] = []

        return section

    def get_options(self, wb_device_parameters):
        options = []

        for index, value in enumerate(wb_device_parameters):
            wb_parameter = wb_device_parameters[value]
            option = self.get_option(wb_parameter)

            if option:
                options.append(option)

        return options

    def get_option(self, wb_parameter):
        option = {}

        wb_parameter_type = self.get_wb_parameter_type(wb_parameter)

        if not wb_parameter_type == 'unknown':

            option_address = wb_parameter['address']
            option_function = self.get_option_function(
                wb_parameter['reg_type'])
            option_name = wb_parameter['title']
            option_value = wb_parameter['default']

            option['link'] = {}
            option['link']['address'] = option_address
            option['link']['function'] = option_function
            option['name'] = option_name
            option['value'] = option_value

            if wb_parameter_type == 'enum':
                option['link']['type'] = 'Integer'

                wb_enum = wb_parameter['enum']
                wb_enum_titles = wb_parameter['enum_titles']

                option['values'] = self.get_sh_option_values(
                    wb_enum, wb_enum_titles)

            if wb_parameter_type == 'value':
                option_min_value = wb_parameter['min']
                option_max_value = wb_parameter['max']

                option['link']['type'] = 'Integer'
                option['minValue'] = option_min_value
                option['maxValue'] = option_max_value

        return option

    def get_option_function(self, wb_reg_type):
        return wb_reg_type.capitalize()
