debian
======
*There is no readme for this layout*

## Layout

### debian/root.layout
``` json
{
  "signed": {
    "_type": "layout",
    "readme": "",
    "expires": "2017-09-02T12:57:02Z",
    "steps": [
      {
        "_type": "step",
        "name": "fetch",
        "expected_command": [
          "dget",
          "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12-2.dsc"
        ],
        "pubkeys": [
          "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "DISALLOW",
            "*"
          ]
        ],
        "expected_products": [
          [
            "ALLOW",
            "*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "extract",
        "expected_command": [
          "dpkg-source",
          "-x",
          "grep_2.12-2.dsc"
        ],
        "pubkeys": [
          "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "fetch"
          ]
        ],
        "expected_products": [
          [
            "ALLOW",
            "*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "modify",
        "expected_command": [],
        "pubkeys": [
          "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "extract"
          ]
        ],
        "expected_products": [
          [
            "ALLOW",
            "*"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "build",
        "expected_command": [
          "dpkg-buildpackage",
          "-us",
          "-uc"
        ],
        "pubkeys": [
          "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "*",
            "WITH",
            "PRODUCTS",
            "FROM",
            "modify"
          ]
        ],
        "expected_products": [
          [
            "ALLOW",
            "*"
          ]
        ]
      }
    ],
    "inspect": [],
    "keys": {
      "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2": {
        "keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
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
      "keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
      "method": "RSASSA-PSS",
      "sig": "9c3a5609e79ea68f9d7aa4b72e5ab1f00b7773f06912b789add45da026f46621b9e..."
    }
  ]
}

```


## Links

### debian/fetch.12c55e46.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "fetch",
    "command": [
      "dget",
      "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12-2.dsc"
    ],
    "materials": {},
    "products": {
      "/home/lukas/demo/grep_2.12-2.debian.tar.bz2": {
        "sha256": "37887d8aecec66e75365abd8c41be94f75e7a3acf1d6b27fc121584f47281525"
      },
      "/home/lukas/demo/grep_2.12-2.dsc": {
        "sha256": "a6a63fd21da40d11ce6ae2bc6f633bd27cd206c2348b2ef306e1b68120f7e58e"
      },
      "/home/lukas/demo/grep_2.12.orig.tar.bz2": {
        "sha256": "0119987171cd60b87c89557524fc6636bdad770dae71917adcaef6abffb1be67"
      }
    },
    "byproducts": {
      "return_value": 1,
      "stdout": "dget: retrieving http://cdn.debian.net/debian/pool/main/g/grep/grep...",
      "stderr": "--2017-08-08 11:05:06--  http://cdn.debian.net/debian/pool/main/g/g..."
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
      "method": "RSASSA-PSS",
      "sig": "a0d3237a59a96343b2e2caee2bf0e27a249a01f796c3fec53f184fc2720b44dd7b2..."
    }
  ]
}

```


### debian/extract.12c55e46.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "extract",
    "command": [
      "dpkg-source",
      "-x",
      "grep_2.12-2.dsc"
    ],
    "materials": {
      "/home/lukas/demo/grep_2.12-2.debian.tar.bz2": {
        "sha256": "37887d8aecec66e75365abd8c41be94f75e7a3acf1d6b27fc121584f47281525"
      },
      "/home/lukas/demo/grep_2.12-2.dsc": {
        "sha256": "a6a63fd21da40d11ce6ae2bc6f633bd27cd206c2348b2ef306e1b68120f7e58e"
      },
      "/home/lukas/demo/grep_2.12.orig.tar.bz2": {
        "sha256": "0119987171cd60b87c89557524fc6636bdad770dae71917adcaef6abffb1be67"
      }
    },
    "products": {
      "/home/lukas/demo/grep-2.12/.pc/.quilt_patches": {
        "sha256": "0623de532bc23399e87e6c1914e8e90e999efbfd26b6b956666a493893739f0d"
      },
      "/home/lukas/demo/grep-2.12/.pc/.quilt_series": {
        "sha256": "9afbb183d1b683d2770aecb9b379093804ccc56027f07ecf7fc252d5b93a8df2"
      },
      "/home/lukas/demo/grep-2.12/.pc/.version": {
        "sha256": "53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3"
      },
      "/home/lukas/demo/grep-2.12/.pc/02-man_rgrep.patch/doc/grep.in.1": {
        "sha256": "0c933cbdacb739761f7cf9be1d9c0543b8a5cb0c1cf4031fc7add8e81146c1a6"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/configure": {
        "sha256": "fda1f6c62f081999b74177f560e14db0b0b2f93cd632ed4a02f6ac2582fc27bf"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/src/pcresearch.c": {
        "sha256": "08e24565e42cf5e2aeff2ca65cc4e3a8de5fa65260ea1a2d1ae872b45c3b6a25"
      },
      "/home/lukas/demo/grep-2.12/.pc/04-446854-grep.1.patch/doc/grep.in.1": {
        "sha256": "90b74e6c5542b0db506c372f77c45ceab8d7289432cfe37bce11d611a4827a4d"
      },
      "/home/lukas/demo/grep-2.12/.pc/70-man_apostrophe.patch/doc/grep.in.1": {
        "sha256": "eee01bf4de92df307b7f1b6fa740e1c0e0c8c28d6a12b6939ddec0708699da25"
      },
      "/home/lukas/demo/grep-2.12/.pc/80-587930-man-ere-reference.patch/doc/grep.in.1": {
        "sha256": "30378876bf1c1a13449c993fb7a6406089f7f77a34f96fed5c6c742e75a395b6"
      },
      "...": "..."
    },
    "byproducts": {
      "return_value": 0,
      "stdout": "dpkg-source: info: extracting grep in grep-2.12\ndpkg-source: info: ...",
      "stderr": "gpgv: Signature made Sun 13 May 2012 08:23:12 AM EDT using DSA key ..."
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
      "method": "RSASSA-PSS",
      "sig": "9b89cf0a74a1d53359460982cdc3dcbdef2b291a284b977fadb839501d7324fe581..."
    }
  ]
}

```


