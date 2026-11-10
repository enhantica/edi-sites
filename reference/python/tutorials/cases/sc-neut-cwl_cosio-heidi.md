Canonical page: https://easydiffraction.org/python/tutorials/cases/sc-neut-cwl_cosio-heidi/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/d42e09fd8e9ae537bbb4d2d3eb16c49fbe3f7999/docs/user/tutorials/sc-neut-cwl_cosio-heidi.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/sc-neut-cwl_cosio-heidi.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Co₂SiO₄ on HEiDi

Fit one Co₂SiO₄ crystal measured on HEiDi at MLZ at 300 K, 55 K and 2.5 K. Each temperature has
its own structure and its own reflections, and the three are fitted independently: each fit sees
only its own data and gives its own goodness of fit and uncertainties. At 2.5 K the cobalt
moments order, and the magnetic structure is fitted too.

The data are those of Sazonov et al., Acta Cryst. B 64 (2008) 661-668. The 2.5 K file has no
usable uncertainties, so they are estimated from the 55 K data of the same crystal (see the
case's provenance); the fitted 2.5 K uncertainties depend on that estimate.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTUwNC45NzA3MDMxMjUgMzU5LjAyOTI5Njg3NSA0MjQuOTcwNzAzMTI1IDI3OS4wNDc4NTE1NjI1QzQwOS45NDMzNTkzNzUgMjY0LjAyMTQ4NDM3NSAzODQuMCAyNzQuNTgxMDU0Njg3NSAzODQuMCAyOTYuMDE4NTU0Njg3NVYzMzYuMEgzNTIuMEwyOTkuMjE4NzUgMjc5LjQ0OTIxODc1TDI0NS44ODU3NDIxODc1IDMzNi41OTE3OTY4NzVMMzE2LjQ0MjM4MjgxMjUgNDEyLjE4ODQ3NjU2MjVDMzE4LjYzMzc4OTA2MjUgNDE0LjUzNTE1NjI1IDMyMS43NTM5MDYyNSA0MTYuMCAzMjUuMjE0ODQzNzUgNDE2LjBIMzg0LjBWNDU1Ljk4MzM5ODQzNzVDMzg0LjAgNDc3LjQ0NDMzNTkzNzUgNDA5Ljk2MDkzNzUgNDg3Ljk2Mzg2NzE4NzUgNDI0Ljk3MDcwMzEyNSA0NzIuOTU0MTAxNTYyNUw1MDQuOTcwNzAzMTI1IDM5Mi45Njk3MjY1NjI1QzUxNC4zNDM3NSAzODMuNTk3NjU2MjUgNTE0LjM0Mzc1IDM2OC40MDIzNDM3NSA1MDQuOTcwNzAzMTI1IDM1OS4wMjkyOTY4NzVaTTEyLjAgMTc2LjBIOTYuMEwxNDguNzgxMjUgMjMyLjU1MDc4MTI1TDIwMi4xMTQyNTc4MTI1IDE3NS40MDgyMDMxMjVMMTMxLjU1NzYxNzE4NzUgOTkuODExNTIzNDM3NUMxMjkuMzY3MTg3NSA5Ny40NjQ4NDM3NSAxMjYuMjQ2MDkzNzUgOTYuMCAxMjIuNzg1MTU2MjUgOTYuMEgxMi4wQzUuMzczMDQ2ODc1IDk2LjAgMC4wIDEwMS4zNzMwNDY4NzUgMC4wIDEwOC4wVjE2NC4wQzAuMCAxNzAuNjI2OTUzMTI1IDUuMzczMDQ2ODc1IDE3Ni4wIDEyLjAgMTc2LjBaTTM4NC4wIDE3Ni4wVjIxNS45ODQzNzVDMzg0LjAgMjM3LjQ0NDMzNTkzNzUgNDA5Ljk2MDkzNzUgMjQ3Ljk2Mzg2NzE4NzUgNDI0Ljk3MDcwMzEyNSAyMzIuOTU1MDc4MTI1TDUwNC45NzA3MDMxMjUgMTUyLjk3MDcwMzEyNUM1MTQuMzQzNzUgMTQzLjU5NzY1NjI1IDUxNC4zNDM3NSAxMjguNDAyMzQzNzUgNTA0Ljk3MDcwMzEyNSAxMTkuMDMwMjczNDM3NUw0MjQuOTcwNzAzMTI1IDM5LjA0ODgyODEyNUM0MDkuOTQzMzU5Mzc1IDI0LjAyMTQ4NDM3NSAzODQuMCAzNC41ODIwMzEyNSAzODQuMCA1Ni4wMTg1NTQ2ODc1Vjk2LjBIMzI1LjIxNDg0Mzc1QzMyMS43NTM5MDYyNSA5Ni4wIDMxOC42MzM3ODkwNjI1IDk3LjQ2NDg0Mzc1IDMxNi40NDIzODI4MTI1IDk5LjgxMTUyMzQzNzVMOTYuMCAzMzYuMEgxMi4wQzUuMzczMDQ2ODc1IDMzNi4wIDAuMCAzNDEuMzczMDQ2ODc1IDAuMCAzNDguMFY0MDQuMEMwLjAgNDEwLjYyNjk1MzEyNSA1LjM3MzA0Njg3NSA0MTYuMCAxMi4wIDQxNi4wSDEyMi43ODUxNTYyNUMxMjYuMTExMzI4MTI1IDQxNi4wIDEyOS4yODgwODU5Mzc1IDQxNC42MTkxNDA2MjUgMTMxLjU1NzYxNzE4NzUgNDEyLjE4ODQ3NjU2MjVMMzUyLjAgMTc2LjBaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Independent</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">sc</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span> <span style="color:#c2185b;background:#c2185b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjYzIxODViIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTE2NC4wNzAzMTI1IDE0OC4wOTk2MDkzNzVDMTY0LjA4Mzk4NDM3NSAxNDguMDk5NjA5Mzc1IDE2NC4wOTY2Nzk2ODc1IDE0OC4xMDI1MzkwNjI1IDE2NC4xMTAzNTE1NjI1IDE0OC4xMDI1MzkwNjI1QzE3MC42NzI4NTE1NjI1IDE0OC4xMDI1MzkwNjI1IDE3Ni4wMDA5NzY1NjI1IDE0Mi43NzQ0MTQwNjI1IDE3Ni4wMDA5NzY1NjI1IDEzNi4yMTE5MTQwNjI1QzE3Ni4wMDA5NzY1NjI1IDEzNi4xNzQ4MDQ2ODc1IDE3Ni4wIDEzNi4xMzc2OTUzMTI1IDE3Ni4wIDEzNi4wOTk2MDkzNzVWNTYuMDk5NjA5Mzc1QzE3Ni4wIDM2LjIzMTQ0NTMxMjUgMTU5Ljg2OTE0MDYyNSAyMC4wOTk2MDkzNzUgMTQwLjAgMjAuMDk5NjA5Mzc1SDM2LjBDMTYuMTMwODU5Mzc1IDIwLjA5OTYwOTM3NSAwLjAgMzYuMjMxNDQ1MzEyNSAwLjAgNTYuMDk5NjA5Mzc1VjEzNi4wOTk2MDkzNzVDMC4wIDE0Mi43MjI2NTYyNSA1LjM3Njk1MzEyNSAxNDguMDk5NjA5Mzc1IDEyLjAgMTQ4LjA5OTYwOTM3NVpNNTEyLjAgMTM2LjA5OTYwOTM3NVY1Ni4wQzUxMi4wIDM2LjEzMDg1OTM3NSA0OTUuODY5MTQwNjI1IDIwLjAgNDc2LjAgMjAuMEgzNzIuMEMzNTIuMTMwODU5Mzc1IDIwLjAgMzM2LjAgMzYuMTMwODU5Mzc1IDMzNi4wIDU2LjBWMTM2LjBDMzM2LjAgMTQyLjYyMzA0Njg3NSAzNDEuMzc2OTUzMTI1IDE0OC4wIDM0OC4wIDE0OC4wSDUwMC4wQzUwMC4wMzcxMDkzNzUgMTQ4LjAgNTAwLjA3NDIxODc1IDE0OC4wMDA5NzY1NjI1IDUwMC4xMTIzMDQ2ODc1IDE0OC4wMDA5NzY1NjI1QzUwNi42NzQ4MDQ2ODc1IDE0OC4wMDA5NzY1NjI1IDUxMi4wMDE5NTMxMjUgMTQyLjY3Mjg1MTU2MjUgNTEyLjAwMTk1MzEyNSAxMzYuMTEwMzUxNTYyNUM1MTIuMDAxOTUzMTI1IDEzNi4xMDc0MjE4NzUgNTEyLjAgMTM2LjEwMzUxNTYyNSA1MTIuMCAxMzYuMDk5NjA5Mzc1Wk0zNDguMCAxODAuMDk5NjA5Mzc1QzM0MS4zNzY5NTMxMjUgMTgwLjA5OTYwOTM3NSAzMzYuMCAxODUuNDc2NTYyNSAzMzYuMCAxOTIuMDk5NjA5Mzc1VjI0NC4wOTk2MDkzNzVDMzM2LjAgMzcyLjIwMDE5NTMxMjUgMTc2LjAgMzcyLjAgMTc2LjAgMjQ0LjA5OTYwOTM3NVYxOTIuMDk5NjA5Mzc1QzE3Ni4wIDE4NS40NzY1NjI1IDE3MC42MjMwNDY4NzUgMTgwLjA5OTYwOTM3NSAxNjQuMCAxODAuMDk5NjA5Mzc1SDEyLjA5OTYwOTM3NUM1LjQ3NjU2MjUgMTgwLjA5OTYwOTM3NSAwLjA5OTYwOTM3NSAxODUuNDc2NTYyNSAwLjA5OTYwOTM3NSAxOTIuMDk5NjA5Mzc1VjE5Mi4yMDAxOTUzMTI1QzAuMjAwMTk1MzEyNSAyMTMuNTk5NjA5Mzc1IDAuNzAwMTk1MzEyNSAyMzIuNSAwLjA5OTYwOTM3NSAyNDUuNUMwLjA5OTYwOTM3NSAzOTYuMDk5NjA5Mzc1IDEzNi4yNjk1MzEyNSA0OTIuMDk5NjA5Mzc1IDI1Ni44NDk2MDkzNzUgNDkyLjA5OTYwOTM3NUMzNzcuNDI5Njg3NSA0OTIuMDk5NjA5Mzc1IDUxMS44NDk2MDkzNzUgMzk2LjA5OTYwOTM3NSA1MTEuODQ5NjA5Mzc1IDI0NS40MDAzOTA2MjVDNTExLjI1IDIzMi41OTk2MDkzNzUgNTExLjY1MDM5MDYyNSAyMTIuNDAwMzkwNjI1IDUxMS44NDk2MDkzNzUgMTkyLjIwMDE5NTMxMjVDNTExLjg1MDU4NTkzNzUgMTkyLjE2NjAxNTYyNSA1MTEuODUwNTg1OTM3NSAxOTIuMTMxODM1OTM3NSA1MTEuODUwNTg1OTM3NSAxOTIuMDk3NjU2MjVDNTExLjg1MDU4NTkzNzUgMTg1LjQ3NTU4NTkzNzUgNTA2LjQ3MjY1NjI1IDE4MC4wOTk2MDkzNzUgNDk5Ljg0OTYwOTM3NSAxODAuMDk5NjA5Mzc1WiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Magnetic structure</span>

## Import the library

```python
import easydiffraction as edi
```

## Define the project

The independent fitting mode fits each experiment on its own, against the structure it links.

```python
project = edi.Project(name='cosio_heidi')
project.analysis.fitting_mode = 'independent'
```

## Define the structures

Load the three structures from EasyDiffraction's collection, one per temperature. Each starts
from the published positions with a small displacement tensor on every site. The 2.5 K structure
also carries the magnetic space group Pnma.1 and the moment directions it allows, Co1 in any
direction and Co2 along b, with every moment at zero. The files mark what the fit frees; the fit
below frees it in stages, so start with all of it fixed.

```python
path = edi.download_data('sc-neut-cwl_cosio-heidi-cosio_300k', destination='data')
project.structures.add_from_cif_path(path)
path = edi.download_data('sc-neut-cwl_cosio-heidi-cosio_55k', destination='data')
project.structures.add_from_cif_path(path)
path = edi.download_data('sc-neut-cwl_cosio-heidi-cosio_2k5', destination='data')
project.structures.add_from_cif_path(path)
for parameter in project.free_parameters:
    parameter.free = False
```

```text
Data 'sc-neut-cwl_cosio-heidi-cosio_300k' is at data/sc-neut-cwl_cosio-heidi-cosio_300k.edi
Data 'sc-neut-cwl_cosio-heidi-cosio_55k' is at data/sc-neut-cwl_cosio-heidi-cosio_55k.edi
Data 'sc-neut-cwl_cosio-heidi-cosio_2k5' is at data/sc-neut-cwl_cosio-heidi-cosio_2k5.edi
```

```python
project.display.structure('cosio_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/1.html"></iframe>
</div>

## Define the experiments

Load the reflections of each temperature and link each dataset to its structure. HEiDi's
wavelength is 0.552 Å; the extinction is FullProf's anisotropic Larson model, with its six
coefficients starting at zero.

```python
data_paths = {
    '300k': edi.download_data('sc-neut-cwl_cosio-heidi-heidi_300k-data', destination='data'),
    '55k': edi.download_data('sc-neut-cwl_cosio-heidi-heidi_55k-data', destination='data'),
    '2k5': edi.download_data('sc-neut-cwl_cosio-heidi-heidi_2k5-data', destination='data'),
}
for temperature, path in data_paths.items():
    project.experiments.add_from_data_path(
        name=f'heidi_{temperature}',
        data_path=path,
        sample_form='single crystal',
        beam_mode='constant wavelength',
        radiation_probe='neutron',
        scattering_type='bragg',
    )
    experiment = project.experiments[f'heidi_{temperature}']
    experiment.instrument.setup_wavelength = 0.552
    experiment.extinction.type = 'larson-anisotropic'
    experiment.linked_structures.create(structure_id=f'cosio_{temperature}', scale=10)
```

```text
Data 'sc-neut-cwl_cosio-heidi-heidi_300k-data' is at data/sc-neut-cwl_cosio-heidi-heidi_300k.hkl
Data 'sc-neut-cwl_cosio-heidi-heidi_55k-data' is at data/sc-neut-cwl_cosio-heidi-heidi_55k.hkl
Data 'sc-neut-cwl_cosio-heidi-heidi_2k5-data' is at data/sc-neut-cwl_cosio-heidi-heidi_2k5.hkl
```

Names for the three structures and experiments.

```python
structure_300k = project.structures['cosio_300k']
structure_55k = project.structures['cosio_55k']
structure_2k5 = project.structures['cosio_2k5']
experiment_300k = project.experiments['heidi_300k']
experiment_55k = project.experiments['heidi_55k']
experiment_2k5 = project.experiments['heidi_2k5']
```

## Perform the analysis

An experiment with nothing free is left out of a fit, so the first stages fit 300 K alone. Each
stage frees one new group: the structure's coordinates and displacement components are the ones
its site symmetry leaves free.

The 300 K reflections against the starting model:

```python
project.display.pattern('heidi_300k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/2.html"></iframe>
</div>

### 300 K: scale

The scale brings the calculated intensities to the measured ones.

```python
experiment_300k.linked_structures['cosio_300k'].scale.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 124px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 1 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        33.37        14.23
      1      0.001      15.51         3.07   78.4% ↓
      2      0.003      15.51         3.07   
  done · converged · 2 iters · reduced χ² 3.07 · wR(F²) 15.51 % · 0.00 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/4.html"></iframe>
</div>

```python
project.display.pattern('heidi_300k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/5.html"></iframe>
</div>

### 300 K: coordinates

```python
for site in structure_300k.atom_sites:
    for coordinate in (site.fract_x, site.fract_y, site.fract_z):
        coordinate.free = not coordinate.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 12 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        15.51         3.09
      1      0.002      15.34         3.03   2.2% ↓
      2      0.004      15.34         3.03   
      3      0.006      15.34         3.03   
  done · converged · 3 iters · reduced χ² 3.03 · wR(F²) 15.34 % · 0.01 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/6.html"></iframe>
</div>

```python
project.display.pattern('heidi_300k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/7.html"></iframe>
</div>

### 300 K: displacements

```python
for tensor in structure_300k.atom_site_aniso:
    for component in (
        tensor.adp_11,
        tensor.adp_22,
        tensor.adp_33,
        tensor.adp_12,
        tensor.adp_13,
        tensor.adp_23,
    ):
        component.free = not component.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 40 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        15.34         3.08
      1      0.004       7.73         0.78   74.6% ↓
      2      0.010       7.67         0.77   1.7% ↓
      3      0.016       7.67         0.77   
  done · converged · 3 iters · reduced χ² 0.77 · wR(F²) 7.67 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/8.html"></iframe>
</div>

```python
project.display.pattern('heidi_300k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/9.html"></iframe>
</div>

### 300 K: extinction

Larson's anisotropic extinction, its six coefficients starting at zero.

```python
experiment_300k.extinction.coefficient_11.free = True
experiment_300k.extinction.coefficient_22.free = True
experiment_300k.extinction.coefficient_33.free = True
experiment_300k.extinction.coefficient_12.free = True
experiment_300k.extinction.coefficient_13.free = True
experiment_300k.extinction.coefficient_23.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         7.67         0.77
      1      0.006       6.25         0.51   33.6% ↓
      2      0.013       6.16         0.50   2.9% ↓
      3      0.019       6.15         0.50   
      4      0.025       6.15         0.50   
  done · converged · 4 iters · reduced χ² 0.50 · wR(F²) 6.15 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/10.html"></iframe>
</div>

```python
project.display.pattern('heidi_300k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/11.html"></iframe>
</div>

### 55 K: scale

The 300 K parameters stay free, so the 300 K experiment is fitted again from where it ended.

```python
experiment_55k.linked_structures['cosio_55k'].scale.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.005       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 1 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        36.92        69.94
      1      0.001       8.90         4.06   94.2% ↓
      2      0.003       8.90         4.06   
      3      0.005       8.90         4.06   
  done · converged · 4 iters · reduced χ² 2.21 · wR(F²) 8.38 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/12.html"></iframe>
</div>

```python
project.display.pattern('heidi_55k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/13.html"></iframe>
</div>

### 55 K: coordinates

```python
for site in structure_55k.atom_sites:
    for coordinate in (site.fract_x, site.fract_y, site.fract_z):
        coordinate.free = not coordinate.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.007       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 12 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         8.90         4.09
      1      0.002       8.78         3.98   2.7% ↓
      2      0.005       8.78         3.98   
      3      0.007       8.78         3.98   
  done · converged · 4 iters · reduced χ² 2.17 · wR(F²) 8.28 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/14.html"></iframe>
</div>

```python
project.display.pattern('heidi_55k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/15.html"></iframe>
</div>

### 55 K: extinction

At 55 K the displacements are small. Freed before the extinction, they would take its place and
Co1's tensor would stop being positive definite, so the extinction comes before them here.

```python
experiment_55k.extinction.coefficient_11.free = True
experiment_55k.extinction.coefficient_22.free = True
experiment_55k.extinction.coefficient_33.free = True
experiment_55k.extinction.coefficient_12.free = True
experiment_55k.extinction.coefficient_13.free = True
experiment_55k.extinction.coefficient_23.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.005       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 18 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         8.78         4.00
      1      0.002       6.80         2.40   40.1% ↓
      2      0.004       6.58         2.25   6.2% ↓
      3      0.006       6.58         2.25   0.1% ↓
      4      0.008       6.58         2.25   
  done · converged · 5 iters · reduced χ² 1.33 · wR(F²) 6.49 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/16.html"></iframe>
</div>

```python
project.display.pattern('heidi_55k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/17.html"></iframe>
</div>

### 55 K: displacements

```python
for tensor in structure_55k.atom_site_aniso:
    for component in (
        tensor.adp_11,
        tensor.adp_22,
        tensor.adp_33,
        tensor.adp_12,
        tensor.adp_13,
        tensor.adp_23,
    ):
        component.free = not component.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.006       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.58         2.29
      1      0.004       3.80         0.76   66.6% ↓
      2      0.009       3.79         0.76   0.4% ↓
      3      0.013       3.79         0.76   
  done · converged · 4 iters · reduced χ² 0.62 · wR(F²) 4.41 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/18.html"></iframe>
</div>

```python
project.display.pattern('heidi_55k')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/19.html"></iframe>
</div>

### 2.5 K: scale

The nuclear structure first, with every moment still at zero, in the order 55 K needed.

```python
experiment_2k5.linked_structures['cosio_2k5'].scale.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.008       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         3.79         0.76
      1      0.006       3.79         0.76   
edi fit: project cosio_heidi, 1424 pts fitted / 1424 loaded, 1 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        39.10        63.48
      1      0.001      13.12         7.15   88.7% ↓
      2      0.003      13.12         7.15   
      3      0.004      13.12         7.15   
  done · converged · 5 iters · reduced χ² 2.72 · wR(F²) 8.82 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/20.html"></iframe>
</div>

```python
project.display.pattern('heidi_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/21.html"></iframe>
</div>

### 2.5 K: coordinates

```python
for site in structure_2k5.atom_sites:
    for coordinate in (site.fract_x, site.fract_y, site.fract_z):
        coordinate.free = not coordinate.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.006       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         3.79         0.76
      1      0.004       3.79         0.76   
edi fit: project cosio_heidi, 1424 pts fitted / 1424 loaded, 12 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        13.12         7.21
      1      0.002      13.01         7.08   1.7% ↓
      2      0.004      13.01         7.08   
      3      0.006      13.01         7.08   
  done · converged · 5 iters · reduced χ² 2.69 · wR(F²) 8.75 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/22.html"></iframe>
</div>

```python
project.display.pattern('heidi_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/23.html"></iframe>
</div>

### 2.5 K: extinction

```python
experiment_2k5.extinction.coefficient_11.free = True
experiment_2k5.extinction.coefficient_22.free = True
experiment_2k5.extinction.coefficient_33.free = True
experiment_2k5.extinction.coefficient_12.free = True
experiment_2k5.extinction.coefficient_13.free = True
experiment_2k5.extinction.coefficient_23.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.007       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         3.79         0.76
      1      0.005       3.79         0.76   
edi fit: project cosio_heidi, 1424 pts fitted / 1424 loaded, 18 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        13.01         7.11
      1      0.002      11.97         6.02   15.4% ↓
      2      0.005      11.88         5.93   1.4% ↓
      3      0.008      11.88         5.93   
      4      0.011      11.88         5.93   
  done · converged · 6 iters · reduced χ² 2.32 · wR(F²) 8.12 % · 0.04 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/24.html"></iframe>
</div>

```python
project.display.pattern('heidi_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/25.html"></iframe>
</div>

### 2.5 K: displacements

```python
for tensor in structure_2k5.atom_site_aniso:
    for component in (
        tensor.adp_11,
        tensor.adp_22,
        tensor.adp_33,
        tensor.adp_12,
        tensor.adp_13,
        tensor.adp_23,
    ):
        component.free = not component.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.013       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         3.79         0.76
      1      0.007       3.79         0.76   
edi fit: project cosio_heidi, 1424 pts fitted / 1424 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        11.88         6.05
      1      0.007      10.52         4.74   21.6% ↓
      2      0.013      10.51         4.74   0.1% ↓
      3      0.020      10.51         4.74   
  done · converged · 5 iters · reduced χ² 1.92 · wR(F²) 7.36 % · 0.07 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/26.html"></iframe>
</div>

Some reflections stay far from their measured intensity: (1 0 0), (0 0 1) and (1 1 0) among
them. Pnma forbids them for nuclear scattering, so with the moments at zero their calculated
intensity is zero; at 2.5 K they are magnetic.

```python
project.display.pattern('heidi_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/27.html"></iframe>
</div>

### 2.5 K: the magnetic moments

Free the moment components the magnetic space group allows. They start at zero, where the
magnetic intensity has no slope, so the fit starts them at 1 μB and says so.

```python
structure_2k5.atom_site_moment['Co1'].crystalaxis_x.free = True
structure_2k5.atom_site_moment['Co1'].crystalaxis_y.free = True
structure_2k5.atom_site_moment['Co1'].crystalaxis_z.free = True
structure_2k5.atom_site_moment['Co2'].crystalaxis_y.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_heidi, 1624 pts fitted / 1624 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         6.15         0.50
      1      0.013       6.15         0.50   
edi fit: project cosio_heidi, 1465 pts fitted / 1465 loaded, 46 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                         3.79         0.76
      1      0.008       3.79         0.76   
edi fit: project cosio_heidi, 1424 pts fitted / 1424 loaded, 50 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        10.51         4.76
      1      0.010       9.16         3.61   24.1% ↓
      2      0.020       3.94         0.67   81.5% ↓
      3      0.029       3.77         0.61   8.2% ↓
      4      0.039       3.77         0.61   
      5      0.049       3.77         0.61   
  done · converged · 7 iters · reduced χ² 0.62 · wR(F²) 4.18 % · 0.10 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/28.html"></iframe>
</div>

```python
project.display.pattern('heidi_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/29.html"></iframe>
</div>

Sazonov et al., Acta Cryst. B 65 (2009) 664-675, Table 4, give Co1 (1.20(3), 3.64(2), 0.57(9))
μB and Co2 3.35(2) μB along b. The fitted moments' uncertainties rest on the estimated 2.5 K
uncertainties.

```python
project.display.structure('cosio_2k5')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-cwl_cosio-heidi/30.html"></iframe>
</div>

## Save the project

```python
project.save_as('sc-neut-cwl_cosio-heidi')
project.report.save_html('sc-neut-cwl_cosio-heidi.html')
```

```text
Saving project to 'sc-neut-cwl_cosio-heidi'
Saving report to 'sc-neut-cwl_cosio-heidi.html'
```
