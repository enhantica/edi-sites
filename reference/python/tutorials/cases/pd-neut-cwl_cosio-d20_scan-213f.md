Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-cwl_cosio-d20_scan-213f/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/d42e09fd8e9ae537bbb4d2d3eb16c49fbe3f7999/docs/user/tutorials/pd-neut-cwl_cosio-d20_scan-213f.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-cwl_cosio-d20_scan-213f.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Co₂SiO₄ on D20, cooling scan

Fit the olivine Co₂SiO₄ with its magnetic structure to the whole D20 cooling scan, 213 patterns
from 497.4 K down to 2.3 K, one after another and from the lowest temperature up. First the fit
is staged on the 2.3 K pattern, the scan's template; then each later pattern starts from the
previous result. The cobalt moments stay free at every temperature and fall towards zero near
the Néel temperature, about 50 K.

The project is the catalogue case `pd-neut-cwl_cosio-d20_scan-213f`, the one the command line
and the app's Examples open. Its two Co sites share one displacement from the start.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0NDggNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTIyNC4yOTk4MDQ2ODc1IDI3My4wQzIzMy43MDAxOTUzMTI1IDI2My41OTk2MDkzNzUgMjMzLjcwMDE5NTMxMjUgMjQ4LjQwMDM5MDYyNSAyMjQuMjAwMTk1MzEyNSAyMzkuMEw4OC4yMDAxOTUzMTI1IDEwMy4wQzc4LjkwMDM5MDYyNSA5My41OTk2MDkzNzUgNjMuNzAwMTk1MzEyNSA5My41OTk2MDkzNzUgNTQuMjk5ODA0Njg3NSAxMDMuMEwzMS43OTk4MDQ2ODc1IDEyNS43OTk4MDQ2ODc1QzIyLjQwMDM5MDYyNSAxMzUuMDk5NjA5Mzc1IDIyLjQwMDM5MDYyNSAxNTAuMjk5ODA0Njg3NSAzMS43OTk4MDQ2ODc1IDE1OS43MDAxOTUzMTI1TDEyOC4yMDAxOTUzMTI1IDI1Ni4wOTk2MDkzNzVMMzEuNzk5ODA0Njg3NSAzNTIuNUMyMi40MDAzOTA2MjUgMzYxLjc5OTgwNDY4NzUgMjIuNDAwMzkwNjI1IDM3Ny4wIDMxLjc5OTgwNDY4NzUgMzg2LjQwMDM5MDYyNUw1NC40MDAzOTA2MjUgNDA5LjBDNjMuNzAwMTk1MzEyNSA0MTguNDAwMzkwNjI1IDc4LjkwMDM5MDYyNSA0MTguNDAwMzkwNjI1IDg4LjI5OTgwNDY4NzUgNDA5LjBaTTQxNi4yOTk4MDQ2ODc1IDIzOS4wIDI4MC4yOTk4MDQ2ODc1IDEwMy4wQzI3MC45MDAzOTA2MjUgOTMuNTk5NjA5Mzc1IDI1NS43MDAxOTUzMTI1IDkzLjU5OTYwOTM3NSAyNDYuNDAwMzkwNjI1IDEwMy4wTDIyMy43OTk4MDQ2ODc1IDEyNS41OTk2MDkzNzVDMjE0LjQwMDM5MDYyNSAxMzUuMCAyMTQuNDAwMzkwNjI1IDE1MC4yMDAxOTUzMTI1IDIyMy43OTk4MDQ2ODc1IDE1OS41TDMyMC4yMDAxOTUzMTI1IDI1NS45MDAzOTA2MjVMMjIzLjc5OTgwNDY4NzUgMzUyLjI5OTgwNDY4NzVDMjE0LjQwMDM5MDYyNSAzNjEuNzAwMTk1MzEyNSAyMTQuNDAwMzkwNjI1IDM3Ni45MDAzOTA2MjUgMjIzLjc5OTgwNDY4NzUgMzg2LjIwMDE5NTMxMjVMMjQ2LjQwMDM5MDYyNSA0MDguNzk5ODA0Njg3NUMyNTUuNzk5ODA0Njg3NSA0MTguMjAwMTk1MzEyNSAyNzEuMCA0MTguMjAwMTk1MzEyNSAyODAuMjk5ODA0Njg3NSA0MDguNzk5ODA0Njg3NUw0MTYuMjk5ODA0Njg3NSAyNzIuNzk5ODA0Njg3NUM0MjUuNzAwMTk1MzEyNSAyNjMuNTk5NjA5Mzc1IDQyNS43MDAxOTUzMTI1IDI0OC40MDAzOTA2MjUgNDE2LjI5OTgwNDY4NzUgMjM5LjBaIi8+PC9zdmc+Cg==" alt="" width="12" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Sequential</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span> <span style="color:#c2185b;background:#c2185b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjYzIxODViIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTE2NC4wNzAzMTI1IDE0OC4wOTk2MDkzNzVDMTY0LjA4Mzk4NDM3NSAxNDguMDk5NjA5Mzc1IDE2NC4wOTY2Nzk2ODc1IDE0OC4xMDI1MzkwNjI1IDE2NC4xMTAzNTE1NjI1IDE0OC4xMDI1MzkwNjI1QzE3MC42NzI4NTE1NjI1IDE0OC4xMDI1MzkwNjI1IDE3Ni4wMDA5NzY1NjI1IDE0Mi43NzQ0MTQwNjI1IDE3Ni4wMDA5NzY1NjI1IDEzNi4yMTE5MTQwNjI1QzE3Ni4wMDA5NzY1NjI1IDEzNi4xNzQ4MDQ2ODc1IDE3Ni4wIDEzNi4xMzc2OTUzMTI1IDE3Ni4wIDEzNi4wOTk2MDkzNzVWNTYuMDk5NjA5Mzc1QzE3Ni4wIDM2LjIzMTQ0NTMxMjUgMTU5Ljg2OTE0MDYyNSAyMC4wOTk2MDkzNzUgMTQwLjAgMjAuMDk5NjA5Mzc1SDM2LjBDMTYuMTMwODU5Mzc1IDIwLjA5OTYwOTM3NSAwLjAgMzYuMjMxNDQ1MzEyNSAwLjAgNTYuMDk5NjA5Mzc1VjEzNi4wOTk2MDkzNzVDMC4wIDE0Mi43MjI2NTYyNSA1LjM3Njk1MzEyNSAxNDguMDk5NjA5Mzc1IDEyLjAgMTQ4LjA5OTYwOTM3NVpNNTEyLjAgMTM2LjA5OTYwOTM3NVY1Ni4wQzUxMi4wIDM2LjEzMDg1OTM3NSA0OTUuODY5MTQwNjI1IDIwLjAgNDc2LjAgMjAuMEgzNzIuMEMzNTIuMTMwODU5Mzc1IDIwLjAgMzM2LjAgMzYuMTMwODU5Mzc1IDMzNi4wIDU2LjBWMTM2LjBDMzM2LjAgMTQyLjYyMzA0Njg3NSAzNDEuMzc2OTUzMTI1IDE0OC4wIDM0OC4wIDE0OC4wSDUwMC4wQzUwMC4wMzcxMDkzNzUgMTQ4LjAgNTAwLjA3NDIxODc1IDE0OC4wMDA5NzY1NjI1IDUwMC4xMTIzMDQ2ODc1IDE0OC4wMDA5NzY1NjI1QzUwNi42NzQ4MDQ2ODc1IDE0OC4wMDA5NzY1NjI1IDUxMi4wMDE5NTMxMjUgMTQyLjY3Mjg1MTU2MjUgNTEyLjAwMTk1MzEyNSAxMzYuMTEwMzUxNTYyNUM1MTIuMDAxOTUzMTI1IDEzNi4xMDc0MjE4NzUgNTEyLjAgMTM2LjEwMzUxNTYyNSA1MTIuMCAxMzYuMDk5NjA5Mzc1Wk0zNDguMCAxODAuMDk5NjA5Mzc1QzM0MS4zNzY5NTMxMjUgMTgwLjA5OTYwOTM3NSAzMzYuMCAxODUuNDc2NTYyNSAzMzYuMCAxOTIuMDk5NjA5Mzc1VjI0NC4wOTk2MDkzNzVDMzM2LjAgMzcyLjIwMDE5NTMxMjUgMTc2LjAgMzcyLjAgMTc2LjAgMjQ0LjA5OTYwOTM3NVYxOTIuMDk5NjA5Mzc1QzE3Ni4wIDE4NS40NzY1NjI1IDE3MC42MjMwNDY4NzUgMTgwLjA5OTYwOTM3NSAxNjQuMCAxODAuMDk5NjA5Mzc1SDEyLjA5OTYwOTM3NUM1LjQ3NjU2MjUgMTgwLjA5OTYwOTM3NSAwLjA5OTYwOTM3NSAxODUuNDc2NTYyNSAwLjA5OTYwOTM3NSAxOTIuMDk5NjA5Mzc1VjE5Mi4yMDAxOTUzMTI1QzAuMjAwMTk1MzEyNSAyMTMuNTk5NjA5Mzc1IDAuNzAwMTk1MzEyNSAyMzIuNSAwLjA5OTYwOTM3NSAyNDUuNUMwLjA5OTYwOTM3NSAzOTYuMDk5NjA5Mzc1IDEzNi4yNjk1MzEyNSA0OTIuMDk5NjA5Mzc1IDI1Ni44NDk2MDkzNzUgNDkyLjA5OTYwOTM3NUMzNzcuNDI5Njg3NSA0OTIuMDk5NjA5Mzc1IDUxMS44NDk2MDkzNzUgMzk2LjA5OTYwOTM3NSA1MTEuODQ5NjA5Mzc1IDI0NS40MDAzOTA2MjVDNTExLjI1IDIzMi41OTk2MDkzNzUgNTExLjY1MDM5MDYyNSAyMTIuNDAwMzkwNjI1IDUxMS44NDk2MDkzNzUgMTkyLjIwMDE5NTMxMjVDNTExLjg1MDU4NTkzNzUgMTkyLjE2NjAxNTYyNSA1MTEuODUwNTg1OTM3NSAxOTIuMTMxODM1OTM3NSA1MTEuODUwNTg1OTM3NSAxOTIuMDk3NjU2MjVDNTExLjg1MDU4NTkzNzUgMTg1LjQ3NTU4NTkzNzUgNTA2LjQ3MjY1NjI1IDE4MC4wOTk2MDkzNzUgNDk5Ljg0OTYwOTM3NSAxODAuMDk5NjA5Mzc1WiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Magnetic structure</span>

