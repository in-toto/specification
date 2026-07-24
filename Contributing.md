This website is maintained by the in-toto steering committee and is modeled after the [Kubernetes documentation contribution workflow](https://kubernetes.io/docs/contribute/).

in-toto documentation contributors:
- Improve existing content
- Create new content
- Translate the documentation
- Manage and publish the documentation parts of the in-toto release cycle

## Getting started

Anyone can open an issue about documentation, or contribute a change with a pull request (PR) to the respective repo.

There are different workflows for changing documentation in in-toto depending on the level of change
that is being made.  

The first type of change is that which is confined to a few lines and which is likely to be
uncontentious.  This is something like a typo fix or a minor clarification.  For example, if you see a sentence
like: "A signed attestation is created by a functionary as it performs a software supply chain step.  This
may be later consumed by a party who verifies a layout."  What "This" refers to in the second sentence may have 
confused you and you may wish to clarify it.  For non-specification changes, simply submit a PR of the 
"typo / minor clarification" type to address this issue.  If you wish to make a change to the specification, 
see the directions below.

The second type of change is more substantial.  This is something like adding a translation of documentation
to a new language, adding a tutorial, reorganizing the pages to have a different flow, etc.  For these, please 
ask on the in-toto documentation slack channel before starting this process.  (The main exception to this is
the [friends](https://github.com/in-toto/friends) repository where adoptions are tracked.  Feel free to create
a PR here directly without talking with us.)  There should be an issue created
on the issue tracker and an ITSC member should thumbs-up this before you begin.  If your documentation is for a
specific sub-project or repository, the approval of a maintainer is perfectly fine instead.  The rationale is 
that we want someone to both help to confirm the documentation is likely to be of use, and also identify a likely
shepherd of the work.  (Note that if you are a maintainer or ITSC member, it is fine to self approve.)

For a change to the specification, it is important to ask first.  So, please start by asking on the in-toto
slack channel.  Depending on the type or scope of this change, it may be as simple as a typo / minor clarification
fix below or it may require a separate process (such as an [ITE](https://github.com/in-toto/ITE)).  For a non-trivial 
change, this process has extra steps and cannot be approved by a single party.  The [specification](https://github.com/in-toto/docs) 
intentionally is a very stable, slow-moving document and so changes to it are conservative in nature.

## Actually Making a Change

You need to be comfortable with [git](https://git-scm.com/) and [GitHub](https://skills.github.com/) to work effectively in our community.

To get involved with documentation:

1.	Sign the CNCF [Contributor License Agreement](https://github.com/kubernetes/community/blob/master/CLA.md).
2.	Familiarize yourself with the documentation repository and the website's static site generator.   If the
    individual repository has guidance for documentation, it supercedes this document's guidance.
3.	Make sure you understand the basic processes for opening a PR. The [Kubernetes documentation on opening a 
 pull request](https://kubernetes.io/docs/contribute/new-content/open-a-pr/) is quite detailed and a good place
 to start if you need guidance.

As was stated above, for trivial, non-specification changes, create a PR directly.  For other changes, you will
need to discuss this with other folks and create an issue.

Do not make edits that cause large diffs, which are not relevant to content.  For example, do not re-wrap lines 
after making a change.  Do not add or delete blank linkes in a document unless there is a clear reason to do so.
Do not add or remove trailing whitespace on lines for a similar reason.

## Style Guideline

The American spelling for words is preferred when writing in the English language.

In general, markdown files are preferred for READMEs and similar documentation.  For webpages, when you contribute
to a repository, match the documentation style and/or web framework for the individual repository.
