Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-cwl_cosio-d20_2k/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/b665bb8f7f66aa43269a426fec07e2a3d78bb0bd/docs/user/tutorials/pd-neut-cwl_cosio-d20_2k.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-cwl_cosio-d20_2k.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Co₂SiO₄ on D20 at 2.3 K

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY3IDIyIj48cmVjdCB3aWR0aD0iNjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMzk4NjQ4IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNDk2IDUxMiIgZmlsbD0iIzM5ODY0OCI+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzM5ODY0OCI+Rml0dGluZzwvdGV4dD48L3N2Zz4=" alt="Fitting" width="67" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDY2IDIyIj48cmVjdCB3aWR0aD0iNjYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjOTY2MDFkIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzk2NjAxZCI+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjOTY2MDFkIj5TaW5nbGU8L3RleHQ+PC9zdmc+" alt="Single" width="66" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNyIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDI3IDIyIj48cmVjdCB3aWR0aD0iMjciIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+cGQ8L3RleHQ+PC9zdmc+" alt="pd" width="27" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzOCIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM4IDIyIj48cmVjdCB3aWR0aD0iMzgiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+bmV1dDwvdGV4dD48L3N2Zz4=" alt="neut" width="38" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzNSIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDM1IDIyIj48cmVjdCB3aWR0aD0iMzUiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjNDI0MjQyIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzQyNDI0MiI+Y3dsPC90ZXh0Pjwvc3ZnPg==" alt="cwl" width="35" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0NiIgaGVpZ2h0PSIyMiIgdmlld0JveD0iMCAwIDQ2IDIyIj48cmVjdCB3aWR0aD0iNDYiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA4NGM3IiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48dGV4dCB4PSI3IiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iIzAwODRjNyI+QnJhZ2c8L3RleHQ+PC9zdmc+" alt="Bragg" width="46" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMjIgMjIiPjxyZWN0IHdpZHRoPSIxMjIiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjMDA3OTZiIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iIzAwNzk2YiI+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+PHRleHQgeD0iMjMiIHk9IjE1LjMiIGZvbnQtZmFtaWx5PSJOb3RvIFNhbnMsIFNlZ29lIFVJLCBIZWx2ZXRpY2EsIEFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjEyIiBmaWxsPSIjMDA3OTZiIj5DcnlzdGFsIHN0cnVjdHVyZTwvdGV4dD48L3N2Zz4=" alt="Crystal structure" width="122" height="22">&nbsp; <img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMzQiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAxMzQgMjIiPjxyZWN0IHdpZHRoPSIxMzQiIGhlaWdodD0iMjIiIHJ4PSI0IiBmaWxsPSIjYzIxODViIiBmaWxsLW9wYWNpdHk9IjAuMTMiLz48c3ZnIHg9IjciIHk9IjUuMCIgd2lkdGg9IjEyIiBoZWlnaHQ9IjEyIiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZmlsbD0iI2MyMTg1YiI+PHBhdGggZD0iTTE2NC4wNzAzMTI1IDE0OC4wOTk2MDkzNzVDMTY0LjA4Mzk4NDM3NSAxNDguMDk5NjA5Mzc1IDE2NC4wOTY2Nzk2ODc1IDE0OC4xMDI1MzkwNjI1IDE2NC4xMTAzNTE1NjI1IDE0OC4xMDI1MzkwNjI1QzE3MC42NzI4NTE1NjI1IDE0OC4xMDI1MzkwNjI1IDE3Ni4wMDA5NzY1NjI1IDE0Mi43NzQ0MTQwNjI1IDE3Ni4wMDA5NzY1NjI1IDEzNi4yMTE5MTQwNjI1QzE3Ni4wMDA5NzY1NjI1IDEzNi4xNzQ4MDQ2ODc1IDE3Ni4wIDEzNi4xMzc2OTUzMTI1IDE3Ni4wIDEzNi4wOTk2MDkzNzVWNTYuMDk5NjA5Mzc1QzE3Ni4wIDM2LjIzMTQ0NTMxMjUgMTU5Ljg2OTE0MDYyNSAyMC4wOTk2MDkzNzUgMTQwLjAgMjAuMDk5NjA5Mzc1SDM2LjBDMTYuMTMwODU5Mzc1IDIwLjA5OTYwOTM3NSAwLjAgMzYuMjMxNDQ1MzEyNSAwLjAgNTYuMDk5NjA5Mzc1VjEzNi4wOTk2MDkzNzVDMC4wIDE0Mi43MjI2NTYyNSA1LjM3Njk1MzEyNSAxNDguMDk5NjA5Mzc1IDEyLjAgMTQ4LjA5OTYwOTM3NVpNNTEyLjAgMTM2LjA5OTYwOTM3NVY1Ni4wQzUxMi4wIDM2LjEzMDg1OTM3NSA0OTUuODY5MTQwNjI1IDIwLjAgNDc2LjAgMjAuMEgzNzIuMEMzNTIuMTMwODU5Mzc1IDIwLjAgMzM2LjAgMzYuMTMwODU5Mzc1IDMzNi4wIDU2LjBWMTM2LjBDMzM2LjAgMTQyLjYyMzA0Njg3NSAzNDEuMzc2OTUzMTI1IDE0OC4wIDM0OC4wIDE0OC4wSDUwMC4wQzUwMC4wMzcxMDkzNzUgMTQ4LjAgNTAwLjA3NDIxODc1IDE0OC4wMDA5NzY1NjI1IDUwMC4xMTIzMDQ2ODc1IDE0OC4wMDA5NzY1NjI1QzUwNi42NzQ4MDQ2ODc1IDE0OC4wMDA5NzY1NjI1IDUxMi4wMDE5NTMxMjUgMTQyLjY3Mjg1MTU2MjUgNTEyLjAwMTk1MzEyNSAxMzYuMTEwMzUxNTYyNUM1MTIuMDAxOTUzMTI1IDEzNi4xMDc0MjE4NzUgNTEyLjAgMTM2LjEwMzUxNTYyNSA1MTIuMCAxMzYuMDk5NjA5Mzc1Wk0zNDguMCAxODAuMDk5NjA5Mzc1QzM0MS4zNzY5NTMxMjUgMTgwLjA5OTYwOTM3NSAzMzYuMCAxODUuNDc2NTYyNSAzMzYuMCAxOTIuMDk5NjA5Mzc1VjI0NC4wOTk2MDkzNzVDMzM2LjAgMzcyLjIwMDE5NTMxMjUgMTc2LjAgMzcyLjAgMTc2LjAgMjQ0LjA5OTYwOTM3NVYxOTIuMDk5NjA5Mzc1QzE3Ni4wIDE4NS40NzY1NjI1IDE3MC42MjMwNDY4NzUgMTgwLjA5OTYwOTM3NSAxNjQuMCAxODAuMDk5NjA5Mzc1SDEyLjA5OTYwOTM3NUM1LjQ3NjU2MjUgMTgwLjA5OTYwOTM3NSAwLjA5OTYwOTM3NSAxODUuNDc2NTYyNSAwLjA5OTYwOTM3NSAxOTIuMDk5NjA5Mzc1VjE5Mi4yMDAxOTUzMTI1QzAuMjAwMTk1MzEyNSAyMTMuNTk5NjA5Mzc1IDAuNzAwMTk1MzEyNSAyMzIuNSAwLjA5OTYwOTM3NSAyNDUuNUMwLjA5OTYwOTM3NSAzOTYuMDk5NjA5Mzc1IDEzNi4yNjk1MzEyNSA0OTIuMDk5NjA5Mzc1IDI1Ni44NDk2MDkzNzUgNDkyLjA5OTYwOTM3NUMzNzcuNDI5Njg3NSA0OTIuMDk5NjA5Mzc1IDUxMS44NDk2MDkzNzUgMzk2LjA5OTYwOTM3NSA1MTEuODQ5NjA5Mzc1IDI0NS40MDAzOTA2MjVDNTExLjI1IDIzMi41OTk2MDkzNzUgNTExLjY1MDM5MDYyNSAyMTIuNDAwMzkwNjI1IDUxMS44NDk2MDkzNzUgMTkyLjIwMDE5NTMxMjVDNTExLjg1MDU4NTkzNzUgMTkyLjE2NjAxNTYyNSA1MTEuODUwNTg1OTM3NSAxOTIuMTMxODM1OTM3NSA1MTEuODUwNTg1OTM3NSAxOTIuMDk3NjU2MjVDNTExLjg1MDU4NTkzNzUgMTg1LjQ3NTU4NTkzNzUgNTA2LjQ3MjY1NjI1IDE4MC4wOTk2MDkzNzUgNDk5Ljg0OTYwOTM3NSAxODAuMDk5NjA5Mzc1WiIvPjwvc3ZnPjx0ZXh0IHg9IjIzIiB5PSIxNS4zIiBmb250LWZhbWlseT0iTm90byBTYW5zLCBTZWdvZSBVSSwgSGVsdmV0aWNhLCBBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxMiIgZmlsbD0iI2MyMTg1YiI+TWFnbmV0aWMgc3RydWN0dXJlPC90ZXh0Pjwvc3ZnPg==" alt="Magnetic structure" width="134" height="22">

