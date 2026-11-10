Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-cwl_cosio-d20_2k/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/281d1666dcc2210ea837a5b5d68acfbdc2006e28/docs/user/tutorials/pd-neut-cwl_cosio-d20_2k.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-cwl_cosio-d20_2k.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Co₂SiO₄ on D20 at 2.3 K

Fit the magnetic structure of the olivine Co₂SiO₄ to constant-wavelength neutron powder data
from D20 at ILL, measured at 2.3 K, below its ordering temperature. The cobalt moments order with
k = 0 in the magnetic space group Pnma.1: Co1 may point in any direction, Co2 only along b.

The project is the catalogue case `pd-neut-cwl_cosio-d20_2k`, the one the command line and the
app's Examples open. Its two Co sites share one displacement, and the two FCJ asymmetry terms are
tied, from the start.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Single</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span> <span style="color:#c2185b;background:#c2185b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjYzIxODViIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTE2NC4wNzAzMTI1IDE0OC4wOTk2MDkzNzVDMTY0LjA4Mzk4NDM3NSAxNDguMDk5NjA5Mzc1IDE2NC4wOTY2Nzk2ODc1IDE0OC4xMDI1MzkwNjI1IDE2NC4xMTAzNTE1NjI1IDE0OC4xMDI1MzkwNjI1QzE3MC42NzI4NTE1NjI1IDE0OC4xMDI1MzkwNjI1IDE3Ni4wMDA5NzY1NjI1IDE0Mi43NzQ0MTQwNjI1IDE3Ni4wMDA5NzY1NjI1IDEzNi4yMTE5MTQwNjI1QzE3Ni4wMDA5NzY1NjI1IDEzNi4xNzQ4MDQ2ODc1IDE3Ni4wIDEzNi4xMzc2OTUzMTI1IDE3Ni4wIDEzNi4wOTk2MDkzNzVWNTYuMDk5NjA5Mzc1QzE3Ni4wIDM2LjIzMTQ0NTMxMjUgMTU5Ljg2OTE0MDYyNSAyMC4wOTk2MDkzNzUgMTQwLjAgMjAuMDk5NjA5Mzc1SDM2LjBDMTYuMTMwODU5Mzc1IDIwLjA5OTYwOTM3NSAwLjAgMzYuMjMxNDQ1MzEyNSAwLjAgNTYuMDk5NjA5Mzc1VjEzNi4wOTk2MDkzNzVDMC4wIDE0Mi43MjI2NTYyNSA1LjM3Njk1MzEyNSAxNDguMDk5NjA5Mzc1IDEyLjAgMTQ4LjA5OTYwOTM3NVpNNTEyLjAgMTM2LjA5OTYwOTM3NVY1Ni4wQzUxMi4wIDM2LjEzMDg1OTM3NSA0OTUuODY5MTQwNjI1IDIwLjAgNDc2LjAgMjAuMEgzNzIuMEMzNTIuMTMwODU5Mzc1IDIwLjAgMzM2LjAgMzYuMTMwODU5Mzc1IDMzNi4wIDU2LjBWMTM2LjBDMzM2LjAgMTQyLjYyMzA0Njg3NSAzNDEuMzc2OTUzMTI1IDE0OC4wIDM0OC4wIDE0OC4wSDUwMC4wQzUwMC4wMzcxMDkzNzUgMTQ4LjAgNTAwLjA3NDIxODc1IDE0OC4wMDA5NzY1NjI1IDUwMC4xMTIzMDQ2ODc1IDE0OC4wMDA5NzY1NjI1QzUwNi42NzQ4MDQ2ODc1IDE0OC4wMDA5NzY1NjI1IDUxMi4wMDE5NTMxMjUgMTQyLjY3Mjg1MTU2MjUgNTEyLjAwMTk1MzEyNSAxMzYuMTEwMzUxNTYyNUM1MTIuMDAxOTUzMTI1IDEzNi4xMDc0MjE4NzUgNTEyLjAgMTM2LjEwMzUxNTYyNSA1MTIuMCAxMzYuMDk5NjA5Mzc1Wk0zNDguMCAxODAuMDk5NjA5Mzc1QzM0MS4zNzY5NTMxMjUgMTgwLjA5OTYwOTM3NSAzMzYuMCAxODUuNDc2NTYyNSAzMzYuMCAxOTIuMDk5NjA5Mzc1VjI0NC4wOTk2MDkzNzVDMzM2LjAgMzcyLjIwMDE5NTMxMjUgMTc2LjAgMzcyLjAgMTc2LjAgMjQ0LjA5OTYwOTM3NVYxOTIuMDk5NjA5Mzc1QzE3Ni4wIDE4NS40NzY1NjI1IDE3MC42MjMwNDY4NzUgMTgwLjA5OTYwOTM3NSAxNjQuMCAxODAuMDk5NjA5Mzc1SDEyLjA5OTYwOTM3NUM1LjQ3NjU2MjUgMTgwLjA5OTYwOTM3NSAwLjA5OTYwOTM3NSAxODUuNDc2NTYyNSAwLjA5OTYwOTM3NSAxOTIuMDk5NjA5Mzc1VjE5Mi4yMDAxOTUzMTI1QzAuMjAwMTk1MzEyNSAyMTMuNTk5NjA5Mzc1IDAuNzAwMTk1MzEyNSAyMzIuNSAwLjA5OTYwOTM3NSAyNDUuNUMwLjA5OTYwOTM3NSAzOTYuMDk5NjA5Mzc1IDEzNi4yNjk1MzEyNSA0OTIuMDk5NjA5Mzc1IDI1Ni44NDk2MDkzNzUgNDkyLjA5OTYwOTM3NUMzNzcuNDI5Njg3NSA0OTIuMDk5NjA5Mzc1IDUxMS44NDk2MDkzNzUgMzk2LjA5OTYwOTM3NSA1MTEuODQ5NjA5Mzc1IDI0NS40MDAzOTA2MjVDNTExLjI1IDIzMi41OTk2MDkzNzUgNTExLjY1MDM5MDYyNSAyMTIuNDAwMzkwNjI1IDUxMS44NDk2MDkzNzUgMTkyLjIwMDE5NTMxMjVDNTExLjg1MDU4NTkzNzUgMTkyLjE2NjAxNTYyNSA1MTEuODUwNTg1OTM3NSAxOTIuMTMxODM1OTM3NSA1MTEuODUwNTg1OTM3NSAxOTIuMDk3NjU2MjVDNTExLjg1MDU4NTkzNzUgMTg1LjQ3NTU4NTkzNzUgNTA2LjQ3MjY1NjI1IDE4MC4wOTk2MDkzNzUgNDk5Ljg0OTYwOTM3NSAxODAuMDk5NjA5Mzc1WiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Magnetic structure</span>

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('pd-neut-cwl_cosio-d20_2k', destination='data')
project = edi.Project.load(project_path)
structure = project.structures['cosio']
experiment = project.experiments['d20']
project.display.constraints()
```

```text
Data 'pd-neut-cwl_cosio-d20_2k' is at data/pd-neut-cwl_cosio-d20_2k-773039d8ca78/pd-neut-cwl_cosio-d20_2k
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 264px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/1.html"></iframe>
</div>

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/2.html"></iframe>
</div>

