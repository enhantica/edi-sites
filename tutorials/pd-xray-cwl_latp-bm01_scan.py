# %%
# Check whether easydiffraction is installed; install it if needed.
# Required for remote environments such as Google Colab.
import importlib.util

if importlib.util.find_spec('easydiffraction') is None:
    # %pip install easydiffraction==2026.11.14 --extra-index-url https://download.easydiffraction.org/pypi/simple/


# %% [markdown]
# # LATP and AlPO₄ on BM01

# %% [markdown]
# <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4OCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDg4IDIyIj48cmVjdCB3aWR0aD0iODgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEwIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDQ4IDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTIyNC4yOTk4MDQ2ODc1IDI3My4wQzIzMy43MDAxOTUzMTI1IDI2My41OTk2MDkzNzUgMjMzLjcwMDE5NTMxMjUgMjQ4LjQwMDM5MDYyNSAyMjQuMjAwMTk1MzEyNSAyMzkuMEw4OC4yMDAxOTUzMTI1IDEwMy4wQzc4LjkwMDM5MDYyNSA5My41OTk2MDkzNzUgNjMuNzAwMTk1MzEyNSA5My41OTk2MDkzNzUgNTQuMjk5ODA0Njg3NSAxMDMuMEwzMS43OTk4MDQ2ODc1IDEyNS43OTk4MDQ2ODc1QzIyLjQwMDM5MDYyNSAxMzUuMDk5NjA5Mzc1IDIyLjQwMDM5MDYyNSAxNTAuMjk5ODA0Njg3NSAzMS43OTk4MDQ2ODc1IDE1OS43MDAxOTUzMTI1TDEyOC4yMDAxOTUzMTI1IDI1Ni4wOTk2MDkzNzVMMzEuNzk5ODA0Njg3NSAzNTIuNUMyMi40MDAzOTA2MjUgMzYxLjc5OTgwNDY4NzUgMjIuNDAwMzkwNjI1IDM3Ny4wIDMxLjc5OTgwNDY4NzUgMzg2LjQwMDM5MDYyNUw1NC40MDAzOTA2MjUgNDA5LjBDNjMuNzAwMTk1MzEyNSA0MTguNDAwMzkwNjI1IDc4LjkwMDM5MDYyNSA0MTguNDAwMzkwNjI1IDg4LjI5OTgwNDY4NzUgNDA5LjBaTTQxNi4yOTk4MDQ2ODc1IDIzOS4wIDI4MC4yOTk4MDQ2ODc1IDEwMy4wQzI3MC45MDAzOTA2MjUgOTMuNTk5NjA5Mzc1IDI1NS43MDAxOTUzMTI1IDkzLjU5OTYwOTM3NSAyNDYuNDAwMzkwNjI1IDEwMy4wTDIyMy43OTk4MDQ2ODc1IDEyNS41OTk2MDkzNzVDMjE0LjQwMDM5MDYyNSAxMzUuMCAyMTQuNDAwMzkwNjI1IDE1MC4yMDAxOTUzMTI1IDIyMy43OTk4MDQ2ODc1IDE1OS41TDMyMC4yMDAxOTUzMTI1IDI1NS45MDAzOTA2MjVMMjIzLjc5OTgwNDY4NzUgMzUyLjI5OTgwNDY4NzVDMjE0LjQwMDM5MDYyNSAzNjEuNzAwMTk1MzEyNSAyMTQuNDAwMzkwNjI1IDM3Ni45MDAzOTA2MjUgMjIzLjc5OTgwNDY4NzUgMzg2LjIwMDE5NTMxMjVMMjQ2LjQwMDM5MDYyNSA0MDguNzk5ODA0Njg3NUMyNTUuNzk5ODA0Njg3NSA0MTguMjAwMTk1MzEyNSAyNzEuMCA0MTguMjAwMTk1MzEyNSAyODAuMjk5ODA0Njg3NSA0MDguNzk5ODA0Njg3NUw0MTYuMjk5ODA0Njg3NSAyNzIuNzk5ODA0Njg3NUM0MjUuNzAwMTk1MzEyNSAyNjMuNTk5NjA5Mzc1IDQyNS43MDAxOTUzMTI1IDI0OC40MDAzOTA2MjUgNDE2LjI5OTgwNDY4NzUgMjM5LjBaIi8+PC9zdmc+PHRleHQgeD0iMjEiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5TZXF1ZW50aWFsPC90ZXh0Pjwvc3ZnPg==" alt="Sequential" width="88" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+eHJheTwvdGV4dD48L3N2Zz4=" alt="xray" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM1IDIyIj48cmVjdCB3aWR0aD0iMzUiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+Y3dsPC90ZXh0Pjwvc3ZnPg==" alt="cwl" width="35" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