```python
import csv
from pathlib import Path

import easydiffraction as edi
```

## Load the project

A sequential fit writes one row per pattern into the project's `analysis/results.csv`, so work
on a copy of the project, saved to a folder of its own.

```python
project_path = edi.download_data('pd-neut-cwl_cosio-d20_scan-213f', destination='data')
project = edi.Project.load(project_path)
project.save_as('pd-neut-cwl_cosio-d20_scan-213f')
structure = project.structures['cosio']
experiment = project.experiments['d20']
```

```text
Data 'pd-neut-cwl_cosio-d20_scan-213f' is at data/pd-neut-cwl_cosio-d20_scan-213f-a86d87ed4b81/pd-neut-cwl_cosio-d20_scan-213f
Saving project to 'pd-neut-cwl_cosio-d20_scan-213f'
```

## Stage the template fit

The template is the 2.3 K pattern. Fit it alone first, in stages, so the scan starts from a
good model: switch the fitting mode to a single fit, and start with nothing free.

```python
project.analysis.fitting_mode = 'single'
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/1.html"></iframe>
</div>

## Perform the analysis

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
<iframe style="width: 100%; height: 236px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/2.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_scan-213f, 1438 pts fitted / 1506 loaded, 5 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       15.23        64.02
      1      0.006     14.24        55.94   12.6% ↓
      2      0.012     14.22        55.83   0.2% ↓
      3      0.017     14.22        55.83   
      4      0.025     14.22        55.83   
  done · converged · 4 iters · reduced χ² 55.83 · Rwp 14.22 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/3.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/4.html"></iframe>
</div>

### Background

The sixteen background points follow the level between the peaks.

```python
for point in experiment.background:
    point.intensity.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_scan-213f, 1438 pts fitted / 1506 loaded, 21 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       14.22        56.46
      1      0.008     13.46        50.59   10.4% ↓
      2      0.017     13.46        50.59   
  done · converged · 2 iters · reduced χ² 50.59 · Rwp 13.46 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/5.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/6.html"></iframe>