## Perform the analysis

The nuclear structure comes first, in the usual order; the magnetic moments come last, once the
nuclear peaks are fitted.

### Scale, 2θ zero and cell

```python
experiment.linked_structures['cosio'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
structure.cell.length_a.free = True
structure.cell.length_b.free = True
structure.cell.length_c.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 236px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 5 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       14.28        56.27
      1      0.003     14.03        54.28   3.5% ↓
      2      0.007     14.03        54.28   
  done · converged · 2 iters · reduced χ² 54.28 · Rwp 14.03 % · 0.01 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/4.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/5.html"></iframe>
</div>

### Background

With the peaks in place, the sixteen background points follow the level between them.

```python
for point in experiment.background:
    point.intensity.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 21 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       14.03        54.89
      1      0.004     13.20        48.60   11.5% ↓
      2      0.009     13.20        48.60   
  done · converged · 2 iters · reduced χ² 48.60 · Rwp 13.20 % · 0.01 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/6.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/7.html"></iframe>
</div>

### Peak widths

```python
experiment.peak.broad_gauss_u.free = True
experiment.peak.broad_gauss_v.free = True
experiment.peak.broad_gauss_w.free = True
experiment.peak.broad_lorentz_y.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 25 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.20        48.74
      1      0.005     13.13        48.24   1.0% ↓
      2      0.008     13.13        48.23   
      3      0.013     13.13        48.23   
  done · converged · 3 iters · reduced χ² 48.23 · Rwp 13.13 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/8.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/9.html"></iframe>
</div>

### Peak asymmetry

The low-angle peaks lean towards low angle. One FCJ term is freed; the other follows it by the
project's constraint.

```python
experiment.peak.asym_fcj_1.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 26 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.13        48.26
      1      0.041     13.13        48.26   
      2      0.045     13.13        48.26   
      3      0.050     13.13        48.26   
      4      0.054     13.13        48.26   
      5      0.059     13.13        48.26   
      6      0.063     13.13        48.26   
      7      0.067     13.13        48.26   
      8      0.071     13.13        48.26   
      9      0.075     13.13        48.25   
     10      0.079     13.13        48.25   
     11      0.084     13.13        48.25   
     12      0.088     13.13        48.25   
     13      0.094     13.13        48.25   
  done · converged · 13 iters · reduced χ² 48.25 · Rwp 13.13 % · 0.10 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/10.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/11.html"></iframe>
