# ROADMAP review (End of December '20)

We've reached the end of the first evaluation period for our 2021 roadmap, and
we are due a review of our activities. Here's a rundown of what has happened in
the scope of the in-toto project's
[ROADMAP](https://github.com/in-toto/docs/blob/master/ROADMAP.md) for this year.

## ITEs

We have had some activity on the in-toto Enhancement (ITE) front. As described
in our ROADMAP, we planned to streamline the development of overlapping parts
of the in-toto and TUF specifications. We observed that the two specifications
primarily overlapped in their descriptions of the metadata document format or
signature wrapper.

This signature wrapper was originally described in the TUF specification as a
lightweight and minimal format for software delivery and software supply chain
metadata. The in-toto project used the same wrapper to maintain consistency. The
in-toto and TUF core teams decided to break this out into a separate
specification that both projects could point to and use. This also enables
adopters of either projects to use the same wrapper for any custom metadata they
may generate.

Mark Lodato (@MarkLodato) of the Binary Authorization team at Google described a
modification of this specification and it now lives
[here](https://github.com/secure-systems-lab/signing-spec/blob/master/specification.md).
Santiago Torres-Arias (@santiagotorres) sponsored ITE-5 which proposes replacing
the current in-toto signature wrapper with the new signing specification.

Mark Lodato and his team also proposed ITE-6 which describes a generalized link
format.

TODO describe ITE-6 @Santiago

- [ITE-5: Replace signature wrapper with SSL signing spec](https://github.com/in-toto/ITE/pull/13)
- [ITE-6: Generalized link format](https://github.com/in-toto/ITE/pull/15)

## Further maturing of implementations and integrations

Several in-toto implementations and subprojects maintained by the core team saw
some activity during this evaluation period.

### in-toto-python

Most notably, we released version 1.0 of our
[primary reference implementation](https://github.com/in-toto/in-toto) written
in Python. All in-toto implementations, and indeed the specification, use
semantic versioning. This release comes with the typical stability guarantees
expected of 1.0 releases. The reference implementation has a roadmap that
details its developments, and its latest roadmap review can be found
[here](https://github.com/in-toto/in-toto/blob/develop/roadmap-reviews/2021/review_1_december_20.md).

### in-toto-golang

We released the first tagged version of in-toto-golang, making it easier for our
adopters to pin and use the package. We are also using this release to evaluate
the stability of in-toto-golang for a potential 1.0 release. You can find
in-toto-golang v0.1.0
[here](https://github.com/in-toto/in-toto-golang/releases/tag/v0.1.0).

Note: in-toto-golang v0.1.0 was released in mid January 2021, but we decided to
include it in the review for this evaluation period to get the word out, rather
than wait several months.

TODO (LP): Mention any work that has happened since the last review.

TODO (LP): Mention 0.1.0 release -> request from adopters? SPIFFE??

### totoify-grafeas

[The totoify-grafeas project](https://github.com/in-toto/totoify-grafeas) once
served as a conduit between the in-toto and Grafeas projects. However, the
Grafeas project has moved on from that time period, and today in-toto is
recognized within Grafeas as a metadata type. We have repurposed this project to
simplify the process of generating in-toto metadata in the Grafeas format, and
pushing this metadata to Grafeas servers. Kristel Fung (@kristelfung)
[worked](https://github.com/in-toto/totoify-grafeas/pull/3) to bring this
translation layer to life.

### kubesec integration

TODO: Kristel's work here

### Arch Linux rebuilder

The in-toto team operates an instance of
[rebuilderd](https://github.com/kpcyrd/rebuilderd) which rebuilds Arch Linux
packages. This project received more attention, and the underlying
infrastructure was beefed up. We hope to obtain meaningful metrics from this
instance which can help the Arch Linux team in their Reproducible Builds-related
efforts. As noted in a previous report, in-toto is also in the process of being
adopted by rebuilderd, and the maintainer, kpcyrd, worked on integrating the
[pull request](https://github.com/kpcyrd/rebuilderd/pull/22) into the project.

### in-toto apt transport
The client-side counterpart of the rebuilders has also seen a recent uptake in
activity. That is, we have added finishing touches to an [initial downstream
release](https://github.com/in-toto/apt-transport-in-toto/pull/26) of our
in-toto-powered, reproducibility-checking [apt
transport](https://github.com/in-toto/apt-transport-in-toto), which we hope to
make available in [Debian Bullseye](https://wiki.debian.org/DebianBullseye).
Big thanks go to Frédéric Pierret (@fepitre) from the @QubesOS core team and
Holger Levsen (@h01ger) from the Reproducible Builds core team for their help.


### Layout Creation Tool

TODO (LP): Mention Yuanrui's and Isha's work on layout creation tooling, update of layout webtool

## Closing Remarks

This is it for this evaluation period. As always, we are very excited to make
meaningful changes while working with Academia, Open Source communities, and the
industry. We are very pleased that the in-toto umbrella encompasses more than
just the core in-toto specification and implementations, and we are happy with
our impact on software supply chain security.
