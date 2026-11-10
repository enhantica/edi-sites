Canonical page: https://easydiffraction.org/cli/structures/

# :fa5-layer-group: Structures in a saved project

Commands calculate from the structures stored in your project and linked by its experiments. They retain the same unit cell, symmetry, atom sites and parameter choices as the application and Python.

## Prepare the structural model

Use the [application structure controls](https://easydiffraction.org/application/structure/structures/) or [Python structure objects](https://easydiffraction.org/python/structures/) to prepare and inspect the structure, then save the complete project.

The command-line interface does not provide a separate structure editor. Its `fit` and `calc` commands load the model from the project rather than taking cell and atom-site definitions as command options.

## Check a calculation

=== "Standalone executable"

    The standalone executable has no `calc`; use the Python package.

=== "Python package"

    ```console
    python -m edi calc path/to/project --dry
    ```

This evaluates the saved model without writing changes. Inspect the output and any errors before starting a fit. See [calculate a pattern](https://easydiffraction.org/cli/calculate/) for output options.

For the common scientific model, read [Structure](https://easydiffraction.org/user-guide/analysis-workflow/structure/). Continue with [Experiments](https://easydiffraction.org/cli/experiments/).
