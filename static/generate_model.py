#!/usr/bin/python
# -*- coding: utf-8 -*-

import gflags
import sys

from ModelCodeGenerator import ModelCodeGenerator


def main(FLAGS):

    generator = ModelCodeGenerator()

    atomics = int(FLAGS.atomics)
    atomic_types = int(FLAGS.atomic_types)
    links = int(FLAGS.links)
    link_types = int(FLAGS.link_types)
    couples = int(FLAGS.couples)
    ports = int(FLAGS.ports)
    test_type = FLAGS.test_type

    info = {
        'vatomics': atomics,
        'vlinks': links,
        'vcoupled': couples,
        'tatomics': atomic_types,
        'tlinks': link_types,
        'tports': ports * 2,
    }

    for k, v in info.iteritems():
        print k + ':', info[k]

    generator.write_ports(ports, ports)

    for i in range(couples):
        generator.write_coupled_model(i, 0, 0, []) # empty model

    for i in range(atomics):
        generator.write_atomic_model(i)

    ic = []

    if test_type == 'link_amount':
        assert( links <= (atomics - 1) and "la cantidad de links debe ser menor o igual a la cantidad de atomicos menos uno (el source)")
        ic = [(0, 0, i+1, 0) for i in range(links)]

    if test_type == 'link_types':
        assert( links <= (atomics / 2) and "la cantidad de links debe ser menor o igual a la mitar de la cantidad de atomicos")
        assert( link_types <= links and "no puede haber menos links que tipos de links")
        equal_links = links - (link_types - 1)
        ic = [(i, 0, i + links, 0) for i in range(equal_links)] 
        ic = ic + [(equal_links + i, i + 1, equal_links + i + links, i + 1) for i in range(link_types - 1)]

    generator.write_top(atomics, couples, ic)
    generator.close_model()


if __name__ == '__main__':

    gflags.DEFINE_string('links', 0, '', short_name='vl')
    gflags.DEFINE_string('link_types', 1, '', short_name='tl')
    gflags.DEFINE_string('atomics', 0, '', short_name='va')
    gflags.DEFINE_string('atomic_types', 1, '', short_name='ta')
    gflags.DEFINE_string('couples', 0, '', short_name='vc')
    gflags.DEFINE_string('ports', 0, '', short_name='tp')
    gflags.DEFINE_string('test_type', None, '', short_name='t')

    FLAGS = gflags.FLAGS

    try:
        argv = FLAGS(sys.argv)  # parse flags
    except gflags.FlagsError, e:
        print '%s\nUsage: %s ARGS\n%s' % (e, sys.argv[0], FLAGS)
        sys.exit(1)

    main(FLAGS)
