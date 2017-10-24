seattle/
=======

There is no readme for this layout

# Layout metadata
## seattle/root.layout
```json
{"_type": "layout",
 "expires": "2017-01-23T13:27:57.683753Z",
 "inspect": [{"_type": "inspection",
              "material_matchrules": [["CREATE", "*"]],
              "name": "untar-linux-installer",
              "product_matchrules": [["CREATE",
                                      "seattle/seattle_repy/vesselinfo"],
                                     ["MATCH",
                                      "PRODUCT",
                                      "seattle/*",
                                      "FROM",
                                      "dummy-untar-linux-base-installer"],
                                     ["CREATE", "*"]],
              "run": "tar xf seattle_linux.tgz"}],
 "keys": {"d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5": {"keyid": "...",
                                                                               "keytype": "rsa",
                                                                               "keyval": {"private": "",
                                                                                          "public": "..."}}},
 "signatures": ["..."],
 "steps": [{"_type": "step",
            "expected_command": "python initialize.py",
            "material_matchrules": [],
            "name": "clone-dependencies",
            "product_matchrules": [["CREATE", "installer-packaging/*"]],
            "pubkeys": ["d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"]},
           {"_type": "step",
            "expected_command": "python build.py",
            "material_matchrules": [["MATCH",
                                     "PRODUCT",
                                     "installer-packaging/*",
                                     "FROM",
                                     "clone-dependencies"]],
            "name": "build-runnable",
            "product_matchrules": [["CREATE", "installer-packaging/*"]],
            "pubkeys": ["d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"]},
           {"_type": "step",
            "expected_command": "edit files manually",
            "material_matchrules": [["MATCH",
                                     "PRODUCT",
                                     "installer-packaging/RUNNABLE/*",
                                     "FROM",
                                     "build-runnable"]],
            "name": "pre-build-file-edit",
            "product_matchrules": [["CREATE", "installer-packaging/*"]],
            "pubkeys": ["d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"]},
           {"_type": "step",
            "expected_command": "python rebuild_base_installers.py "
                                "0.1-in-toto-in-seattle",
            "material_matchrules": [["MATCH",
                                     "PRODUCT",
                                     "installer-packaging/*",
                                     "FROM",
                                     "pre-build-file-edit"]],
            "name": "build-base-installers",
            "product_matchrules": [["CREATE",
                                    "custominstallerbuilder/html/static/installers/base/*"]],
            "pubkeys": ["d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"]},
           {"_type": "step",
            "expected_command": "tar xf "
                                "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz",
            "material_matchrules": [["MATCH",
                                     "PRODUCT",
                                     "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz",
                                     "FROM",
                                     "build-base-installers"]],
            "name": "dummy-untar-linux-base-installer",
            "product_matchrules": [["CREATE", "*"]],
            "pubkeys": ["d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"]}]}
```

# Link metadata

## seattle/dummy-untar-linux-base-installer.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": "", "stdout": ""},
 "command": ["tar",
             "xf",
             "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz"],
 "materials": {"...": "...",
               "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz": {"sha256": "87d1d..."}},
 "name": "dummy-untar-linux-base-installer",
 "products": {"...": "...",
              "seattle/seattle_repy/Mac_BSD_resources.py": {"sha256": "a56e6..."},
              "seattle/seattle_repy/exception_hierarchy.py": {"sha256": "13f09..."},
              "seattle/seattle_repy/modules/clearinghouse/__init__.py": {"sha256": "7fe86..."},
              "seattle/seattle_repy/py_BandwidthServer.py": {"sha256": "b84b6..."},
              "seattle/seattle_repy/repyV2/virtual_namespace.py": {"sha256": "01c77..."},
              "seattle/seattle_repy/secureclient.r2py": {"sha256": "1117f..."},
              "seattle/seattle_repy/signeddata.r2py": {"sha256": "685c0..."},
              "seattle/seattle_repy/sshkey.r2py": {"sha256": "efe5c..."},
              "seattle/seattle_repy/stop_all_seattle_processes.py": {"sha256": "86e38..."}},
 "return_value": 0,
 "signatures": [{"keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
                 "method": "RSASSA-PSS",
                 "sig": "aa05b3773b3cad3a1d70b7ae43fd37f168a59c7e..."}]}
