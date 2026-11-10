Canonical page: https://easydiffraction.org/python/tutorials/cases/sc-neut-tof_taurine-senju/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/e9334c7713570499c3a02e4010c0832ce46d44fd/docs/user/tutorials/sc-neut-tof_taurine-senju.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/sc-neut-tof_taurine-senju.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Taurine on SENJU

Fit the amino-sulfonic acid taurine to six time-of-flight neutron single-crystal datasets from
SENJU at J-PARC together, each reflection measured at its own wavelength.

The project is the catalogue case `sc-neut-tof_taurine-senju`, the one the command line and the
app's Examples open. Banks 2 to 6 share bank 1's three extinction terms, from the start.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVDMzIwLjI2MDc0MjE4NzUgMTc5LjAzOTA2MjUgMzEzLjQ3NTU4NTkzNzUgMTczLjM1MTU2MjUgMzA2LjA4OTg0Mzc1IDE2OC4xOTQzMzU5Mzc1QzI5OS42ODg0NzY1NjI1IDE2My43MjU1ODU5Mzc1IDI5MS4wMjczNDM3NSAxNjQuNDA0Mjk2ODc1IDI4NS41MDU4NTkzNzUgMTY5LjkyNDgwNDY4NzVMMjY0LjQ1MjE0ODQzNzUgMTkwLjk4MDQ2ODc1QzI1Ni4xMDE1NjI1IDE5OS4zMzAwNzgxMjUgMjUyLjM1ODM5ODQzNzUgMjEwLjIxODc1IDI1Mi43NTM5MDYyNSAyMjAuNzg2MTMyODEyNUMyNTIuOTU0MTAxNTYyNSAyMjYuMDE3NTc4MTI1IDI1NS42NTAzOTA2MjUgMjMwLjYxMDM1MTU2MjUgMjU5LjcwMTE3MTg3NSAyMzMuMzkxNjAxNTYyNUMyNjIuNjEzMjgxMjUgMjM1LjM5NzQ2MDkzNzUgMjY2LjM0MDgyMDMxMjUgMjM4LjI2NjYwMTU2MjUgMjcwLjA0MTk5MjE4NzUgMjQxLjk2MDkzNzVDMjk4LjExNTIzNDM3NSAyNzAuMDM0MTc5Njg3NSAyOTguMjMzMzk4NDM3NSAzMTUuNTk5NjA5Mzc1IDI3MC4wNDE5OTIxODc1IDM0My43OTEwMTU2MjVMMjAyLjg0MTc5Njg3NSA0MTAuOTgxNDQ1MzEyNUMxNzQuNjAyNTM5MDYyNSA0MzkuMjE5NzI2NTYyNSAxMjguNTQxMDE1NjI1IDQzOS4wNDk4MDQ2ODc1IDEwMC41MTY2MDE1NjI1IDQxMC40NzA3MDMxMjVDNzIuNzY2NjAxNTYyNSAzODIuMTcwODk4NDM3NSA3My42NDY0ODQzNzUgMzM2LjUzNzEwOTM3NSAxMDEuNjcxODc1IDMwOC41MTA3NDIxODc1TDExNC43NTg3ODkwNjI1IDI5NS40MjM4MjgxMjVDMTE5LjEwOTM3NSAyOTEuMDc0MjE4NzUgMTIwLjUyODMyMDMxMjUgMjg0LjYzMzc4OTA2MjUgMTE4LjU0MTk5MjE4NzUgMjc4LjgxMTUyMzQzNzVDMTEyLjY3NzczNDM3NSAyNjEuNjE4MTY0MDYyNSAxMDkuNSAyNDMuODEzNDc2NTYyNSAxMDguODUxNTYyNSAyMjYuMDkwODIwMzEyNUMxMDguMzQzNzUgMjEyLjE4NDU3MDMxMjUgOTEuMzk4NDM3NSAyMDUuNjQ0NTMxMjUgODEuNTU3NjE3MTg3NSAyMTUuNDg1MzUxNTYyNUw0NC40NTIxNDg0Mzc1IDI1Mi41OTA4MjAzMTI1Qy0xNC44MTgzNTkzNzUgMzExLjg1MDU4NTkzNzUgLTE0LjgxODM1OTM3NSA0MDguMjkxMDE1NjI1IDQ0LjQ1MjE0ODQzNzUgNDY3LjU1MDc4MTI1QzEwMy43MTI4OTA2MjUgNTI2LjgxMzQ3NjU2MjUgMjAwLjE0MTYwMTU2MjUgNTI2LjgyMTI4OTA2MjUgMjU5LjQxMjEwOTM3NSA0NjcuNTUwNzgxMjVMMzI2LjYxMjMwNDY4NzUgNDAwLjM1MDU4NTkzNzVDMzI2LjczMjQyMTg3NSA0MDAuMjMxNDQ1MzEyNSAzMjYuODYyMzA0Njg3NSA0MDAuMTAwNTg1OTM3NSAzMjYuOTcxNjc5Njg3NSAzOTkuOTgxNDQ1MzEyNUMzODUuNTM5MDYyNSAzNDEuMDg4ODY3MTg3NSAzODYuMzU5Mzc1IDI0NS4yMDAxOTUzMTI1IDMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVaTTQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVDNDA4LjI4NjEzMjgxMjUgLTE0LjgxMzQ3NjU2MjUgMzExLjg1NzQyMTg3NSAtMTQuODIxMjg5MDYyNSAyNTIuNTg2OTE0MDYyNSA0NC40NDkyMTg3NUwxODUuMzg2NzE4NzUgMTExLjY0OTQxNDA2MjVDMTg1LjI2NjYwMTU2MjUgMTExLjc2ODU1NDY4NzUgMTg1LjEzNjcxODc1IDExMS44OTk0MTQwNjI1IDE4NS4wMjczNDM3NSAxMTIuMDE4NTU0Njg3NUMxMjYuNDYwOTM3NSAxNzAuOTExMTMyODEyNSAxMjUuNjM5NjQ4NDM3NSAyNjYuNzk5ODA0Njg3NSAxODUuMzg2NzE4NzUgMzI2LjYwOTM3NUMxOTEuNzM4MjgxMjUgMzMyLjk1OTk2MDkzNzUgMTk4LjUyMjQ2MDkzNzUgMzM4LjY0ODQzNzUgMjA1LjkwODIwMzEyNSAzNDMuODA0Njg3NUMyMTIuMzA5NTcwMzEyNSAzNDguMjczNDM3NSAyMjAuOTcxNjc5Njg3NSAzNDcuNTkzNzUgMjI2LjQ5MjE4NzUgMzQyLjA3NDIxODc1TDI0Ny41NDU4OTg0Mzc1IDMyMS4wMTg1NTQ2ODc1QzI1NS44OTY0ODQzNzUgMzEyLjY2ODk0NTMxMjUgMjU5LjYzOTY0ODQzNzUgMzAxLjc4MDI3MzQzNzUgMjU5LjI0NDE0MDYyNSAyOTEuMjEyODkwNjI1QzI1OS4wNDM5NDUzMTI1IDI4NS45ODE0NDUzMTI1IDI1Ni4zNDc2NTYyNSAyODEuMzg4NjcxODc1IDI1Mi4yOTY4NzUgMjc4LjYwNzQyMTg3NUMyNDkuMzg0NzY1NjI1IDI3Ni42MDE1NjI1IDI0NS42NTcyMjY1NjI1IDI3My43MzI0MjE4NzUgMjQxLjk1NjA1NDY4NzUgMjcwLjAzODA4NTkzNzVDMjEzLjg4MjgxMjUgMjQxLjk2NDg0Mzc1IDIxMy43NjQ2NDg0Mzc1IDE5Ni4zOTk0MTQwNjI1IDI0MS45NTYwNTQ2ODc1IDE2OC4yMDgwMDc4MTI1TDMwOS4xNTYyNSAxMDEuMDE3NTc4MTI1QzMzNy4zOTQ1MzEyNSA3Mi43NzkyOTY4NzUgMzgzLjQ1NjA1NDY4NzUgNzIuOTQ5MjE4NzUgNDExLjQ4MTQ0NTMxMjUgMTAxLjUyODMyMDMxMjVDNDM5LjIzMTQ0NTMxMjUgMTI5LjgyODEyNSA0MzguMzUyNTM5MDYyNSAxNzUuNDYxOTE0MDYyNSA0MTAuMzI2MTcxODc1IDIwMy40ODgyODEyNUwzOTcuMjM5MjU3ODEyNSAyMTYuNTc1MTk1MzEyNUMzOTIuODg4NjcxODc1IDIyMC45MjQ4MDQ2ODc1IDM5MS40Njk3MjY1NjI1IDIyNy4zNjUyMzQzNzUgMzkzLjQ1NjA1NDY4NzUgMjMzLjE4NjUyMzQzNzVDMzk5LjMyMDMxMjUgMjUwLjM4MDg1OTM3NSA0MDIuNDk4MDQ2ODc1IDI2OC4xODU1NDY4NzUgNDAzLjE0NjQ4NDM3NSAyODUuOTA4MjAzMTI1QzQwMy42NTUyNzM0Mzc1IDI5OS44MTQ0NTMxMjUgNDIwLjU5OTYwOTM3NSAzMDYuMzUzNTE1NjI1IDQzMC40NDA0Mjk2ODc1IDI5Ni41MTM2NzE4NzVMNDY3LjU0NTg5ODQzNzUgMjU5LjQwODIwMzEyNUM1MjYuODE3MzgyODEyNSAyMDAuMTQ5NDE0MDYyNSA1MjYuODE3MzgyODEyNSAxMDMuNzA4OTg0Mzc1IDQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Joint</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">sc</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">tof</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span>

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('sc-neut-tof_taurine-senju', destination='data')
project = edi.Project.load(project_path)
structure = project.structures['taurine']
senju_1 = project.experiments['senju_1']
senju_2 = project.experiments['senju_2']
senju_3 = project.experiments['senju_3']
senju_4 = project.experiments['senju_4']
senju_5 = project.experiments['senju_5']
senju_6 = project.experiments['senju_6']
project.display.constraints()
```

```text
Data 'sc-neut-tof_taurine-senju' is at data/sc-neut-tof_taurine-senju-b5deb357e7e8/sc-neut-tof_taurine-senju
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 1020px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/1.html"></iframe>
</div>

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/2.html"></iframe>
</div>

