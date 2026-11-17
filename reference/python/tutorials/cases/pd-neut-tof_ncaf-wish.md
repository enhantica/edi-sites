Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-tof_ncaf-wish/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/d1635833c786f7c650d8889c76a93a5244c93e6b/docs/user/tutorials/pd-neut-tof_ncaf-wish.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-tof_ncaf-wish.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Na₂Ca₃Al₂F₁₄ on WISH

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI1OSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDU5IDIyIj48cmVjdCB3aWR0aD0iNTkiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVDMzIwLjI2MDc0MjE4NzUgMTc5LjAzOTA2MjUgMzEzLjQ3NTU4NTkzNzUgMTczLjM1MTU2MjUgMzA2LjA4OTg0Mzc1IDE2OC4xOTQzMzU5Mzc1QzI5OS42ODg0NzY1NjI1IDE2My43MjU1ODU5Mzc1IDI5MS4wMjczNDM3NSAxNjQuNDA0Mjk2ODc1IDI4NS41MDU4NTkzNzUgMTY5LjkyNDgwNDY4NzVMMjY0LjQ1MjE0ODQzNzUgMTkwLjk4MDQ2ODc1QzI1Ni4xMDE1NjI1IDE5OS4zMzAwNzgxMjUgMjUyLjM1ODM5ODQzNzUgMjEwLjIxODc1IDI1Mi43NTM5MDYyNSAyMjAuNzg2MTMyODEyNUMyNTIuOTU0MTAxNTYyNSAyMjYuMDE3NTc4MTI1IDI1NS42NTAzOTA2MjUgMjMwLjYxMDM1MTU2MjUgMjU5LjcwMTE3MTg3NSAyMzMuMzkxNjAxNTYyNUMyNjIuNjEzMjgxMjUgMjM1LjM5NzQ2MDkzNzUgMjY2LjM0MDgyMDMxMjUgMjM4LjI2NjYwMTU2MjUgMjcwLjA0MTk5MjE4NzUgMjQxLjk2MDkzNzVDMjk4LjExNTIzNDM3NSAyNzAuMDM0MTc5Njg3NSAyOTguMjMzMzk4NDM3NSAzMTUuNTk5NjA5Mzc1IDI3MC4wNDE5OTIxODc1IDM0My43OTEwMTU2MjVMMjAyLjg0MTc5Njg3NSA0MTAuOTgxNDQ1MzEyNUMxNzQuNjAyNTM5MDYyNSA0MzkuMjE5NzI2NTYyNSAxMjguNTQxMDE1NjI1IDQzOS4wNDk4MDQ2ODc1IDEwMC41MTY2MDE1NjI1IDQxMC40NzA3MDMxMjVDNzIuNzY2NjAxNTYyNSAzODIuMTcwODk4NDM3NSA3My42NDY0ODQzNzUgMzM2LjUzNzEwOTM3NSAxMDEuNjcxODc1IDMwOC41MTA3NDIxODc1TDExNC43NTg3ODkwNjI1IDI5NS40MjM4MjgxMjVDMTE5LjEwOTM3NSAyOTEuMDc0MjE4NzUgMTIwLjUyODMyMDMxMjUgMjg0LjYzMzc4OTA2MjUgMTE4LjU0MTk5MjE4NzUgMjc4LjgxMTUyMzQzNzVDMTEyLjY3NzczNDM3NSAyNjEuNjE4MTY0MDYyNSAxMDkuNSAyNDMuODEzNDc2NTYyNSAxMDguODUxNTYyNSAyMjYuMDkwODIwMzEyNUMxMDguMzQzNzUgMjEyLjE4NDU3MDMxMjUgOTEuMzk4NDM3NSAyMDUuNjQ0NTMxMjUgODEuNTU3NjE3MTg3NSAyMTUuNDg1MzUxNTYyNUw0NC40NTIxNDg0Mzc1IDI1Mi41OTA4MjAzMTI1Qy0xNC44MTgzNTkzNzUgMzExLjg1MDU4NTkzNzUgLTE0LjgxODM1OTM3NSA0MDguMjkxMDE1NjI1IDQ0LjQ1MjE0ODQzNzUgNDY3LjU1MDc4MTI1QzEwMy43MTI4OTA2MjUgNTI2LjgxMzQ3NjU2MjUgMjAwLjE0MTYwMTU2MjUgNTI2LjgyMTI4OTA2MjUgMjU5LjQxMjEwOTM3NSA0NjcuNTUwNzgxMjVMMzI2LjYxMjMwNDY4NzUgNDAwLjM1MDU4NTkzNzVDMzI2LjczMjQyMTg3NSA0MDAuMjMxNDQ1MzEyNSAzMjYuODYyMzA0Njg3NSA0MDAuMTAwNTg1OTM3NSAzMjYuOTcxNjc5Njg3NSAzOTkuOTgxNDQ1MzEyNUMzODUuNTM5MDYyNSAzNDEuMDg4ODY3MTg3NSAzODYuMzU5Mzc1IDI0NS4yMDAxOTUzMTI1IDMyNi42MTIzMDQ2ODc1IDE4NS4zOTA2MjVaTTQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVDNDA4LjI4NjEzMjgxMjUgLTE0LjgxMzQ3NjU2MjUgMzExLjg1NzQyMTg3NSAtMTQuODIxMjg5MDYyNSAyNTIuNTg2OTE0MDYyNSA0NC40NDkyMTg3NUwxODUuMzg2NzE4NzUgMTExLjY0OTQxNDA2MjVDMTg1LjI2NjYwMTU2MjUgMTExLjc2ODU1NDY4NzUgMTg1LjEzNjcxODc1IDExMS44OTk0MTQwNjI1IDE4NS4wMjczNDM3NSAxMTIuMDE4NTU0Njg3NUMxMjYuNDYwOTM3NSAxNzAuOTExMTMyODEyNSAxMjUuNjM5NjQ4NDM3NSAyNjYuNzk5ODA0Njg3NSAxODUuMzg2NzE4NzUgMzI2LjYwOTM3NUMxOTEuNzM4MjgxMjUgMzMyLjk1OTk2MDkzNzUgMTk4LjUyMjQ2MDkzNzUgMzM4LjY0ODQzNzUgMjA1LjkwODIwMzEyNSAzNDMuODA0Njg3NUMyMTIuMzA5NTcwMzEyNSAzNDguMjczNDM3NSAyMjAuOTcxNjc5Njg3NSAzNDcuNTkzNzUgMjI2LjQ5MjE4NzUgMzQyLjA3NDIxODc1TDI0Ny41NDU4OTg0Mzc1IDMyMS4wMTg1NTQ2ODc1QzI1NS44OTY0ODQzNzUgMzEyLjY2ODk0NTMxMjUgMjU5LjYzOTY0ODQzNzUgMzAxLjc4MDI3MzQzNzUgMjU5LjI0NDE0MDYyNSAyOTEuMjEyODkwNjI1QzI1OS4wNDM5NDUzMTI1IDI4NS45ODE0NDUzMTI1IDI1Ni4zNDc2NTYyNSAyODEuMzg4NjcxODc1IDI1Mi4yOTY4NzUgMjc4LjYwNzQyMTg3NUMyNDkuMzg0NzY1NjI1IDI3Ni42MDE1NjI1IDI0NS42NTcyMjY1NjI1IDI3My43MzI0MjE4NzUgMjQxLjk1NjA1NDY4NzUgMjcwLjAzODA4NTkzNzVDMjEzLjg4MjgxMjUgMjQxLjk2NDg0Mzc1IDIxMy43NjQ2NDg0Mzc1IDE5Ni4zOTk0MTQwNjI1IDI0MS45NTYwNTQ2ODc1IDE2OC4yMDgwMDc4MTI1TDMwOS4xNTYyNSAxMDEuMDE3NTc4MTI1QzMzNy4zOTQ1MzEyNSA3Mi43NzkyOTY4NzUgMzgzLjQ1NjA1NDY4NzUgNzIuOTQ5MjE4NzUgNDExLjQ4MTQ0NTMxMjUgMTAxLjUyODMyMDMxMjVDNDM5LjIzMTQ0NTMxMjUgMTI5LjgyODEyNSA0MzguMzUyNTM5MDYyNSAxNzUuNDYxOTE0MDYyNSA0MTAuMzI2MTcxODc1IDIwMy40ODgyODEyNUwzOTcuMjM5MjU3ODEyNSAyMTYuNTc1MTk1MzEyNUMzOTIuODg4NjcxODc1IDIyMC45MjQ4MDQ2ODc1IDM5MS40Njk3MjY1NjI1IDIyNy4zNjUyMzQzNzUgMzkzLjQ1NjA1NDY4NzUgMjMzLjE4NjUyMzQzNzVDMzk5LjMyMDMxMjUgMjUwLjM4MDg1OTM3NSA0MDIuNDk4MDQ2ODc1IDI2OC4xODU1NDY4NzUgNDAzLjE0NjQ4NDM3NSAyODUuOTA4MjAzMTI1QzQwMy42NTUyNzM0Mzc1IDI5OS44MTQ0NTMxMjUgNDIwLjU5OTYwOTM3NSAzMDYuMzUzNTE1NjI1IDQzMC40NDA0Mjk2ODc1IDI5Ni41MTM2NzE4NzVMNDY3LjU0NTg5ODQzNzUgMjU5LjQwODIwMzEyNUM1MjYuODE3MzgyODEyNSAyMDAuMTQ5NDE0MDYyNSA1MjYuODE3MzgyODEyNSAxMDMuNzA4OTg0Mzc1IDQ2Ny41NDY4NzUgNDQuNDQ5MjE4NzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5Kb2ludDwvdGV4dD48L3N2Zz4=" alt="Joint" width="59" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+bmV1dDwvdGV4dD48L3N2Zz4=" alt="neut" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI4IDIyIj48cmVjdCB3aWR0aD0iMjgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+dG9mPC90ZXh0Pjwvc3ZnPg==" alt="tof" width="28" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">

