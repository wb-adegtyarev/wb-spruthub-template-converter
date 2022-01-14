from . import dictionaries as dicts

class WbToShConverter:
    polling_time = 1000

    def is_enum_parameter(self, wb_parameter):
        result = False
        for index,value in enumerate(wb_parameter):
            if value == 'enum':
                result = True
                break

        return result    


    def is_value_parameter(self, wb_parameter):
        result = False
        for index,value in enumerate(wb_parameter):
            if value == 'min' or value == 'max':
                result = True
                break

        return result  


    def is_visible_service(self, service_name):
        return service_name in dicts.sh_services_visible


    def get_wb_parameter_type(self, wb_parameter):
        result = 'unknown'

        if self.is_enum_parameter(wb_parameter):
            result = 'enum'

        if self.is_value_parameter(wb_parameter):
            result = 'value'        

        return result


    def get_model_id_by_name(self, wb_device_name):
        if wb_device_name in dicts.wb_devices:
            result = dicts.wb_devices[wb_device_name]['model_id']
        else:
            result = 'unknown'

        return result

    def get_type_by_name(self, wb_device_name):
        if wb_device_name in dicts.wb_devices:
            result = dicts.wb_devices[wb_device_name]['type']
        else:
            result = 'unknown'

        return result

    def get_sh_name_by_name(self, wb_device_name):
        if wb_device_name in dicts.wb_devices:
            result = dicts.wb_devices[wb_device_name]['sh_name']
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

    
    def get_services(self, wb_device_channels, wb_device_name):
        services = []

        for index, value in enumerate(wb_device_channels):
            service = self.get_service(value, wb_device_name)

            if service:
                services.append(service)

        return services

    
    def get_service(self, wb_channel, wb_device_name):
        service = {}
        service_scale = ''

        channel_name = wb_channel['name']
        service_char_function = self.get_function(wb_channel['reg_type'])
        service_char_address = wb_channel['address']
        service_type =  self.get_type(wb_channel['type'], wb_device_name, channel_name)

        if 'scale' in wb_channel:
            service_scale = wb_channel['scale']

        if service_type:            
            service_char_type = self.get_characteristic_type(service_type)
            service['name'] = channel_name
            service['visible'] = self.is_visible_service(channel_name)
            service['type'] = service_type
            service['characteristics'] = []
            service['characteristics'].append({})
            service['characteristics'][0]['type'] = service_char_type
            service['characteristics'][0]['link'] = {}    
            service['characteristics'][0]['link']['address'] = service_char_address
            service['characteristics'][0]['link']['function'] = service_char_function 
            service['characteristics'][0]['link']['pollingTime'] = self.polling_time 

            if service_scale:
                service['characteristics'][0]['link']['scale'] = service_scale



        return service        


    def get_section(self, wb_device_name, section_id):
        section = {}       
        
        section['manufacturer'] = 'WirenBoard'
        section['model'] = wb_device_name
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
            option_function = self.get_function(wb_parameter['reg_type'])
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

                option['values'] = self.get_sh_option_values(wb_enum, wb_enum_titles)
            
            if wb_parameter_type == 'value':
                option_min_value = wb_parameter['min']
                option_max_value = wb_parameter['max']

                option['link']['type'] = 'Integer'
                option['minValue'] = option_min_value
                option['maxValue'] = option_max_value

        return option


    def get_function(self, wb_reg_type):
        return dicts.wb_sh_reg_type_mathes[wb_reg_type]


    def get_type(self, wb_type, wb_device_name, channel_name):
        result = ''
        sh_custom = dicts.sh_custom
        wb_device_type = self.get_type_by_name(wb_device_name)
        custom_type = ''

        if wb_device_type in sh_custom:
            if channel_name in sh_custom[wb_device_type]['custom_types']:
                custom_type = sh_custom[wb_device_type]['custom_types'][channel_name]
    
        if len(custom_type)>0:
            result = custom_type
        else:
            wb_sh_type_mathes = dicts.wb_sh_type_mathes

            if wb_type in wb_sh_type_mathes:
                result = wb_sh_type_mathes[wb_type]

        return result

    def get_characteristic_type(self, service_type):
        return dicts.sh_characteristic_types[service_type]