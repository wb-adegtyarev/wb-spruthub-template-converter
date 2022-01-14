import json


class ShTemplateWriter:

    sh_template = []

    def write_services_in_section(self, services, sh_section):
        for index, value in enumerate(services):
            sh_section['services'].append(value)

        self.sh_template.append(sh_section)
        return 0

    def write_options_in_section(self, options, sh_section):
        section_id = sh_section['serial']
        sh_template = self.sh_template

        for index, value in enumerate(sh_template):
            if value['serial'] == section_id:
                for index, value in enumerate(options):
                    sh_section['options'].append(value)
                break
        return 0

    def write_init_section(self, wb_device_model_id, sh_name=''):

        init = {
            'modelId': {
                'type': 'String',
                'address': 200,
                'function': 'Holding',
                'length': 6
            },
            'firmware': {
                'type': 'String',
                'address': 250,
                'function': 'Holding',
                'length': 15
            }
        }

        option = {
            "link": {
                "type": "Integer",
                "address": 128,
                "function": "Holding"
            },
            "name": "Modbus-address",
            "value": 1,
            "minValue": 1,
            "maxValue": 252
        }

        init_section = self.sh_template[0]

        if sh_name:
            init_section['name'] = sh_name

        init_section['modelId'] = wb_device_model_id
        init_section['init'] = init
        init_section['options'].append(option)

        return 0

    def get_sh_template(self):
        return self.sh_template

    def clear_sh_template(self):
        self.sh_template = []
        return 0

    def save_sh_temlate(self, json_file):
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.sh_template, f, ensure_ascii=False, indent=4)