Fit the magnetic structure of the olivine Co₂SiO₄ to constant-wavelength neutron powder data
from D20 at ILL, measured at 2.3 K, below its ordering temperature. The cobalt moments order with
k = 0 in the magnetic space group Pnma.1: Co1 may point in any direction, Co2 only along b.

The project is the catalogue case `pd-neut-cwl_cosio-d20_2k`, the one the command line and the
app's Examples open. Its two Co sites share one displacement, and the two FCJ asymmetry terms are
tied, from the start.

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
      1      0.015     14.03        54.28   3.5% ↓
  done · converged · 1 iters · reduced χ² 54.28 · Rwp 14.03 % · 0.02 s
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
      1      0.013     13.20        48.60   11.5% ↓
  done · converged · 1 iters · reduced χ² 48.60 · Rwp 13.20 % · 0.02 s
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
      1      0.023     13.13        48.23   1.0% ↓
  done · converged · 1 iters · reduced χ² 48.23 · Rwp 13.13 % · 0.03 s
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
      1      0.071     13.13        48.26   
      2      0.074     13.13        48.26   
      3      0.078     13.13        48.26   
      4      0.081     13.13        48.25   
      5      0.084     13.13        48.25   
      6      0.087     13.13        48.25   
      7      0.092     13.13        48.25   
  done · converged · 7 iters · reduced χ² 48.25 · Rwp 13.13 % · 0.10 s
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
      1      0.028     13.06        48.14   1.0% ↓
  done · converged · 1 iters · reduced χ² 48.14 · Rwp 13.06 % · 0.03 s
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
      1      0.031      5.57         8.79   81.8% ↓
      2      0.036      5.26         7.84   10.8% ↓
      3      0.040      5.09         7.33   6.5% ↓
      4      0.045      4.89         6.76   7.7% ↓
      5      0.050      4.88         6.74   0.4% ↓
      6      0.055      4.88         6.73   0.2% ↓
      7      0.061      4.87         6.72   0.2% ↓
      8      0.066      4.87         6.71   0.1% ↓
      9      0.072      4.87         6.71   
     10      0.078      4.87         6.71   
     11      0.086      4.87         6.71   
  done · converged · 11 iters · reduced χ² 6.71 · Rwp 4.87 % · 0.09 s
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
      1      0.032      4.70         6.25   7.0% ↓
      2      0.039      4.70         6.25   
      3      0.044      4.70         6.25   
      4      0.050      4.70         6.25   
      5      0.055      4.70         6.25   
      6      0.060      4.70         6.25   
      7      0.066      4.70         6.25   
      8      0.070      4.70         6.25   
      9      0.076      4.70         6.25   
     10      0.083      4.70         6.25   
  done · converged · 10 iters · reduced χ² 6.25 · Rwp 4.70 % · 0.09 s
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
