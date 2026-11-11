Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-xray-cwl_latp-bm01_scan/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/31c4020e3f94ad78b1fe5aa418770054995eab79/docs/user/tutorials/pd-xray-cwl_latp-bm01_scan.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-xray-cwl_latp-bm01_scan.ipynb){ .md-button .ed-tutorial-button download }
</div>

# LATP and AlPO₄ on BM01

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4OCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDg4IDIyIj48cmVjdCB3aWR0aD0iODgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEwIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDQ4IDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTIyNC4yOTk4MDQ2ODc1IDI3My4wQzIzMy43MDAxOTUzMTI1IDI2My41OTk2MDkzNzUgMjMzLjcwMDE5NTMxMjUgMjQ4LjQwMDM5MDYyNSAyMjQuMjAwMTk1MzEyNSAyMzkuMEw4OC4yMDAxOTUzMTI1IDEwMy4wQzc4LjkwMDM5MDYyNSA5My41OTk2MDkzNzUgNjMuNzAwMTk1MzEyNSA5My41OTk2MDkzNzUgNTQuMjk5ODA0Njg3NSAxMDMuMEwzMS43OTk4MDQ2ODc1IDEyNS43OTk4MDQ2ODc1QzIyLjQwMDM5MDYyNSAxMzUuMDk5NjA5Mzc1IDIyLjQwMDM5MDYyNSAxNTAuMjk5ODA0Njg3NSAzMS43OTk4MDQ2ODc1IDE1OS43MDAxOTUzMTI1TDEyOC4yMDAxOTUzMTI1IDI1Ni4wOTk2MDkzNzVMMzEuNzk5ODA0Njg3NSAzNTIuNUMyMi40MDAzOTA2MjUgMzYxLjc5OTgwNDY4NzUgMjIuNDAwMzkwNjI1IDM3Ny4wIDMxLjc5OTgwNDY4NzUgMzg2LjQwMDM5MDYyNUw1NC40MDAzOTA2MjUgNDA5LjBDNjMuNzAwMTk1MzEyNSA0MTguNDAwMzkwNjI1IDc4LjkwMDM5MDYyNSA0MTguNDAwMzkwNjI1IDg4LjI5OTgwNDY4NzUgNDA5LjBaTTQxNi4yOTk4MDQ2ODc1IDIzOS4wIDI4MC4yOTk4MDQ2ODc1IDEwMy4wQzI3MC45MDAzOTA2MjUgOTMuNTk5NjA5Mzc1IDI1NS43MDAxOTUzMTI1IDkzLjU5OTYwOTM3NSAyNDYuNDAwMzkwNjI1IDEwMy4wTDIyMy43OTk4MDQ2ODc1IDEyNS41OTk2MDkzNzVDMjE0LjQwMDM5MDYyNSAxMzUuMCAyMTQuNDAwMzkwNjI1IDE1MC4yMDAxOTUzMTI1IDIyMy43OTk4MDQ2ODc1IDE1OS41TDMyMC4yMDAxOTUzMTI1IDI1NS45MDAzOTA2MjVMMjIzLjc5OTgwNDY4NzUgMzUyLjI5OTgwNDY4NzVDMjE0LjQwMDM5MDYyNSAzNjEuNzAwMTk1MzEyNSAyMTQuNDAwMzkwNjI1IDM3Ni45MDAzOTA2MjUgMjIzLjc5OTgwNDY4NzUgMzg2LjIwMDE5NTMxMjVMMjQ2LjQwMDM5MDYyNSA0MDguNzk5ODA0Njg3NUMyNTUuNzk5ODA0Njg3NSA0MTguMjAwMTk1MzEyNSAyNzEuMCA0MTguMjAwMTk1MzEyNSAyODAuMjk5ODA0Njg3NSA0MDguNzk5ODA0Njg3NUw0MTYuMjk5ODA0Njg3NSAyNzIuNzk5ODA0Njg3NUM0MjUuNzAwMTk1MzEyNSAyNjMuNTk5NjA5Mzc1IDQyNS43MDAxOTUzMTI1IDI0OC40MDAzOTA2MjUgNDE2LjI5OTgwNDY4NzUgMjM5LjBaIi8+PC9zdmc+PHRleHQgeD0iMjEiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5TZXF1ZW50aWFsPC90ZXh0Pjwvc3ZnPg==" alt="Sequential" width="88" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+eHJheTwvdGV4dD48L3N2Zz4=" alt="xray" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM1IDIyIj48cmVjdCB3aWR0aD0iMzUiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+Y3dsPC90ZXh0Pjwvc3ZnPg==" alt="cwl" width="35" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

