# -*- coding: utf-8 -*-
import os


class ModelCodeGenerator:
    """
    Writes c++ cadmium model code to the <model_name>.hpp file.
    """

    def __init__(self, template_folder='templates', TIME='float'):

        # main template
        main_path = os.curdir + os.sep + template_folder + os.sep + 'main.tpl.cpp'
        self.main_template = open(main_path, 'r').read().format(TIME=TIME)

        # atomic template
        atomic_tpl_path = os.curdir + os.sep + template_folder + os.sep + 'atomic.tpl.hpp'
        self.atomic_template = open(atomic_tpl_path, 'r').read()

        # atomic ports definition template
        ports_tpl_path = os.curdir + os.sep + template_folder + os.sep + 'ports.tpl.hpp'
        self.ports_def_template = open(ports_tpl_path, 'r').read()

        # coupled template
        coupled_tpl_path = os.curdir + os.sep + template_folder + os.sep + 'coupled.tpl.hpp'
        self.coupled_template = open(coupled_tpl_path, 'r').read()

        # coupled template for TOP model
        top_tpl_path = os.curdir + os.sep + template_folder + os.sep + 'top.tpl.hpp'
        self.top_template = open(top_tpl_path, 'r').read()

        # single port template
        self.port_template = 'struct {out_in}_{port_number}: public cadmium::{out_in}_port<int>{{}};'

        self.ic_template = 'cadmium::modeling::IC<atomic_{model_number_1}, ports::out_{port_number_1}, atomic_{model_number_2}, ports::in_{port_number_2}>'

        self.model_file = open('main.cpp', 'wb')
        self.ports_file = open('ports.hpp', 'wb')

        self.write_includes()

    def write_atomic_model(self, model_number):
        self.write(self.atomic_template.format(model_number = model_number))

    def write_coupled_model(self, model_number, atomic_models, coupled_models, ic):

        sub_models = ['atomic_' + str(x) for x in range(atomic_models)] + ['coupled_' + str(x) for x in range(coupled_models)]

        ics = []

        for (model_number_1, port_number_1, model_number_2, port_number_2) in ic:
            ics.append(self.ic_template.format(model_number_1=str(model_number_1), port_number_1=str(port_number_1), model_number_2=str(model_number_2), port_number_2=str(port_number_2)))

        self.write(self.coupled_template.format(model_number=model_number, sub_models=', '.join(sub_models), ic=', '.join(ics)))

    def write_top(self, atomic_models, coupled_models, ic):

        sub_models = ['atomic_' + str(x) for x in range(atomic_models)] + ['coupled_' + str(x) for x in range(coupled_models)]

        ics = []

        for (model_number_1, port_number_1, model_number_2, port_number_2) in ic:
            ics.append(self.ic_template.format(model_number_1=str(model_number_1), port_number_1=str(port_number_1), model_number_2=str(model_number_2), port_number_2=str(port_number_2)))

        self.write(self.top_template.format(sub_models=', '.join(sub_models), ic=', '.join(ics)))

    def write_ports(self, out_ports, in_ports):

        output_ports_def = '\n\t'.join([self.port_template.format(out_in='out', port_number=port_number) for port_number in range(out_ports)])
        output_ports_names = ','.join(['out_' + str(port_number) for port_number in range(out_ports)])

        input_ports_def = '\n\t'.join([self.port_template.format(out_in='in', port_number=port_number) for port_number in range(in_ports)])
        input_ports_names = ','.join(['in_' + str(port_number) for port_number in range(in_ports)])

        self.write_to_ports(self.ports_def_template.format(output_ports_definitions=output_ports_def,
                                                           input_ports_definitions=input_ports_def,
                                                           output_port_names=output_ports_names,
                                                           input_port_names=input_ports_names))

    def write(self, code):
        self.model_file.write(code + '\n')
        self.model_file.flush()

    def write_to_ports(self, code):
        self.ports_file.write(code + '\n')
        self.ports_file.flush()

    def close_model(self):
        self.write(self.main_template)

        self.write_to_ports('')
        self.write_to_ports('#endif //PORTS_TEST_CPP')

        self.model_file.close()
        self.ports_file.close()

    def write_includes(self):

        self.write_to_ports('#ifndef PORTS_TEST_CPP')
        self.write_to_ports('#define PORTS_TEST_CPP')
        self.write_to_ports('')
        self.write_to_ports('#include <cadmium/modeling/ports.hpp>')
        self.write_to_ports('')

        self.write('#include \"empty_atomic.hpp\"')
        self.write('#include \"ports.hpp\"')
        self.write('')
        self.write('#include <iostream>')
        self.write('')
        self.write('#include <cadmium/logger/common_loggers.hpp>')
        self.write('#include <cadmium/engine/pdevs_runner.hpp>')
        self.write('#include <cadmium/modeling/coupled_model.hpp>')        
        self.write('')
        self.write('')