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

        reader = self.reader
        generator = self.generator
        writer = self.writer

        for index, value in enumerate(self.wb_templates):
            json_file = '{}{}'.format(self.wb_templates_dir, value)

            reader.read_template(json_file)

            wb_device_name = reader.get_device_name()
            generator.init(wb_device_name)
            writer.init(wb_device_name)

            wb_device_model_id = generator.get_model_id()

            if wb_device_model_id:
                sh_name = reader.get_title()
                wb_device_channels = reader.get_channels()
                wb_device_parameters = reader.get_parameters()

                sh_services = generator.get_services(
                    wb_device_channels)
                sh_options = generator.get_options(wb_device_parameters)

                writer.clear_sh_template()
                writer.write_services(sh_services, 'main')
                writer.write_options(sh_options, 'main')
                writer.write_init_section(wb_device_model_id, sh_name)
                writer.save_sh_temlate('{}{}.json'.format(
                    self.sh_templates_dir, wb_device_name))


template_converter = WbShTemplateConverter()
template_converter.convert()