# %% [markdown]
# Fit three phases, LATP and two AlPO₄ forms, to 73 synchrotron X-ray patterns from BM01 at ESRF,
# one after another, with linked displacement parameters.
#
# It builds the catalogue case `pd-xray-cwl_latp-bm01_scan` step by step: the same project the
# command line fits and the app's Examples open. Al shares Ti's site, coordinate and displacement,
# and the impurity phase's displacements are shared.

# %% [markdown]
# ## Import the library

# %%
import csv
import zipfile
from pathlib import Path

import easydiffraction as edi

# %% [markdown]
# ## Define the project
#
# A new project is empty: it holds no structure and no experiment until you add them.

# %%
project = edi.Project(name='pd-xray-cwl_latp-bm01_scan')

# %% [markdown]
# ## Define the structures
#
# Load the three structures from EasyDiffraction's collection. Each CIF gives its space group, cell
# and atom sites.

# %%
path = edi.download_data('pd-xray-cwl_latp-bm01_scan-latp', destination='data')
project.structures.add_from_cif_path(path)
path = edi.download_data('pd-xray-cwl_latp-bm01_scan-alpo4_c2221', destination='data')
project.structures.add_from_cif_path(path)
path = edi.download_data('pd-xray-cwl_latp-bm01_scan-alpo4_p63mc', destination='data')
project.structures.add_from_cif_path(path)
latp = project.structures['latp']
c2221 = project.structures['alpo4_c2221']
p63mc = project.structures['alpo4_p63mc']

# %%
project.display.structure('latp')

# %% [markdown]
# ## Define the experiment
#
# Create the experiment from the measured data in EasyDiffraction's collection, then describe the
# instrument, the peak profile, the background and the structure it links.

# %%
data_path = edi.download_data('pd-xray-cwl_latp-bm01_scan-bm01-data', destination='data')
project.experiments.add_from_data_path(
    name='bm01',
    data_path=data_path,
    sample_form='powder',
    beam_mode='constant wavelength',
    radiation_probe='xray',
    scattering_type='bragg',
)
experiment = project.experiments['bm01']
experiment.xray_dispersion = 'sasaki1989'
experiment.peak.type = 'cwl-pseudo-voigt-berar-baldinozzi'
experiment.absorption.type = 'cylinder-hewat'
experiment.instrument.name = 'BM01'
experiment.instrument.facility = 'ESRF'
experiment.xray_dispersion = 'sasaki1989'
experiment.peak.broad_gauss_u = 0.019
experiment.peak.broad_gauss_v = 0.019
experiment.peak.broad_gauss_w = 0.0156
experiment.peak.mixing_eta_0 = 0.374
experiment.peak.asym_beba_a0 = 0.088
experiment.peak.asym_beba_b0 = 0.0043
experiment.peak.cutoff_fwhm = 8
experiment.instrument.setup_wavelength = 0.69687
experiment.instrument.calib_twotheta_offset = -0.0388
experiment.absorption.mu_r = 0.3
experiment.excluded_regions.create(start=0, end=3.8)
experiment.excluded_regions.create(start=62.3, end=180)
experiment.linked_structures.create(structure_id='latp', scale=4.15)
experiment.linked_structures.create(
    structure_id='alpo4_c2221',
    scale=0.54,
)
experiment.linked_structures.create(
    structure_id='alpo4_p63mc',
    scale=1.6,
)
experiment.background.create(id='4', position=4.0117, intensity=37000000)
experiment.background.create(id='5', position=5.3148, intensity=41700000)
experiment.background.create(id='7', position=7.1929, intensity=52700000)
experiment.background.create(id='8', position=8.2721, intensity=67200000)
experiment.background.create(id='9', position=8.9749, intensity=82700000)
experiment.background.create(id='10', position=10.0793, intensity=79800000)
experiment.background.create(id='12', position=12.3508, intensity=48200000)
experiment.background.create(id='14', position=13.9092, intensity=37100000)
experiment.background.create(id='16', position=15.6032, intensity=30700000)
experiment.background.create(id='18', position=18.1069, intensity=26100000)
experiment.background.create(id='20', position=20.4202, intensity=24300000)
experiment.background.create(id='23', position=22.675, intensity=22900000)
experiment.background.create(id='25', position=25.3704, intensity=22700000)
experiment.background.create(id='27', position=27.1127, intensity=25100000)
experiment.background.create(id='30', position=29.6603, intensity=24400000)
experiment.background.create(id='33', position=32.5461, intensity=25900000)
experiment.background.create(id='36', position=35.7233, intensity=19290000)
experiment.background.create(id='38', position=37.9048, intensity=15950000)
experiment.background.create(id='40', position=40.4041, intensity=16580000)
experiment.background.create(id='43', position=42.6881, intensity=18850000)
experiment.background.create(id='45', position=44.899, intensity=18080000)
experiment.background.create(id='47', position=47.0073, intensity=17900000)
experiment.background.create(id='49', position=49.2474, intensity=19470000)
experiment.background.create(id='51', position=51.0337, intensity=20370000)
experiment.background.create(id='53', position=53.2738, intensity=21920000)
experiment.background.create(id='55', position=55.2504, intensity=22390000)
experiment.background.create(id='57', position=56.9107, intensity=21830000)
experiment.background.create(id='59', position=58.6676, intensity=23840000)
experiment.background.create(id='61', position=61.4348, intensity=18960000)
experiment.background.create(id='62', position=62.25, intensity=15500000)