</div>

### Atom positions

Co1 sits on a centre of symmetry and the other sites on the mirror plane, so only their free
coordinates are fitted. The displacements stay at their room-temperature values.

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
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 37 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.13        48.63
      1      0.007     13.06        48.16   1.0% ↓
      2      0.013     13.06        48.14   
      3      0.020     13.06        48.14   
  done · converged · 3 iters · reduced χ² 48.14 · Rwp 13.06 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/12.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/13.html"></iframe>
</div>

### Magnetic moments

With the nuclear peaks fitted, the moments fit the magnetic peaks. The magnetic space group lets
Co1 point in any direction and Co2 only along b.

```python
structure.atom_site_moment['Co1'].crystalaxis_x.free = True
structure.atom_site_moment['Co1'].crystalaxis_y.free = True
structure.atom_site_moment['Co1'].crystalaxis_z.free = True
structure.atom_site_moment['Co2'].crystalaxis_y.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 41 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.06        48.28
      1      0.011     10.60        31.78   34.2% ↓
      2      0.016      7.03        13.99   56.0% ↓
      3      0.022      6.74        12.85   8.1% ↓
      4      0.027      6.04        10.33   19.6% ↓
      5      0.032      5.58         8.80   14.8% ↓
      6      0.039      5.42         8.32   5.5% ↓
      7      0.045      5.26         7.84   5.8% ↓
      8      0.050      5.09         7.33   6.4% ↓
      9      0.056      4.91         6.84   6.8% ↓
     10      0.061      4.90         6.80   0.5% ↓
     11      0.067      4.87         6.72   1.2% ↓
     12      0.077      4.87         6.71   0.1% ↓
     13      0.084      4.87         6.71   
     14      0.092      4.87         6.71   
     15      0.099      4.87         6.71   
     16      0.106      4.87         6.71   
     17      0.113      4.87         6.71   
     18      0.120      4.87         6.71   
     19      0.128      4.87         6.71   
     20      0.134      4.87         6.71   
     21      0.141      4.87         6.71   
     22      0.147      4.87         6.71   
     23      0.155      4.87         6.71   
     24      0.161      4.87         6.71   
     25      0.167      4.87         6.71   
     26      0.174      4.87         6.71   
     27      0.182      4.87         6.71   
     28      0.188      4.87         6.71   
     29      0.195      4.87         6.71   
     30      0.201      4.87         6.71   
     31      0.209      4.87         6.71   
     32      0.216      4.87         6.71   
     33      0.222      4.87         6.71   
     34      0.233      4.87         6.71   
  done · converged · 34 iters · reduced χ² 6.71 · Rwp 4.87 % · 0.24 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/14.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/15.html"></iframe>
</div>

### Magnetic form factor

Last, the j2 term of the Co²⁺ form factor, which changes how the magnetic intensities fall with
angle. It moves together with the moments, so it comes after them.

```python
structure.magnetic_form_factor['Co'].j2_coefficient.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_2k, 1438 pts fitted / 1506 loaded, 42 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.87         6.72
      1      0.008      4.72         6.30   6.2% ↓
      2      0.014      4.70         6.26   0.6% ↓
      3      0.023      4.70         6.25   0.3% ↓
      4      0.032      4.70         6.25   
      5      0.038      4.70         6.25   
      6      0.045      4.70         6.25   
      7      0.051      4.70         6.25   
      8      0.058      4.70         6.25   
      9      0.064      4.70         6.25   
     10      0.071      4.70         6.25   
     11      0.078      4.70         6.25   
     12      0.084      4.70         6.25   
     13      0.091      4.70         6.25   
     14      0.097      4.70         6.25   
     15      0.104      4.70         6.25   
     16      0.110      4.70         6.25   
     17      0.119      4.70         6.25   
  done · converged · 17 iters · reduced χ² 6.25 · Rwp 4.70 % · 0.13 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/16.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/17.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/18.html"></iframe>
</div>

```python
project.display.structure('cosio')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_2k/19.html"></iframe>
</div>

## Save the project

```python
project.save_as('pd-neut-cwl_cosio-d20_2k')
project.report.save_html('pd-neut-cwl_cosio-d20_2k.html')
```

```text
Saving project to 'pd-neut-cwl_cosio-d20_2k'
Saving report to 'pd-neut-cwl_cosio-d20_2k.html'
```
