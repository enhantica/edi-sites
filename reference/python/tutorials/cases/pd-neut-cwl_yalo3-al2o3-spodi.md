Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-cwl_yalo3-al2o3-spodi/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/048352ed3f9e42de2c449a301c7e2ed696bbcf5d/docs/user/tutorials/pd-neut-cwl_yalo3-al2o3-spodi.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-cwl_yalo3-al2o3-spodi.ipynb){ .md-button .ed-tutorial-button download }
</div>

# YAlO₃ and Al₂O₃ on SPODI

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY2IDIyIj48cmVjdCB3aWR0aD0iNjYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5TaW5nbGU8L3RleHQ+PC9zdmc+" alt="Single" width="66" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+bmV1dDwvdGV4dD48L3N2Zz4=" alt="neut" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM1IDIyIj48cmVjdCB3aWR0aD0iMzUiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+Y3dsPC90ZXh0Pjwvc3ZnPg==" alt="cwl" width="35" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

Fit two phases, YAlO₃ and corundum Al₂O₃, in one constant-wavelength neutron pattern from SPODI
at FRM II, measured at 3 K, with a shared Bérar-Baldinozzi profile and cylinder absorption.

It builds the catalogue case `pd-neut-cwl_yalo3-al2o3-spodi` step by step: the same project the
command line fits and the app's Examples open.

## Import the library

```python
import easydiffraction as edi
```

## Define the project

A new project is empty: it holds no structure and no experiment until you add them.

```python
project = edi.Project(name='pd-neut-cwl_yalo3-al2o3-spodi')
```

## Define the structures

Load the two structures from EasyDiffraction's collection. Each CIF gives its space group, cell
and atom sites.

```python
path = edi.download_data('pd-neut-cwl_yalo3-al2o3-spodi-YAlO3', destination='data')
project.structures.add_from_cif_path(path)
path = edi.download_data('pd-neut-cwl_yalo3-al2o3-spodi-Al2O3', destination='data')
project.structures.add_from_cif_path(path)
yalo3 = project.structures['YAlO3']
alumina = project.structures['Al2O3']
```

```text
Data 'pd-neut-cwl_yalo3-al2o3-spodi-YAlO3' is at data/pd-neut-cwl_yalo3-al2o3-spodi-YAlO3.edi
Data 'pd-neut-cwl_yalo3-al2o3-spodi-Al2O3' is at data/pd-neut-cwl_yalo3-al2o3-spodi-Al2O3.edi
```

```python
project.display.structure('YAlO3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/1.html"></iframe>
</div>

## Define the experiment

Create the experiment from the measured data in EasyDiffraction's collection, then describe the
instrument, the peak profile, the background and the structure it links.

```python
data_path = edi.download_data('pd-neut-cwl_yalo3-al2o3-spodi-spodi-data', destination='data')
project.experiments.add_from_data_path(
    name='spodi',
    data_path=data_path,
    sample_form='powder',
    beam_mode='constant wavelength',
    radiation_probe='neutron',
    scattering_type='bragg',
)
experiment = project.experiments['spodi']
experiment.neutron_scattering_length = 'sears1992'
experiment.peak.type = 'cwl-pseudo-voigt-berar-baldinozzi'
experiment.absorption.type = 'cylinder-hewat'
experiment.instrument.name = 'SPODI'
experiment.instrument.facility = 'FRM II'
experiment.peak.broad_gauss_u = 0.04
experiment.peak.broad_gauss_v = -0.05
experiment.peak.broad_gauss_w = 0.1
experiment.peak.mixing_eta_0 = 0.1
experiment.peak.asym_beba_limit = 160
experiment.instrument.setup_wavelength = 1.54816
experiment.absorption.mu_r = 0.0221
experiment.excluded_regions.create(start=0, end=4)
experiment.excluded_regions.create(start=153.95, end=180)
experiment.linked_structures.create(structure_id='YAlO3', scale=30)
experiment.linked_structures.create(structure_id='Al2O3', scale=0.2)
experiment.background.create(position=4.0500, intensity=2100.0)
experiment.background.create(position=4.7770, intensity=2100.0)
experiment.background.create(position=6.7860, intensity=2100.0)
experiment.background.create(position=13.2590, intensity=2100.0)
experiment.background.create(position=18.1700, intensity=2100.0)
experiment.background.create(position=23.7500, intensity=2100.0)
experiment.background.create(position=32.0090, intensity=2100.0)
experiment.background.create(position=36.4730, intensity=2100.0)
experiment.background.create(position=47.1880, intensity=2100.0)
experiment.background.create(position=52.0980, intensity=2100.0)
experiment.background.create(position=59.0180, intensity=2100.0)
experiment.background.create(position=69.9550, intensity=2100.0)
experiment.background.create(position=80.0000, intensity=2100.0)
experiment.background.create(position=90.4910, intensity=2100.0)
experiment.background.create(position=101.2050, intensity=2100.0)
experiment.background.create(position=106.3390, intensity=2100.0)
experiment.background.create(position=108.7950, intensity=2100.0)
experiment.background.create(position=112.5890, intensity=2100.0)
experiment.background.create(position=119.2860, intensity=2100.0)
experiment.background.create(position=128.2140, intensity=2100.0)
experiment.background.create(position=133.1250, intensity=2100.0)
experiment.background.create(position=140.9380, intensity=2100.0)
experiment.background.create(position=145.6250, intensity=2100.0)
experiment.background.create(position=148.0800, intensity=2100.0)
experiment.background.create(position=151.9000, intensity=2100.0)
```

```text
Data 'pd-neut-cwl_yalo3-al2o3-spodi-spodi-data' is at data/pd-neut-cwl_yalo3-al2o3-spodi-spodi.xye
```

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/2.html"></iframe>
</div>

## Perform the analysis

The fit follows diffraction-lib's three cycles for this case (its YAP tutorial). diffraction-lib
frees the Lorentzian Y and two asymmetry terms where this profile has the mixing η₀ and four.

### Cells, scales and 2θ zero

Both phases' cells and scales, and the zero shift, put the peaks of both phases in place.

```python
for parameter in (
    yalo3.cell.length_a,
    yalo3.cell.length_b,
    yalo3.cell.length_c,
    alumina.cell.length_a,
    alumina.cell.length_c,
):
    parameter.free = True
