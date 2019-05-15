seattle
======
*There is no readme for this layout*

## Layout

### seattle/root.layout
``` json
{
  "signed": {
    "_type": "layout",
    "readme": "",
    "expires": "2017-01-23T13:27:57Z",
    "steps": [
      {
        "_type": "step",
        "name": "clone-dependencies",
        "expected_command": [
          "python",
          "initialize.py"
        ],
        "pubkeys": [
          "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"
        ],
        "threshold": 1,
        "expected_materials": [],
        "expected_products": [
          [
            "CREATE",
            "installer-packaging/*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "build-runnable",
        "expected_command": [
          "python",
          "build.py"
        ],
        "pubkeys": [
          "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "installer-packaging/*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "clone-dependencies"
          ]
        ],
        "expected_products": [
          [
            "CREATE",
            "installer-packaging/*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "pre-build-file-edit",
        "expected_command": [
          "edit",
          "files",
          "manually"
        ],
        "pubkeys": [
          "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "installer-packaging/RUNNABLE/*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "build-runnable"
          ]
        ],
        "expected_products": [
          [
            "CREATE",
            "installer-packaging/*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "build-base-installers",
        "expected_command": [
          "python",
          "rebuild_base_installers.py",
          "0.1-in-toto-in-seattle"
        ],
        "pubkeys": [
          "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "installer-packaging/*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "pre-build-file-edit"
          ]
        ],
        "expected_products": [
          [
            "CREATE",
            "custominstallerbuilder/html/static/installers/base/*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "dummy-untar-linux-base-installer",
        "expected_command": [
          "tar",
          "xf",
          "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz"
        ],
        "pubkeys": [
          "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz",
            "WITH",
            "PRODUCTS",
            "FROM",
            "build-base-installers"
          ]
        ],
        "expected_products": [
          [
            "CREATE",
            "*"
          ]
        ]
      }
    ],
    "inspect": [
      {
        "_type": "inspection",
        "name": "untar-linux-installer",
        "run": [
          "tar",
          "xf",
          "seattle_linux.tgz"
        ],
        "expected_materials": [
          [
            "CREATE",
            "*"
          ]
        ],
        "expected_products": [
          [
            "CREATE",
            "seattle/seattle_repy/vesselinfo"
          ],
          [
            "MATCH",
            "seattle/*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "dummy-untar-linux-base-installer"
          ],
          [
            "CREATE",
            "*"
          ]
        ]
      }
    ],
    "keys": {
      "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5": {
        "keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
        "keytype": "rsa",
        "keyval": {
          "private": "",
          "public": "-----BEGIN PUBLIC KEY-----\nMIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKC..."
        }
      }
    }
  },
  "signatures": [
    {
      "keyid": "85ed317c5950f8c5921bb547bdecb4e7c697c9502164d60d9c922ff384b083c5",
      "method": "RSASSA-PSS",
      "sig": "ceb3ce5664472dccee0ec9fdf20a281418ab6b537374659786f75718e506b016005..."
    }
  ]
}

```


## Links

