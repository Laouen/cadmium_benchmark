#!/usr/bin/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import gflags
import sys

from ModelCodeGenerator import ModelCodeGenerator


def main(FLAGS):

    generator = ModelCodeGenerator()
    
    generator.write('int main() {\n')

    atomics = int(FLAGS.atomics)
    links = int(FLAGS.links)
    test_type = FLAGS.test_type

    info = {
        'vatomics': atomics,
        'vlinks': links,
        'vcoupled': 0,
        'tatomics': 0,
        'tlinks': 0,
        'tports': 0
    }

    for k, v in info.iteritems():
        print k + ':', info[k]

    generator.write_ports(1, 1)

    for i in range(atomics):
        generator.write_atomic_model(i)

    if test_type == 'explicit_definition':
        generator.write('\tcadmium::dynamic::modeling::ICs ics = {')
        for i in range(links):
            sep = ',' if i < (links - 1) else ''
            generator.write('\t\t' + generator.ic_template.format(model_number_1="0", model_number_2="0") + sep)
        generator.write('\t};\n\n')
    else:
        for_loop = '\tcadmium::dynamic::modeling::ICs ics;\n' \
                   '\tfor (int i = 0; i < ' + str(links) + '; i++) {\n' \
                   '\t\tics.push_back(makeic("model_1","model_2"));\n' \
                   '\t}\n\n'
        generator.write(for_loop)

    generator.write('\treturn 0;\n}')

    generator.write_to_ports('')
    generator.write_to_ports('#endif //PORTS_TEST_CPP')

    generator.model_file.close()
    generator.ports_file.close()


if __name__ == '__main__':

    gflags.DEFINE_string('links', 0, '', short_name='vl')
    gflags.DEFINE_string('atomics', 0, '', short_name='va')
    gflags.DEFINE_string('test_type', None, '', short_name='t')

    FLAGS = gflags.FLAGS

    try:
        argv = FLAGS(sys.argv)  # parse flags
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], FLAGS)
        sys.exit(1)

    main(FLAGS)
