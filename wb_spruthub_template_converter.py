import os
from modules import wb_template_reader
from modules import sh_template_generator
from modules import sh_template_writer

absFilePath = os.path.abspath(__file__)
current_dir, filename = os.path.split(absFilePath)
wb_templates_dir = '{}/{}/'.format(current_dir, 'wb_templates')
sh_templates_dir = '{}/{}/'.format(current_dir, 'sh_templates')
wb_templates = []


def get_wb_templates():
    return os.listdir(wb_templates_dir)

if not os.path.exists(wb_templates_dir):
    os.mkdir(wb_templates_dir)

if not os.path.exists(sh_templates_dir):
    os.mkdir(sh_templates_dir)

reader = wb_template_reader.WbTemplateReader()
generator = sh_template_generator.WbToShConverter()
writer = sh_template_writer.ShTemplateWriter()

wb_templates = get_wb_templates()   

for index, value in enumerate(wb_templates):    

    json_file = '{}{}'.format(wb_templates_dir, value)

    reader.read_template(json_file)

    wb_device_name = reader.get_device_name()
    wb_device_model_id = generator.get_model_id_by_name(wb_device_name)
    sh_name =  generator.get_sh_name_by_name(wb_device_name)
    wb_device_parameters = reader.get_parameters()
    wb_device_channels = reader.get_channels()

    sh_services = generator.get_services(wb_device_channels, wb_device_name)
    sh_options = generator.get_options(wb_device_parameters)

    sh_section = generator.get_section(wb_device_name, 'main')

    writer.clear_sh_template()
    writer.write_services_in_section(sh_services, sh_section)
    writer.write_options_in_section(sh_options, sh_section)
    writer.write_init_section(wb_device_model_id, sh_name)
    writer.save_sh_temlate('{}{}.json'.format(sh_templates_dir, wb_device_name))