### seattle/clone-dependencies.d66d18.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "clone-dependencies",
    "command": [
      "python",
      "initialize.py"
    ],
    "materials": {},
    "products": {
      "installer-packaging/DEPENDENCIES/affix/.travis.yml": {
        "sha256": "d0c6c6a72dcfba6b22e321783c3455c6a680aa7bacc04db8adf184630696b999"
      },
      "installer-packaging/DEPENDENCIES/affix/LICENSE": {
        "sha256": "c58358858f917e4bac08df11f6c89f39743dec35aaabdd629eea6a50341206a8"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_exceptions.r2py": {
        "sha256": "809ff340dffb0972797844fb956a53ff3d26418180553ff13ee4fa81db0a6bc3"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_repy_network_api_wrapper.r2py": {
        "sha256": "dc1e91306e28dfb40d21ceb6de82b6cffff207c9fca36f3e2c2d613d35e3ce4c"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_stack.r2py": {
        "sha256": "97b147a4f3cf2bda14486def2af8d06fe96208747b239ad8c36d73efceb72e7c"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_wrapper_lib.r2py": {
        "sha256": "9f225939d3507c90a58ae8a6157f254390612d78e94c72d67ebe56375e193bfe"
      },
      "installer-packaging/DEPENDENCIES/affix/appveyor.yml": {
        "sha256": "8d9eab5b578723043ce354bcadc3fcb2695a39b964f68a6601ac2f911a1108ef"
      },
      "installer-packaging/DEPENDENCIES/affix/components/baseaffix.r2py": {
        "sha256": "8b21380dc7a25403b279c077ff9d326ea4a0a4f73f84737f0675b9452b46ad13"
      },
      "installer-packaging/DEPENDENCIES/affix/components/canihear.r2py": {
        "sha256": "fb5e95a2b921160d2446e38003280a0b49b71ff83214b12c76c8db845a9bf888"
      },
      "...": "..."
    },
    "byproducts": {
      "return_value": 0,
      "stdout": "Checking out repo from https://github.com/SeattleTestbed/nodemanage...",
      "stderr": ""
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
      "method": "RSASSA-PSS",
      "sig": "367e5d1b7a2d0cefaf44d01cdc0dd55558c0adee5d4edccf1b41ade76c84d0cfdc3..."
    }
  ]
}

```


### seattle/build-runnable.d66d18.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "build-runnable",
    "command": [
      "python",
      "build.py"
    ],
    "materials": {
      "installer-packaging/DEPENDENCIES/affix/.travis.yml": {
        "sha256": "d0c6c6a72dcfba6b22e321783c3455c6a680aa7bacc04db8adf184630696b999"
      },
      "installer-packaging/DEPENDENCIES/affix/LICENSE": {
        "sha256": "c58358858f917e4bac08df11f6c89f39743dec35aaabdd629eea6a50341206a8"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_exceptions.r2py": {
        "sha256": "809ff340dffb0972797844fb956a53ff3d26418180553ff13ee4fa81db0a6bc3"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_repy_network_api_wrapper.r2py": {
        "sha256": "dc1e91306e28dfb40d21ceb6de82b6cffff207c9fca36f3e2c2d613d35e3ce4c"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_stack.r2py": {
        "sha256": "97b147a4f3cf2bda14486def2af8d06fe96208747b239ad8c36d73efceb72e7c"
      },
      "installer-packaging/DEPENDENCIES/affix/affix_wrapper_lib.r2py": {
        "sha256": "9f225939d3507c90a58ae8a6157f254390612d78e94c72d67ebe56375e193bfe"
      },
      "installer-packaging/DEPENDENCIES/affix/appveyor.yml": {
        "sha256": "8d9eab5b578723043ce354bcadc3fcb2695a39b964f68a6601ac2f911a1108ef"
      },
      "installer-packaging/DEPENDENCIES/affix/components/baseaffix.r2py": {
        "sha256": "8b21380dc7a25403b279c077ff9d326ea4a0a4f73f84737f0675b9452b46ad13"
      },
      "installer-packaging/DEPENDENCIES/affix/components/canihear.r2py": {
        "sha256": "fb5e95a2b921160d2446e38003280a0b49b71ff83214b12c76c8db845a9bf888"
      },
      "...": "..."
    },
    "products": {
      "installer-packaging/RUNNABLE/LICENSE": {
        "sha256": "95fd62575bd6de09864bce5286e3654989ef4be834e039e92f5b6b3e533069f2"
      },
      "installer-packaging/RUNNABLE/README.md": {
        "sha256": "a4e3870180bae75c2f22d45c12dbf89e7056f219d440d9fde6663684ab23c9f4"
      },
      "installer-packaging/RUNNABLE/advertise.r2py": {
        "sha256": "30b979fa11919eb7adbdf931788cbba28e7cc4210e172ba8ae7468a3fff6570a"
      },
      "installer-packaging/RUNNABLE/advertise_objects.r2py": {
        "sha256": "f76eee0a4b595335c7894d8db26cddb4574bcaac652f5d8f3154dbad16e791e7"
      },
      "installer-packaging/RUNNABLE/advertisepipe.r2py": {
        "sha256": "8ca0f7c2fca8fb481ae87bc4f0b1c0843ff05626dd9c5315593675d23c59e37b"
      },
      "installer-packaging/RUNNABLE/advertiseserver_v2.r2py": {
        "sha256": "51952a3c7c025017c9ee1d53a27c96b2ba8e57d559a16682d0dbff914cc508d6"
      },
      "installer-packaging/RUNNABLE/appveyor.yml": {
        "sha256": "8d9eab5b578723043ce354bcadc3fcb2695a39b964f68a6601ac2f911a1108ef"
      },
      "installer-packaging/RUNNABLE/argparse.r2py": {
        "sha256": "a1057faa6631c8077c427a6a961899f44c7222dc00ba16bf905ba0e1401a01f9"
      },
      "installer-packaging/RUNNABLE/base64.r2py": {
        "sha256": "ff0b77447dd36cb203cf03afdbd2d1aaeab8c9e8a3831c0416a04c74b0873b7d"
      },
      "...": "..."
    },
    "byproducts": {
      "return_value": 0,
      "stdout": "Building into /home/cib/installer-packaging/RUNNABLE\nDone building!\n",
      "stderr": ""
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
      "method": "RSASSA-PSS",
      "sig": "a8c1296c9aed0d7a2f8625aa3a5825e373e90a0d2c6fce65934920671390a6b45ee..."
    }
  ]
}

```


