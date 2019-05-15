#!/usr/bin/env python
"""
<Program Name>
  metadata.py

<Author>
  Santiago Torres <santiago@nyu.edu>
  Lukas Puehringer <lukas.puehringer@nyu.edu>

<Started>
  Oct 24, 2017

<Copyright>
  See LICENSE for licensing information.

<Purpose>
  Generate Markdown-formatted summary from in-toto software supply chain layout
  and link metadata. Metadata fields are ordered and long strings are
  truncated for readability.

"""
import os
import json
import argparse
import glob
import random
import six
from collections import OrderedDict
from pprint import pformat

MAIN_TEMPLATE = """{name}
=======

{description}

# Layout metadata
## {layout_filename}
```json
{layout_metadata}
```

# Link metadata
{link_template}
"""

LINK_TEMPLATE = """
## {name}.link
``` json
{metadata}
```

"""

def beautify(obj, max_str_len=70, max_list_len=10, max_dict_len=10,
    dict_key_order_lists=None):
  """Beautify the passed object, truncating long strings, lists
  and dictionaries, and printing dictionary keys in the order passed by
  `dict_key_orders`.

  Truncation:
    - the last 3 characters of a truncated string are replaced with ellipsis
    - the last item of a truncated list is replaced with ellipsis
    - a dict is transformed to an OrderedDict and the last key and value are
      each replaced with ellipsis

  Dict ordering:
    Dict keys on any level of the passed obj are compared with all lists in
    the passed `dict_key_order_lists`. If there is a match the passed order
    is used. Note that the keys of a truncated dict without the ellipsis
    key is used for comparison.

  """
  if max_str_len < 3:
    raise ValueError("'max_str_len' must be >= 3, got: " + str(max_str_len))

  if max_list_len < 1:
    raise ValueError("'max_list_len' must be >= 1, got: " + str(max_list_len))

  if max_dict_len < 1:
    raise ValueError("'max_dict_len' must be >= 1, got: " + str(max_dict_len))

  return _beautify(obj, max_str_len=max_str_len, max_list_len=max_list_len,
      max_dict_len=max_dict_len, dict_key_order_lists=dict_key_order_lists)


def _beautify(obj, **kw):
  """Recurisve helper for beautify. See beautify for more info. """

  # Truncate strings
  if isinstance(obj, six.string_types):
    if len(obj) > kw["max_str_len"]:
      obj = obj[:kw["max_str_len"] - 3] + "..."

  # Truncate list and recurse into _beautify for each  item
  elif isinstance(obj, list):
    if len(obj) > kw["max_list_len"]:
      obj = obj[:kw["max_list_len"] - 1] + ["..."]

    tmp_obj = []
    for item in obj:
      tmp_obj.append(_beautify(item, **kw))
    obj = tmp_obj

  # Truncate dict and recurse into _beautify for each item
  elif isinstance(obj, dict):
    dict_keys = list(obj.keys())

    # If the keys of this dict is the same set as any of the passed
    # ordered key lists, we use that order below
    for key_order in kw["dict_key_order_lists"]:
      if set(dict_keys) == set(key_order):
        dict_keys = key_order
        break

    truncate = len(dict_keys) > kw["max_dict_len"]
    if truncate:
      dict_keys = dict_keys[:kw["max_dict_len"] - 1]

    # An ordered dict is required for both, ordering the dict keys and also
    # to add a terminal ellipsis pair in case of truncation
    tmp_obj = OrderedDict()
    for key in dict_keys:
      tmp_obj[key] = _beautify(obj[key], **kw)

    if truncate:
      tmp_obj["..."] = "..."

    obj = tmp_obj

  return obj


def load_layout_metadata(folder):
  return _load_metadata(folder, 'root.layout')

def load_link_metadata(folder, name, keyid):
  return _load_metadata(folder, "{}.{}.link".format(name, keyid))

def populate_link_template(folder):

  links = glob.glob(os.path.join(folder, "*.link"))

  resulting_template = ""

  for link in links:
    name, keyid, _ = link.split(".")
    metadata = load_link_metadata(folder, name.split(os.path.sep)[1], keyid)

    if len(metadata['products']) > 10:
      new_list = random.sample(metadata['products'].keys(), 9)
      product_subset = {x: metadata['products'][x] for x in new_list}
      metadata['products'] = product_subset

    for product in metadata['products']:
      metadata['products'][product]['sha256'] =  metadata['products'][product]['sha256'][:5] + "..."
    metadata['products']['...'] = "..." 

    if len(metadata['materials']) > 10:

      new_list = random.sample(metadata['materials'].keys(), 9)
      material_subset = {x: metadata['materials'][x] for x in new_list}
      metadata['materials'] = material_subset
    for material in metadata['materials']:
      metadata['materials'][material]['sha256'] =  metadata['materials'][material]['sha256'][:5] + "..."
    metadata['materials']['...'] = "..." 

    for byproduct in metadata['byproducts']:
      if len(metadata['byproducts'][byproduct]) > 200:
        metadata['byproducts'][byproduct] = metadata['byproducts'][byproduct][:200] + "..."
      metadata['byproducts'][byproduct] = metadata['byproducts'][byproduct].replace("'", "’")

    for signature in metadata['signatures']:
      signature['sig'] = signature['sig'][:40] + "..."

    if not metadata['return_value']:
      metadata['return_value'] = 0

    resulting_template += LINK_TEMPLATE.format(name=name, 
        metadata=pformat(metadata).replace("'", '"'))

  return resulting_template

def populate_template(folder):

  layout = load_layout_metadata(folder)
  link_template = populate_link_template(folder)

  description = "There is no readme for this layout"
  name = "{name}root.layout".format(name=folder)

  if 'readme' in layout:
    description = layout['readme']
    del layout['readme']

  layout["signatures"] = ["..."]
  for keyid in layout['keys']:
    layout['keys'][keyid]['keyid'] = "..."
    layout['keys'][keyid]['keyval']['public'] = "..."

  result = MAIN_TEMPLATE.format(name=folder, description=description,
      layout_filename=name, layout_metadata=pformat(layout).replace("'", '"'),
      link_template=link_template)

  output_filename = "{}.md".format(folder.strip(os.path.sep))
  with open(output_filename, "w") as fp:
    fp.write(result)

def main():

  parser = argparse.ArgumentParser(
        description="Compiles a series of metadata located in the target"
        "folder")
  # Whitespace padding to align with program name
  lpad = (len(parser.prog) + 1) * " "
  parser.usage = ("\n"
      "%(prog)s  --example-folder <folder>\n{0}".format(lpad))
  in_toto_args = parser.add_argument_group("example-settings")
  in_toto_args.add_argument("-f", "--example-folder", type=str, required=True,
    help="The folder where a metadata group is located")

  args = parser.parse_args()
  populate_template(args.example_folder)

def _load_metadata(folder, metadata_filename):

  metadata_path = os.path.join(folder, metadata_filename)
  with open(metadata_path) as fp:
    metadata = json.load(fp)

  return metadata 

# TODO: we could cleverly recurse and show the inherittance, but do we really
# want to?
if __name__ == "__main__":
  main()
