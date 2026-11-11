Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-xray-cwl_pbso4-d1a-lab/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/d7c02db17aac3254f27711b10edc61accb050d80/docs/user/tutorials/pd-neut-xray-cwl_pbso4-d1a-lab.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-xray-cwl_pbso4-d1a-lab.ipynb){ .md-button .ed-tutorial-button download }
</div>

# PbSO₄ on D1A and a laboratory diffractometer

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1OSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDU5IDIyIj48cmVjdCB3aWR0aD0iNTkiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVDMzIwLjI2MDc0MjE4NzUgMTc5LjAzOTA2MjUgMzEzLjQ3NTU4NTkzNzUgMTczLjM1MTU2MjUgMzA2LjA4OTg0Mzc1IDE2OC4xOTQzMzU5Mzc1QzI5OS42ODg0NzY1NjI1IDE2My43MjU1ODU5Mzc1IDI5MS4wMjczNDM3NSAxNjQuNDA0Mjk2ODc1IDI4NS41MDU4NTkzNzUgMTY5LjkyNDgwNDY4NzVMMjY0LjQ1MjE0ODQzNzUgMTkwLjk4MDQ2ODc1QzI1Ni4xMDE1NjI1IDE5OS4zMzAwNzgxMjUgMjUyLjM1ODM5ODQzNzUgMjEwLjIxODc1IDI1Mi43NTM5MDYyNSAyMjAuNzg2MTMyODEyNUMyNTIuOTU0MTAxNTYyNSAyMjYuMDE3NTc4MTI1IDI1NS42NTAzOTA2MjUgMjMwLjYxMDM1MTU2MjUgMjU5LjcwMTE3MTg3NSAyMzMuMzkxNjAxNTYyNUMyNjIuNjEzMjgxMjUgMjM1LjM5NzQ2MDkzNzUgMjY2LjM0MDgyMDMxMjUgMjM4LjI2NjYwMTU2MjUgMjcwLjA0MTk5MjE4NzUgMjQxLjk2MDkzNzVDMjk4LjExNTIzNDM3NSAyNzAuMDM0MTc5Njg3NSAyOTguMjMzMzk4NDM3NSAzMTUuNTk5NjA5Mzc1IDI3MC4wNDE5OTIxODc1IDM0My43OTEwMTU2MjVMMjAyLjg0MTc5Njg3NSA0MTAuOTgxNDQ1MzEyNUMxNzQuNjAyNTM5MDYyNSA0MzkuMjE5NzI2NTYyNSAxMjguNTQxMDE1NjI1IDQzOS4wNDk4MDQ2ODc1IDEwMC41MTY2MDE1NjI1IDQxMC40NzA3MDMxMjVDNzIuNzY2NjAxNTYyNSAzODIuMTcwODk4NDM3NSA3My42NDY0ODQzNzUgMzM2LjUzNzEwOTM3NSAxMDEuNjcxODc1IDMwOC41MTA3NDIxODc1TDExNC43NTg3ODkwNjI1IDI5NS40MjM4MjgxMjVDMTE5LjEwOTM3NSAyOTEuMDc0MjE4NzUgMTIwLjUyODMyMDMxMjUgMjg0LjYzMzc4OTA2MjUgMTE4LjU0MTk5MjE4NzUgMjc4LjgxMTUyMzQzNzVDMTEyLjY3NzczNDM3NSAyNjEuNjE4MTY0MDYyNSAxMDkuNSAyNDMuODEzNDc2NTYyNSAxMDguODUxNTYyNSAyMjYuMDkwODIwMzEyNUMxMDguMzQzNzUgMjEyLjE4NDU3MDMxMjUgOTEuMzk4NDM3NSAyMDUuNjQ0NTMxMjUgODEuNTU3NjE3MTg3NSAyMTUuNDg1MzUxNTYyNUw0NC40NTIxNDg0Mzc1IDI1Mi41OTA4MjAzMTI1Qy0xNC44MTgzNTkzNzUgMzExLjg1MDU4NTkzNzUgLTE0LjgxODM1OTM3NSA0MDguMjkxMDE1NjI1IDQ0LjQ1MjE0ODQzNzUgNDY3LjU1MDc4MTI1QzEwMy43MTI4OTA2MjUgNTI2LjgxMzQ3NjU2MjUgMjAwLjE0MTYwMTU2MjUgNTI2LjgyMTI4OTA2MjUgMjU5LjQxMjEwOTM3NSA0NjcuNTUwNzgxMjVMMzI2LjYxMjMwNDY4NzUgNDAwLjM1MDU4NTkzNzVDMzI2LjczMjQyMTg3NSA0MDAuMjMxNDQ1MzEyNSAzMjYuODYyMzA0Njg3NSA0MDAuMTAwNTg1OTM3NSAzMjYuOTcxNjc5Njg3NSAzOTkuOTgxNDQ1MzEyNUMzODUuNTM5MDYyNSAzNDEuMDg4ODY3MTg3NSAzODYuMzU5Mzc1IDI0NS4yMDAxOTUzMTI1IDMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVaTTQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVDNDA4LjI4NjEzMjgxMjUgLTE0LjgxMzQ3NjU2MjUgMzExLjg1NzQyMTg3NSAtMTQuODIxMjg5MDYyNSAyNTIuNTg2OTE0MDYyNSA0NC40NDkyMTg3NUwxODUuMzg2NzE4NzUgMTExLjY0OTQxNDA2MjVDMTg1LjI2NjYwMTU2MjUgMTExLjc2ODU1NDY4NzUgMTg1LjEzNjcxODc1IDExMS44OTk0MTQwNjI1IDE4NS4wMjczNDM3NSAxMTIuMDE4NTU0Njg3NUMxMjYuNDYwOTM3NSAxNzAuOTExMTMyODEyNSAxMjUuNjM5NjQ4NDM3NSAyNjYuNzk5ODA0Njg3NSAxODUuMzg2NzE4NzUgMzI2LjYwOTM3NUMxOTEuNzM4MjgxMjUgMzMyLjk1OTk2MDkzNzUgMTk4LjUyMjQ2MDkzNzUgMzM4LjY0ODQzNzUgMjA1LjkwODIwMzEyNSAzNDMuODA0Njg3NUMyMTIuMzA5NTcwMzEyNSAzNDguMjczNDM3NSAyMjAuOTcxNjc5Njg3NSAzNDcuNTkzNzUgMjI2LjQ5MjE4NzUgMzQyLjA3NDIxODc1TDI0Ny41NDU4OTg0Mzc1IDMyMS4wMTg1NTQ2ODc1QzI1NS44OTY0ODQzNzUgMzEyLjY2ODk0NTMxMjUgMjU5LjYzOTY0ODQzNzUgMzAxLjc4MDI3MzQzNzUgMjU5LjI0NDE0MDYyNSAyOTEuMjEyODkwNjI1QzI1OS4wNDM5NDUzMTI1IDI4NS45ODE0NDUzMTI1IDI1Ni4zNDc2NTYyNSAyODEuMzg4NjcxODc1IDI1Mi4yOTY4NzUgMjc4LjYwNzQyMTg3NUMyNDkuMzg0NzY1NjI1IDI3Ni42MDE1NjI1IDI0NS42NTcyMjY1NjI1IDI3My43MzI0MjE4NzUgMjQxLjk1NjA1NDY4NzUgMjcwLjAzODA4NTkzNzVDMjEzLjg4MjgxMjUgMjQxLjk2NDg0Mzc1IDIxMy43NjQ2NDg0Mzc1IDE5Ni4zOTk0MTQwNjI1IDI0MS45NTYwNTQ2ODc1IDE2OC4yMDgwMDc4MTI1TDMwOS4xNTYyNSAxMDEuMDE3NTc4MTI1QzMzNy4zOTQ1MzEyNSA3Mi43NzkyOTY4NzUgMzgzLjQ1NjA1NDY4NzUgNzIuOTQ5MjE4NzUgNDExLjQ4MTQ0NTMxMjUgMTAxLjUyODMyMDMxMjVDNDM5LjIzMTQ0NTMxMjUgMTI5LjgyODEyNSA0MzguMzUyNTM5MDYyNSAxNzUuNDYxOTE0MDYyNSA0MTAuMzI2MTcxODc1IDIwMy40ODgyODEyNUwzOTcuMjM5MjU3ODEyNSAyMTYuNTc1MTk1MzEyNUMzOTIuODg4NjcxODc1IDIyMC45MjQ4MDQ2ODc1IDM5MS40Njk3MjY1NjI1IDIyNy4zNjUyMzQzNzUgMzkzLjQ1NjA1NDY4NzUgMjMzLjE4NjUyMzQzNzVDMzk5LjMyMDMxMjUgMjUwLjM4MDg1OTM3NSA0MDIuNDk4MDQ2ODc1IDI2OC4xODU1NDY4NzUgNDAzLjE0NjQ4NDM3NSAyODUuOTA4MjAzMTI1QzQwMy42NTUyNzM0Mzc1IDI5OS44MTQ0NTMxMjUgNDIwLjU5OTYwOTM3NSAzMDYuMzUzNTE1NjI1IDQzMC40NDA0Mjk2ODc1IDI5Ni41MTM2NzE4NzVMNDY3LjU0NTg5ODQzNzUgMjU5LjQwODIwMzEyNUM1MjYuODE3MzgyODEyNSAyMDAuMTQ5NDE0MDYyNSA1MjYuODE3MzgyODEyNSAxMDMuNzA4OTg0Mzc1IDQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5Kb2ludDwvdGV4dD48L3N2Zz4=" alt="Joint" width="59" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+bmV1dDwvdGV4dD48L3N2Zz4=" alt="neut" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+eHJheTwvdGV4dD48L3N2Zz4=" alt="xray" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM1IDIyIj48cmVjdCB3aWR0aD0iMzUiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+Y3dsPC90ZXh0Pjwvc3ZnPg==" alt="cwl" width="35" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