### seattle/pre-build-file-edit.d66d18.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "pre-build-file-edit",
    "command": [],
    "materials": {
      "installer-packaging/RUNNABLE/LICENSE": {
        "sha256": "95fd62575bd6de09864bce5286e3654989ef4be834e039e92f5b6b3e533069f2"
      },
      "installer-packaging/RUNNABLE/README.md": {
        "sha256": "a4e3870180bae75c2f22d45c12dbf89e7056f219d440d9fde6663684ab23c9f4"
      },
      "installer-packaging/RUNNABLE/advertise.r2py": {
        "sha256": "30b979fa11919eb7adbdf931788cbba28e7cc4210e172ba8ae7468a3fff6570a"
      },
      "installer-packaging/RUNNABLE/advertise_objects.r2py": {
        "sha256": "f76eee0a4b595335c7894d8db26cddb4574bcaac652f5d8f3154dbad16e791e7"
      },
      "installer-packaging/RUNNABLE/advertisepipe.r2py": {
        "sha256": "8ca0f7c2fca8fb481ae87bc4f0b1c0843ff05626dd9c5315593675d23c59e37b"
      },
      "installer-packaging/RUNNABLE/advertiseserver_v2.r2py": {
        "sha256": "51952a3c7c025017c9ee1d53a27c96b2ba8e57d559a16682d0dbff914cc508d6"
      },
      "installer-packaging/RUNNABLE/appveyor.yml": {
        "sha256": "8d9eab5b578723043ce354bcadc3fcb2695a39b964f68a6601ac2f911a1108ef"
      },
      "installer-packaging/RUNNABLE/argparse.r2py": {
        "sha256": "a1057faa6631c8077c427a6a961899f44c7222dc00ba16bf905ba0e1401a01f9"
      },
      "installer-packaging/RUNNABLE/base64.r2py": {
        "sha256": "ff0b77447dd36cb203cf03afdbd2d1aaeab8c9e8a3831c0416a04c74b0873b7d"
      },
      "...": "..."
    },
    "products": {
      "installer-packaging/RUNNABLE/LICENSE": {
        "sha256": "95fd62575bd6de09864bce5286e3654989ef4be834e039e92f5b6b3e533069f2"
      },
      "installer-packaging/RUNNABLE/README.md": {
        "sha256": "a4e3870180bae75c2f22d45c12dbf89e7056f219d440d9fde6663684ab23c9f4"
      },
      "installer-packaging/RUNNABLE/advertise.r2py": {
        "sha256": "30b979fa11919eb7adbdf931788cbba28e7cc4210e172ba8ae7468a3fff6570a"
      },
      "installer-packaging/RUNNABLE/advertise_objects.r2py": {
        "sha256": "f76eee0a4b595335c7894d8db26cddb4574bcaac652f5d8f3154dbad16e791e7"
      },
      "installer-packaging/RUNNABLE/advertisepipe.r2py": {
        "sha256": "8ca0f7c2fca8fb481ae87bc4f0b1c0843ff05626dd9c5315593675d23c59e37b"
      },
      "installer-packaging/RUNNABLE/advertiseserver_v2.r2py": {
        "sha256": "51952a3c7c025017c9ee1d53a27c96b2ba8e57d559a16682d0dbff914cc508d6"
      },
      "installer-packaging/RUNNABLE/appveyor.yml": {
        "sha256": "8d9eab5b578723043ce354bcadc3fcb2695a39b964f68a6601ac2f911a1108ef"
      },
      "installer-packaging/RUNNABLE/argparse.r2py": {
        "sha256": "a1057faa6631c8077c427a6a961899f44c7222dc00ba16bf905ba0e1401a01f9"
      },
      "installer-packaging/RUNNABLE/base64.r2py": {
        "sha256": "ff0b77447dd36cb203cf03afdbd2d1aaeab8c9e8a3831c0416a04c74b0873b7d"
      },
      "...": "..."
    },
    "byproducts": {
      "return_value": null
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
      "method": "RSASSA-PSS",
      "sig": "656cbf10cdd2475a08a0f18232f9caa040f40fa36a5c5142c30b51233a31156f8b6..."
    }
  ]
}

