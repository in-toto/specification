# Docs
This repostiory contains the specification and other related documents.

- You can read the current version of the specification [here](https://github.com/in-toto/docs/blob/master/in-toto-spec.md).
- The latest stable version (1.0) is [here](https://github.com/in-toto/docs/blob/v1.0/in-toto-spec.md).

## Release Cadence
Note that the specification is released whenever there is a change deemed important enough by a majority of [the ITSC](https://github.com/in-toto/community/blob/main/GOVERNANCE.md#the-in-toto-steering-committee-itsc).   As this is a specification, it is not expected to change frequently, hence many months will regularly pass before a new release is provided.   See the [ITE repository](https://github.com/in-toto/ITE) for information about how to propose changes to the specification and get more immediate feedback.

## Support For Old Releases
The specification is a living document and as such is expected to improve over time.  The expectation is that changes will improve the security and usability over in-toto implementations and thus will be desirable for implementers to adopt.   However, the community will also happily answer questions about implementations that match older versions of the specification.   In particular, we expect changes around why a specific change was made to occur whenever a non-trivial alteration is performed.   Feel free to ask on our slack channel or in a commnuity call!

Given the slow rate of change of the specification and the incremental nature of those changes, we do not have any cutoff for which versions of the specification we will answer questions about.   We reserve the right to change this in the future.

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
  creating an in-toto layout.

## Other informative repositories

Along with this Docs repository, the in-toto enhancements
([ITE](https://github.com/in-toto/ITE)) repository contains information about
features, recommendations and other extensions that are not part of the core
specification