</div>

### Peak widths

U, V and W only: across a temperature scan the Lorentzian term and the asymmetry stay at their
2.3 K values, as do the form factor's j2 term.

```python
experiment.peak.broad_gauss_u.free = True
experiment.peak.broad_gauss_v.free = True
experiment.peak.broad_gauss_w.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_scan-213f, 1438 pts fitted / 1506 loaded, 24 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.46        50.70
      1      0.008     13.29        49.39   2.6% ↓
      2      0.015     13.29        49.35   0.1% ↓
      3      0.023     13.28        49.35   
  done · converged · 3 iters · reduced χ² 49.35 · Rwp 13.28 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/7.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/8.html"></iframe>
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
edi fit: project pd-neut-cwl_cosio-d20_scan-213f, 1438 pts fitted / 1506 loaded, 35 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.28        49.74
      1      0.008     13.22        49.28   0.9% ↓
      2      0.015     13.22        49.27   
      3      0.024     13.22        49.27   
  done · converged · 3 iters · reduced χ² 49.27 · Rwp 13.22 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/9.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/10.html"></iframe>
</div>

### Displacements

Co2's displacement follows Co1's by the project's constraint.

```python
for site in structure.atom_sites:
    site.adp_iso.free = not site.adp_iso.user_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_cosio-d20_scan-213f, 1438 pts fitted / 1506 loaded, 40 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.22        49.45
      1      0.009     13.01        47.86   3.2% ↓
      2      0.016     13.00        47.83   0.1% ↓
      3      0.026     13.00        47.83   
  done · converged · 3 iters · reduced χ² 47.83 · Rwp 13.00 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/11.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/12.html"></iframe>
