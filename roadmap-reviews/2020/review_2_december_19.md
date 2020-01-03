# ROADMAP review (End of August '19)

We've reached the end of the first evaluation period for our 2020 roadmap, and
we are due a review of our activities. Here's a rundown of what has happened in
the scope of the in-toto project's
[ROADMAP](https://github.com/in-toto/docs/blob/master/ROADMAP.md) for this
year.

## ITE

- talk about ITE 4

The TUF and in-toto ITE's had very little activity, as we've been working on
other fronts lately. 
- [ITE-2: Using TUF and in-toto to build compromise-resilient CI/CD](https://github.com/in-toto/ITE/pull/4)
- [ITE-3: Real-world example of combining TUF and in-toto for packaging Datadog Agent integrations](
https://github.com/in-toto/ITE/pull/5)

In addition, and as further evidence of our committment to integrating with
SPDX, we have a new ITE to add to the family: 

- [ITE-4: Add generic URI schemes for artifacts in in-toto metadata ](https://github.com/in-toto/ITE/pull/6)

This ITE will allow in-toto to not only refer to artifacts as files, but rather
as more rich elements, such as (you guessed right) SPDX elements, or CI actions
(like GitHub's) and more!

## Maturing of existing sub-projects

### Jenkins

We have had very little activity on the Jenkins plugin side, mostly because the
reduce featureset has had very little to update and/or fix. However, we are
brewing support for [Grafeas](https://github.com/grafeas/grafeas) as a
transport. This way, the in-toto Jenkins plugin will be able to store in-toto
link metadata in a Grafeas server seamlessly. More to come on this front!

### Kubernetes components

As part of our work with the Grafeas adoption, we have had the chance to
evaluate a user story of the in-toto admission controller that uses Grafeas to
store link metadata (and possibly query other metadata as part of its
verification process). Although only sketches have come out so far, we are very
excited to show this to everybody once things come to fruition.

### GPG support

We started using securesystemlib's version of the gpg module. In addition, as
one of our industry partners requested, we gave the module support for
[ed25519](https://github.com/secure-systems-lab/securesystemslib/pull/188) keys
and signatures. As a result, everybody can benefit from a more feature-rich gpg
submodule.

### Apt transport and rebuilders

The apt transport and rebuilder saw a lot of work from Senior and Junior
members of the team. The work was divided on three fronts.

- Kristel Fung (@kristelfung) joined the team in a more-permanent fashion, and
  continued her work on making the rebuilder monitor more robust and to use the
  newer interface for buildinfos. We have continuously tested these changes on
  the rebuilder we host here at NYU.
- On the second front, Lukas took the hard task of starting to package the
  debian apt-transport into the Debian repositories. This way, setting up
  in-toto for your debian machines will be very simple and provide a high
  assurance case of package reproducibility.

### Kubesec integration

We managed to work with the amazing team at ControlPlane, in order to provide
the ability of signing your [kubesec scans using
in-toto](https://github.com/controlplaneio/kubesec/pull/75). We believe this is
a great step forward not only to improve the security of the scanner ecosystem
(by effectively generating signed http exchanges), but to set a precedent for
other scanner services that may want to integrate in-toto --- the total diff
was around 50 lines.

## Closing remarks.

This is it for this evaluation period. This period has mostly been centered
around showing people how to use in-toto in their ecosystem. As such, we've
moved greatly in the direction of a broader industry adoption. We believe that,
before the closing ROADMAP review, we'll have many surprises to share regarding
adoption, user stories and more.
