Canonical page: https://easydiffraction.org/python/tutorials/cases/sc-neut-tof_taurine-senju/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/212509209e8914c22f7cde3bcc243dd014c80739/docs/user/tutorials/sc-neut-tof_taurine-senju.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/sc-neut-tof_taurine-senju.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Taurine on SENJU

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1OSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDU5IDIyIj48cmVjdCB3aWR0aD0iNTkiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVDMzIwLjI2MDc0MjE4NzUgMTc5LjAzOTA2MjUgMzEzLjQ3NTU4NTkzNzUgMTczLjM1MTU2MjUgMzA2LjA4OTg0Mzc1IDE2OC4xOTQzMzU5Mzc1QzI5OS42ODg0NzY1NjI1IDE2My43MjU1ODU5Mzc1IDI5MS4wMjczNDM3NSAxNjQuNDA0Mjk2ODc1IDI4NS41MDU4NTkzNzUgMTY5LjkyNDgwNDY4NzVMMjY0LjQ1MjE0ODQzNzUgMTkwLjk4MDQ2ODc1QzI1Ni4xMDE1NjI1IDE5OS4zMzAwNzgxMjUgMjUyLjM1ODM5ODQzNzUgMjEwLjIxODc1IDI1Mi43NTM5MDYyNSAyMjAuNzg2MTMyODEyNUMyNTIuOTU0MTAxNTYyNSAyMjYuMDE3NTc4MTI1IDI1NS42NTAzOTA2MjUgMjMwLjYxMDM1MTU2MjUgMjU5LjcwMTE3MTg3NSAyMzMuMzkxNjAxNTYyNUMyNjIuNjEzMjgxMjUgMjM1LjM5NzQ2MDkzNzUgMjY2LjM0MDgyMDMxMjUgMjM4LjI2NjYwMTU2MjUgMjcwLjA0MTk5MjE4NzUgMjQxLjk2MDkzNzVDMjk4LjExNTIzNDM3NSAyNzAuMDM0MTc5Njg3NSAyOTguMjMzMzk4NDM3NSAzMTUuNTk5NjA5Mzc1IDI3MC4wNDE5OTIxODc1IDM0My43OTEwMTU2MjVMMjAyLjg0MTc5Njg3NSA0MTAuOTgxNDQ1MzEyNUMxNzQuNjAyNTM5MDYyNSA0MzkuMjE5NzI2NTYyNSAxMjguNTQxMDE1NjI1IDQzOS4wNDk4MDQ2ODc1IDEwMC41MTY2MDE1NjI1IDQxMC40NzA3MDMxMjVDNzIuNzY2NjAxNTYyNSAzODIuMTcwODk4NDM3NSA3My42NDY0ODQzNzUgMzM2LjUzNzEwOTM3NSAxMDEuNjcxODc1IDMwOC41MTA3NDIxODc1TDExNC43NTg3ODkwNjI1IDI5NS40MjM4MjgxMjVDMTE5LjEwOTM3NSAyOTEuMDc0MjE4NzUgMTIwLjUyODMyMDMxMjUgMjg0LjYzMzc4OTA2MjUgMTE4LjU0MTk5MjE4NzUgMjc4LjgxMTUyMzQzNzVDMTEyLjY3NzczNDM3NSAyNjEuNjE4MTY0MDYyNSAxMDkuNSAyNDMuODEzNDc2NTYyNSAxMDguODUxNTYyNSAyMjYuMDkwODIwMzEyNUMxMDguMzQzNzUgMjEyLjE4NDU3MDMxMjUgOTEuMzk4NDM3NSAyMDUuNjQ0NTMxMjUgODEuNTU3NjE3MTg3NSAyMTUuNDg1MzUxNTYyNUw0NC40NTIxNDg0Mzc1IDI1Mi41OTA4MjAzMTI1Qy0xNC44MTgzNTkzNzUgMzExLjg1MDU4NTkzNzUgLTE0LjgxODM1OTM3NSA0MDguMjkxMDE1NjI1IDQ0LjQ1MjE0ODQzNzUgNDY3LjU1MDc4MTI1QzEwMy43MTI4OTA2MjUgNTI2LjgxMzQ3NjU2MjUgMjAwLjE0MTYwMTU2MjUgNTI2LjgyMTI4OTA2MjUgMjU5LjQxMjEwOTM3NSA0NjcuNTUwNzgxMjVMMzI2LjYxMjMwNDY4NzUgNDAwLjM1MDU4NTkzNzVDMzI2LjczMjQyMTg3NSA0MDAuMjMxNDQ1MzEyNSAzMjYuODYyMzA0Njg3NSA0MDAuMTAwNTg1OTM3NSAzMjYuOTcxNjc5Njg3NSAzOTkuOTgxNDQ1MzEyNUMzODUuNTM5MDYyNSAzNDEuMDg4ODY3MTg3NSAzODYuMzU5Mzc1IDI0NS4yMDAxOTUzMTI1IDMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVaTTQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVDNDA4LjI4NjEzMjgxMjUgLTE0LjgxMzQ3NjU2MjUgMzExLjg1NzQyMTg3NSAtMTQuODIxMjg5MDYyNSAyNTIuNTg2OTE0MDYyNSA0NC40NDkyMTg3NUwxODUuMzg2NzE4NzUgMTExLjY0OTQxNDA2MjVDMTg1LjI2NjYwMTU2MjUgMTExLjc2ODU1NDY4NzUgMTg1LjEzNjcxODc1IDExMS44OTk0MTQwNjI1IDE4NS4wMjczNDM3NSAxMTIuMDE4NTU0Njg3NUMxMjYuNDYwOTM3NSAxNzAuOTExMTMyODEyNSAxMjUuNjM5NjQ4NDM3NSAyNjYuNzk5ODA0Njg3NSAxODUuMzg2NzE4NzUgMzI2LjYwOTM3NUMxOTEuNzM4MjgxMjUgMzMyLjk1OTk2MDkzNzUgMTk4LjUyMjQ2MDkzNzUgMzM4LjY0ODQzNzUgMjA1LjkwODIwMzEyNSAzNDMuODA0Njg3NUMyMTIuMzA5NTcwMzEyNSAzNDguMjczNDM3NSAyMjAuOTcxNjc5Njg3NSAzNDcuNTkzNzUgMjI2LjQ5MjE4NzUgMzQyLjA3NDIxODc1TDI0Ny41NDU4OTg0Mzc1IDMyMS4wMTg1NTQ2ODc1QzI1NS44OTY0ODQzNzUgMzEyLjY2ODk0NTMxMjUgMjU5LjYzOTY0ODQzNzUgMzAxLjc4MDI3MzQzNzUgMjU5LjI0NDE0MDYyNSAyOTEuMjEyODkwNjI1QzI1OS4wNDM5NDUzMTI1IDI4NS45ODE0NDUzMTI1IDI1Ni4zNDc2NTYyNSAyODEuMzg4NjcxODc1IDI1Mi4yOTY4NzUgMjc4LjYwNzQyMTg3NUMyNDkuMzg0NzY1NjI1IDI3Ni42MDE1NjI1IDI0NS42NTcyMjY1NjI1IDI3My43MzI0MjE4NzUgMjQxLjk1NjA1NDY4NzUgMjcwLjAzODA4NTkzNzVDMjEzLjg4MjgxMjUgMjQxLjk2NDg0Mzc1IDIxMy43NjQ2NDg0Mzc1IDE5Ni4zOTk0MTQwNjI1IDI0MS45NTYwNTQ2ODc1IDE2OC4yMDgwMDc4MTI1TDMwOS4xNTYyNSAxMDEuMDE3NTc4MTI1QzMzNy4zOTQ1MzEyNSA3Mi43NzkyOTY4NzUgMzgzLjQ1NjA1NDY4NzUgNzIuOTQ5MjE4NzUgNDExLjQ4MTQ0NTMxMjUgMTAxLjUyODMyMDMxMjVDNDM5LjIzMTQ0NTMxMjUgMTI5LjgyODEyNSA0MzguMzUyNTM5MDYyNSAxNzUuNDYxOTE0MDYyNSA0MTAuMzI2MTcxODc1IDIwMy40ODgyODEyNUwzOTcuMjM5MjU3ODEyNSAyMTYuNTc1MTk1MzEyNUMzOTIuODg4NjcxODc1IDIyMC45MjQ4MDQ2ODc1IDM5MS40Njk3MjY1NjI1IDIyNy4zNjUyMzQzNzUgMzkzLjQ1NjA1NDY4NzUgMjMzLjE4NjUyMzQzNzVDMzk5LjMyMDMxMjUgMjUwLjM4MDg1OTM3NSA0MDIuNDk4MDQ2ODc1IDI2OC4xODU1NDY4NzUgNDAzLjE0NjQ4NDM3NSAyODUuOTA4MjAzMTI1QzQwMy42NTUyNzM0Mzc1IDI5OS44MTQ0NTMxMjUgNDIwLjU5OTYwOTM3NSAzMDYuMzUzNTE1NjI1IDQzMC40NDA0Mjk2ODc1IDI5Ni41MTM2NzE4NzVMNDY3LjU0NTg5ODQzNzUgMjU5LjQwODIwMzEyNUM1MjYuODE3MzgyODEyNSAyMDAuMTQ5NDE0MDYyNSA1MjYuODE3MzgyODEyNSAxMDMuNzA4OTg0Mzc1IDQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5Kb2ludDwvdGV4dD48L3N2Zz4=" alt="Joint" width="59" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+c2M8L3RleHQ+PC9zdmc+" alt="sc" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+bmV1dDwvdGV4dD48L3N2Zz4=" alt="neut" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI4IDIyIj48cmVjdCB3aWR0aD0iMjgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+dG9mPC90ZXh0Pjwvc3ZnPg==" alt="tof" width="28" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

