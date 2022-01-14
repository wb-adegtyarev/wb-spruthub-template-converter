import json
import re


class WbTemplateReader:

    wb_template = ''

    def read_template(self, json_file):
        self.wb_template = ''
        with open(json_file, 'r') as j:
            self.wb_template = json.load(j)
            return 0

    def get_device_name(self):
        return self.wb_template['device']['name']

    def get_title(self):
        title = self.get_translate(self.wb_template['title'])
        return  self.parse_title(title)

    def parse_title(self, title):
        regex = r'\((.*?)\)'
        matches = re.findall(regex, title)
        result = matches[0]
       
        if result:
            result = result.capitalize()
        else:
            result = title                

        return result

    def get_parameters(self):
        return self.wb_template['device']['parameters']

    def get_channels(self):
        return self.wb_template['device']['channels']

    def get_subdevices(self):
        return self.wb_template['device']['subdevices']

    def get_translate(self, string, language='en'):
        device = self.wb_template['device']

        if 'translations' in device:
            if language in device['translations']:
                if string in device['translations'][language]:
                    return device['translations'][language][string]
            else:
                return string
