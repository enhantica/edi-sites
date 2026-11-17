Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-xray-cwl_lam7o3-p021/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/0fa31db22c4ad74028c166bbd6e6e07771e96e60/docs/user/tutorials/pd-xray-cwl_lam7o3-p021.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-xray-cwl_lam7o3-p021.ipynb){ .md-button .ed-tutorial-button download }
</div>

# La(Ti,Cr,Mn,Fe,Co,Ni,Cu)O₃ on P02.1

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY2IDIyIj48cmVjdCB3aWR0aD0iNjYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5TaW5nbGU8L3RleHQ+PC9zdmc+" alt="Single" width="66" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+eHJheTwvdGV4dD48L3N2Zz4=" alt="xray" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM1IDIyIj48cmVjdCB3aWR0aD0iMzUiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+Y3dsPC90ZXh0Pjwvc3ZnPg==" alt="cwl" width="35" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

Fit the high-entropy perovskite La(Ti,Cr,Mn,Fe,Co,Ni,Cu)O₃, seven cations on one site, to
synchrotron X-ray powder data from P02.1 at PETRA III.

It builds the catalogue case `pd-xray-cwl_lam7o3-p021` step by step: the same project the command
line fits and the app's Examples open. The seven metals sharing one site have one displacement,
held by constraints.

## Import the library

```python
import easydiffraction as edi
```

## Define the project

A new project is empty: it holds no structure and no experiment until you add them.

```python
project = edi.Project(name='pd-xray-cwl_lam7o3-p021')
```

## Define the structure

Load the structure from EasyDiffraction's collection. Its CIF gives the space group, the cell and
the atom sites.

```python
path = edi.download_data('pd-xray-cwl_lam7o3-p021-lam7o3', destination='data')
project.structures.add_from_cif_path(path)
structure = project.structures['lam7o3']
```

```text
Data 'pd-xray-cwl_lam7o3-p021-lam7o3' is at data/pd-xray-cwl_lam7o3-p021-lam7o3.edi
```

```python
project.display.structure('lam7o3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/1.html"></iframe>
</div>

## Define the experiment

Create the experiment from the measured data in EasyDiffraction's collection, then describe the
instrument, the peak profile, the background and the structure it links.

```python
data_path = edi.download_data('pd-xray-cwl_lam7o3-p021-p021-data', destination='data')
project.experiments.add_from_data_path(
    name='p021',
    data_path=data_path,
    sample_form='powder',
    beam_mode='constant wavelength',
    radiation_probe='xray',
    scattering_type='bragg',
)
experiment = project.experiments['p021']
experiment.xray_form_factor = 'it1992'
experiment.xray_dispersion = 'sasaki1989'
experiment.peak.type = 'cwl-tch-pseudo-voigt'
experiment.instrument.name = 'P02.1'
experiment.instrument.facility = 'PETRA III'
experiment.peak.broad_gauss_u = 0.04
experiment.peak.broad_gauss_v = -0.01
experiment.peak.broad_gauss_w = 0.001
experiment.peak.broad_lorentz_x = 0.1
experiment.peak.cutoff_fwhm = 30
experiment.instrument.setup_wavelength = 0.207109
experiment.excluded_regions.create(start=0, end=2)
experiment.excluded_regions.create(start=15, end=20)
experiment.linked_structures.create(structure_id='lam7o3', scale=0.000005)
experiment.background.create(id='2.0', position=2.0033379, intensity=300)
experiment.background.create(id='2.3', position=2.297792, intensity=300)
experiment.background.create(id='2.7', position=2.7079241, intensity=300)
experiment.background.create(id='2.9', position=2.8761833, intensity=300)
experiment.background.create(id='3.0', position=2.9813454, intensity=300)
experiment.background.create(id='3.1', position=3.1180563, intensity=300)
experiment.background.create(id='3.7', position=3.7174802, intensity=300)
experiment.background.create(id='4.1', position=4.1381288, intensity=300)
experiment.background.create(id='4.3', position=4.2748394, intensity=300)
experiment.background.create(id='4.4', position=4.3905177, intensity=300)
experiment.background.create(id='4.5', position=4.5482607, intensity=300)
experiment.background.create(id='4.9', position=4.9268441, intensity=300)
experiment.background.create(id='5.1', position=5.1371684, intensity=300)
experiment.background.create(id='7', position=7.4086699, intensity=300)
experiment.background.create(id='8', position=8.0922232, intensity=300)
experiment.background.create(id='10', position=9.7748175, intensity=300)
experiment.background.create(id='11', position=10.910567, intensity=300)
experiment.background.create(id='12', position=12.498515, intensity=300)
experiment.background.create(id='14.7', position=14.70692, intensity=300)
experiment.background.create(id='15.0', position=14.990857, intensity=300)
```

```text
Data 'pd-xray-cwl_lam7o3-p021-p021-data' is at data/pd-xray-cwl_lam7o3-p021-p021.xye
```

The constraints the fit keeps, each between two named parameters (aliases).

```python
project.analysis.aliases.create(id='biso_Ti', param=structure.atom_sites['Ti'].adp_iso)
project.analysis.aliases.create(id='biso_Cr', param=structure.atom_sites['Cr'].adp_iso)
project.analysis.aliases.create(id='biso_Mn', param=structure.atom_sites['Mn'].adp_iso)
project.analysis.aliases.create(id='biso_Fe', param=structure.atom_sites['Fe'].adp_iso)
project.analysis.aliases.create(id='biso_Co', param=structure.atom_sites['Co'].adp_iso)
project.analysis.aliases.create(id='biso_Ni', param=structure.atom_sites['Ni'].adp_iso)
project.analysis.aliases.create(id='biso_Cu', param=structure.atom_sites['Cu'].adp_iso)
project.analysis.aliases.create(id='biso_O1', param=structure.atom_sites['O1'].adp_iso)
project.analysis.aliases.create(id='biso_O2', param=structure.atom_sites['O2'].adp_iso)
project.analysis.constraints.create(id='1', expression='biso_Cr = biso_Ti')
project.analysis.constraints.create(id='2', expression='biso_Mn = biso_Ti')
project.analysis.constraints.create(id='3', expression='biso_Fe = biso_Ti')
project.analysis.constraints.create(id='4', expression='biso_Co = biso_Ti')
project.analysis.constraints.create(id='5', expression='biso_Ni = biso_Ti')
project.analysis.constraints.create(id='6', expression='biso_Cu = biso_Ti')
project.analysis.constraints.create(id='7', expression='biso_O2 = biso_O1')
```

```python
project.display.constraints()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 544px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/2.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/3.html"></iframe>
</div>

