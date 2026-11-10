Canonical page: https://easydiffraction.org/user-guide/analysis-workflow/report/

# :fa5-clipboard-list: Report

A report brings the model and analysis outcome into a document for inspection and sharing. It complements the complete project, which retains the editable analysis.

## What to retain

A useful scientific account identifies the structures, experiments, observations, analysis choices and outcome. Inspect the fitted values, uncertainties and agreement factors together with the observed/calculated patterns and residuals.

Report settings select optional material such as charts, correlations, reflection information, data points and scan evolution. Include what the reader needs to assess the result, and retain the complete project when a report omits large data tables.

## Choose an output

| Output | Purpose | Current interface support |
| --- | --- | --- |
| Interactive HTML | Share a readable document with interactive figures | Application, Python and Command line |
| Offline HTML | Embed chart libraries so the document can be opened without fetching them | Application, Python and Command line |
| PDF | Share a paginated document with static figures | Application |
| CIF report | Exchange a scientific account of structures, experiments and results | Application, Python and Command line |

A structural CIF used as input and a CIF report serve different purposes. Neither replaces the complete project; see [data formats](https://easydiffraction.org/user-guide/data-formats/).

## Save the model and the report

Saving a project and writing its report are separate actions. A model or report-settings change can make a previously saved report out of date. A file that has been removed can be marked missing.

Check report state before sharing it. Keep the report together with the matching project, measured data provenance and software version. For a scan, include the template, file order and information about failed or incomplete results.

## Generate the document

- [Application: Report page, export formats and saved-state indicators](https://easydiffraction.org/application/report/).
- [Python: report rendering and save methods](https://easydiffraction.org/python/reports/).
- [Command line: report output and freshness checks](https://easydiffraction.org/cli/reports/).

Use [citation and reproducibility](https://easydiffraction.org/about/citation/) when preparing a publication or handing an analysis to a collaborator.
