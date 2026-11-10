Canonical page: https://easydiffraction.org/cli/experiments/

# :fa5-microscope: Experiments in a saved project

The saved experiment supplies measured data or a calculation range, instrument settings, peak profile, background, exclusions and links to structures. Commands use these settings when loading the complete project.

## Prepare the experiment

Use the [application experiment controls](https://easydiffraction.org/application/experiment/experiments/) or [Python experiment objects](https://easydiffraction.org/python/experiments/) to import observations and configure the experiment, then save the project.

The command line operates on that saved experiment. It does not create an experiment from a raw pattern file or offer a second set of instrument and background options on the fit command.

## Choose the run

- [Calculate](https://easydiffraction.org/cli/calculate/) evaluates the model, including experiments with simulation ranges.
- [Fit](https://easydiffraction.org/cli/fit/) uses measured observations and the fitting mode saved in the project.

Use `--dry` when you want to calculate or fit without writing project changes. It still executes the calculation or fit.

The shared [Experiment](https://easydiffraction.org/user-guide/analysis-workflow/experiment/) stage explains the model, and [fitting modes](https://easydiffraction.org/user-guide/analysis-workflow/analysis/#fitting-modes) explains single, joint and scan analyses.