# %% [markdown]
# The constraints the fit keeps, each between two named parameters (aliases).

# %%
project.analysis.aliases.create(id='z_Ti1', param=latp.atom_sites['Ti1'].fract_z)
project.analysis.aliases.create(id='z_Al1', param=latp.atom_sites['Al1'].fract_z)
project.analysis.aliases.create(id='b_Ti1', param=latp.atom_sites['Ti1'].adp_iso)
project.analysis.aliases.create(id='b_Al1', param=latp.atom_sites['Al1'].adp_iso)
project.analysis.aliases.create(id='b2_Al1', param=c2221.atom_sites['Al1'].adp_iso)
project.analysis.aliases.create(id='b2_P1', param=c2221.atom_sites['P1'].adp_iso)
project.analysis.aliases.create(id='b2_O1', param=c2221.atom_sites['O1'].adp_iso)
project.analysis.aliases.create(id='b2_O2', param=c2221.atom_sites['O2'].adp_iso)
project.analysis.constraints.create(id='z_Al1', expression='z_Al1 = z_Ti1')
project.analysis.constraints.create(id='b_Al1', expression='b_Al1 = b_Ti1')
project.analysis.constraints.create(id='b2_P1', expression='b2_P1 = b2_Al1')
project.analysis.constraints.create(id='b2_O1', expression='b2_O1 = b2_Al1')
project.analysis.constraints.create(id='b2_O2', expression='b2_O2 = b2_Al1')

# %%
project.save_as('pd-xray-cwl_latp-bm01_scan')
project.display.constraints()

# %% [markdown]
# The scan's patterns come from the collection as one archive. Unpack them into the project's
# folder and declare them as the scan the sequential fit runs over, from the last file up.

# %%
scan_path = edi.download_data('pd-xray-cwl_latp-bm01_scan-scan', destination='data')
with zipfile.ZipFile(scan_path) as archive:
    archive.extractall('pd-xray-cwl_latp-bm01_scan/experiments/bm01_scan')
project.analysis.sequential_fit.data_dir = 'experiments/bm01_scan'
project.analysis.sequential_fit.file_pattern = '*.dat'
project.analysis.sequential_fit.reverse = True
project.analysis.template_file = 'latp_312.dat'
project.save()

# %% [markdown]
# ## Stage the template fit
#
# The template is the scan's first pattern. Fit it alone first, in stages, so the scan starts from
# a good model: switch the fitting mode to a single fit.

