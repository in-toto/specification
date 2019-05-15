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

MAIN_TEMPLATE = """{title}
======
{description}

## Layout
{layout_str}
## Links
{links_str}
"""

METADATA_TEMPLATE = """
### {title}
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


def beautify_layout(layout):
  """Beautify in-toto layout with layout-specific dict field ordering. """
  return beautify(layout, dict_key_order_lists=[
      ["signed", "signatures"],
      ["_type", "readme", "expires", "steps", "inspect", "keys"],
      ["keyid", "keytype", "keyval"],
      ["_type", "name", "expected_command", "pubkeys", "threshold",
       "expected_materials", "expected_products"],
      ["_type", "name", "run", "expected_materials", "expected_products"]])


def beautify_link(link):
  """Beautify in-toto link with link-specific dict field ordering. """
  return beautify(link, dict_key_order_lists=[
      ["signed", "signatures"],
      ["_type", "name", "command",  "materials", "products", "byproducts",
      "environment"],
      ["return_value", "stdout", "stderr"]])


def load_metadata(path):
  with open(path) as fp:
    metadata = json.load(fp)
  return metadata


def create_markdown_summary(folder):
  """ From passed folder load 'root.layout' and '*.link' files corresponding
  to the steps defined in the layout and create a markdown-formatted
  summary in the current working directory.

  """
  project_name = os.path.basename(os.path.normpath(folder))

  layout_name = "root.layout"
  layout_path = os.path.join(folder, layout_name)
  layout_title = os.path.join(project_name, layout_name)
  layout = load_metadata(layout_path)

  layout_str = METADATA_TEMPLATE.format(
      title=layout_title,
      metadata=json.dumps(beautify_layout(layout), indent=2))

  links_str = ""
  for step in layout["signed"]["steps"]:
    link_paths = glob.glob(os.path.join(folder,
        "{}.*.link".format(step["name"])))

    for link_path in link_paths:
      link_name = os.path.basename(link_path)
      link_title = os.path.join(project_name, link_name)
      link = load_metadata(link_path)
      links_str += METADATA_TEMPLATE.format(
          title=link_title,
          metadata=json.dumps(beautify_link(link), indent=2))

  description = layout["signed"]["readme"] or \
      "*There is no readme for this layout*"

  result = MAIN_TEMPLATE.format(
      title=project_name,
      description=description,
      layout_str=layout_str,
      links_str=links_str)

  output_filename = "{}.md".format(project_name)
  with open(output_filename, "w") as fp:
    fp.write(result)


def main():
  parser = argparse.ArgumentParser(
      description="Generate Markdown-formatted summary from in-toto software "
      " supply chain layout and link metadata.")

  # Whitespace padding to align with program name
  parser.usage = "%(prog)s  --example-folder <folder>"
  in_toto_args = parser.add_argument_group("example-settings")
  in_toto_args.add_argument("-f", "--example-folder", type=str, required=True,
      help="The folder where a metadata group is located. The layout name "
      "is expected to be 'root.layout'. The passed folder name is used as "
      "title and to write a '<name>.md' to cwd.")

  args = parser.parse_args()
  create_markdown_summary(args.example_folder)

# TODO: we could cleverly recurse and show the inherittance, but do we really
# want to?
if __name__ == "__main__":
  main()