experiment.linked_structures['YAlO3'].scale.free = True
experiment.linked_structures['Al2O3'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 8 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       18.59       201.52
      1      0.053     13.38       104.43   48.2% ↓
      2      0.062     13.38       104.42   
      3      0.073     13.38       104.42   
  done · converged · 3 iters · reduced χ² 104.42 · Rwp 13.38 % · 0.08 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/3.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/4.html"></iframe>
</div>

### Background

```python
for point in experiment.background:
    point.intensity.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 33 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.38       105.32
      1      0.084     11.96        84.07   20.2% ↓
      2      0.121     11.96        84.07   
  done · converged · 2 iters · reduced χ² 84.07 · Rwp 11.96 % · 0.13 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/5.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/6.html"></iframe>
</div>

### Peak widths

The Gaussian widths and the mixing η₀.

```python
for parameter in (
    experiment.peak.broad_gauss_u,
    experiment.peak.broad_gauss_v,
    experiment.peak.broad_gauss_w,
    experiment.peak.mixing_eta_0,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 37 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.96        84.18
      1      0.125     11.46        77.34   8.1% ↓
  done · converged · 1 iters · reduced χ² 77.34 · Rwp 11.46 % · 0.13 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/7.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/8.html"></iframe>
</div>

### Asymmetry

The four Bérar-Baldinozzi asymmetry terms.

```python
for parameter in (
    experiment.peak.asym_beba_a0,
    experiment.peak.asym_beba_b0,
    experiment.peak.asym_beba_a1,
    experiment.peak.asym_beba_b1,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 41 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.46        77.45
      1      0.125     11.28        74.99   3.2% ↓
  done · converged · 1 iters · reduced χ² 74.99 · Rwp 11.28 % · 0.14 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/9.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/10.html"></iframe>
</div>

### Atom positions

The coordinates the symmetry leaves free in both phases.

```python
for parameter in (
    yalo3.atom_sites['Y'].fract_x,
    yalo3.atom_sites['Y'].fract_y,
    yalo3.atom_sites['O1'].fract_x,
    yalo3.atom_sites['O1'].fract_y,
    yalo3.atom_sites['O2'].fract_x,
    yalo3.atom_sites['O2'].fract_y,
    yalo3.atom_sites['O2'].fract_z,
    alumina.atom_sites['Al1'].fract_z,
    alumina.atom_sites['O1'].fract_x,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 50 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.28        75.22
      1      0.130      6.46        24.69   67.2% ↓
      2      0.143      6.46        24.69   
      3      0.190      6.46        24.69   
  done · converged · 3 iters · reduced χ² 24.69 · Rwp 6.46 % · 0.20 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/11.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/12.html"></iframe>
</div>

### Displacements

Every site's displacement in both phases.

```python
for structure in (yalo3, alumina):
    for site in structure.atom_sites:
        site.adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 56 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        6.46        24.74
      1      0.115      4.06         9.77   60.5% ↓
      2      0.128      4.06         9.77   
      3      0.140      4.06         9.77   
      4      0.153      4.06         9.76   
      5      0.165      4.06         9.76   0.1% ↓
      6      0.178      4.05         9.75   0.1% ↓
      7      0.190      4.05         9.73   0.1% ↓
      8      0.203      4.05         9.73   
      9      0.217      4.05         9.73   
     10      0.256      4.05         9.73   
  done · converged · 10 iters · reduced χ² 9.73 · Rwp 4.05 % · 0.27 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/13.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/14.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/15.html"></iframe>
</div>

```python
project.display.structure('YAlO3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/16.html"></iframe>
</div>

```python
project.display.structure('Al2O3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/17.html"></iframe>
</div>

## Report

The HTML report draws the measured, calculated and difference patterns with the reflection
positions, and lists the structures, the experiments and the fit. Open it in a browser.

```python
project.report.save_html('pd-neut-cwl_yalo3-al2o3-spodi.html')
```

```text
Saving report to 'pd-neut-cwl_yalo3-al2o3-spodi.html'
```

## Save the project

```python
project.save_as('pd-neut-cwl_yalo3-al2o3-spodi')
```

```text
Saving project to 'pd-neut-cwl_yalo3-al2o3-spodi'
```