# %%
project.analysis.fitting_mode = 'single'

# %%
project.display.pattern('bm01')

# %% [markdown]
# ## Perform the analysis
#
# The fit goes in stages, freeing one group of parameters at a time.

# %% [markdown]
# ### Scales, 2θ zero and cells
#
# The three phases' scales and cells and the zero shift.

# %%
experiment.linked_structures['latp'].scale.free = True
experiment.linked_structures['alpo4_c2221'].scale.free = True
experiment.linked_structures['alpo4_p63mc'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
for parameter in (
    latp.cell.length_a,
    latp.cell.length_c,
    c2221.cell.length_a,
    c2221.cell.length_b,
    c2221.cell.length_c,
    p63mc.cell.length_a,
    p63mc.cell.length_c,
):
    parameter.free = True

# %%
project.display.parameters.free()

# %%
project.analysis.fit()
project.display.fit.results()

# %%
project.display.pattern('bm01')

# %% [markdown]
# ### Background

# %%
for point in experiment.background:
    point.intensity.free = True

# %%
project.analysis.fit()
project.display.fit.results()

# %%
project.display.pattern('bm01')

# %% [markdown]
# ### Peak widths

# %%
for parameter in (
    experiment.peak.broad_gauss_u,
    experiment.peak.broad_gauss_v,
    experiment.peak.broad_gauss_w,
    experiment.peak.mixing_eta_0,
):
    parameter.free = True

# %%
project.analysis.fit()
project.display.fit.results()

# %%
project.display.pattern('bm01')

# %% [markdown]
# ### Peak asymmetry

# %%
experiment.peak.asym_beba_a0.free = True
experiment.peak.asym_beba_b0.free = True

# %%
project.analysis.fit()
project.display.fit.results()

# %%
project.display.pattern('bm01')

# %% [markdown]
# ### LATP positions
#
# The main phase's free coordinates; Al's follows Ti's.

# %%
for parameter in (
    latp.atom_sites['Ti1'].fract_z,
    latp.atom_sites['P1'].fract_x,
    latp.atom_sites['O1'].fract_x,
    latp.atom_sites['O1'].fract_y,
    latp.atom_sites['O1'].fract_z,
    latp.atom_sites['O2'].fract_x,
    latp.atom_sites['O2'].fract_y,
    latp.atom_sites['O2'].fract_z,
):
    parameter.free = True

# %%
project.analysis.fit()
project.display.fit.results()

# %%
project.display.pattern('bm01')

# %% [markdown]
# ### LATP displacements

# %%
for parameter in (
    latp.atom_sites['Ti1'].adp_iso,
    latp.atom_sites['P1'].adp_iso,
    latp.atom_sites['O1'].adp_iso,
    latp.atom_sites['O2'].adp_iso,
):
    parameter.free = True

# %%
project.analysis.fit()
project.display.fit.results()

# %%
project.display.pattern('bm01')

# %%
project.display.fit.correlations()

# %%
project.display.structure('latp')

# %%
project.display.structure('alpo4_c2221')

# %%
project.display.structure('alpo4_p63mc')

# %% [markdown]
# ## Fit the scan
#
# Back to the sequential mode, with the template's free parameters. Each pattern starts from the
# fit before it.

# %%
project.analysis.fitting_mode = 'sequential'
fitted = []
result = project.fit_sequential(on_file_complete=lambda *args: fitted.append(args))
print(result.status.name.lower(), 'after', len(fitted), 'patterns')

# %% [markdown]
# ## The results
#
# One row per pattern, in the order they were fitted.

# %%
results = Path('pd-xray-cwl_latp-bm01_scan/analysis/results.csv')
with results.open(newline='', encoding='utf-8') as file:
    rows = list(csv.DictReader(file))
print(len(rows), 'rows; columns:', ', '.join(list(rows[0])[:6]), '...')

# %% [markdown]
# ## Report

# %%
project.report.save_html('pd-xray-cwl_latp-bm01_scan.html')

# %% [markdown]
# ## Save the project
#
# The fitted template and the scan results are in the project folder already; save the
# project once more after the fits.

# %%
project.save()