Fit PbSO₄ to two patterns at once, the Rietveld round robin's neutron pattern from D1A at ILL
and its laboratory X-ray pattern: one structure, two experiments.

The project is the catalogue case `pd-neut-xray-cwl_pbso4-d1a-lab`, the one the command line and
the app's Examples open.

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('pd-neut-xray-cwl_pbso4-d1a-lab', destination='data')
project = edi.Project.load(project_path)
structure = project.structures['pbso4']
d1a = project.experiments['d1a']
lab = project.experiments['lab']
```

```text
Data 'pd-neut-xray-cwl_pbso4-d1a-lab' is at data/pd-neut-xray-cwl_pbso4-d1a-lab-ce92206a5a9d/pd-neut-xray-cwl_pbso4-d1a-lab
```

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/1.html"></iframe>
</div>

## Perform the analysis

Both patterns fit together. diffraction-lib's tutorial of this case frees everything at once,
and also the D1A wavelength, which this case keeps fixed.

### Scales, 2θ zeros and cell

```python
d1a.linked_structures['pbso4'].scale.free = True
lab.linked_structures['pbso4'].scale.free = True
d1a.instrument.calib_twotheta_offset.free = True
lab.instrument.calib_twotheta_offset.free = True
structure.cell.length_a.free = True
structure.cell.length_b.free = True
structure.cell.length_c.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 292px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/2.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 7 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       64.60       241.50
      1      0.370     27.86        44.92   81.4% ↓
      2      0.415     27.34        43.27   3.7% ↓
      3      0.461     26.85        41.73   3.6% ↓
      4      0.507     26.38        40.29   3.4% ↓
      5      0.552     25.95        38.96   3.3% ↓
      6      0.597     25.50        37.63   3.4% ↓
      7      0.643     25.02        36.23   3.7% ↓
      8      0.688     24.52        34.79   4.0% ↓
      9      0.733     24.01        33.36   4.1% ↓
     10      0.779     23.47        31.88   4.4% ↓
     11      0.824     22.90        30.36   4.8% ↓
     12      0.869     22.34        28.88   4.9% ↓
     13      0.914     21.80        27.51   4.7% ↓
     14      0.959     21.31        26.28   4.5% ↓
     15      1.005     20.89        25.26   3.9% ↓
     16      1.050     20.57        24.49   3.0% ↓
     17      1.096     20.35        23.96   2.2% ↓
     18      1.141     20.21        23.63   1.4% ↓
     19      1.186     20.12        23.44   0.8% ↓
     20      1.232     20.08        23.33   0.5% ↓
     21      1.277     20.05        23.27   0.2% ↓
     22      1.322     20.04        23.24   0.1% ↓
     23      1.368     20.03        23.23   0.1% ↓
     24      1.413     20.03        23.22   
     25      1.458     20.03        23.22   
     26      1.503     20.03        23.22   
     27      1.549     20.03        23.21   
     28      1.594     20.03        23.21   
     29      1.639     20.03        23.21   
     30      1.685     20.03        23.21   
     31      1.764     20.03        23.21   
  done · converged · 31 iters · reduced χ² 23.21 · Rwp 20.03 % · 1.82 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/3.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/4.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/5.html"></iframe>
