Canonical page: https://easydiffraction.org/cli/python/

# Command line from the Python package

The Python package includes the command-line interface. You do not need to write a Python script or use a notebook.

## Install the package

Follow [Python setup](https://easydiffraction.org/python/setup/) for the package and environment. The same installation provides both `import edi` and `python -m edi`.

## Run a command

Activate the environment containing the package, then check the command:

=== "Standalone executable"

    ```console
    edi --help
    ```

=== "Python package"

    ```console
    python -m edi --help
    ```

Pass a saved project directly:

=== "Standalone executable"

    ```console
    edi fit path/to/project --output fitted-project
    ```

=== "Python package"

    ```console
    python -m edi fit path/to/project --output fitted-project
    ```

The Python package's command line also provides `calc`, `export`, `undo`, `collection`, `report` and the [data and tutorial downloads](https://easydiffraction.org/cli/data/), plus live fit progress. Use [Run a fit](https://easydiffraction.org/cli/fit/) for the options, or [Run an example](https://easydiffraction.org/cli/tutorials/) to try a complete case.
