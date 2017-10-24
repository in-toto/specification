#!/usr/bin/env python
import os
import json
import argparse
import glob
import random

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