Fit the amino-sulfonic acid taurine to six time-of-flight neutron single-crystal datasets from
SENJU at J-PARC together, each reflection measured at its own wavelength.

It builds the catalogue case `sc-neut-tof_taurine-senju` step by step: the same project the
command line fits and the app's Examples open. Banks 2 to 6 share bank 1's three extinction
terms.

## Import the library

```python
import easydiffraction as edi
```

## Define the project

A new project is empty: it holds no structure and no experiment until you add them. The joint
fitting mode fits every experiment at once, against one set of structures.

```python
project = edi.Project(name='sc-neut-tof_taurine-senju')
project.analysis.fitting_mode = 'joint'
```

## Define the structure

Load the structure from EasyDiffraction's collection. Its CIF gives the space group, the cell and
the atom sites.

```python
path = edi.download_data('sc-neut-tof_taurine-senju-taurine', destination='data')
project.structures.add_from_cif_path(path)
structure = project.structures['taurine']
```

```text
Data 'sc-neut-tof_taurine-senju-taurine' is at data/sc-neut-tof_taurine-senju-taurine.edi
```

```python
project.display.structure('taurine')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/1.html"></iframe>
</div>

## Define the experiments

Create the six experiments from their measured data in EasyDiffraction's collection, then
describe each one's instrument, peak profile, background and the structures it links.

```python
data_path = edi.download_data('sc-neut-tof_taurine-senju-senju_1-data', destination='data')
project.experiments.add_from_data_path(
    name='senju_1',
    data_path=data_path,
    sample_form='single crystal',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
senju_1 = project.experiments['senju_1']
senju_1.neutron_scattering_length = 'sears1992'
senju_1.extinction.type = 'larson-anisotropic'
senju_1.instrument.name = 'SENJU'
senju_1.instrument.facility = 'J-PARC'
senju_1.linked_structures.create(structure_id='taurine', scale=2.762)
```

```text
Data 'sc-neut-tof_taurine-senju-senju_1-data' is at data/sc-neut-tof_taurine-senju-senju_1.hkl
```

```python
data_path = edi.download_data('sc-neut-tof_taurine-senju-senju_2-data', destination='data')
project.experiments.add_from_data_path(
    name='senju_2',
    data_path=data_path,
    sample_form='single crystal',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
senju_2 = project.experiments['senju_2']
senju_2.neutron_scattering_length = 'sears1992'
senju_2.extinction.type = 'larson-anisotropic'
senju_2.instrument.name = 'SENJU'
senju_2.instrument.facility = 'J-PARC'
senju_2.linked_structures.create(structure_id='taurine', scale=3.829)
```

```text
Data 'sc-neut-tof_taurine-senju-senju_2-data' is at data/sc-neut-tof_taurine-senju-senju_2.hkl
```

```python
data_path = edi.download_data('sc-neut-tof_taurine-senju-senju_3-data', destination='data')
project.experiments.add_from_data_path(
    name='senju_3',
    data_path=data_path,
    sample_form='single crystal',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
senju_3 = project.experiments['senju_3']
senju_3.neutron_scattering_length = 'sears1992'
senju_3.extinction.type = 'larson-anisotropic'
senju_3.instrument.name = 'SENJU'
senju_3.instrument.facility = 'J-PARC'
senju_3.linked_structures.create(structure_id='taurine', scale=3.211)
```

```text
Data 'sc-neut-tof_taurine-senju-senju_3-data' is at data/sc-neut-tof_taurine-senju-senju_3.hkl
```

```python
data_path = edi.download_data('sc-neut-tof_taurine-senju-senju_4-data', destination='data')
project.experiments.add_from_data_path(
    name='senju_4',
    data_path=data_path,
    sample_form='single crystal',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
senju_4 = project.experiments['senju_4']
senju_4.neutron_scattering_length = 'sears1992'
senju_4.extinction.type = 'larson-anisotropic'
senju_4.instrument.name = 'SENJU'
senju_4.instrument.facility = 'J-PARC'
senju_4.linked_structures.create(structure_id='taurine', scale=2.809)
```

```text
Data 'sc-neut-tof_taurine-senju-senju_4-data' is at data/sc-neut-tof_taurine-senju-senju_4.hkl
```

```python
data_path = edi.download_data('sc-neut-tof_taurine-senju-senju_5-data', destination='data')
project.experiments.add_from_data_path(
    name='senju_5',
    data_path=data_path,
    sample_form='single crystal',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
senju_5 = project.experiments['senju_5']
senju_5.neutron_scattering_length = 'sears1992'
senju_5.extinction.type = 'larson-anisotropic'
senju_5.instrument.name = 'SENJU'
senju_5.instrument.facility = 'J-PARC'
senju_5.linked_structures.create(structure_id='taurine', scale=2.739)
```

```text
Data 'sc-neut-tof_taurine-senju-senju_5-data' is at data/sc-neut-tof_taurine-senju-senju_5.hkl
```

```python
data_path = edi.download_data('sc-neut-tof_taurine-senju-senju_6-data', destination='data')
project.experiments.add_from_data_path(
    name='senju_6',
    data_path=data_path,
    sample_form='single crystal',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
senju_6 = project.experiments['senju_6']
senju_6.neutron_scattering_length = 'sears1992'
senju_6.extinction.type = 'larson-anisotropic'
senju_6.instrument.name = 'SENJU'
senju_6.instrument.facility = 'J-PARC'
senju_6.linked_structures.create(structure_id='taurine', scale=2.936)
```

```text
Data 'sc-neut-tof_taurine-senju-senju_6-data' is at data/sc-neut-tof_taurine-senju-senju_6.hkl
```

The constraints the fit keeps, each between two named parameters (aliases).

```python
project.analysis.aliases.create(id='x11_1', param=senju_1.extinction.coefficient_11)
project.analysis.aliases.create(id='x22_1', param=senju_1.extinction.coefficient_22)
project.analysis.aliases.create(id='x33_1', param=senju_1.extinction.coefficient_33)
project.analysis.aliases.create(id='x11_2', param=senju_2.extinction.coefficient_11)
project.analysis.aliases.create(id='x22_2', param=senju_2.extinction.coefficient_22)
project.analysis.aliases.create(id='x33_2', param=senju_2.extinction.coefficient_33)
project.analysis.aliases.create(id='x11_3', param=senju_3.extinction.coefficient_11)
project.analysis.aliases.create(id='x22_3', param=senju_3.extinction.coefficient_22)
project.analysis.aliases.create(id='x33_3', param=senju_3.extinction.coefficient_33)
project.analysis.aliases.create(id='x11_4', param=senju_4.extinction.coefficient_11)
project.analysis.aliases.create(id='x22_4', param=senju_4.extinction.coefficient_22)
project.analysis.aliases.create(id='x33_4', param=senju_4.extinction.coefficient_33)
project.analysis.aliases.create(id='x11_5', param=senju_5.extinction.coefficient_11)
project.analysis.aliases.create(id='x22_5', param=senju_5.extinction.coefficient_22)
project.analysis.aliases.create(id='x33_5', param=senju_5.extinction.coefficient_33)
project.analysis.aliases.create(id='x11_6', param=senju_6.extinction.coefficient_11)
project.analysis.aliases.create(id='x22_6', param=senju_6.extinction.coefficient_22)
project.analysis.aliases.create(id='x33_6', param=senju_6.extinction.coefficient_33)
project.analysis.constraints.create(id='x11_2', expression='x11_2 = x11_1')
project.analysis.constraints.create(id='x22_2', expression='x22_2 = x22_1')
project.analysis.constraints.create(id='x33_2', expression='x33_2 = x33_1')
project.analysis.constraints.create(id='x11_3', expression='x11_3 = x11_1')
project.analysis.constraints.create(id='x22_3', expression='x22_3 = x22_1')
project.analysis.constraints.create(id='x33_3', expression='x33_3 = x33_1')
project.analysis.constraints.create(id='x11_4', expression='x11_4 = x11_1')
project.analysis.constraints.create(id='x22_4', expression='x22_4 = x22_1')
project.analysis.constraints.create(id='x33_4', expression='x33_4 = x33_1')
project.analysis.constraints.create(id='x11_5', expression='x11_5 = x11_1')
project.analysis.constraints.create(id='x22_5', expression='x22_5 = x22_1')
project.analysis.constraints.create(id='x33_5', expression='x33_5 = x33_1')
project.analysis.constraints.create(id='x11_6', expression='x11_6 = x11_1')
project.analysis.constraints.create(id='x22_6', expression='x22_6 = x22_1')
project.analysis.constraints.create(id='x33_6', expression='x33_6 = x33_1')
```

```python
project.display.constraints()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 1020px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/2.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/3.html"></iframe>
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
<iframe style="width: 100%; height: 264px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/4.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 1540 pts fitted / 1540 loaded, 6 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                       603.89     39397.22
      1      0.032      74.43       598.54   98.5% ↓
  done · converged · 1 iters · reduced χ² 598.54 · wR(F²) 74.43 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/5.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/6.html"></iframe>
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
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 1540 pts fitted / 1540 loaded, 20 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        74.43       604.05
      1      0.023      58.82       377.23   37.6% ↓
      2      0.028      58.82       377.22   
  done · converged · 2 iters · reduced χ² 377.22 · wR(F²) 58.82 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/7.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/8.html"></iframe>
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
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 1540 pts fitted / 1540 loaded, 23 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        58.82       377.97
      1      0.028      56.89       353.56   6.5% ↓
      2      0.032      56.89       353.56   
  done · converged · 2 iters · reduced χ² 353.56 · wR(F²) 56.89 % · 0.04 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/9.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/10.html"></iframe>
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
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 1540 pts fitted / 1540 loaded, 65 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        56.89       363.63
      1      0.045      55.50       346.03   4.8% ↓
      2      0.052      54.60       334.99   3.2% ↓
      3      0.058      48.09       259.81   22.4% ↓
      4      0.069      41.94       197.62   23.9% ↓
      5      0.075      34.60       134.50   31.9% ↓
      6      0.081      32.18       116.35   13.5% ↓
      7      0.088      31.76       113.36   2.6% ↓
      8      0.094      31.67       112.70   0.6% ↓
      9      0.100      31.65       112.56   0.1% ↓
     10      0.107      31.65       112.53   
     11      0.114      31.65       112.52   
     12      0.120      31.65       112.52   
  done · converged · 12 iters · reduced χ² 112.52 · wR(F²) 31.65 % · 0.13 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/11.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/12.html"></iframe>
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
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.S1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.O1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.O2.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.O3.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.N1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H2.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H3.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.C1.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H11.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H12.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.C2.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H21.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
/tmp/ipykernel_4291/4011545669.py:4: UserWarning: crysta.domain.dependent_free_ignored: parameter 'taurine.atom_site.H22.adp_iso' is constrained by 'the equivalent isotropic value of its beta tensor'; free = True is ignored and it stays dependent (cannot be fitted: set by a constraint)
  tensor.adp_11.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project sc-neut-tof_taurine-senju, 6 banks (senju_1, senju_2, senju_3, senju_4, senju_5, senju_6), 1540 pts fitted / 1540 loaded, 135 free
   iter   time (s) wR(F²) (%)  reduced χ²   change
                        31.65       118.12
      1      0.104      20.73        50.70   57.1% ↓
      2      0.119      20.69        50.47   0.5% ↓
      3      0.133      20.68        50.43   0.1% ↓
      4      0.149      20.68        50.42   
      5      0.164      20.68        50.42   
  done · converged · 5 iters · reduced χ² 50.42 · wR(F²) 20.68 % · 0.20 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/13.html"></iframe>
</div>

```python
project.display.pattern('senju_1')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/14.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/15.html"></iframe>
</div>

```python
project.display.structure('taurine')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/sc-neut-tof_taurine-senju/16.html"></iframe>
</div>

## Report

The HTML report draws the measured, calculated and difference patterns with the reflection
positions, and lists the structures, the experiments and the fit. Open it in a browser.

```python
project.report.save_html('sc-neut-tof_taurine-senju.html')
```

```text
Saving report to 'sc-neut-tof_taurine-senju.html'
```

## Save the project

```python
project.save_as('sc-neut-tof_taurine-senju')
```

```text
Saving project to 'sc-neut-tof_taurine-senju'
```
