# Artifact Specification

## 1 Introduction

### 1.1 Scope

FIXME:

### 1.2 Motivation

FIXME: 
### 1.3 History and credit

September 26, 2019 -- This document is created

### 1.4 Context

FIXME:

## 2 Artifact format

FIXME: wthis will be massaged around.

In order to achieve the properties described in Section 1, link and layout
metadata must contain information that correctly depicts which operations are
intended, and that presents specifics of each operation within the supply
chain. In the following section, we describe which information is gathered and
how it is laid out within link and layout metadata.

### 2.1 Metaformat

To provide descriptive examples, we will adopt "canonical JSON," as described
in
[http://wiki.laptop.org/go/Canonical\_JSON](http://wiki.laptop.org/go/Canonical_JSON),
as the data format. However, applications that desire to implement in-toto are
not required to use JSON.  Discussion about the intended data format for
in-toto can be found in the in-toto website.

### 2.2 File formats: general principles

All signed files (i.e., link and layout files) have the format:

```json
{
  "signed" : "<ROLE>",
  "signatures" : [
      { "keyid" : "<KEYID>",
        "method" : "<METHOD>",
        "sig" : "<SIGNATURE>" }, 
  "..."
  ]
}
```

Where, ROLE is a dictionary whose "\_type" field describes the metadata type (as
described in sections 2.3 and 2.4). KEYID is the identifier of the key signing
the ROLE dictionary. METHOD is the key signing method used to generate the
signature. SIGNATURE is a signature of the canonical JSON form of ROLE.

The current reference implementation of in-toto defines three signing methods,
although in-toto is not restricted to any particular key signing method, key
type, or cryptographic library:

*   "RSASSA-PSS" : RSA Probabilistic signature scheme with [appendix](http://tools.ietf.org/html/rfc3447#page-29).
The underlying hash function is SHA256.
*   "ed25519" : Elliptic curve digital signature algorithm based on
    [Twisted Edwards curves](http://ed25519.cr.yp.to/).
*   "ecdsa" : [Elliptic curve digital signature algorithm](https://tools.ietf.org/html/rfc6979)

All keys have the format:

```json
  { "keytype" : "<KEYTYPE>",
    "keyval" : "<KEYVAL>" }
```

where KEYTYPE is a string describing the type of the key, and how it is used to
sign documents. The type determines the interpretation of KEYVAL.

We define two key types at present: 'rsa' and 'ed25519'.

The 'rsa' format is:

```json
  { "keytype" : "rsa",
    "keyval" : { "public" : "<PUBLIC>",
                 "private" : "<PRIVATE>" }
  }
```

where PUBLIC and PRIVATE are in PEM format and are strings.  All RSA keys must
be at least 2048 bits.

The elliptic-curve variants ('ed25519' and 'ecdsa') format are:

```json
  { "keytype" : "ed25519",
    "keyval" : { "public" : "<PUBLIC>",
                 "private" : "<PRIVATE>" }
  }
```

```json
  { "keytype" : "ecdsa",
    "keyval" : { "public" : "<PUBLIC>",
                 "private" : "<PRIVATE>" }
  }
```

where PUBLIC and PRIVATE are both 32-byte (256-bit) strings.

Link and Layout metadata does not include the private portion of the key
object:

```json
  { "keytype" : "rsa",
    "keyval" : { "public" : "<PUBLIC>"}
  }
```

The KEYID of a key is the hexadecimal encoding of the SHA-256 hash of the
canonical JSON form of the key, where the "private" object key is excluded.

Date-time data follows the ISO 8601 standard.  The expected format of the
combined date and time string is "YYYY-MM-DDTHH:MM:SSZ".  Time is always in
UTC, and the "Z" time zone designator is attached to indicate a zero UTC
offset.  An example date-time string is "1985-10-21T01:21:00Z".

#### 2.2.1 Hash object format

Hashes within in-toto are represented using a hash object. A hash object is a
dictionary that specifies one or more hashes, including the cryptographic hash
function. For example: `{ "sha256": HASH, ... }`, where HASH is the sha256 hash
encoded in hexadecimal notation.

### 2.3 File formats: layout

The layout file will be signed by a trusted key (e.g., one that was distributed
beforehand) and will indicate which keys are authorized for signing the link
metadata, as well as the required steps to perform in this supply chain.

The format of the layout file is as follows:

```json
{ "_type" : "layout",
  "expires" : "<EXPIRES>",
  "readme": "<README>",
  "keys" : {
     "<KEYID>" : "<PUBKEY_OBJECT>"
  },
  "steps" : [
    "<STEP>",
    "..."
  ],
  "inspections" : [
    "<INSPECTION>",
    "..."
  ]
}
```

EXPIRES determines when layout metadata should be considered expired and no
longer trusted by clients. Clients MUST NOT trust an expired file.

An optional README text can be added on the readme field. This is used to
provide a human-readable description of this supply chain.

The "keys" list will contain a list of all the public keys used in the steps
section, as they are described in 2.2.

The `"steps"` section will contain a list of restrictions for each step within
the supply chain. It is also possible to further define steps by means of
sublayouts, so that they can further specify requirements to a section of the
supply chain (section 2.4.1).  We will describe the contents of the steps list
in section 2.3.1.

The `"inspections"` section will contain a list of restrictions for each step
within the link. In contrast to steps, inspecting is done by the client upon
verification. We will elaborate on the specifics of this process in section
2.3.2.


#### 2.3.1 Steps

Steps performed by a functionary in the supply chain are declared as follows:

```json
{ "_name": "<NAME>",
  "threshold": "<THRESHOLD>",
  "expected_materials": [
     [ "<ARTIFACT_RULE>" ],
     "..."
  ],
  "expected_products": [
     [ "<ARTIFACT_RULE>" ],
     "..."
  ],
  "pubkeys": [
     "<KEYID>",
     "..."
  ],
  "expected_command": "<COMMAND>"
}
```

The `NAME` string will be used to identify this step within the supply chain.
NAME values are unique and so they MUST not repeat in different step
descriptions.

The `"threshold"` field must contain an integer file indicating how many pieces
of link metadata must be provided to verify this step. This field is intended
to be used for steps that require a higher degree of trust, so multiple
functionaries must perform the operation and report the same results. If only
one functionary is expected to perform the step, then the "threshold" field
should be set to 1.

The `"expected_materials"` and `"expected_products"` fields contain a list of
`ARTIFACT_RULES`, as they are described in section 2.3.3. These rules are used
to ensure that no materials or products were altered between steps.

The `"pubkeys"` field will contain a list of KEYIDs (as described in section
2.2) of the keys that can sign the link metadata that corresponds to this step.

Finally, the `"expected_command"` field contains a string, COMMAND, describing
the suggested command to run. It is important to mention that, in a case where
a functionary’s key is compromised, this field can easily be forged (e.g., by
changing the PATH environment variable in a host) and thus it should not be
trusted for security checks. In addition, commands may be executed with
different flags at the behest of the functionary's personal preference (e.g., a
developer may run a command with --color=full or not). Because of this, during
verification, clients should only show a warning if the expected command field
does not match its counterpart in the link metadata. This warning may help
auditors check whether something was out of the norm, but will not make
verification fail, as these changes are not necessarily a problem.

It is also possible to divide a subchain by having a third-party project owner
define a layout for a section of the supply chain. This can be done by means of
sublayouts (as described in section 2.5).

#### 2.3.2 Inspections

In contrast to steps, inspections indicate operations that need to be performed
on the final product at the time of verification.  For example, unpacking a tar
archive to inspect its contents is an inspection step. When indicating
inspections, ARTIFACT rules  can be defined to ensure the integrity of the
final product. For example, MATCH rules are usually found in inspections to
provide insight about artifacts that were created or modified inside the supply
chain.

An inspection contains the following fields.

```json
{ "_name": "<NAME>",
  "expected_materials": [
     [ "<ARTIFACT_RULE>" ],
     "..."
  ],
  "expected_products": [
     [ "<ARTIFACT_RULE>" ],
     "..."
  ],
  "run": "<COMMAND>"
}
```

Similar to steps, the `NAME` string will be used to identify this inspection
within the supply chain. NAME values are unique and so they MUST NOT repeat in
either steps or inspections.

The `"expected_materials"` and `"expected_products"` products fields behave in
the same way as they do for the steps as defined in section 2.3.1.

Finally, the `"run"` field contains the command to run. This field will be used
to spawn a new process in the verification system to create a new piece of link
metadata that correspond to the inspection steps. After running the indicated
command, the materials and products fields will be verified using the artifact
rules for materials and products.

##### 2.3.2.1 Inspection interface

Executables used during an inspection need to communicate the result of running
the command with in-toto. To do so, in-toto provides a simple inspection
interface using the executable's return value:

* If the return value is 0, then the inspection was successful. All the
  artifacts and the rest of the information is recorded using the in-toto-run
tool, in the same fashion as used to collect steps.
* If the result is greater than 0 and less than 127, then the inspection was
  not successful and validation should halt.

#### 2.3.3 Artifact Rules

Artifact rules are used to connect steps together through their materials or
products. When connecting steps together, in-toto allows the project owner to
enforce the existence of certain artifacts within a step (e.g., a "README.md" file can
only be created in the "create-documentation" step) and authorize operations on
artifacts (e.g., the "compile" step can use the materials from the "checkout-vcs" step).
The artifact rule format is the following:

```bash
    {MATCH <pattern> [IN <source-path-prefix>] WITH (MATERIALS|PRODUCTS) [IN <destination-path-prefix>] FROM <step> ||
    CREATE <pattern> ||
    DELETE <pattern> ||
    MODIFY <pattern> ||
    ALLOW <pattern> ||
    REQUIRE <pattern> ||
    DISALLOW <pattern>}
```

The `"pattern"` value is a path-pattern that will be matched against paths
reported in the link metadata, including bash-style wildcards (e.g.,  `"*"`). The
following rules can be specified for a step or inspection:

* **MATCH**: indicates that the artifacts filtered in using
  `"source-path-prefix/pattern"` must be matched to a `"MATERIAL"` or `"PRODUCT"` from a
destination step with the `"destination-path-prefix/pattern"` filter. For example,
`"MATCH foo WITH PRODUCTS FROM compilation"` indicates that the file `"foo"`, a
product of the step `"compilation"`, must correspond to either a material or a
product in this step (depending on where this artifact rule was listed).  More
complex uses of the MATCH rule are presented in the examples of section 5.3.

The `"IN <prefix>"` clauses are optional, and they are used to match products
and materials whose path differs from the one presented in the destination
step. This is the case for steps that relocate files as part of their tasks. For
example `"MATCH foo IN lib WITH PRODUCT IN build/lib FROM compilation"` will ensure
that the file `"lib/foo"` matches `"build/lib/foo"` from the compilation step.


* **ALLOW**: indicates that artifacts matched by the pattern are allowed as
  materials or products of this step.
* **DISALLOW**: indicates that artifacts matched by the pattern are not allowed
  as materials or products of this step.
* **REQUIRE**: indicates that a pattern must appear as a material or product of
  this step.
* **CREATE**: indicates that products matched by the pattern must not appear as
  materials of this step.
* **DELETE**: indicates that materials matched by the pattern must not appear
  as products of this step.
* **MODIFY**: indicates that products matched by this pattern must appear as
  materials of this step, and their hashes must not by the same.


##### 2.3.3.1 Rule processing

Artifact rules reside in the `"expected_products"` and `"expected_materials"`
fields of a step and are applied sequentially on a queue of `"materials"` or
`"products"` from the step's corresponding link metadata. They operate in a
similar fashion as firewall rules do. This means if an artifact is successfully
consumed by a rule, it is removed from the queue and cannot be consumed by
subsequent rules. There is an implicit `"ALLOW *"` at the end of each rule
list. By explicitly specifying `"DISALLOW *"`, in-toto verification fails if an
artifact was not consumed by an earlier rule. Here, we describe an algorithm to
illustrate the behavior of the rules being applied:

```python
VERIFY_EXPECTED_ARTIFACTS(rule_set, link, target_links)

# load the artifacts from the link
artifacts = load_artifacts_as_queue(link)

# iterate over all the rules
for rule in rules:
  consumed_artifacts, rule_error = apply_rule(rule, artifacts)

  if rule_error:
    return ERROR("Rule failed to verify!")

  artifacts -= consumed_artifacts

return SUCCESS
```


##### 2.3.3.2 MATCH rule behavior

The match rule is used to tie different steps together, by means of their
materials and products. The main rationale behind the match rule is to identify
the origins of artifacts as they are passed around in the supply chain. In this
sense, the match rule will be used to identify which step should be providing a
material used in a step, as well as force products to match with products of
previous steps.

In order to ensure the correctness of the match rule, it is important to
describe the way it operates. To avoid any ambiguities, this will be done with
the following pseudocode:

```python
MATCH(source_materials_or_products_set, destination_materials_or_products_set,
  rule)

# Filter source and destination materials using the rule’s patterns
source_artifacts_filtered = filter(rule.source_prefix + rule.source_pattern,
                                   source_materials_or_products_set)

destination_artifacts_filtered = \
    filter(rule.destination_prefix + rule.destination_pattern,
             destination_materials_or_products_set)

# Apply the IN clauses, to the paths, if any
for artifact in source_artifacts_filtered:
  artifact.path -= rule.source_in_clause
for artifact in destination_artifacts_filtered:
  artifact.path -= rule.destination_in_clause

# Create an empty list for consumed artifacts
consumed_artifacts = []

# compare both sets
for artifact in source_artifacts_filtered:
  destination_artifact = find_artifact_by_path(destination_artifacts,
                                                artifact.path)
  # the artifact with this path does not exist?
  if destination_artifact == NULL:
    continue

  # are the files not the same?
  if destination_artifact.hash != artifact.hash:
    continue

  # Only if source and destination artifact match, will we mark it as consumed
  add_to_consumed_artifacts(artifact)

# Return consumed artifacts to modify the queue for further rule processing
return consumed_artifacts
```


##### 2.3.3.3 DISALLOW rule behavior

The disallow rule is the only rule that can error out of rule processing. If a
disallow rule pattern finds any remaining files in the artifact queue it means
that no prior rule has successfully consumed those artifacts, i.e. the
artifacts were not authorized by any rule.

```python
DISALLOW(rule, artifacts)

artifacts = filter(rule.pattern, artifacts)

if artifacts
  return ERROR

return SUCCESS
```

### 2.4 File formats: `[name].[KEYID-PREFIX].link`


The `[name].[KEYID-PREFIX].link` file will contain the information recorded
from the execution of a supply chain step. It lists relevant information, such
as the command executed, the materials used, and the changes made to such
materials (products), as well as other host information.


The name for link metadata files must contain two elements: the name of the
step, and the first six bytes of the functionary’s keyid separated by a dot.
The `KEYID` portion of the name is used to avoid collisions in steps that have
thresholds higher than one.


The format of the `[name].[KEYID-PREFIX].link` file is as follows:

```json
{ "_type" : "link",
  "_name" :  "<NAME>",
  "command" : "<COMMAND>",
  "materials": {
     "<PATH>": "<HASH>",
     "..." : "..."
  },
  "products": {
     "<PATH>": "<HASH>",
     "..." : "..."
  },
  "byproducts": {
    "stdin": "",
    "stdout": "",
    "return-value": ""
  },
  "environment": {
    "variables": "<ENV>",
    "filesystem": "<FS>",
    "workdir": "<CWD>"
  }
}
```

To identify to which step a piece of link metadata belongs, the `NAME` field must
be set to the same identifier as the step described in the layout, as specified
in section 2.3.1.

The `COMMAND` field contains the command and its arguments as executed by the
functionary.


The `"materials"` and `"products"` fields are dictionaries keyed by a file’s
`PATH`. Each `HASH` value is a hash object as described in section 2.2.1.

The `"byproducts"` field is an opaque dictionary that contains additional
information about the step performed. Byproducts are not verified by in-toto’s
default verification routine. However, the information gathered can be used for
further scrutiny during an inspection step. At a minimum, the byproducts
dictionary should have standard output (stdout), standard input (stdin) and
return value (return-value), even if no values are filled in.

Finally, the environment dictionary contains information about the environment
in which the step was carried out. Although the environment dictionary is an
opaque field, it should at least contain the `"variables"`, `"filesystem"`, and
`"workdir"` keys, even if no values are filled in for them. 

#### 2.4.1 Environment Information

The format of the environment information is not mandated by the in-toto
specification, but we recommend to store the following:

* **variables**: a list of environment variables set in the host system.
* **filesystem**: a list of filepath/hash values of the relevant files in the
  filesystem. Another alternative could be to store an MTREE of the relevant
directories. A third alternative would be to use the hashes of the relevant
filesystem layers.
* **workdir**: the path of the current working directory.

These values can be used to detect mistakes during compilation or invalid hosts
carrying out steps.

The following is a depiction of the previous recommendation:

```json
{ "environment": {
    "variables": [
      "LANG=en_US.UTF-8",
      "USER=santiago",
      "PWD=/home/santiago",
      "HOME=/home/santiago",
      "SHELL=/bin/bash",
      "PATH=/home/santiago/bin:/home/santiago/bin:/usr/local/sbin"
    ],
    "filesystem": [" ",
      " #           user: (null)", 
      " #        machine: LykOS",
      " #           tree: /home/santiago/Documents/personal/programas/in-toto/docs",
      " #           date: Thu Jul 27 16:02:58 2017",
      " ",
      " ",
      " # .",
      " /set type=file uid=1000 gid=1000 mode=0644 nlink=1 flags=none",
      " .               type=dir mode=0755 nlink=3 size=4096 \\",
      "                 time=1495734432.214631931",
      "     LICENSE     size=1086 time=1495734432.214631931",
      "     README.md   size=50 time=1495734432.214631931",
      "     in-toto-spec.pdf \\",
      "                 size=220978 time=1495734432.217965320",
      " .."],
      "workdir": "/home/santiago/Documents/personal/programas/in-toto/docs"
  }
}
``` 
 
 The previous example contains a list of environment variables as printed out
by the env command, a list of files as printed out by the mtree -c command and,
finally, the output of the pwd command. This information can be used to infer
information about the current execution environment. Operating systems and
containerization solutions could use tools to record and store information
relevant to their toolchain (e.g., dpkg-query list for debian, or information
about the docker layers in the manifest).

### 2.5 Specifying sublayouts

It is possible that a project owner cannot define all the steps at the
appropriate level of detail. Such a case might occur with a software project
that statically compiles a third-party library or when a vendor is packaging
software that is written upstream. When this is the case, additional layouts
can be used to describe parts of the supply chain with more granularity. We
call these additional layouts sublayouts.

To create a sublayout, a series of steps are declared, and thus the functionary
will take the role of a third party project owner. Sublayouts are saved with
the `[name].[keyid-prefix].link` format, and they will have the same format
described for a layout file described in section 2.3 instead of the usual
contents of a link metadata file.

For example, consider a project in which the build step is not completely clear
for the project owner (Alice). However, Alice trusts Bob to perform this
operation. Bob, in turn, trusts additional functionaries to perform
build-related operations. Because of this, Bob will create a sublayout of the
build step by creating a layout file. This newly-created layout file will
contain further steps, keyids and artifact rules within the steps.  The
signature of this new layout file must match the one the top-level project
owner intended for this step (in this case, Bob's).

#### 2.5.1 Artifact rules in sublayouts

When using sublayouts, the artifact rules that apply to the equivalent step are
applied to the materials of the first step in the sublayout and the products of
the last step of the sublayout. This is, for the upper-layer layout, the
materials and products presented for matching will be derived from the
materials of the first step and the products of the last step.

In the context of our example above, Alice's layout will define the artifact
rules that apply to the build step. When Alice's layout is verified, the
verification algorithm will recurse into Bob's layout, perform verification and
present a "virtual" piece of link metadata that can be used to verify Alice's
layout. The materials of this virtual piece of link metadata will be those of
the first step on Bob's sublayout, and the products will be those on the last
step of Bob's sublayout.


#### 2.5.2 Namespacing link metadata

Link metadata that pertains to a sublayout must be placed in a filesystem
directory for such layout. The name of the directory will have the same
format as the link metadata filename without the .link metadata suffix. This is
necessary to avoid clashes between step names on layouts and sublayouts, as the
creator of a layout may not be aware of the names used by the creators of
sublayouts.

In our example above, the layout file would be stored under the name
`build.BOBS-KEYID-PREFIX.link`, and the corresponding pieces of link metadata
will be stored in a directory named `build.BOBS-KEYID-PREFIX`.

#### 2.5.3 Inspections on sublayouts

Inspections in sublayouts can be verified in two ways:

* A piece of signed link metadata is presented for the inspection. The key to
  sign for this piece of link metadata must be the same key used to sign the
sublayout file.
* If the piece of link metadata is not present, the client must perform that
  inspection upon validation. When this is the case, the inspection must be run
while validating the sublayout. This means when the verification algorithm
recurses inside the sublayout.

If inspections are to be run during verification, its materials and products
are not presented to the upper layer layout. This is because it is highly
unlikely the results of the inspections are to be used by the upper-layer
layout.