```


### seattle/build-base-installers.d66d18.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "build-base-installers",
    "command": [
      "python",
      "rebuild_base_installers.py",
      "0.1-in-toto-in-seattle"
    ],
    "materials": {
      "installer-packaging/RUNNABLE/LICENSE": {
        "sha256": "95fd62575bd6de09864bce5286e3654989ef4be834e039e92f5b6b3e533069f2"
      },
      "installer-packaging/RUNNABLE/README.md": {
        "sha256": "a4e3870180bae75c2f22d45c12dbf89e7056f219d440d9fde6663684ab23c9f4"
      },
      "installer-packaging/RUNNABLE/advertise.r2py": {
        "sha256": "30b979fa11919eb7adbdf931788cbba28e7cc4210e172ba8ae7468a3fff6570a"
      },
      "installer-packaging/RUNNABLE/advertise_objects.r2py": {
        "sha256": "f76eee0a4b595335c7894d8db26cddb4574bcaac652f5d8f3154dbad16e791e7"
      },
      "installer-packaging/RUNNABLE/advertisepipe.r2py": {
        "sha256": "8ca0f7c2fca8fb481ae87bc4f0b1c0843ff05626dd9c5315593675d23c59e37b"
      },
      "installer-packaging/RUNNABLE/advertiseserver_v2.r2py": {
        "sha256": "51952a3c7c025017c9ee1d53a27c96b2ba8e57d559a16682d0dbff914cc508d6"
      },
      "installer-packaging/RUNNABLE/appveyor.yml": {
        "sha256": "8d9eab5b578723043ce354bcadc3fcb2695a39b964f68a6601ac2f911a1108ef"
      },
      "installer-packaging/RUNNABLE/argparse.r2py": {
        "sha256": "a1057faa6631c8077c427a6a961899f44c7222dc00ba16bf905ba0e1401a01f9"
      },
      "installer-packaging/RUNNABLE/base64.r2py": {
        "sha256": "ff0b77447dd36cb203cf03afdbd2d1aaeab8c9e8a3831c0416a04c74b0873b7d"
      },
      "...": "..."
    },
    "products": {
      "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_android.zip": {
        "sha256": "77d91291b1d7d1127490aebc73cb47f372dea267bc706576bbf92535a37fa0a0"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_linux.tgz": {
        "sha256": "87d1d193917b41a96e8c69b5df268a5ac044f3b892b3392a472daef8c94adae3"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_mac.tgz": {
        "sha256": "e67f9f0b95f67229b25433e09a64bb36357742420f0f7489a6f009a517670236"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_0.1-in-toto-in-seattle_win.zip": {
        "sha256": "29f0d2e6f23996018327675cbc36eab3eb4bcb56b9001017085a7f9a4d17adae"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_android.zip": {
        "sha256": "77d91291b1d7d1127490aebc73cb47f372dea267bc706576bbf92535a37fa0a0"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz": {
        "sha256": "87d1d193917b41a96e8c69b5df268a5ac044f3b892b3392a472daef8c94adae3"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_mac.tgz": {
        "sha256": "e67f9f0b95f67229b25433e09a64bb36357742420f0f7489a6f009a517670236"
      },
      "custominstallerbuilder/html/static/installers/base/seattle_win.zip": {
        "sha256": "29f0d2e6f23996018327675cbc36eab3eb4bcb56b9001017085a7f9a4d17adae"
      }
    },
    "byproducts": {
      "return_value": 0,
      "stdout": "Archiving old base installers to /home/cib/custominstallerbuilder/h...",
      "stderr": ""
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
      "method": "RSASSA-PSS",
      "sig": "7b592b27665d3b547aacd4c59a3871972edb4a923202728fe458ddbe49c6c20952c..."
    }
  ]
}

```