</div>

### Backgrounds

D1A's points and the laboratory pattern's Chebyshev terms.

```python
for point in d1a.background:
    point.intensity.free = True
for term in lab.background_terms:
    term.coef.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 21 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       20.03        23.25
      1      0.398     19.11        21.17   9.0% ↓
      2      0.480     19.11        21.17   
  done · converged · 2 iters · reduced χ² 21.17 · Rwp 19.11 % · 0.54 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/6.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/7.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/8.html"></iframe>
</div>

### Peak widths

```python
d1a.peak.broad_gauss_u.free = True
d1a.peak.broad_gauss_v.free = True
d1a.peak.broad_gauss_w.free = True
d1a.peak.mixing_eta_0.free = True
lab.peak.broad_gauss_u.free = True
lab.peak.broad_gauss_v.free = True
lab.peak.broad_gauss_w.free = True
lab.peak.mixing_eta_0.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 29 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       19.11        21.19
      1      0.601     11.62         7.84   63.0% ↓
      2      0.706     11.49         7.66   2.3% ↓
      3      0.819     11.42         7.57   1.1% ↓
      4      0.934     11.40         7.54   0.4% ↓
      5      1.051     11.39         7.53   0.1% ↓
      6      1.170     11.39         7.53   
      7      1.289     11.39         7.53   
      8      1.407     11.39         7.53   
      9      1.525     11.39         7.53   
     10      1.729     11.39         7.53   
  done · converged · 10 iters · reduced χ² 7.53 · Rwp 11.39 % · 1.87 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/9.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/10.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/11.html"></iframe>
