# Docs
Specification and other related documents.

- You can read the current version of the specification [here](https://github.com/in-toto/docs/blob/master/in-toto-spec.md).
- The latest stable version (0.9) is [here](https://github.com/in-toto/docs/blob/v0.9/in-toto-spec.md).

## Generating PDF

### Requirements
1. [git](https://git-scm.com/ "git")
2. [Pandoc with LaTex, must include enumitem](https://pandoc.org/ "Pandoc")
3. [GNU Make](https://www.gnu.org/software/make/ "GNU Make")

The documentation can be generated into a printable PDF by compiling the
markdown file.

```bash
make pdf
```

## Examples and Demos

There are a couple of repositories within this organization that you can use to
play around and better understand in-toto. Here's a list of them along with a
brief description.

- [demo](https://github.com/in-toto/demo): This is a very basic dummy supply
  chain example to help you understand the in-toto python toolchain. We
  recommend getting started here.
- [kubectl-in-toto](https://github.com/in-toto/kubectl-in-toto): Inside of this
  repository, you will find a demo to test a kubectl in-toto plugin to scan
  containers in your kubernetes deployment against in-toto metadata.
- [demo OpenSUSE](https://github.com/in-toto/demo-opensuse): This repository
  uses the OpenSUSE build toolchain to exemplify how in-toto could be
  integrated inside of OpenSUSE-based distros.
- [totoify-grafeas](https://github.com/in-toto/totoify-grafeas): This repository
  provides an interface that converts standard in-toto links into Grafeas
  occurrences, and back for use in an in-toto verification workflow.
- [layout-web-tool](https://github.com/in-toto/layout-web-tool): The
  layout-web-tool is a simple Flask-based web app that walks users through
  creating an in-toto layout. This tool is
  [hosted](https://in-toto.engineering.nyu.edu/) for interested project owners
  to try out.


## Other informative repositories

Along with this Docs repository, the in-toto enhancements
([ITE](https://github.com/in-toto/ITE)) repository contains information about
features, recommendations and other extensions that are not part of the core
specification
