#!/usr/bin/env python
import os
import re


GLOBAL_VAR = re.compile(r'^var\s+([^\s=]+)', re.MULTILINE)


def main():
    for fn in os.listdir('.'):
        if (fn not in ['config_base.js', 'config_prod.js']
            and not (
                fn.startswith('inc_data_')
                and fn.endswith('.js')
                and not fn.endswith('_dev.js'))):
            continue
        with open(fn, 'r') as f:
            data = f.read()
        for var in GLOBAL_VAR.finditer(data):
            varname = var.group(1)
            print 'config.%s = %s;' % (varname, varname)


if __name__ == '__main__':
    main()