Fit Na₂Ca₃Al₂F₁₄ to time-of-flight neutron powder data from WISH at ISIS, all five detector bank
pairs at once. Each bank has its own calibration and profile; the structure is shared.

It builds the catalogue case `pd-neut-tof_ncaf-wish` step by step: the same project the command
line fits and the app's Examples open.

## Import the library

```python
import easydiffraction as edi
```

## Define the project

A new project is empty: it holds no structure and no experiment until you add them. The joint
fitting mode fits every experiment at once, against one set of structures.

```python
project = edi.Project(name='pd-neut-tof_ncaf-wish')
project.analysis.fitting_mode = 'joint'
```

## Define the structure

Load the structure from EasyDiffraction's collection. Its CIF gives the space group, the cell and
the atom sites.

```python
path = edi.download_data('pd-neut-tof_ncaf-wish-ncaf', destination='data')
project.structures.add_from_cif_path(path)
structure = project.structures['ncaf']
```

```text
Data 'pd-neut-tof_ncaf-wish-ncaf' is at data/pd-neut-tof_ncaf-wish-ncaf.edi
```

```python
project.display.structure('ncaf')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/1.html"></iframe>
</div>

## Define the experiments

Create the five experiments from their measured data in EasyDiffraction's collection, then
describe each one's instrument, peak profile, background and the structures it links.

```python
data_path = edi.download_data('pd-neut-tof_ncaf-wish-wish_1_10-data', destination='data')
project.experiments.add_from_data_path(
    name='wish_1_10',
    data_path=data_path,
    sample_form='powder',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
wish_1_10 = project.experiments['wish_1_10']
wish_1_10.neutron_scattering_length = 'sears1992'
wish_1_10.peak.type = 'tof-jorgensen-von-dreele'
wish_1_10.absorption.type = 'cylinder'
wish_1_10.instrument.name = 'WISH'
wish_1_10.instrument.facility = 'ISIS'
wish_1_10.peak.cutoff_fwhm = 8
wish_1_10.peak.broad_gauss_sigma_2 = 15.4063
wish_1_10.peak.broad_lorentz_gamma_1 = 8.2904
wish_1_10.peak.decay_beta_0 = 0.004707
wish_1_10.peak.decay_beta_1 = 0.137368
wish_1_10.peak.rise_alpha_0 = 0.014439
wish_1_10.peak.rise_alpha_1 = 0.05507
wish_1_10.instrument.setup_twotheta_bank = 27.081
wish_1_10.instrument.calib_d_to_tof_linear = 4985.32
wish_1_10.instrument.calib_d_to_tof_quadratic = 1.85733
wish_1_10.excluded_regions.create(start=0, end=7000)
wish_1_10.excluded_regions.create(start=240000, end=300000)
wish_1_10.linked_structures.create(structure_id='ncaf', scale=40)
wish_1_10.background.create(position=6056.0952, intensity=210.0)
wish_1_10.background.create(position=7099.4761, intensity=210.0)
wish_1_10.background.create(position=8008.2271, intensity=210.0)
wish_1_10.background.create(position=8816.0059, intensity=210.0)
wish_1_10.background.create(position=9724.7568, intensity=210.0)
wish_1_10.background.create(position=10532.5352, intensity=210.0)
wish_1_10.background.create(position=11710.5459, intensity=210.0)
wish_1_10.background.create(position=12619.2969, intensity=210.0)
wish_1_10.background.create(position=13393.4180, intensity=210.0)
wish_1_10.background.create(position=14470.4561, intensity=210.0)
wish_1_10.background.create(position=15614.8096, intensity=210.0)
wish_1_10.background.create(position=17264.0254, intensity=210.0)
wish_1_10.background.create(position=19283.4707, intensity=210.0)
wish_1_10.background.create(position=20192.2207, intensity=210.0)
wish_1_10.background.create(position=22346.2969, intensity=210.0)
wish_1_10.background.create(position=24433.0586, intensity=210.0)
wish_1_10.background.create(position=27563.2012, intensity=210.0)
wish_1_10.background.create(position=30356.7695, intensity=210.0)
wish_1_10.background.create(position=33049.3672, intensity=210.0)
wish_1_10.background.create(position=35203.4414, intensity=210.0)
wish_1_10.background.create(position=38826.4766, intensity=210.0)
wish_1_10.background.create(position=44447.2695, intensity=210.0)
wish_1_10.background.create(position=50068.0625, intensity=210.0)
wish_1_10.background.create(position=55587.8828, intensity=210.0)
wish_1_10.background.create(position=63586.3867, intensity=210.0)
wish_1_10.background.create(position=74289.4531, intensity=210.0)
wish_1_10.background.create(position=86385.1953, intensity=210.0)
wish_1_10.background.create(position=98097.9844, intensity=210.0)
wish_1_10.background.create(position=114791.3281, intensity=210.0)
wish_1_10.background.create(position=128630.5156, intensity=210.0)
wish_1_10.background.create(position=147091.2500, intensity=210.0)
wish_1_10.background.create(position=167026.9219, intensity=210.0)
wish_1_10.background.create(position=187448.0156, intensity=210.0)
wish_1_10.background.create(position=208808.5312, intensity=210.0)
wish_1_10.background.create(position=231077.7812, intensity=210.0)
wish_1_10.background.create(position=252332.8281, intensity=210.0)
```

```text
Data 'pd-neut-tof_ncaf-wish-wish_1_10-data' is at data/pd-neut-tof_ncaf-wish-wish_1_10.xye
```

```python
data_path = edi.download_data('pd-neut-tof_ncaf-wish-wish_2_9-data', destination='data')
project.experiments.add_from_data_path(
    name='wish_2_9',
    data_path=data_path,
    sample_form='powder',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
wish_2_9 = project.experiments['wish_2_9']
wish_2_9.neutron_scattering_length = 'sears1992'
wish_2_9.peak.type = 'tof-jorgensen-von-dreele'
wish_2_9.absorption.type = 'cylinder'
wish_2_9.instrument.name = 'WISH'
wish_2_9.instrument.facility = 'ISIS'
wish_2_9.peak.cutoff_fwhm = 8
wish_2_9.peak.broad_gauss_sigma_1 = 34
wish_2_9.peak.broad_gauss_sigma_2 = 11
wish_2_9.peak.broad_lorentz_gamma_1 = 1
wish_2_9.peak.decay_beta_0 = 0.0061
wish_2_9.peak.decay_beta_1 = 0.096
wish_2_9.peak.rise_alpha_0 = 0.053
wish_2_9.peak.rise_alpha_1 = 0.031
wish_2_9.instrument.setup_twotheta_bank = 58.33
wish_2_9.instrument.calib_d_to_tof_linear = 10389.9
wish_2_9.instrument.calib_d_to_tof_quadratic = 1.85233
wish_2_9.excluded_regions.create(start=0, end=7000)
wish_2_9.excluded_regions.create(start=134000, end=300000)
wish_2_9.linked_structures.create(structure_id='ncaf', scale=40)
wish_2_9.background.create(position=7246.0732, intensity=220.0)
wish_2_9.background.create(position=9265.5195, intensity=220.0)
wish_2_9.background.create(position=11097.9795, intensity=220.0)
wish_2_9.background.create(position=13080.0303, intensity=220.0)
wish_2_9.background.create(position=15473.4473, intensity=220.0)
wish_2_9.background.create(position=16931.9355, intensity=220.0)
wish_2_9.background.create(position=18614.8086, intensity=220.0)
wish_2_9.background.create(position=20596.8594, intensity=220.0)
wish_2_9.background.create(position=22504.1133, intensity=220.0)
wish_2_9.background.create(position=26169.0332, intensity=220.0)
wish_2_9.background.create(position=28113.6875, intensity=220.0)
wish_2_9.background.create(position=30320.1172, intensity=220.0)
wish_2_9.background.create(position=34770.3828, intensity=220.0)
wish_2_9.background.create(position=40155.5703, intensity=220.0)
wish_2_9.background.create(position=48341.8086, intensity=220.0)
wish_2_9.background.create(position=58540.0156, intensity=220.0)
wish_2_9.background.create(position=69139.8672, intensity=220.0)
wish_2_9.background.create(position=80953.6328, intensity=220.0)
wish_2_9.background.create(position=94214.6562, intensity=220.0)
wish_2_9.background.create(position=107677.6328, intensity=220.0)
wish_2_9.background.create(position=120889.3047, intensity=220.0)
wish_2_9.background.create(position=132602.0938, intensity=220.0)
```

```text
Data 'pd-neut-tof_ncaf-wish-wish_2_9-data' is at data/pd-neut-tof_ncaf-wish-wish_2_9.xye
```

```python
data_path = edi.download_data('pd-neut-tof_ncaf-wish-wish_3_8-data', destination='data')
project.experiments.add_from_data_path(
    name='wish_3_8',
    data_path=data_path,
    sample_form='powder',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
wish_3_8 = project.experiments['wish_3_8']
wish_3_8.neutron_scattering_length = 'sears1992'
wish_3_8.peak.type = 'tof-jorgensen-von-dreele'
wish_3_8.absorption.type = 'cylinder'
wish_3_8.instrument.name = 'WISH'
wish_3_8.instrument.facility = 'ISIS'
wish_3_8.peak.cutoff_fwhm = 8
wish_3_8.peak.broad_gauss_sigma_1 = 30
wish_3_8.peak.broad_gauss_sigma_2 = 8.3
wish_3_8.peak.broad_lorentz_gamma_1 = 0.0002
wish_3_8.peak.decay_beta_0 = 0.0069
wish_3_8.peak.decay_beta_1 = 0.032
wish_3_8.peak.rise_alpha_0 = -0.016
wish_3_8.peak.rise_alpha_1 = 0.16
wish_3_8.instrument.setup_twotheta_bank = 90
wish_3_8.instrument.calib_d_to_tof_linear = 15105.5
wish_3_8.instrument.calib_d_to_tof_quadratic = 1.00785
wish_3_8.excluded_regions.create(start=0, end=9000)
wish_3_8.excluded_regions.create(start=116000, end=300000)
wish_3_8.linked_structures.create(structure_id='ncaf', scale=40)
wish_3_8.background.create(position=9089.7529, intensity=240.0)
wish_3_8.background.create(position=11580.4033, intensity=240.0)
wish_3_8.background.create(position=13667.1650, intensity=240.0)
wish_3_8.background.create(position=15551.9824, intensity=240.0)
wish_3_8.background.create(position=17739.7168, intensity=240.0)
wish_3_8.background.create(position=20364.9961, intensity=240.0)
wish_3_8.background.create(position=22653.7031, intensity=240.0)
wish_3_8.background.create(position=24740.4648, intensity=240.0)
wish_3_8.background.create(position=27130.1406, intensity=240.0)
wish_3_8.background.create(position=29957.3672, intensity=240.0)
wish_3_8.background.create(position=32616.3047, intensity=240.0)
wish_3_8.background.create(position=36150.3359, intensity=240.0)
wish_3_8.background.create(position=40963.3516, intensity=240.0)
wish_3_8.background.create(position=47265.5195, intensity=240.0)
wish_3_8.background.create(position=53391.1758, intensity=240.0)
wish_3_8.background.create(position=62005.2383, intensity=240.0)
wish_3_8.background.create(position=71866.8672, intensity=240.0)
wish_3_8.background.create(position=82913.9922, intensity=240.0)
wish_3_8.background.create(position=90385.9375, intensity=240.0)
wish_3_8.background.create(position=99649.2188, intensity=240.0)
wish_3_8.background.create(position=107356.7656, intensity=240.0)
wish_3_8.background.create(position=115337.3203, intensity=240.0)
```

```text
Data 'pd-neut-tof_ncaf-wish-wish_3_8-data' is at data/pd-neut-tof_ncaf-wish-wish_3_8.xye
```

```python
data_path = edi.download_data('pd-neut-tof_ncaf-wish-wish_4_7-data', destination='data')
project.experiments.add_from_data_path(
    name='wish_4_7',
    data_path=data_path,
    sample_form='powder',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
wish_4_7 = project.experiments['wish_4_7']
wish_4_7.neutron_scattering_length = 'sears1992'
wish_4_7.peak.type = 'tof-jorgensen-von-dreele'
wish_4_7.absorption.type = 'cylinder'
wish_4_7.instrument.name = 'WISH'
wish_4_7.instrument.facility = 'ISIS'
wish_4_7.peak.cutoff_fwhm = 8
wish_4_7.peak.broad_gauss_sigma_1 = 14
wish_4_7.peak.broad_gauss_sigma_2 = 8.9
wish_4_7.peak.decay_beta_0 = 0.0074
wish_4_7.peak.decay_beta_1 = 0.017
wish_4_7.peak.rise_alpha_0 = -0.015
wish_4_7.peak.rise_alpha_1 = 0.16
wish_4_7.instrument.setup_twotheta_bank = 121.66
wish_4_7.instrument.calib_d_to_tof_linear = 18660.1
wish_4_7.instrument.calib_d_to_tof_quadratic = -0.47488
wish_4_7.excluded_regions.create(start=0, end=9000)
wish_4_7.excluded_regions.create(start=108000, end=300000)
wish_4_7.linked_structures.create(structure_id='ncaf', scale=40)
wish_4_7.background.create(position=9089.7529, intensity=250.0)
wish_4_7.background.create(position=10671.6523, intensity=250.0)
wish_4_7.background.create(position=12287.2100, intensity=250.0)
wish_4_7.background.create(position=14037.3975, intensity=250.0)
wish_4_7.background.create(position=15451.0088, intensity=250.0)
wish_4_7.background.create(position=16763.6504, intensity=250.0)
wish_4_7.background.create(position=18076.2910, intensity=250.0)
wish_4_7.background.create(position=19456.2461, intensity=250.0)
wish_4_7.background.create(position=20465.9688, intensity=250.0)
wish_4_7.background.create(position=21879.5801, intensity=250.0)
wish_4_7.background.create(position=23798.0566, intensity=250.0)
wish_4_7.background.create(position=25447.2715, intensity=250.0)
wish_4_7.background.create(position=28072.5508, intensity=250.0)
wish_4_7.background.create(position=30058.3418, intensity=250.0)
wish_4_7.background.create(position=32582.6504, intensity=250.0)
wish_4_7.background.create(position=34804.0391, intensity=250.0)
wish_4_7.background.create(position=37160.0625, intensity=250.0)
wish_4_7.background.create(position=40323.8594, intensity=250.0)
wish_4_7.background.create(position=46894.5391, intensity=250.0)
wish_4_7.background.create(position=50630.5156, intensity=250.0)
wish_4_7.background.create(position=54602.0938, intensity=250.0)
wish_4_7.background.create(position=58439.0430, intensity=250.0)
wish_4_7.background.create(position=66519.8203, intensity=250.0)
wish_4_7.background.create(position=75001.5000, intensity=250.0)
wish_4_7.background.create(position=83649.2188, intensity=250.0)
wish_4_7.background.create(position=92770.3828, intensity=250.0)
wish_4_7.background.create(position=101524.3047, intensity=250.0)
wish_4_7.background.create(position=107313.3906, intensity=250.0)
```

```text
Data 'pd-neut-tof_ncaf-wish-wish_4_7-data' is at data/pd-neut-tof_ncaf-wish-wish_4_7.xye
```

```python
data_path = edi.download_data('pd-neut-tof_ncaf-wish-wish_5_6-data', destination='data')
project.experiments.add_from_data_path(
    name='wish_5_6',
    data_path=data_path,
    sample_form='powder',
    beam_mode='time-of-flight',
    radiation_probe='neutron',
    scattering_type='bragg',
)
wish_5_6 = project.experiments['wish_5_6']
wish_5_6.neutron_scattering_length = 'sears1992'
wish_5_6.peak.type = 'tof-jorgensen-von-dreele'
wish_5_6.absorption.type = 'cylinder'
wish_5_6.instrument.name = 'WISH'
wish_5_6.instrument.facility = 'ISIS'
wish_5_6.peak.cutoff_fwhm = 8
wish_5_6.peak.broad_gauss_sigma_2 = 7.7
wish_5_6.peak.broad_lorentz_gamma_1 = 0.0019
wish_5_6.peak.decay_beta_0 = 0.0077
wish_5_6.peak.decay_beta_1 = 0.012
wish_5_6.peak.rise_alpha_0 = -0.012
wish_5_6.peak.rise_alpha_1 = 0.14
wish_5_6.instrument.calib_d_to_tof_linear = 20772.9
wish_5_6.instrument.calib_d_to_tof_quadratic = -1.08308
wish_5_6.excluded_regions.create(start=0, end=9000)
wish_5_6.excluded_regions.create(start=104000, end=300000)
wish_5_6.linked_structures.create(structure_id='ncaf', scale=40)
wish_5_6.background.create(position=11136.8740, intensity=260.0)
wish_5_6.background.create(position=13313.3877, intensity=260.0)
wish_5_6.background.create(position=9162.3037, intensity=260.0)
wish_5_6.background.create(position=14906.5078, intensity=260.0)
wish_5_6.background.create(position=16454.7500, intensity=260.0)
wish_5_6.background.create(position=17352.2812, intensity=260.0)
wish_5_6.background.create(position=18743.4551, intensity=260.0)
wish_5_6.background.create(position=20179.5078, intensity=260.0)
wish_5_6.background.create(position=21368.7363, intensity=260.0)
wish_5_6.background.create(position=22176.0391, intensity=260.0)
wish_5_6.background.create(position=22827.2266, intensity=260.0)
wish_5_6.background.create(position=24644.7285, intensity=260.0)
wish_5_6.background.create(position=26439.7910, intensity=260.0)
wish_5_6.background.create(position=28257.2930, intensity=260.0)
wish_5_6.background.create(position=31196.7109, intensity=260.0)
wish_5_6.background.create(position=34034.4062, intensity=260.0)
wish_5_6.background.create(position=37265.5195, intensity=260.0)
wish_5_6.background.create(position=41214.6602, intensity=260.0)
wish_5_6.background.create(position=44827.2266, intensity=260.0)
wish_5_6.background.create(position=49830.9648, intensity=260.0)
wish_5_6.background.create(position=52905.0117, intensity=260.0)
wish_5_6.background.create(position=58204.9375, intensity=260.0)
wish_5_6.background.create(position=62916.9805, intensity=260.0)
wish_5_6.background.create(position=70186.9844, intensity=260.0)
wish_5_6.background.create(position=74204.9375, intensity=260.0)
wish_5_6.background.create(position=82103.2188, intensity=260.0)
wish_5_6.background.create(position=91958.8672, intensity=260.0)
wish_5_6.background.create(position=102712.0391, intensity=260.0)
```

```text
Data 'pd-neut-tof_ncaf-wish-wish_5_6-data' is at data/pd-neut-tof_ncaf-wish-wish_5_6.xye
```

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/2.html"></iframe>
</div>

## Perform the analysis

Five banks fit together. diffraction-lib's tutorial of this case fits two banks at once with
everything free; this one has five, so it stages them.

### Scales and time-of-flight calibration

Each bank's scale and DIFC offset and linear term put its peaks in place and at the right
height.

```python
for parameter in (
    wish_1_10.linked_structures['ncaf'].scale,
    wish_2_9.linked_structures['ncaf'].scale,
    wish_3_8.linked_structures['ncaf'].scale,
    wish_4_7.linked_structures['ncaf'].scale,
    wish_5_6.linked_structures['ncaf'].scale,
):
    parameter.free = True
for parameter in (
    wish_1_10.instrument.calib_d_to_tof_offset,
    wish_1_10.instrument.calib_d_to_tof_linear,
    wish_2_9.instrument.calib_d_to_tof_offset,
    wish_2_9.instrument.calib_d_to_tof_linear,
    wish_3_8.instrument.calib_d_to_tof_offset,
    wish_3_8.instrument.calib_d_to_tof_linear,
    wish_4_7.instrument.calib_d_to_tof_offset,
    wish_4_7.instrument.calib_d_to_tof_linear,
    wish_5_6.instrument.calib_d_to_tof_offset,
    wish_5_6.instrument.calib_d_to_tof_linear,
):
    parameter.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 516px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 15 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       29.70       140.21
      1      0.526     19.91        62.98   55.1% ↓
      2      0.587     19.90        62.95   
      3      0.647     19.90        62.95   
      4      0.707     19.90        62.95   
      5      0.768     19.90        62.95   
      6      0.892     19.90        62.95   
  done · converged · 6 iters · reduced χ² 62.95 · Rwp 19.90 % · 0.97 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/4.html"></iframe>
</div>

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/5.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/6.html"></iframe>
</div>

```python
project.display.pattern('wish_3_8')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/7.html"></iframe>
</div>

```python
project.display.pattern('wish_4_7')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/8.html"></iframe>
</div>

```python
project.display.pattern('wish_5_6')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/9.html"></iframe>
</div>

### Background

Each bank's background points; bank 1-10's first and last stay fixed, as its source has them.

```python
for point in wish_1_10.background:
    point.intensity.free = True
for point in wish_2_9.background:
    point.intensity.free = True
for point in wish_3_8.background:
    point.intensity.free = True
for point in wish_4_7.background:
    point.intensity.free = True
for point in wish_5_6.background:
    point.intensity.free = True
wish_1_10.background[0].intensity.free = False
wish_1_10.background[35].intensity.free = False
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 149 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       19.90        63.39
      1      0.938     13.97        31.21   50.8% ↓
  done · converged · 1 iters · reduced χ² 31.21 · Rwp 13.97 % · 1.10 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/10.html"></iframe>
</div>

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/11.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/12.html"></iframe>
</div>

```python
project.display.pattern('wish_3_8')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/13.html"></iframe>
</div>

```python
project.display.pattern('wish_4_7')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/14.html"></iframe>
</div>

```python
project.display.pattern('wish_5_6')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/15.html"></iframe>
</div>

### Peak asymmetry

Each bank's back-to-back exponentials, the terms its data determine; bank 1-10 keeps its
instrument values.

```python
for parameter in (
    wish_2_9.peak.rise_alpha_0,
    wish_2_9.peak.rise_alpha_1,
    wish_2_9.peak.decay_beta_0,
    wish_2_9.peak.decay_beta_1,
    wish_3_8.peak.rise_alpha_0,
    wish_3_8.peak.rise_alpha_1,
    wish_3_8.peak.decay_beta_0,
    wish_3_8.peak.decay_beta_1,
    wish_4_7.peak.rise_alpha_0,
    wish_4_7.peak.rise_alpha_1,
    wish_4_7.peak.decay_beta_0,
    wish_4_7.peak.decay_beta_1,
    wish_5_6.peak.rise_alpha_0,
    wish_5_6.peak.rise_alpha_1,
    wish_5_6.peak.decay_beta_0,
    wish_5_6.peak.decay_beta_1,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 165 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.97        31.24
      1      0.964     10.41        17.36   44.4% ↓
      2      1.082     10.30        17.00   2.1% ↓
      3      1.202     10.26        16.85   0.9% ↓
      4      1.321     10.24        16.80   0.3% ↓
      5      1.440     10.23        16.78   0.1% ↓
      6      1.560     10.23        16.77   
      7      1.680     10.23        16.77   
      8      1.800     10.23        16.77   
      9      1.920     10.23        16.77   
     10      2.039     10.23        16.77   
     11      2.159     10.23        16.77   
     12      2.370     10.23        16.77   
  done · converged · 12 iters · reduced χ² 16.77 · Rwp 10.23 % · 2.56 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/16.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/17.html"></iframe>
</div>

### Gaussian widths

The Gaussian width terms the banks' data determine.

```python
for parameter in (
    wish_2_9.peak.broad_gauss_sigma_1,
    wish_2_9.peak.broad_gauss_sigma_2,
    wish_3_8.peak.broad_gauss_sigma_1,
    wish_3_8.peak.broad_gauss_sigma_2,
    wish_4_7.peak.broad_gauss_sigma_1,
    wish_4_7.peak.broad_gauss_sigma_2,
    wish_5_6.peak.broad_gauss_sigma_2,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 172 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       10.23        16.78
      1      1.081     10.00        16.02   4.5% ↓
      2      1.209     10.00        16.02   
      3      1.336     10.00        16.02   
      4      1.473     10.00        16.02   
      5      1.602     10.00        16.02   
      6      1.730     10.00        16.02   
      7      1.858     10.00        16.01   
      8      1.986      9.99        16.00   0.1% ↓
      9      2.114      9.99        15.98   0.2% ↓
     10      2.245      9.98        15.96   0.1% ↓
     11      2.380      9.97        15.93   0.2% ↓
     12      2.513      9.97        15.93   
     13      2.749      9.97        15.93   
  done · converged · 13 iters · reduced χ² 15.93 · Rwp 9.97 % · 2.96 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/18.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/19.html"></iframe>
</div>

### Lorentzian width

Bank 2-9's Lorentzian term.

```python
wish_2_9.peak.broad_lorentz_gamma_1.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 173 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        9.97        15.93
      1      1.750      9.97        15.93   
  done · converged · 1 iters · reduced χ² 15.93 · Rwp 9.97 % · 2.07 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/20.html"></iframe>
</div>

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/21.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/22.html"></iframe>
</div>

```python
project.display.pattern('wish_3_8')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/23.html"></iframe>
</div>

```python
project.display.pattern('wish_4_7')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/24.html"></iframe>
</div>

```python
project.display.pattern('wish_5_6')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/25.html"></iframe>
</div>

### Absorption

Banks 2-9 to 5-6 each fit their absorption.

```python
for parameter in (
    wish_2_9.absorption.abscor1,
    wish_3_8.absorption.abscor1,
    wish_4_7.absorption.abscor1,
    wish_5_6.absorption.abscor1,
):
    parameter.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 177 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        9.97        15.94
      1      1.392      9.91        15.74   1.2% ↓
      2      1.530      9.91        15.74   
      3      1.768      9.91        15.74   
  done · converged · 3 iters · reduced χ² 15.74 · Rwp 9.91 % · 1.99 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/26.html"></iframe>
</div>

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/27.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/28.html"></iframe>
</div>

```python
project.display.pattern('wish_3_8')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/29.html"></iframe>
</div>

```python
project.display.pattern('wish_4_7')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/30.html"></iframe>
</div>

```python
project.display.pattern('wish_5_6')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/31.html"></iframe>
</div>

### Atom positions

The coordinates the cubic symmetry leaves free.

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
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 187 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        9.91        15.75
      1      1.574      8.07        10.43   33.8% ↓
      2      1.731      8.07        10.43   
      3      1.985      8.07        10.43   
  done · converged · 3 iters · reduced χ² 10.43 · Rwp 8.07 % · 2.28 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/32.html"></iframe>
</div>

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/33.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/34.html"></iframe>
</div>

```python
project.display.pattern('wish_3_8')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/35.html"></iframe>
</div>

```python
project.display.pattern('wish_4_7')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/36.html"></iframe>
</div>

```python
project.display.pattern('wish_5_6')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/37.html"></iframe>
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
edi fit: joint project pd-neut-tof_ncaf-wish, 5 banks (wish_1_10, wish_2_9, wish_3_8, wish_4_7, wish_5_6), 18973 pts fitted / 20475 loaded, 193 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        8.07        10.43
      1     10.318      7.69         9.50   9.0% ↓
      2     11.004      7.69         9.50   
  done · converged · 2 iters · reduced χ² 9.50 · Rwp 7.69 % · 11.60 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/38.html"></iframe>
</div>

```python
project.display.pattern('wish_1_10')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/39.html"></iframe>
</div>

```python
project.display.pattern('wish_2_9')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/40.html"></iframe>
</div>

```python
project.display.pattern('wish_3_8')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/41.html"></iframe>
</div>

```python
project.display.pattern('wish_4_7')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/42.html"></iframe>
</div>

```python
project.display.pattern('wish_5_6')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/43.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/44.html"></iframe>
</div>

```python
project.display.structure('ncaf')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_ncaf-wish/45.html"></iframe>
</div>

## Report

The HTML report draws the measured, calculated and difference patterns with the reflection
positions, and lists the structures, the experiments and the fit. Open it in a browser.

```python
project.report.save_html('pd-neut-tof_ncaf-wish.html')
```

```text
Saving report to 'pd-neut-tof_ncaf-wish.html'
```

## Save the project

```python
project.save_as('pd-neut-tof_ncaf-wish')
```

```text
Saving project to 'pd-neut-tof_ncaf-wish'
```
