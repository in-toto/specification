debian/
=======

There is no readme for this layout

# Layout metadata
## debian/root.layout
```json
{"_type": "layout",
 "expires": "2017-09-02T12:57:02Z",
 "inspect": [],
 "keys": {"12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2": {"keyid": "...",
                                                                               "keytype": "rsa",
                                                                               "keyval": {"private": "",
                                                                                          "public": "..."}}},
 "signatures": ["..."],
 "steps": [{"_type": "step",
            "expected_command": ["dget",
                                 "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12-2.dsc"],
            "expected_materials": [["DISALLOW", "*"]],
            "expected_products": [["ALLOW", "*"]],
            "name": "fetch",
            "pubkeys": ["12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"],
            "threshold": 1},
           {"_type": "step",
            "expected_command": ["dpkg-source", "-x", "grep_2.12-2.dsc"],
            "expected_materials": [["MATCH",
                                    "*",
                                    "WITH",
                                    "PRODUCTS",
                                    "FROM",
                                    "fetch"]],
            "expected_products": [["ALLOW", "*"]],
            "name": "extract",
            "pubkeys": ["12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"],
            "threshold": 1},
           {"_type": "step",
            "expected_command": [],
            "expected_materials": [["MATCH",
                                    "*",
                                    "WITH",
                                    "PRODUCTS",
                                    "FROM",
                                    "extract"]],
            "expected_products": [["ALLOW", "*"]],
            "name": "modify",
            "pubkeys": ["12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"],
            "threshold": 1},
           {"_type": "step",
            "expected_command": ["dpkg-buildpackage", "-us", "-uc"],
            "expected_materials": [["MATCH",
                                    "*",
                                    "WITH",
                                    "PRODUCTS",
                                    "FROM",
                                    "modify"]],
            "expected_products": [["ALLOW", "*"]],
            "name": "build",
            "pubkeys": ["12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2"],
            "threshold": 1}]}
```

# Link metadata

## debian/extract.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": "gpgv: Signature made Sun 13 May 2012 08:23:12 AM "
                          "EDT using DSA key ID 6FECCDE0\n"
                          "gpgv: Can’t check signature: public key not found\n"
                          "dpkg-source: warning: failed to verify signature on "
                          "./grep_2.12-2.dsc\n",
                "stdout": "dpkg-source: info: extracting grep in grep-2.12\n"
                          "dpkg-source: info: unpacking "
                          "grep_2.12.orig.tar.bz2\n"
                          "dpkg-source: info: unpacking "
                          "grep_2.12-2.debian.tar.bz2\n"
                          "dpkg-source: info: applying 02-man_rgrep.pat..."},
 "command": ["dpkg-source", "-x", "grep_2.12-2.dsc"],
 "materials": {"...": "...",
               "/home/lukas/demo/grep_2.12-2.debian.tar.bz2": {"sha256": "37887..."},
               "/home/lukas/demo/grep_2.12-2.dsc": {"sha256": "a6a63..."},
               "/home/lukas/demo/grep_2.12.orig.tar.bz2": {"sha256": "01199..."}},
 "name": "extract",
 "products": {"...": "...",
              "/home/lukas/demo/grep-2.12/configure.ac": {"sha256": "72946..."},
              "/home/lukas/demo/grep-2.12/gnulib-tests/unsetenv.c": {"sha256": "a06e3..."},
              "/home/lukas/demo/grep-2.12/lib/dirfd.c": {"sha256": "a0540..."},
              "/home/lukas/demo/grep-2.12/lib/gettext.h": {"sha256": "a3e97..."},
              "/home/lukas/demo/grep-2.12/lib/quote.h": {"sha256": "3eeb3..."},
              "/home/lukas/demo/grep-2.12/m4/dup.m4": {"sha256": "9db31..."},
              "/home/lukas/demo/grep-2.12/m4/fts.m4": {"sha256": "36bbe..."},
              "/home/lukas/demo/grep-2.12/m4/warn-on-use.m4": {"sha256": "b79d1..."},
              "/home/lukas/demo/grep-2.12/tests/bre.tests": {"sha256": "caf58..."}},
 "return_value": 0,
 "signatures": [{"keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
                 "method": "RSASSA-PSS",
                 "sig": "9b89cf0a74a1d53359460982cdc3dcbdef2b291a..."}]}
```


## debian/modify.link
``` json
{"_type": "Link",
 "byproducts": {},
 "command": [],
 "materials": {"...": "...",
               "/home/lukas/demo/grep-2.12/gnulib-tests/test-exclude4.sh": {"sha256": "55979..."},
               "/home/lukas/demo/grep-2.12/gnulib-tests/test-iswblank.c": {"sha256": "3b548..."},
               "/home/lukas/demo/grep-2.12/gnulib-tests/test-sys_stat.c": {"sha256": "a3a52..."},
               "/home/lukas/demo/grep-2.12/lib/binary-io.h": {"sha256": "f03de..."},
               "/home/lukas/demo/grep-2.12/lib/fd-safer.c": {"sha256": "ccd06..."},
               "/home/lukas/demo/grep-2.12/lib/iconv_close.c": {"sha256": "45702..."},
               "/home/lukas/demo/grep-2.12/m4/environ.m4": {"sha256": "fb236..."},
               "/home/lukas/demo/grep-2.12/m4/strtoumax.m4": {"sha256": "732a0..."},
               "/home/lukas/demo/grep-2.12/tests/spencer1": {"sha256": "d03fc..."}},
 "name": "modify",
 "products": {"...": "...",
              "/home/lukas/demo/grep-2.12/build-aux/useless-if-before-free": {"sha256": "c06f0..."},
              "/home/lukas/demo/grep-2.12/lib/i-ring.h": {"sha256": "38177..."},
              "/home/lukas/demo/grep-2.12/lib/iconv_open-osf.h": {"sha256": "9d361..."},
              "/home/lukas/demo/grep-2.12/lib/ignore-value.h": {"sha256": "19463..."},
              "/home/lukas/demo/grep-2.12/lib/isblank.c": {"sha256": "407be..."},
              "/home/lukas/demo/grep-2.12/lib/unistd--.h": {"sha256": "7ba49..."},
              "/home/lukas/demo/grep-2.12/lib/xstriconv.c": {"sha256": "2bd69..."},
              "/home/lukas/demo/grep-2.12/m4/environ.m4": {"sha256": "fb236..."},
              "/home/lukas/demo/grep-2.12/po/stamp-po": {"sha256": "2cd8e..."}},
 "return_value": 0,
 "signatures": [{"keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
                 "method": "RSASSA-PSS",
                 "sig": "6c922765260c71bbe0eef0267c2ad6f226eeec43..."}]}
