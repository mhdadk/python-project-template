# Template for Python projects

This repository contains a template that I use for research projects written in Python. These research projects often involve the use of different types of data (images, audio, video, csv files, etc.), and this template is convenient for these kinds of projects. This template makes use of [Poetry](https://python-poetry.org/) for package and environment management.

## Getting started

To get started with this template, do the following:

1. Create a new repository using this template by clicking on the "Use this template" button on the top-right of this page.
2. Clone the newly created repository locally.
3. `cd` into the `src` directory under the cloned repository and then run `poetry install` to install all required dependencies.
4. Read through the "Structure" section below to get an idea of what each directory in the top-level directory means.
5. Read through the [README file under the `src` directory](src/README.md) to get an idea of where different kind of code should go in the repository.
6. (Optional) Read through the other README files under each directory to get a better understanding of what each directory and sub-directory is used for.
7. Start writing code.

## Structure

The following is a brief description of each top-level directory in this repository.

### `src`

The `src` directory contains all the Python code written for this project. For more information on this directory, see [its README file](src/README.md).

### `notes`

In any research project, one will often need to write down personal notes related to the research being conducted. This is what the `notes` directory is used for. For more information on this directory, see [its README file](notes/README.md).

### `data`

The `data` directory contains all the file types that do not belong in the `src` and `notes` directories. This includes images, audio files, videos, large csv files, etc. For more information on this directory, see [its README file](data/README.md).
