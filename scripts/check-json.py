#!/usr/bin/env python3

import json

def find_json_snippets(data):

    # we can obtain all the jsons with a couple of 
    # calls to split. This is easier than doing a stack-based
    # naive syntax processor
    data = data.split("```json")

    result = []
    for chunk in data[1:]:
        result.append(chunk.split("```")[0])

    # here, result holds only jsons.
    return result

def _annotate_error(exception, data, snippet):

    # we assume the snippet exists. I can't think of a way this wouldn't
    # happen
    index = data.index(snippet)

    lineno = data[:index].count("\n")
    return ("A decode error ({}) was found around line {}"
            "").format(exception.msg, lineno + exception.lineno)

def verify_inline_json(filename="in-toto-spec.md"):

    # notice I don't do any buffering here, so don't use any crazy-sized
    # markdown files. (we could probably validate this size if so desired...)
    with open(filename) as fp:
        data = fp.read()

    snippets = find_json_snippets(data)

    # we will iterate over the snippets now and see if we succeed
    for snippet in snippets:
        try:
            json.loads(snippet)
        except Exception as e:
            print(_annotate_error(e, data, snippet))
            continue

if __name__ == "__main__":
    verify_inline_json()