```


## debian/fetch.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": "--2017-08-08 11:05:06--  "
                          "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12-2.dsc\n"
                          "Resolving cdn.debian.net (cdn.debian.net)... "
                          "149.20.4.15, 5.153.231.4, 128.31.0.62, ...\n"
                          "Connecting to cdn.debian....",
                "stdout": "dget: retrieving "
                          "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12-2.dsc\n"
                          "dget: retrieving "
                          "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12.orig.tar.bz2\n"
                          "dget: retrieving http://cdn.debian...."},
 "command": ["dget",
             "http://cdn.debian.net/debian/pool/main/g/grep/grep_2.12-2.dsc"],
 "materials": {"...": "..."},
 "name": "fetch",
 "products": {"...": "...",
              "/home/lukas/demo/grep_2.12-2.debian.tar.bz2": {"sha256": "37887..."},
              "/home/lukas/demo/grep_2.12-2.dsc": {"sha256": "a6a63..."},
              "/home/lukas/demo/grep_2.12.orig.tar.bz2": {"sha256": "01199..."}},
 "return_value": 1,
 "signatures": [{"keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
                 "method": "RSASSA-PSS",
                 "sig": "a0d3237a59a96343b2e2caee2bf0e27a249a01f7..."}]}
```


## debian/build.link
``` json
{"_type": "Link",
 "byproducts": {"stderr": " dpkg-source --before-build grep-2.12\n"
                          " fakeroot debian/rules clean\n"
                          " dpkg-source -b grep-2.12\n"
                          " debian/rules build\n"
                          "configure: WARNING: Included lib/regex.c not used\n"
                          " fakeroot debian/rules binary\n"
                          "dpkg-sh...",
                "stdout": "dpkg-buildpackage: source package grep\n"
                          "dpkg-buildpackage: source version 2.12-2.1\n"
                          "dpkg-buildpackage: source distribution UNRELEASED\n"
                          "dpkg-buildpackage: source changed by Lukas "
                          "Puehringer <lukas.puehrin..."},
 "command": ["dpkg-buildpackage", "-us", "-uc"],
 "materials": {"...": "...",
               "/home/lukas/demo/grep-2.12/doc/version.texi": {"sha256": "5f969..."},
               "/home/lukas/demo/grep-2.12/gnulib-tests/test-exclude4.sh": {"sha256": "55979..."},
               "/home/lukas/demo/grep-2.12/gnulib-tests/test-quotearg-simple.c": {"sha256": "2e95c..."},
               "/home/lukas/demo/grep-2.12/lib/fd-safer.c": {"sha256": "ccd06..."},
               "/home/lukas/demo/grep-2.12/lib/strerror.c": {"sha256": "7cfff..."},
               "/home/lukas/demo/grep-2.12/lib/strings.in.h": {"sha256": "65bd7..."},
               "/home/lukas/demo/grep-2.12/m4/putenv.m4": {"sha256": "9e9c2..."},
               "/home/lukas/demo/grep-2.12/po/eo.gmo": {"sha256": "9304e..."},
               "/home/lukas/demo/grep-2.12/po/tr.po": {"sha256": "b05b9..."}},
 "name": "build",
 "products": {"...": "...",
              "/home/lukas/demo/grep-2.12/Makefile.in": {"sha256": "e913f..."},
              "/home/lukas/demo/grep-2.12/debian/grep/usr/share/locale/eo/LC_MESSAGES/grep.mo": {"sha256": "9304e..."},
              "/home/lukas/demo/grep-2.12/gnulib-tests/test-environ.c": {"sha256": "99f3b..."},
              "/home/lukas/demo/grep-2.12/gnulib-tests/test-exclude6.sh": {"sha256": "86e7f..."},
              "/home/lukas/demo/grep-2.12/gnulib-tests/test-localeconv.c": {"sha256": "cd744..."},
              "/home/lukas/demo/grep-2.12/lib/msvc-nothrow.c": {"sha256": "2f664..."},
              "/home/lukas/demo/grep-2.12/lib/xstriconv.h": {"sha256": "392ce..."},
              "/home/lukas/demo/grep-2.12/po/he.gmo": {"sha256": "fdfee..."},
              "/home/lukas/demo/grep-2.12/tests/file": {"sha256": "30dae..."}},
 "return_value": 0,
 "signatures": [{"keyid": "12c55e46654c682d3ffd3b63492adf422e6812eb1ac41574d083b9e770d1e4c2",
                 "method": "RSASSA-PSS",
                 "sig": "3877a06dee3f6e140e20d5100964adb38c1c63dd..."}]}
```