Fit three phases, LATP and two AlPO₄ forms, to 73 synchrotron X-ray patterns from BM01 at ESRF,
one after another, with linked displacement parameters.

The project is the catalogue case `pd-xray-cwl_latp-bm01_scan`, the one the command line and the
app's Examples open. Al shares Ti's site, coordinate and displacement, and the impurity phase's
displacements are shared, from the start.

```python
import csv
from pathlib import Path

import easydiffraction as edi
```

## Load the project

A sequential fit writes one row per pattern into the project's `analysis/results.csv`, so work
on a copy of the project, saved to a folder of its own.

```python
project_path = edi.download_data('pd-xray-cwl_latp-bm01_scan', destination='data')
project = edi.Project.load(project_path)
project.save_as('pd-xray-cwl_latp-bm01_scan')
latp = project.structures['latp']
c2221 = project.structures['alpo4_c2221']
p63mc = project.structures['alpo4_p63mc']
experiment = project.experiments['bm01']
project.display.constraints()
```

```text
Data 'pd-xray-cwl_latp-bm01_scan' is at data/pd-xray-cwl_latp-bm01_scan-67292a68d53c/pd-xray-cwl_latp-bm01_scan
Saving project to 'pd-xray-cwl_latp-bm01_scan'
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 460px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/1.html"></iframe>
</div>

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

## Stage the template fit

The template is the scan's first pattern. Fit it alone first, in stages, so the scan starts from
a good model: switch the fitting mode to a single fit.

```python
project.analysis.fitting_mode = 'single'
```

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/2.html"></iframe>
</div>

## Perform the analysis

The fit goes in stages, freeing one group of parameters at a time.

### Scales, 2θ zero and cells

The three phases' scales and cells and the zero shift.

```python
experiment.linked_structures['latp'].scale.free = True
experiment.linked_structures['alpo4_c2221'].scale.free = True
experiment.linked_structures['alpo4_p63mc'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
latp.cell.length_a.free = True
latp.cell.length_c.free = True
c2221.cell.length_a.free = True
c2221.cell.length_b.free = True
c2221.cell.length_c.free = True
p63mc.cell.length_a.free = True
p63mc.cell.length_c.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 404px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_latp-bm01_scan, 3114 pts fitted / 3163 loaded, 11 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.51 140198364.17
      1      0.234      4.51 140107944.41   0.1% ↓
      2      0.265      4.51 140107929.77   
  done · converged · 2 iters · reduced χ² 140107929.77 · Rwp 4.51 % · 0.29 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/4.html"></iframe>
</div>

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/5.html"></iframe>
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
edi fit: project pd-xray-cwl_latp-bm01_scan, 3114 pts fitted / 3163 loaded, 41 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.51 141475726.02
      1      0.362      4.51 141465247.68   
  done · converged · 1 iters · reduced χ² 141465247.68 · Rwp 4.51 % · 0.39 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/6.html"></iframe>
</div>

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/7.html"></iframe>
</div>

### Peak widths

```python
experiment.peak.broad_gauss_u.free = True
experiment.peak.broad_gauss_v.free = True
experiment.peak.broad_gauss_w.free = True
experiment.peak.mixing_eta_0.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_latp-bm01_scan, 3114 pts fitted / 3163 loaded, 45 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.51 141649627.27
      1      0.310      4.51 141612911.93   
      2      0.340      4.51 141612401.39   
      3      0.425      4.51 141612383.74   
  done · converged · 3 iters · reduced χ² 141612383.74 · Rwp 4.51 % · 0.45 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/8.html"></iframe>
</div>

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/9.html"></iframe>
</div>

### Peak asymmetry

```python
experiment.peak.asym_beba_a0.free = True
experiment.peak.asym_beba_b0.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_latp-bm01_scan, 3114 pts fitted / 3163 loaded, 47 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.51 141704729.33
      1      0.282      4.51 141696161.48   
      2      0.372      4.51 141696113.17   
  done · converged · 2 iters · reduced χ² 141696113.17 · Rwp 4.51 % · 0.40 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/10.html"></iframe>
</div>

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/11.html"></iframe>
</div>

### LATP positions

The main phase's free coordinates; Al's follows Ti's.

```python
latp.atom_sites['Ti1'].fract_z.free = True
latp.atom_sites['P1'].fract_x.free = True
latp.atom_sites['O1'].fract_x.free = True
latp.atom_sites['O1'].fract_y.free = True
latp.atom_sites['O1'].fract_z.free = True
latp.atom_sites['O2'].fract_x.free = True
latp.atom_sites['O2'].fract_y.free = True
latp.atom_sites['O2'].fract_z.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_latp-bm01_scan, 3114 pts fitted / 3163 loaded, 55 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.51 142066681.62
      1      0.416      4.51 142050495.11   
  done · converged · 1 iters · reduced χ² 142050495.11 · Rwp 4.51 % · 0.45 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/12.html"></iframe>
</div>

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/13.html"></iframe>
</div>

### LATP displacements

```python
latp.atom_sites['Ti1'].adp_iso.free = True
latp.atom_sites['P1'].adp_iso.free = True
latp.atom_sites['O1'].adp_iso.free = True
latp.atom_sites['O2'].adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_latp-bm01_scan, 3114 pts fitted / 3163 loaded, 59 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.51 142236485.94
      1      0.397      4.51 142228556.43   
  done · converged · 1 iters · reduced χ² 142228556.43 · Rwp 4.51 % · 0.43 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/14.html"></iframe>
</div>

```python
project.display.pattern('bm01')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/15.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/16.html"></iframe>
</div>

```python
project.display.structure('latp')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/17.html"></iframe>
</div>

```python
project.display.structure('alpo4_c2221')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/18.html"></iframe>
</div>

```python
project.display.structure('alpo4_p63mc')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_latp-bm01_scan/19.html"></iframe>
</div>

## Fit the scan

Back to the sequential mode, with the template's free parameters. Each pattern starts from the
fit before it.

```python
project.analysis.fitting_mode = 'sequential'
fitted = []
result = project.fit_sequential(on_file_complete=lambda *args: fitted.append(args))
print(result.status.name.lower(), 'after', len(fitted), 'patterns')
```

```text
done after 73 patterns
```

## The results

One row per pattern, in the order they were fitted.

```python
results = Path('pd-xray-cwl_latp-bm01_scan/analysis/results.csv')
with results.open(newline='', encoding='utf-8') as file:
    rows = list(csv.DictReader(file))
print(len(rows), 'rows; columns:', ', '.join(list(rows[0])[:6]), '...')
```

```text
73 rows; columns: file_path, fit_result.reduced_chi_square, fit_result.success, fit_result.iterations, alpo4_c2221.cell.length_a, alpo4_c2221.cell.length_a.uncertainty ...
```

## Save the report

```python
project.report.save_html('pd-xray-cwl_latp-bm01_scan.html')
```

```text
Saving report to 'pd-xray-cwl_latp-bm01_scan.html'
```