```


## seattle/build-runnable.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": "",
                "stdout": "Building into "
                          "/home/cib/installer-packaging/RUNNABLE\n"
                          "Done building!\n"},
 "command": ["python", "build.py"],
 "materials": {"...": "...",
               "installer-packaging/DEPENDENCIES/nodemanager/tests/nmtestaddfiletovessel_emptyfilename.mix": {"sha256": "7138b..."},
               "installer-packaging/DEPENDENCIES/portability/scripts/initialize.py": {"sha256": "4579c..."},
               "installer-packaging/DEPENDENCIES/repy_v1/apps/tcp/tests/integrations/z_test_loopback_double_connect.repy": {"sha256": "f7982..."},
               "installer-packaging/DEPENDENCIES/repy_v1/apps/tcp/tests/run_tests.py": {"sha256": "3d556..."},
               "installer-packaging/DEPENDENCIES/repy_v1/apps/tryrepy/web/js/ace/theme-solarized_light.js": {"sha256": "a3e34..."},
               "installer-packaging/DEPENDENCIES/repy_v1/freebsd_api.py": {"sha256": "4329a..."},
               "installer-packaging/DEPENDENCIES/repy_v1/tests/cpu_f.3_restrictions.cpu.3": {"sha256": "6a800..."},
               "installer-packaging/DEPENDENCIES/seash/pyreadline/clipboard/ironpython_clipboard.py": {"sha256": "d4fc0..."},
               "installer-packaging/DEPENDENCIES/seash/tests/guest1.privatekey": {"sha256": "44fd8..."}},
 "name": "build-runnable",
 "products": {"...": "...",
              "installer-packaging/RUNNABLE/parallelize.r2py": {"sha256": "4733c..."},
              "installer-packaging/RUNNABLE/pycryptorsa.r2py": {"sha256": "1514a..."},
              "installer-packaging/RUNNABLE/seattle_linux/seattle/uninstall.sh": {"sha256": "01670..."},
              "installer-packaging/RUNNABLE/seattle_repy/appveyor.yml": {"sha256": "8d9ea..."},
              "installer-packaging/RUNNABLE/seattle_repy/argparse.r2py": {"sha256": "a1057..."},
              "installer-packaging/RUNNABLE/seattle_repy/namingandresolveraffix.r2py": {"sha256": "69bf3..."},
              "installer-packaging/RUNNABLE/seattle_repy/repyV2/win_cpu_nanny.py": {"sha256": "80f8a..."},
              "installer-packaging/RUNNABLE/seattle_repy/xmlrpc_common.r2py": {"sha256": "a89fd..."},
              "installer-packaging/RUNNABLE/seattle_win/seattle/install.bat": {"sha256": "40e49..."}},
 "return_value": 0,
 "signatures": [{"keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
                 "method": "RSASSA-PSS",
                 "sig": "a8c1296c9aed0d7a2f8625aa3a5825e373e90a0d..."}]}
```


## seattle/pre-build-file-edit.link
``` json
{"_type": "Link",
 "byproducts": {},
 "command": "",
 "materials": {"...": "...",
               "installer-packaging/RUNNABLE/cachedadvertise.r2py": {"sha256": "4624d..."},
               "installer-packaging/RUNNABLE/checkpythonversion.py": {"sha256": "a978b..."},
               "installer-packaging/RUNNABLE/encasementlib.r2py": {"sha256": "03ae7..."},
               "installer-packaging/RUNNABLE/portable_popen.py": {"sha256": "cd1b7..."},
               "installer-packaging/RUNNABLE/seattle_repy/freebsd_api.py": {"sha256": "4329a..."},
               "installer-packaging/RUNNABLE/seattle_repy/repyV1/tracebackrepy.py": {"sha256": "73558..."},
               "installer-packaging/RUNNABLE/seattle_repy/repyV1/virtual_namespace.py": {"sha256": "75ee3..."},
               "installer-packaging/RUNNABLE/seattle_repy/repyV2/encoding_header.py": {"sha256": "13e63..."},
               "installer-packaging/RUNNABLE/seattle_repy/softwareupdater.py": {"sha256": "21f29..."}},
 "name": "pre-build-file-edit",
 "products": {"...": "...",
              "installer-packaging/RUNNABLE/rsa.r2py": {"sha256": "0ede3..."},
              "installer-packaging/RUNNABLE/seattle_repy/LICENSE": {"sha256": "95fd6..."},
              "installer-packaging/RUNNABLE/seattle_repy/experimentlib.r2py": {"sha256": "3efed..."},
              "installer-packaging/RUNNABLE/seattle_repy/pyreadline/console/__init__.py": {"sha256": "14f33..."},
              "installer-packaging/RUNNABLE/seattle_repy/pyreadline/unicode_helper.py": {"sha256": "a1a0b..."},
              "installer-packaging/RUNNABLE/seattle_repy/seash_modules.py": {"sha256": "57745..."},
              "installer-packaging/RUNNABLE/seattle_repy/seattleuninstaller.py": {"sha256": "19604..."},
              "installer-packaging/RUNNABLE/seattle_repy/signeddata.r2py": {"sha256": "685c0..."},
              "installer-packaging/RUNNABLE/xmlrpc_common.r2py": {"sha256": "a89fd..."}},
 "return_value": 0,
 "signatures": [{"keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
                 "method": "RSASSA-PSS",
                 "sig": "656cbf10cdd2475a08a0f18232f9caa040f40fa3..."}]}
```


