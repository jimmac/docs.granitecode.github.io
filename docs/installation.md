# Installation & Setup

## Installation

Granite.Code can be installed from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=redhat.granitecode), and can be installed on Windows, Mac, and Linux.

We recommend that Linux users we recommend install the <a href="https://code.visualstudio.com/download">tarball version of VS Code</a>, rather than the RPM, DEB or Flatpak versions. This ensures that VS Code is able to update itself.

## Setup

Granite.Code defaults to a local AI setup, with AI models hosted on your computer and no data shared with the outside world. On first run, the Granite.Code extension launches a wizard which downloads the Granite models needed for this, as well as setting up the environment that the models will run in.

If you need to restart the setup wizard for any reason, it can be launched from the VS Code command palette using the `Granite.Code: Setup Granite as code assistant` command.

Once you have set up Granite.Code, we recommend that you try out the [getting started tutorial](FIXME).

## System Requirements

Granite.Code should only be used with hardware that is capable of effectively running the Granite models. Our current recommendation is that it should only be used with 

* Discrete NVIDIA and AMD gpus for Linux and Windows, or
* M-series Macbooks with M2 or higher, and at least 20-24GB of memory
