polypasswordhasher
======
*There is no readme for this layout*

## Layout

### polypasswordhasher/root.layout
``` json
{
  "signed": {
    "_type": "layout",
    "readme": "",
    "expires": "2016-12-10T13:09:03Z",
    "steps": [
      {
        "_type": "step",
        "name": "tag-release",
        "expected_command": [
          "git",
          "tag"
        ],
        "pubkeys": [
          "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f"
        ],
        "threshold": 1,
        "expected_materials": [],
        "expected_products": [
          [
            "CREATE",
            "polypasswordhasher/*.py"
          ],
          [
            "CREATE",
            "setup.py"
          ],
          [
            "CREATE",
            "test/test*.py"
          ],
          [
            "CREATE",
            "test/__init__.py"
          ],
          [
            "CREATE",
            "test/runtests.py"
          ],
          [
            "CREATE",
            "src/fastpolymath.c"
          ],
          [
            "CREATE",
            "include/fastpolymath.h"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "build-sdist",
        "expected_command": [
          "python",
          "setup.py",
          "sdist"
        ],
        "pubkeys": [
          "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "polypasswordhasher/*.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "src/fastpolymath.c",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "include/fastpolymath.h",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "setup.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test/test*.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test/__init__.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test/runtests.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ]
        ],
        "expected_products": [
          [
            "CREATE",
            "dist/PolyPasswordHasher-0.2a0.tar.gz"
          ]
        ]
      },
      {
        "_type": "step",
        "name": "test",
        "expected_command": [
          "python",
          "setup.py",
          "test"
        ],
        "pubkeys": [
          "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f"
        ],
        "threshold": 1,
        "expected_materials": [
          [
            "MATCH",
            "polypasswordhasher/*.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "src/fastpolymath.c",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "include/fastpolymath.h",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test/test*.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test/__init__*.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test/runtests.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "setup.py",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ]
        ],
        "expected_products": []
      }
    ],
    "inspect": [
      {
        "_type": "inspection",
        "name": "untar",
        "run": [
          "tar",
          "xvf",
          "PolyPasswordHasher-0.2a0.tar.gz"
        ],
        "expected_materials": [
          [
            "MATCH",
            "PolyPasswordHasher-0.2a0.tar.gz",
            "WITH",
            "PRODUCTS",
            "IN",
            "dist",
            "FROM",
            "build-sdist"
          ],
          [
            "CREATE",
            "*"
          ]
        ],
        "expected_products": [
          [
            "MATCH",
            "*.py",
            "IN",
            "PolyPasswordHasher-0.2a0/polypasswordhasher",
            "WITH",
            "PRODUCTS",
            "IN",
            "polypasswordhasher",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "fastpolymath.c",
            "IN",
            "PolyPasswordHasher-0.2a0/src",
            "WITH",
            "PRODUCTS",
            "IN",
            "src",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "fastpolymath.h",
            "IN",
            "PolyPasswordHasher-0.2a0/include",
            "WITH",
            "PRODUCTS",
            "IN",
            "include",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "test*.py",
            "IN",
            "PolyPasswordHasher-0.2a0/test",
            "WITH",
            "PRODUCTS",
            "IN",
            "test",
            "FROM",
            "tag-release"
          ],
          [
            "MATCH",
            "setup.py",
            "IN",
            "PolyPasswordHasher-0.2a0",
            "WITH",
            "PRODUCTS",
            "FROM",
            "tag-release"
          ],
          [
            "CREATE",
            "*"
          ]
        ]
      }
    ],
    "keys": {
      "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f": {
        "keyid": "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f",
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
      "keyid": "ee4ca725ae71eb8be7971505a301f6c6b9d1b0b25ccbf18b1532e7171b9741b5",
      "method": "RSASSA-PSS",
      "sig": "90119b3329753ed3cf58e20071c99cf68e4eb56dcecd98bb409da4ff7ce3e1351d7..."
    }
  ]
}

```


## Links

### polypasswordhasher/tag-release.xxx.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "tag-release",
    "command": [
      "git",
      "tag",
      "v0.2a"
    ],
    "materials": {},
    "products": {
      "include/fastpolymath.h": {
        "sha256": "5be4945cdd1b958d3e8029c7b76333311485c2ccbc3e81ff64bfeb4e7a6fb5be"
      },
      "polypasswordhasher/__init__.py": {
        "sha256": "a7464a8ee4ba930a554ff6cd87b3aad5b6328eda4732c5af55eb154e50569ac2"
      },
      "polypasswordhasher/fastshamirsecret.py": {
        "sha256": "5b46ebba43be20ed20ea271b12c78e1b0fa8d53dbea8a53d48074977fe9b97cc"
      },
      "polypasswordhasher/polypasswordhasher.py": {
        "sha256": "79b33112d045e244e8748b4e630aab3256ab664fc0dcc2cdc3262e847e180e13"
      },
      "polypasswordhasher/shamirsecret.py": {
        "sha256": "cbc6d7dd59c65044300faadf1ce696469f8509622b35824643b1f35f5f8435fb"
      },
      "setup.py": {
        "sha256": "f407ce7094ea452a3df6bd9cb8190fcd7c6e79e73593387cc84c70b94592f3d0"
      },
      "src/fastpolymath.c": {
        "sha256": "79e0f36bf1e30460d0492e3f8bf1af4f40aabc54cddf47d68b6b28d124449a0f"
      },
      "test/__init__.py": {
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      },
      "test/runtests.py": {
        "sha256": "fc65bc6775a866c687e9d7dc6d5c5f0bb4f9ef2ab658d34287a99e86fd13acf2"
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
      "keyid": "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f",
      "method": "RSASSA-PSS",
      "sig": "1edb549421d6ad62751b166f52b9868eded6680936b47a1d9907e904be7befce4b3..."
    }
  ]
}

