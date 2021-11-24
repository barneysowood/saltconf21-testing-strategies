# Saltconf21 testing strategies

Demonstration repository for my Saltconf21 talk "Strategies for testing Salt states"

* [Talk recording](https://youtu.be/FI7RFE4sAHM)

* [Slides and demos](https://sowood.co.uk/talks/saltconf21-testing-strategies/talk-web.html)


## Getting started

The setup script will configure a python virtualenv with salt installed.

Run `./setup` and wait until the script completes.

## Using the salt cli tools

Run `source vitualenv/bin/activate` to enable the virtualenv for you shell session.
You can then run `salt-call` which will use configuration and states in the local directory.