## seattle/build-base-installers.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": "",
                "stdout": "Archiving old base installers to "
                          "/home/cib/custominstallerbuilder/html/static/installers/old_base_installers/\n"
                          "Warning: failure after this point may leave "
                          "seattlegeni with no base installers!\n"
                          "Building ..."},
 "command": ["python", "rebuild_base_installers.py", "0.1-in-toto-in-seattle"],
 "materials": {"...": "...",
               "installer-packaging/RUNNABLE/experimentlib.r2py": {"sha256": "3efed..."},
               "installer-packaging/RUNNABLE/librepy.r2py": {"sha256": "387a1..."},
               "installer-packaging/RUNNABLE/seattle_repy/centralizedadvertise_v2.r2py": {"sha256": "0c7e2..."},
               "installer-packaging/RUNNABLE/seattle_repy/modules/modules/__init__.py": {"sha256": "ad461..."},
               "installer-packaging/RUNNABLE/seattle_repy/pyreadline/console/__init__.py": {"sha256": "14f33..."},
               "installer-packaging/RUNNABLE/seattle_repy/pyreadline/keysyms/keysyms.py": {"sha256": "dc0f6..."},
               "installer-packaging/RUNNABLE/seattle_repy/repyunit.r2py": {"sha256": "e441f..."},
               "installer-packaging/RUNNABLE/seattle_repy/servicelogger.py": {"sha256": "ef629..."},
               "installer-packaging/RUNNABLE/sha.r2py": {"sha256": "83b80..."}},
 "name": "build-base-installers",
 "products": {"...": "...",
              "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_android.zip": {"sha256": "77d91..."},
              "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_linux.tgz": {"sha256": "87d1d..."},
              "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_mac.tgz": {"sha256": "e67f9..."},
              "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_win.zip": {"sha256": "29f0d..."},
              "custominstallerbuilder/html/static/installers/base/seattle_android.zip": {"sha256": "77d91..."},
              "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz": {"sha256": "87d1d..."},
              "custominstallerbuilder/html/static/installers/base/seattle_mac.tgz": {"sha256": "e67f9..."},
              "custominstallerbuilder/html/static/installers/base/seattle_win.zip": {"sha256": "29f0d..."}},
 "return_value": 0,
 "signatures": [{"keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
                 "method": "RSASSA-PSS",
                 "sig": "7b592b27665d3b547aacd4c59a3871972edb4a92..."}]}
```


## seattle/clone-dependencies.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": "",
                "stdout": "Checking out repo from "
                          "https://github.com/SeattleTestbed/nodemanager ...\n"
                          "Done!\n"
                          "Checking out repo from "
                          "https://github.com/SeattleTestbed/softwareupdater "
                          "...\n"
                          "Done!\n"
                          "Checking out repo from https://github...."},
 "command": ["python", "initialize.py"],
 "materials": {"...": "..."},
 "name": "clone-dependencies",
 "products": {"...": "...",
              "installer-packaging/DEPENDENCIES/repy_v1/apps/example/example.4.1.repy": {"sha256": "6711e..."},
              "installer-packaging/DEPENDENCIES/repy_v1/apps/example/restrictions.test": {"sha256": "9c22a..."},
              "installer-packaging/DEPENDENCIES/repy_v1/apps/tcp/tests/units/z_test_state_machine_close.repy": {"sha256": "acce9..."},
              "installer-packaging/DEPENDENCIES/repy_v1/apps/tryrepy/web/js/tr_repy.js": {"sha256": "0f413..."},
              "installer-packaging/DEPENDENCIES/repy_v1/tests/cpu_f.1_restrictions.cpu.05": {"sha256": "04c28..."},
              "installer-packaging/DEPENDENCIES/repy_v1/tests/ut_repytests_testnetmessdupgoodhandle.py": {"sha256": "d8967..."},
              "installer-packaging/DEPENDENCIES/repy_v1/tests/ut_repytests_testwaitforconnfunctions.py": {"sha256": "39cb6..."},
              "installer-packaging/DEPENDENCIES/repy_v1/tests/ut_repytests_veryslownetsend-testloopsend.py": {"sha256": "14807..."},
              "installer-packaging/DEPENDENCIES/seash/modules/variables/__init__.py": {"sha256": "8a318..."}},
 "return_value": 0,
 "signatures": [{"keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
                 "method": "RSASSA-PSS",
                 "sig": "367e5d1b7a2d0cefaf44d01cdc0dd55558c0adee..."}]}
```