## Perform the analysis

The fit follows diffraction-lib's change of model for this case: isotropic displacements first,
then anisotropic tensors. diffraction-lib does not fit the positions, which this case does, so
they get a stage of their own.

### Scales, every site isotropic

Each bank's scale, with every site's displacement isotropic for now.

```python
for site in structure.atom_sites:
    site.adp_type = 'Biso'
for experiment in project.experiments:
    experiment.linked_structures['taurine'].scale.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 264px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 947 pts fitted / 1540 loaded, 6 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                       179.47      5665.97
      1      0.002      51.73       470.74   91.7% ↓
      2      0.004      51.73       470.73   
  done · converged · 2 iters · reduced χ² 470.73 · wR(F²) 51.73 % · 0.01 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/4.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/5.html"></iframe>
</div>

### Isotropic displacements

Every site's isotropic displacement.

```python
for site in structure.atom_sites:
    site.adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 947 pts fitted / 1540 loaded, 20 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        51.73       477.84
      1      0.005      31.17       173.48   63.7% ↓
      2      0.009      27.18       131.89   24.0% ↓
      3      0.012      26.94       129.62   1.7% ↓
      4      0.017      26.94       129.57   
      5      0.020      26.94       129.56   
      6      0.024      26.94       129.56   
  done · converged · 6 iters · reduced χ² 129.56 · wR(F²) 26.94 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/6.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/7.html"></iframe>