</div>

### Magnetic moments

Last, the moments: Co1 in any direction, Co2 along b.

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
edi fit: project pd-neut-cwl_cosio-d20_scan-213f, 1438 pts fitted / 1506 loaded, 44 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.00        47.97
      1      0.011     10.87        33.54   30.1% ↓
      2      0.018      4.94         6.91   79.4% ↓
      3      0.024      4.71         6.30   8.8% ↓
      4      0.031      4.69         6.25   0.8% ↓
      5      0.041      4.69         6.24   0.2% ↓
      6      0.048      4.69         6.24   
      7      0.056      4.69         6.24   
      8      0.063      4.69         6.24   
      9      0.071      4.69         6.24   
     10      0.078      4.69         6.24   
     11      0.086      4.69         6.24   
     12      0.096      4.69         6.24   
     13      0.103      4.69         6.24   
     14      0.110      4.69         6.24   
     15      0.119      4.69         6.24   
     16      0.127      4.69         6.24   
     17      0.134      4.69         6.24   
     18      0.142      4.69         6.24   
     19      0.149      4.69         6.24   
     20      0.159      4.69         6.24   
     21      0.166      4.69         6.24   
     22      0.177      4.69         6.24   
  done · converged · 22 iters · reduced χ² 6.24 · Rwp 4.69 % · 0.19 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/13.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20_scan-213f/14.html"></iframe>
</div>

## Fit the scan

Back to the sequential mode, with the template's free parameters. The fit can stop between
patterns: here it stops after five, all below 3 K, and the rows it wrote stay.

```python
project.analysis.fitting_mode = 'sequential'
fitted = []
result = project.fit_sequential(
    on_file_complete=lambda *args: fitted.append(args),
    should_cancel=lambda: len(fitted) >= 5,
)
print(result.status.name.lower(), 'after', len(fitted), 'patterns')
```

```text
cancelled after 5 patterns
```

## Resume

Starting again continues with the first pattern that has no row yet, from the last fitted
values. The whole scan takes a while.

```python
result = project.fit_sequential(on_file_complete=lambda *args: fitted.append(args))
print(result.status.name.lower(), 'with', len(fitted), 'patterns fitted in all')
```

```text
done with 213 patterns fitted in all
```

## The moments against temperature

One row per pattern, in the order they were fitted. The moment columns name their site and
component.

```python
results = Path('pd-neut-cwl_cosio-d20_scan-213f/analysis/results.csv')
with results.open(newline='', encoding='utf-8') as file:
    rows = list(csv.DictReader(file))
moments = [name for name in rows[0] if 'crystalaxis' in name and not name.endswith('_su')]
print(len(rows), 'rows; moment columns:', ', '.join(moments))
```

```text
213 rows; moment columns: cosio.atom_site_moment.Co1.crystalaxis_x, cosio.atom_site_moment.Co1.crystalaxis_x.uncertainty, cosio.atom_site_moment.Co1.crystalaxis_y, cosio.atom_site_moment.Co1.crystalaxis_y.uncertainty, cosio.atom_site_moment.Co1.crystalaxis_z, cosio.atom_site_moment.Co1.crystalaxis_z.uncertainty, cosio.atom_site_moment.Co2.crystalaxis_y, cosio.atom_site_moment.Co2.crystalaxis_y.uncertainty
```

## Save the report

The HTML report draws the measured, calculated and difference patterns with the nuclear and the
magnetic reflection positions, and lists the structure and the fit. Open it in a browser.

```python
project.report.save_html('pd-neut-cwl_cosio-d20_scan-213f.html')
```

```text
Saving report to 'pd-neut-cwl_cosio-d20_scan-213f.html'
```
