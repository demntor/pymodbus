#!/usr/bin/python
'''
Pydoctor API Runner
---------------------

Using pkg_resources, we attempt to see if pydoctor is installed,
if so, we use its cli program to compile the documents
'''
try:
    import sys, os
    import pkg_resources
    pkg_resources.require("epydoc")

    from pydoctor.driver import main
    sys.argv = '''pydoctor.py --quiet
        --project-name=Pymodbus
        --project-url=http://code.google.com/p/pymodbus/
        --add-package=../../pymodbus
        --html-output=pydoctor
        --html-write-function-pages --make-html'''.split()
    main()
except: pass