### seattle/dummy-untar-linux-base-installer.d66d18.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "dummy-untar-linux-base-installer",
    "command": [
      "tar",
      "xf",
      "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz"
    ],
    "materials": {
      "custominstallerbuilder/html/static/installers/base/seattle_linux.tgz": {
        "sha256": "87d1d193917b41a96e8c69b5df268a5ac044f3b892b3392a472daef8c94adae3"
      }
    },
    "products": {
      "seattle/install.sh": {
        "sha256": "ca523d1ca5b331278fc4eb7a09c0296314b00dd7d90e47e90dee3d7572fe73ea"
      },
      "seattle/seattle_repy/BandwidthClient.py": {
        "sha256": "3538c302e2412d095c15cd00b1b85f68af6b42cff0a624aa53dc560cc0341770"
      },
      "seattle/seattle_repy/BandwidthServer.py": {
        "sha256": "3369ef9eaf7e7ce02c304c55699738c0a6a6c21dcc1e053b7e10875f9d5dc4ff"
      },
      "seattle/seattle_repy/LICENSE": {
        "sha256": "95fd62575bd6de09864bce5286e3654989ef4be834e039e92f5b6b3e533069f2"
      },
      "seattle/seattle_repy/LICENSE.txt": {
        "sha256": "c349ed2c887cc4798462516fb3fbeea19e4f8dcf81444983006ef7e15d876de9"
      },
      "seattle/seattle_repy/Linux_resources.py": {
        "sha256": "b2520913a0a27ae6c716190fa3f4c23a3b02fc174da99b816c90f20acf57dfb6"
      },
      "seattle/seattle_repy/Mac_BSD_resources.py": {
        "sha256": "a56e6e1725f22d4b055b9a9bd5e7e6a349a1a18b180992c42563936d4c7f9e3f"
      },
      "seattle/seattle_repy/README.txt": {
        "sha256": "6a72741a949dba40179472a93c7b458f7cfd38f2261baf131712b9139ebaa921"
      },
      "seattle/seattle_repy/Win_WinCE_resources.py": {
        "sha256": "137856aac0ca9b6c1116ffb19c39cc355ce4734afe97911a39e1664698ea16af"
      },
      "...": "..."
    },
    "byproducts": {
      "return_value": 0,
      "stdout": "",
      "stderr": ""
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "d66d18e768284e519ed2d0774376faf4859cb6529bf6e392621b8d42752206d5",
      "method": "RSASSA-PSS",
      "sig": "aa05b3773b3cad3a1d70b7ae43fd37f168a59c7e65b24affe81dae0a290981e10e0..."
    }
  ]
}

```