### debian/modify.12c55e46.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "modify",
    "command": [],
    "materials": {
      "/home/lukas/demo/grep-2.12/.pc/.quilt_patches": {
        "sha256": "0623de532bc23399e87e6c1914e8e90e999efbfd26b6b956666a493893739f0d"
      },
      "/home/lukas/demo/grep-2.12/.pc/.quilt_series": {
        "sha256": "9afbb183d1b683d2770aecb9b379093804ccc56027f07ecf7fc252d5b93a8df2"
      },
      "/home/lukas/demo/grep-2.12/.pc/.version": {
        "sha256": "53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3"
      },
      "/home/lukas/demo/grep-2.12/.pc/02-man_rgrep.patch/doc/grep.in.1": {
        "sha256": "0c933cbdacb739761f7cf9be1d9c0543b8a5cb0c1cf4031fc7add8e81146c1a6"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/configure": {
        "sha256": "fda1f6c62f081999b74177f560e14db0b0b2f93cd632ed4a02f6ac2582fc27bf"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/src/pcresearch.c": {
        "sha256": "08e24565e42cf5e2aeff2ca65cc4e3a8de5fa65260ea1a2d1ae872b45c3b6a25"
      },
      "/home/lukas/demo/grep-2.12/.pc/04-446854-grep.1.patch/doc/grep.in.1": {
        "sha256": "90b74e6c5542b0db506c372f77c45ceab8d7289432cfe37bce11d611a4827a4d"
      },
      "/home/lukas/demo/grep-2.12/.pc/70-man_apostrophe.patch/doc/grep.in.1": {
        "sha256": "eee01bf4de92df307b7f1b6fa740e1c0e0c8c28d6a12b6939ddec0708699da25"
      },
      "/home/lukas/demo/grep-2.12/.pc/80-587930-man-ere-reference.patch/doc/grep.in.1": {
        "sha256": "30378876bf1c1a13449c993fb7a6406089f7f77a34f96fed5c6c742e75a395b6"
      },
      "...": "..."
    },
    "products": {
      "/home/lukas/demo/grep-2.12/.pc/.quilt_patches": {
        "sha256": "0623de532bc23399e87e6c1914e8e90e999efbfd26b6b956666a493893739f0d"
      },
      "/home/lukas/demo/grep-2.12/.pc/.quilt_series": {
        "sha256": "9afbb183d1b683d2770aecb9b379093804ccc56027f07ecf7fc252d5b93a8df2"
      },
      "/home/lukas/demo/grep-2.12/.pc/.version": {
        "sha256": "53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3"
      },
      "/home/lukas/demo/grep-2.12/.pc/02-man_rgrep.patch/doc/grep.in.1": {
        "sha256": "0c933cbdacb739761f7cf9be1d9c0543b8a5cb0c1cf4031fc7add8e81146c1a6"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/configure": {
        "sha256": "fda1f6c62f081999b74177f560e14db0b0b2f93cd632ed4a02f6ac2582fc27bf"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/src/pcresearch.c": {
        "sha256": "08e24565e42cf5e2aeff2ca65cc4e3a8de5fa65260ea1a2d1ae872b45c3b6a25"
      },
      "/home/lukas/demo/grep-2.12/.pc/04-446854-grep.1.patch/doc/grep.in.1": {
        "sha256": "90b74e6c5542b0db506c372f77c45ceab8d7289432cfe37bce11d611a4827a4d"
      },
      "/home/lukas/demo/grep-2.12/.pc/70-man_apostrophe.patch/doc/grep.in.1": {
        "sha256": "eee01bf4de92df307b7f1b6fa740e1c0e0c8c28d6a12b6939ddec0708699da25"
      },
      "/home/lukas/demo/grep-2.12/.pc/80-587930-man-ere-reference.patch/doc/grep.in.1": {
        "sha256": "30378876bf1c1a13449c993fb7a6406089f7f77a34f96fed5c6c742e75a395b6"
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
      "keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
      "method": "RSASSA-PSS",
      "sig": "6c922765260c71bbe0eef0267c2ad6f226eeec43ef45b5dcba6314f52adba655265..."
    }
  ]
}