</div>

### Peak asymmetry, D1A

The D1A pattern's four Bérar-Baldinozzi terms.

```python
d1a.peak.asym_beba_a0.free = True
d1a.peak.asym_beba_b0.free = True
d1a.peak.asym_beba_a1.free = True
d1a.peak.asym_beba_b1.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 33 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.39         7.53
      1      0.933      9.65         5.40   28.2% ↓
      2      1.017      9.64         5.39   0.2% ↓
      3      1.100      9.64         5.39   
      4      1.181      9.64         5.39   
      5      1.263      9.64         5.39   
      6      1.345      9.64         5.39   
      7      1.483      9.64         5.39   
  done · converged · 7 iters · reduced χ² 5.39 · Rwp 9.64 % · 1.59 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/12.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/13.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/14.html"></iframe>
</div>

### Peak asymmetry, laboratory

The laboratory pattern's first-order terms.

```python
lab.peak.asym_beba_a0.free = True
lab.peak.asym_beba_b0.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 35 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        9.64         5.39
      1      0.743      9.45         5.19   3.9% ↓
      2      0.832      9.45         5.19   
      3      0.922      9.45         5.19   
      4      1.014      9.45         5.19   
      5      1.179      9.45         5.19   
  done · converged · 5 iters · reduced χ² 5.19 · Rwp 9.45 % · 1.29 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/15.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/16.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/17.html"></iframe>
</div>

### Atom positions

The neutron and X-ray patterns together see the oxygen as well as the lead, so all free
coordinates fit at once.

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
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 46 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        9.45         5.19
      1      0.939      8.47         4.17   19.7% ↓
      2      1.106      8.47         4.17   
  done · converged · 2 iters · reduced χ² 4.17 · Rwp 8.47 % · 1.24 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/18.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/19.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/20.html"></iframe>
</div>

### Displacements

```python
for site in structure.atom_sites:
    site.adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-xray-cwl_pbso4-d1a-lab, 2 banks (d1a, lab), 8709 pts fitted / 8911 loaded, 51 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        8.47         4.17
      1      0.726      5.80         1.96   53.1% ↓
      2      0.842      5.80         1.96   
  done · converged · 2 iters · reduced χ² 1.96 · Rwp 5.80 % · 0.93 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/21.html"></iframe>
</div>

```python
project.display.pattern('d1a')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/22.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/23.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/24.html"></iframe>
</div>

```python
project.display.structure('pbso4')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-xray-cwl_pbso4-d1a-lab/25.html"></iframe>
</div>

## Save the project

```python
project.save_as('pd-neut-xray-cwl_pbso4-d1a-lab')
project.report.save_html('pd-neut-xray-cwl_pbso4-d1a-lab.html')
```

```text
Saving project to 'pd-neut-xray-cwl_pbso4-d1a-lab'
Saving report to 'pd-neut-xray-cwl_pbso4-d1a-lab.html'
```
