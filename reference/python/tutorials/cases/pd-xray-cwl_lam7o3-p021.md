Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-xray-cwl_lam7o3-p021/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/281d1666dcc2210ea837a5b5d68acfbdc2006e28/docs/user/tutorials/pd-xray-cwl_lam7o3-p021.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-xray-cwl_lam7o3-p021.ipynb){ .md-button .ed-tutorial-button download }
</div>

# La(Ti,Cr,Mn,Fe,Co,Ni,Cu)O₃ on P02.1

Fit the high-entropy perovskite La(Ti,Cr,Mn,Fe,Co,Ni,Cu)O₃, seven cations on one site, to
synchrotron X-ray powder data from P02.1 at PETRA III.

The project is the catalogue case `pd-xray-cwl_lam7o3-p021`, the one the command line and the
app's Examples open. The seven metals sharing one site have one displacement, held by
constraints from the start.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Single</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">xray</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span>

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('pd-xray-cwl_lam7o3-p021', destination='data')
project = edi.Project.load(project_path)
structure = project.structures['lam7o3']
experiment = project.experiments['p021']
project.display.constraints()
```

```text
Data 'pd-xray-cwl_lam7o3-p021' is at data/pd-xray-cwl_lam7o3-p021-3eba8bb5594a/pd-xray-cwl_lam7o3-p021
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 544px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/1.html"></iframe>
</div>

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/2.html"></iframe>
</div>

## Perform the analysis

The fit goes in stages, freeing one group of parameters at a time.

### Scale, 2θ zero and cell

The scale, the zero shift and the cell put the peaks in place and at the right height.

```python
experiment.linked_structures['lam7o3'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
structure.cell.length_a.free = True
structure.cell.length_b.free = True
structure.cell.length_c.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 236px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1459 loaded, 5 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       60.60       246.85
      1      0.004     42.69       122.50   50.4% ↓
      2      0.008     38.20        98.09   19.9% ↓
      3      0.012     35.23        83.41   15.0% ↓
      4      0.016     34.19        78.58   5.8% ↓
      5      0.019     33.91        77.27   1.7% ↓
      6      0.023     33.81        76.83   0.6% ↓
      7      0.027     33.76        76.62   0.3% ↓
      8      0.031     33.73        76.49   0.2% ↓
      9      0.035     33.72        76.41   0.1% ↓
     10      0.039     33.70        76.35   0.1% ↓
     11      0.043     33.69        76.31   0.1% ↓
     12      0.047     33.69        76.29   
     13      0.050     33.68        76.27   
     14      0.054     33.68        76.26   
     15      0.058     33.68        76.25   
     16      0.061     33.68        76.25   
     17      0.065     33.68        76.24   
     18      0.069     33.68        76.24   
     19      0.074     33.68        76.24   
  done · converged · 19 iters · reduced χ² 76.24 · Rwp 33.68 % · 0.08 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/4.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/5.html"></iframe>
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
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1459 loaded, 25 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       33.68        77.50
      1      0.006     10.57         7.63   90.2% ↓
      2      0.011     10.54         7.58   0.6% ↓
      3      0.015     10.53         7.58   0.1% ↓
      4      0.019     10.53         7.58   
      5      0.024     10.53         7.57   
      6      0.028     10.53         7.57   
      7      0.032     10.53         7.57   
      8      0.036     10.53         7.57   
      9      0.041     10.53         7.57   
     10      0.045     10.53         7.57   
     11      0.049     10.52         7.57   
     12      0.053     10.52         7.57   
     13      0.057     10.52         7.57   
     14      0.063     10.52         7.57   
  done · converged · 14 iters · reduced χ² 7.57 · Rwp 10.52 % · 0.07 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/6.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/7.html"></iframe>
</div>

### Peak widths

The Gaussian widths and the Lorentzian X.

```python
experiment.peak.broad_gauss_u.free = True
experiment.peak.broad_gauss_v.free = True
experiment.peak.broad_gauss_w.free = True
experiment.peak.broad_lorentz_x.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1459 loaded, 29 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       10.52         7.59
      1      0.006      7.07         3.43   54.9% ↓
      2      0.011      6.29         2.71   20.8% ↓
      3      0.017      6.04         2.50   7.8% ↓
      4      0.023      5.89         2.38   5.0% ↓
      5      0.029      5.77         2.29   3.9% ↓
      6      0.035      5.74         2.26   1.1% ↓
      7      0.048      5.57         2.13   5.9% ↓
      8      0.054      5.40         2.00   6.0% ↓
      9      0.060      5.20         1.85   7.3% ↓
     10      0.066      3.76         0.97   47.8% ↓
     11      0.072      3.60         0.89   8.2% ↓
     12      0.077      3.57         0.87   1.9% ↓
     13      0.082      3.56         0.87   0.3% ↓
     14      0.088      3.56         0.87   0.1% ↓
     15      0.093      3.56         0.87   0.1% ↓
     16      0.098      3.55         0.87   0.4% ↓
     17      0.103      3.54         0.86   1.0% ↓
     18      0.109      3.49         0.84   2.3% ↓
     19      0.114      3.43         0.81   3.6% ↓
     20      0.119      3.36         0.77   4.2% ↓
     21      0.124      3.24         0.72   6.8% ↓
     22      0.130      3.04         0.63   12.2% ↓
     23      0.135      2.85         0.56   12.1% ↓
     24      0.140      2.80         0.54   3.6% ↓
     25      0.146      2.79         0.53   0.2% ↓
     26      0.153      2.79         0.53   
  done · converged · 26 iters · reduced χ² 0.53 · Rwp 2.79 % · 0.16 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/8.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/9.html"></iframe>