```


### debian/build.12c55e46.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "build",
    "command": [
      "dpkg-buildpackage",
      "-us",
      "-uc"
    ],
    "materials": {
      "/home/lukas/demo/grep-2.12/.pc/.quilt_patches": {
        "sha256": "0623de532bc23399e87e6c1914e8e90e999efbfd26b6b956666a493893739f0d"
      },
      "/home/lukas/demo/grep-2.12/.pc/.quilt_series": {
        "sha256": "9afbb183d1b683d2770aecb9b379093804ccc56027f07ecf7fc252d5b93a8df2"
      },
      "/home/lukas/demo/grep-2.12/.pc/.version": {
        "sha256": "53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3"
      },
      "/home/lukas/demo/grep-2.12/.pc/02-man_rgrep.patch/doc/grep.in.1": {
        "sha256": "0c933cbdacb739761f7cf9be1d9c0543b8a5cb0c1cf4031fc7add8e81146c1a6"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/configure": {
        "sha256": "fda1f6c62f081999b74177f560e14db0b0b2f93cd632ed4a02f6ac2582fc27bf"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/src/pcresearch.c": {
        "sha256": "08e24565e42cf5e2aeff2ca65cc4e3a8de5fa65260ea1a2d1ae872b45c3b6a25"
      },
      "/home/lukas/demo/grep-2.12/.pc/04-446854-grep.1.patch/doc/grep.in.1": {
        "sha256": "90b74e6c5542b0db506c372f77c45ceab8d7289432cfe37bce11d611a4827a4d"
      },
      "/home/lukas/demo/grep-2.12/.pc/70-man_apostrophe.patch/doc/grep.in.1": {
        "sha256": "eee01bf4de92df307b7f1b6fa740e1c0e0c8c28d6a12b6939ddec0708699da25"
      },
      "/home/lukas/demo/grep-2.12/.pc/80-587930-man-ere-reference.patch/doc/grep.in.1": {
        "sha256": "30378876bf1c1a13449c993fb7a6406089f7f77a34f96fed5c6c742e75a395b6"
      },
      "...": "..."
    },
    "products": {
      "/home/lukas/demo/grep-2.12/.pc/.quilt_patches": {
        "sha256": "0623de532bc23399e87e6c1914e8e90e999efbfd26b6b956666a493893739f0d"
      },
      "/home/lukas/demo/grep-2.12/.pc/.quilt_series": {
        "sha256": "9afbb183d1b683d2770aecb9b379093804ccc56027f07ecf7fc252d5b93a8df2"
      },
      "/home/lukas/demo/grep-2.12/.pc/.version": {
        "sha256": "53c234e5e8472b6ac51c1ae1cab3fe06fad053beb8ebfd8977b010655bfdd3c3"
      },
      "/home/lukas/demo/grep-2.12/.pc/02-man_rgrep.patch/doc/grep.in.1": {
        "sha256": "0c933cbdacb739761f7cf9be1d9c0543b8a5cb0c1cf4031fc7add8e81146c1a6"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/configure": {
        "sha256": "fda1f6c62f081999b74177f560e14db0b0b2f93cd632ed4a02f6ac2582fc27bf"
      },
      "/home/lukas/demo/grep-2.12/.pc/03-397262-dlopen-pcre.patch/src/pcresearch.c": {
        "sha256": "08e24565e42cf5e2aeff2ca65cc4e3a8de5fa65260ea1a2d1ae872b45c3b6a25"
      },
      "/home/lukas/demo/grep-2.12/.pc/04-446854-grep.1.patch/doc/grep.in.1": {
        "sha256": "90b74e6c5542b0db506c372f77c45ceab8d7289432cfe37bce11d611a4827a4d"
      },
      "/home/lukas/demo/grep-2.12/.pc/70-man_apostrophe.patch/doc/grep.in.1": {
        "sha256": "eee01bf4de92df307b7f1b6fa740e1c0e0c8c28d6a12b6939ddec0708699da25"
      },
      "/home/lukas/demo/grep-2.12/.pc/80-587930-man-ere-reference.patch/doc/grep.in.1": {
        "sha256": "30378876bf1c1a13449c993fb7a6406089f7f77a34f96fed5c6c742e75a395b6"
      },
      "...": "..."
    },
    "byproducts": {
      "return_value": 0,
      "stdout": "dpkg-buildpackage: source package grep\ndpkg-buildpackage: source ve...",
      "stderr": " dpkg-source --before-build grep-2.12\n fakeroot debian/rules clean\n..."
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
      "method": "RSASSA-PSS",
      "sig": "3877a06dee3f6e140e20d5100964adb38c1c63dd89803087204d561c0adbfed17c2..."
    }
  ]
}

```