```


### polypasswordhasher/build-sdist.xxx.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "build-sdist",
    "command": [
      "python",
      "setup.py",
      "sdist"
    ],
    "materials": {
      "include/fastpolymath.h": {
        "sha256": "5be4945cdd1b958d3e8029c7b76333311485c2ccbc3e81ff64bfeb4e7a6fb5be"
      },
      "polypasswordhasher/__init__.py": {
        "sha256": "a7464a8ee4ba930a554ff6cd87b3aad5b6328eda4732c5af55eb154e50569ac2"
      },
      "polypasswordhasher/fastshamirsecret.py": {
        "sha256": "5b46ebba43be20ed20ea271b12c78e1b0fa8d53dbea8a53d48074977fe9b97cc"
      },
      "polypasswordhasher/polypasswordhasher.py": {
        "sha256": "79b33112d045e244e8748b4e630aab3256ab664fc0dcc2cdc3262e847e180e13"
      },
      "polypasswordhasher/shamirsecret.py": {
        "sha256": "cbc6d7dd59c65044300faadf1ce696469f8509622b35824643b1f35f5f8435fb"
      },
      "setup.py": {
        "sha256": "f407ce7094ea452a3df6bd9cb8190fcd7c6e79e73593387cc84c70b94592f3d0"
      },
      "src/fastpolymath.c": {
        "sha256": "79e0f36bf1e30460d0492e3f8bf1af4f40aabc54cddf47d68b6b28d124449a0f"
      },
      "test/__init__.py": {
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      },
      "test/runtests.py": {
        "sha256": "fc65bc6775a866c687e9d7dc6d5c5f0bb4f9ef2ab658d34287a99e86fd13acf2"
      },
      "...": "..."
    },
    "products": {
      "dist/PolyPasswordHasher-0.2a0.tar.gz": {
        "sha256": "3620c4cab08f973431c048ec958dd76a9f6c2baa4cefdb85227856e2de100075"
      }
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
      "keyid": "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f",
      "method": "RSASSA-PSS",
      "sig": "a73e47fd3a9c7775431313c14c6e5d27a0d1e0e2396c0fd8b41bf0b7232d4f75c8e..."
    }
  ]
}

```


### polypasswordhasher/test.xxx.link
``` json
{
  "signed": {
    "_type": "link",
    "name": "test",
    "command": [
      "python",
      "setup.py",
      "test"
    ],
    "materials": {
      "include/fastpolymath.h": {
        "sha256": "5be4945cdd1b958d3e8029c7b76333311485c2ccbc3e81ff64bfeb4e7a6fb5be"
      },
      "polypasswordhasher/__init__.py": {
        "sha256": "a7464a8ee4ba930a554ff6cd87b3aad5b6328eda4732c5af55eb154e50569ac2"
      },
      "polypasswordhasher/fastshamirsecret.py": {
        "sha256": "5b46ebba43be20ed20ea271b12c78e1b0fa8d53dbea8a53d48074977fe9b97cc"
      },
      "polypasswordhasher/polypasswordhasher.py": {
        "sha256": "79b33112d045e244e8748b4e630aab3256ab664fc0dcc2cdc3262e847e180e13"
      },
      "polypasswordhasher/shamirsecret.py": {
        "sha256": "cbc6d7dd59c65044300faadf1ce696469f8509622b35824643b1f35f5f8435fb"
      },
      "setup.py": {
        "sha256": "f407ce7094ea452a3df6bd9cb8190fcd7c6e79e73593387cc84c70b94592f3d0"
      },
      "src/fastpolymath.c": {
        "sha256": "79e0f36bf1e30460d0492e3f8bf1af4f40aabc54cddf47d68b6b28d124449a0f"
      },
      "test/__init__.py": {
        "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
      },
      "test/runtests.py": {
        "sha256": "fc65bc6775a866c687e9d7dc6d5c5f0bb4f9ef2ab658d34287a99e86fd13acf2"
      },
      "...": "..."
    },
    "products": {},
    "byproducts": {
      "return_value": 0,
      "stdout": "",
      "stderr": ""
    },
    "environment": {}
  },
  "signatures": [
    {
      "keyid": "48c92a75036a01a864a3a5546fddb601733e135692718afd3f896935474ffb7f",
      "method": "RSASSA-PSS",
      "sig": "80977ff9bc0265724ceb952ad99c2c35206e4ad4364d843e2b9d8e79057e70515c1..."
    }
  ]
}

```


