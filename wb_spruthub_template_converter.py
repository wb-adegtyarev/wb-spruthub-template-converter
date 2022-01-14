import os
from modules import wb_template_reader
from modules import sh_template_generator
from modules import sh_template_writer


class WbShTemplateConverter:

    absFilePath = os.path.abspath(__file__)
    current_dir, filename = os.path.split(absFilePath)
    wb_templates_dir = '{}/{}/'.format(current_dir, 'wb_templates')
    sh_templates_dir = '{}/{}/'.format(current_dir, 'sh_templates')
    wb_templates = []

    def init(self):
        if not os.path.exists(self.wb_templates_dir):
            os.mkdir(self.wb_templates_dir)

        if not os.path.exists(self.sh_templates_dir):
            os.mkdir(self.sh_templates_dir)

        self.reader = wb_template_reader.WbTemplateReader()
        self.generator = sh_template_generator.ShTemplateGenerator()
        self.writer = sh_template_writer.ShTemplateWriter()

        self.wb_templates = self.get_wb_templates()

    def get_wb_templates(self):
        return os.listdir(self.wb_templates_dir)

    def convert(self):
        self.init()

        for index, value in enumerate(self.wb_templates):
            reader = self.reader
            generator = self.generator
            writer = self.writer

            json_file = '{}{}'.format(self.wb_templates_dir, value)

            reader.read_template(json_file)

            wb_device_name = reader.get_device_name()
            wb_device_model_id = generator.get_model_id_by_name(wb_device_name)
            sh_name = generator.get_sh_name_by_name(wb_device_name)
            wb_device_parameters = reader.get_parameters()
            wb_device_channels = reader.get_channels()

            sh_services = generator.get_services(
                wb_device_channels, wb_device_name)
            sh_options = generator.get_options(wb_device_parameters)

            sh_section = generator.get_section(wb_device_name, 'main')

            writer.clear_sh_template()
            writer.write_services_in_section(sh_services, sh_section)
            writer.write_options_in_section(sh_options, sh_section)
            writer.write_init_section(wb_device_model_id, sh_name)
            writer.save_sh_temlate('{}{}.json'.format(
                self.sh_templates_dir, wb_device_name))


template_converter = WbShTemplateConverter()
template_converter.convert()
