import json

class WbTemplateReader:

    wb_template = ''

    def read_template(self, json_file):
        self.wb_template = ''
        with open(json_file, 'r') as j:            
            self.wb_template = json.load(j)        
            return 0

    def get_device_name(self):
        return self.wb_template['device']['name']  

    def get_parameters(self):
        return self.wb_template['device']['parameters']

    def get_channels(self):
        return self.wb_template['device']['channels']

    def get_subdevices(self):
        return self.wb_template['device']['subdevices']