</div>

### Background from the fitted model

With a fitted peak model, estimate the background again with the calculated peaks subtracted,
which follows the low-angle background better, then free the new points and fit again.

```python
experiment.background.auto_estimate(use_model='subtract', n_points=20)
for point in experiment.background:
    point.intensity.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1459 loaded, 29 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.03         1.11
      1      0.008      2.71         0.50   54.7% ↓
      2      0.014      2.71         0.50   
      3      0.020      2.71         0.50   
      4      0.029      2.71         0.50   
  done · converged · 4 iters · reduced χ² 0.50 · Rwp 2.71 % · 0.04 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/10.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/11.html"></iframe>
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
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1459 loaded, 36 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        2.71         0.51
      1      0.010      1.81         0.23   55.3% ↓
      2      0.017      1.78         0.22   3.5% ↓
      3      0.025      1.78         0.22   
      4      0.032      1.78         0.22   
      5      0.039      1.78         0.22   0.1% ↓
      6      0.047      1.78         0.22   0.4% ↓
      7      0.054      1.77         0.22   1.1% ↓
      8      0.061      1.75         0.21   2.4% ↓
      9      0.068      1.71         0.20   3.5% ↓
     10      0.075      1.69         0.20   2.8% ↓
     11      0.082      1.68         0.19   1.1% ↓
     12      0.089      1.68         0.19   0.2% ↓
     13      0.097      1.68         0.19   
     14      0.106      1.68         0.19   
  done · converged · 14 iters · reduced χ² 0.19 · Rwp 1.68 % · 0.12 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/12.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/13.html"></iframe>
</div>

### Displacements

La's, the mixed site's (through Ti) and O1's; O2's follows O1's.

```python
structure.atom_sites['La'].adp_iso.free = True
structure.atom_sites['Ti'].adp_iso.free = True
structure.atom_sites['O1'].adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_lam7o3-p021, 1236 pts fitted / 1459 loaded, 39 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        1.68         0.19
      1      0.010      1.62         0.18   6.5% ↓
      2      0.018      1.61         0.18   1.8% ↓
      3      0.025      1.60         0.18   0.4% ↓
      4      0.033      1.60         0.18   0.4% ↓
      5      0.041      1.60         0.18   0.2% ↓
      6      0.049      1.60         0.18   0.1% ↓
      7      0.057      1.60         0.18   0.3% ↓
      8      0.065      1.59         0.18   0.7% ↓
      9      0.073      1.58         0.17   1.0% ↓
     10      0.081      1.58         0.17   0.9% ↓
     11      0.089      1.57         0.17   0.4% ↓
     12      0.096      1.57         0.17   0.1% ↓
     13      0.106      1.57         0.17   
  done · converged · 13 iters · reduced χ² 0.17 · Rwp 1.57 % · 0.12 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/14.html"></iframe>
</div>

```python
project.display.pattern('p021')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/15.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/16.html"></iframe>
</div>

```python
project.display.structure('lam7o3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_lam7o3-p021/17.html"></iframe>
</div>

## Save the project

```python
project.save_as('pd-xray-cwl_lam7o3-p021')
project.report.save_html('pd-xray-cwl_lam7o3-p021.html')
```

```text
Saving project to 'pd-xray-cwl_lam7o3-p021'
Saving report to 'pd-xray-cwl_lam7o3-p021.html'
```