## Perform the analysis

The fit goes in stages, freeing one group of parameters at a time.

### Scale, 2θ zero and cell

The scale, the zero shift and the cell put the peaks in place and at the right height.

```python
experiment.linked_structures['lam7o3'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
structure.cell.length_a.free = True
structure.cell.length_b.free = True
structure.cell.length_c.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 236px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/4.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1396 loaded, 5 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       60.60       246.85
      1      0.023     34.19        78.59   68.2% ↓
      2      0.027     33.91        77.28   1.7% ↓
      3      0.030     33.81        76.83   0.6% ↓
      4      0.033     33.76        76.62   0.3% ↓
      5      0.037     33.73        76.49   0.2% ↓
      6      0.040     33.72        76.41   0.1% ↓
      7      0.043     33.70        76.35   0.1% ↓
      8      0.047     33.69        76.31   0.1% ↓
      9      0.050     33.69        76.29   
     10      0.053     33.68        76.27   
     11      0.057     33.68        76.26   
     12      0.060     33.68        76.25   
     13      0.063     33.68        76.25   
     14      0.066     33.68        76.24   
     15      0.070     33.68        76.24   
     16      0.073     33.68        76.24   
     17      0.077     33.68        76.24   
  done · converged · 17 iters · reduced χ² 76.24 · Rwp 33.68 % · 0.08 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/5.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/6.html"></iframe>
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
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1396 loaded, 25 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       33.68        77.50
      1      0.026     10.53         7.58   90.2% ↓
      2      0.030     10.53         7.57   
      3      0.033     10.53         7.57   
      4      0.037     10.53         7.57   
      5      0.040     10.53         7.57   
      6      0.044     10.53         7.57   
      7      0.048     10.53         7.57   
      8      0.051     10.52         7.57   
      9      0.055     10.52         7.57   
     10      0.058     10.52         7.57   
     11      0.062     10.52         7.57   
     12      0.067     10.52         7.57   
  done · converged · 12 iters · reduced χ² 7.57 · Rwp 10.52 % · 0.07 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/7.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/8.html"></iframe>
</div>

### Peak widths

The Gaussian widths and the Lorentzian X.

```python
for parameter in (
    experiment.peak.broad_gauss_u,
    experiment.peak.broad_gauss_v,
    experiment.peak.broad_gauss_w,
    experiment.peak.broad_lorentz_x,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1396 loaded, 29 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       10.52         7.59
      1      0.033      5.89         2.38   68.7% ↓
      2      0.038      5.77         2.29   3.9% ↓
      3      0.043      5.74         2.26   1.1% ↓
      4      0.053      5.64         2.18   3.5% ↓
      5      0.059      5.30         1.92   11.8% ↓
      6      0.065      4.77         1.56   19.0% ↓
      7      0.070      4.13         1.17   24.9% ↓
      8      0.075      3.65         0.91   22.1% ↓
      9      0.079      3.59         0.88   3.1% ↓
     10      0.084      3.57         0.87   1.3% ↓
     11      0.089      3.56         0.87   0.2% ↓
     12      0.094      3.56         0.87   0.1% ↓
     13      0.098      3.56         0.87   0.1% ↓
     14      0.103      3.55         0.86   0.4% ↓
     15      0.107      3.53         0.86   1.1% ↓
     16      0.112      3.49         0.83   2.5% ↓
     17      0.116      3.42         0.80   3.7% ↓
     18      0.121      3.35         0.77   4.3% ↓
     19      0.126      3.22         0.71   7.4% ↓
     20      0.130      3.01         0.62   12.7% ↓
     21      0.135      2.83         0.55   11.3% ↓
     22      0.140      2.79         0.54   2.8% ↓
     23      0.144      2.79         0.53   0.1% ↓
     24      0.149      2.79         0.53   
     25      0.155      2.79         0.53   
  done · converged · 25 iters · reduced χ² 0.53 · Rwp 2.79 % · 0.16 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/9.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/10.html"></iframe>
</div>

### Background from the fitted model

With a fitted peak model, estimate the background again with the calculated peaks subtracted,
which follows the low-angle background better, then free the new points and fit again.

```python
experiment.background.auto_estimate(use_model='subtract', n_points=20)
for point in experiment.background:
    point.intensity.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1396 loaded, 29 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.03         1.11
      1      0.040      2.71         0.50   54.7% ↓
  done · converged · 1 iters · reduced χ² 0.50 · Rwp 2.71 % · 0.05 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/11.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/12.html"></iframe>
</div>

### Atom positions

```python
for site in structure.atom_sites:
    for coordinate in (site.fract_x, site.fract_y, site.fract_z):
        coordinate.free = not coordinate.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1396 loaded, 36 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        2.71         0.51
      1      0.048      1.78         0.22   56.9% ↓
      2      0.055      1.78         0.22   0.1% ↓
      3      0.061      1.78         0.22   0.4% ↓
      4      0.067      1.77         0.22   1.1% ↓
      5      0.074      1.75         0.21   2.4% ↓
      6      0.080      1.71         0.20   3.5% ↓
      7      0.087      1.69         0.20   2.8% ↓
      8      0.093      1.68         0.19   1.1% ↓
      9      0.100      1.68         0.19   0.2% ↓
     10      0.106      1.68         0.19   
     11      0.112      1.68         0.19   
     12      0.121      1.68         0.19   
  done · converged · 12 iters · reduced χ² 0.19 · Rwp 1.68 % · 0.13 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/13.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/14.html"></iframe>
</div>

### Displacements

La's, the mixed site's (through Ti) and O1's; O2's follows O1's.

```python
structure.atom_sites['La'].adp_iso.free = True
structure.atom_sites['Ti'].adp_iso.free = True
structure.atom_sites['O1'].adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1396 loaded, 39 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        1.68         0.19
      1      0.050      1.60         0.18   8.9% ↓
      2      0.057      1.60         0.18   0.2% ↓
      3      0.063      1.60         0.18   0.1% ↓
      4      0.070      1.60         0.18   0.3% ↓
      5      0.077      1.59         0.18   0.7% ↓
      6      0.084      1.58         0.17   1.0% ↓
      7      0.090      1.58         0.17   0.9% ↓
      8      0.097      1.57         0.17   0.4% ↓
      9      0.104      1.57         0.17   0.1% ↓
     10      0.110      1.57         0.17   
     11      0.119      1.57         0.17   
  done · converged · 11 iters · reduced χ² 0.17 · Rwp 1.57 % · 0.13 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/15.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/16.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/17.html"></iframe>
</div>

```python
project.display.structure('lam7o3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/18.html"></iframe>
</div>

## Report

The HTML report draws the measured, calculated and difference patterns with the reflection
positions, and lists the structures, the experiments and the fit. Open it in a browser.

```python
project.report.save_html('pd-xray-cwl_lam7o3-p021.html')
```

```text
Saving report to 'pd-xray-cwl_lam7o3-p021.html'
```

## Save the project

```python
project.save_as('pd-xray-cwl_lam7o3-p021')
```

```text
Saving project to 'pd-xray-cwl_lam7o3-p021'
```