</div>

### Extinction

Bank 1's three extinction terms, which the other banks share.

```python
senju_1.extinction.coefficient_11.free = True
senju_1.extinction.coefficient_22.free = True
senju_1.extinction.coefficient_33.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 947 pts fitted / 1540 loaded, 23 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        26.94       129.98
      1      0.004      22.14        87.84   32.4% ↓
      2      0.009      20.47        75.09   14.5% ↓
      3      0.014      20.27        73.57   2.0% ↓
      4      0.018      20.26        73.55   
      5      0.024      20.26        73.55   
  done · converged · 5 iters · reduced χ² 73.55 · wR(F²) 20.26 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/8.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/9.html"></iframe>
</div>

### Positions

All fourteen sites' coordinates.

```python
for site in structure.atom_sites:
    site.fract_x.free = True
    site.fract_y.free = True
    site.fract_z.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 947 pts fitted / 1540 loaded, 65 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        20.26        77.05
      1      0.009      17.17        55.36   28.2% ↓
      2      0.017      17.04        54.51   1.5% ↓
      3      0.023      17.04        54.49   
      4      0.029      17.04        54.49   
  done · converged · 4 iters · reduced χ² 54.49 · wR(F²) 17.04 % · 0.04 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/10.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/11.html"></iframe>
</div>

### Anisotropic displacements

Back to anisotropic displacements (edi converts the values), with every tensor component free.

```python
for site in structure.atom_sites:
    site.adp_type = 'beta'
for tensor in structure.atom_site_aniso:
    tensor.adp_11.free = True
    tensor.adp_22.free = True
    tensor.adp_33.free = True
    tensor.adp_12.free = True
    tensor.adp_13.free = True
    tensor.adp_23.free = True
```

```text
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.S1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.O1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.O2.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.O3.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.N1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H2.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H3.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.C1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H11.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H12.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.C2.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H21.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4169/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H22.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 947 pts fitted / 1540 loaded, 135 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        17.04        59.19
      1      0.017      13.02        34.56   41.6% ↓
      2      0.033      12.20        30.32   12.3% ↓
      3      0.049      12.19        30.27   0.2% ↓
      4      0.066      12.19        30.27   
  done · converged · 4 iters · reduced χ² 30.27 · wR(F²) 12.19 % · 0.12 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/12.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/13.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/14.html"></iframe>
</div>

```python
project.display.structure('taurine')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/15.html"></iframe>
</div>

## Save the project

```python
project.save_as('sc-neut-tof_taurine-senju')
project.report.save_html('sc-neut-tof_taurine-senju.html')
```

```text
Saving project to 'sc-neut-tof_taurine-senju'
Saving report to 'sc-neut-tof_taurine-senju.html'
```
