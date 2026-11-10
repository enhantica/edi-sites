Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-cwl_yalo3-al2o3-spodi/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/d42e09fd8e9ae537bbb4d2d3eb16c49fbe3f7999/docs/user/tutorials/pd-neut-cwl_yalo3-al2o3-spodi.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-cwl_yalo3-al2o3-spodi.ipynb){ .md-button .ed-tutorial-button download }
</div>

# YAlO₃ and Al₂O₃ on SPODI

Fit two phases, YAlO₃ and corundum Al₂O₃, in one constant-wavelength neutron pattern from SPODI
at FRM II, measured at 3 K, with a shared Bérar-Baldinozzi profile and cylinder absorption.

The project is the catalogue case `pd-neut-cwl_yalo3-al2o3-spodi`, the one the command line and
the app's Examples open.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Single</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" width="14" height="14" style="height:0.85em;width:auto;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span>

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('pd-neut-cwl_yalo3-al2o3-spodi', destination='data')
project = edi.Project.load(project_path)
yalo3 = project.structures['YAlO3']
alumina = project.structures['Al2O3']
experiment = project.experiments['spodi']
```

```text
Data 'pd-neut-cwl_yalo3-al2o3-spodi' is at data/pd-neut-cwl_yalo3-al2o3-spodi-5ae8d5ec72da/pd-neut-cwl_yalo3-al2o3-spodi
```

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/1.html"></iframe>
</div>

## Perform the analysis

The fit follows diffraction-lib's three cycles for this case (its YAP tutorial). diffraction-lib
frees the Lorentzian Y and two asymmetry terms where this profile has the mixing η₀ and four.

### Cells, scales and 2θ zero

Both phases' cells and scales, and the zero shift, put the peaks of both phases in place.

```python
yalo3.cell.length_a.free = True
yalo3.cell.length_b.free = True
yalo3.cell.length_c.free = True
alumina.cell.length_a.free = True
alumina.cell.length_c.free = True
experiment.linked_structures['YAlO3'].scale.free = True
experiment.linked_structures['Al2O3'].scale.free = True
experiment.instrument.calib_twotheta_offset.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 8 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       18.59       201.52
      1      0.008     13.43       105.14   47.8% ↓
      2      0.015     13.38       104.44   0.7% ↓
      3      0.022     13.38       104.43   
      4      0.029     13.38       104.43   
      5      0.036     13.38       104.42   
      6      0.042     13.38       104.42   
      7      0.049     13.38       104.42   
      8      0.059     13.38       104.42   
  done · converged · 8 iters · reduced χ² 104.42 · Rwp 13.38 % · 0.07 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/2.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/3.html"></iframe>
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
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 33 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.38       105.32
      1      0.038     11.96        84.08   20.2% ↓
      2      0.054     11.96        84.08   
      3      0.064     11.96        84.07   
      4      0.073     11.96        84.07   
      5      0.084     11.96        84.06   
      6      0.092     11.96        84.06   
      7      0.102     11.96        84.06   
      8      0.110     11.96        84.06   
      9      0.120     11.96        84.06   
     10      0.157     11.96        84.06   
  done · converged · 10 iters · reduced χ² 84.06 · Rwp 11.96 % · 0.17 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/4.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/5.html"></iframe>
</div>

### Peak widths

The Gaussian widths and the mixing η₀.

```python
experiment.peak.broad_gauss_u.free = True
experiment.peak.broad_gauss_v.free = True
experiment.peak.broad_gauss_w.free = True
experiment.peak.mixing_eta_0.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 37 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.96        84.18
      1      0.038     11.47        77.42   8.0% ↓
      2      0.047     11.46        77.33   0.1% ↓
      3      0.057     11.46        77.33   
      4      0.074     11.46        77.33   
      5      0.082     11.46        77.33   
      6      0.093     11.46        77.33   
      7      0.102     11.46        77.32   
      8      0.140     11.46        77.32   
  done · converged · 8 iters · reduced χ² 77.32 · Rwp 11.46 % · 0.15 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/6.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/7.html"></iframe>
</div>

### Asymmetry

The four Bérar-Baldinozzi asymmetry terms.

```python
experiment.peak.asym_beba_a0.free = True
experiment.peak.asym_beba_b0.free = True
experiment.peak.asym_beba_a1.free = True
experiment.peak.asym_beba_b1.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 41 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.46        77.43
      1      0.036     11.30        75.33   2.7% ↓
      2      0.045     11.28        75.05   0.4% ↓
      3      0.055     11.28        74.99   0.1% ↓
      4      0.064     11.28        74.99   
      5      0.072     11.28        74.99   
      6      0.106     11.28        74.99   
  done · converged · 6 iters · reduced χ² 74.99 · Rwp 11.28 % · 0.12 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/8.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/9.html"></iframe>
</div>

### Atom positions

The coordinates the symmetry leaves free in both phases.

```python
yalo3.atom_sites['Y'].fract_x.free = True
yalo3.atom_sites['Y'].fract_y.free = True
yalo3.atom_sites['O1'].fract_x.free = True
yalo3.atom_sites['O1'].fract_y.free = True
yalo3.atom_sites['O2'].fract_x.free = True
yalo3.atom_sites['O2'].fract_y.free = True
yalo3.atom_sites['O2'].fract_z.free = True
alumina.atom_sites['Al1'].fract_z.free = True
alumina.atom_sites['O1'].fract_x.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 50 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.28        75.22
      1      0.043      6.52        25.17   66.5% ↓
      2      0.056      6.46        24.71   1.8% ↓
      3      0.077      6.46        24.70   
      4      0.091      6.46        24.69   
      5      0.104      6.46        24.69   
      6      0.117      6.46        24.69   
      7      0.130      6.46        24.69   
      8      0.144      6.46        24.69   
      9      0.156      6.46        24.69   
     10      0.169      6.46        24.69   
     11      0.182      6.46        24.69   
     12      0.195      6.46        24.69   
     13      0.207      6.46        24.69   
     14      0.224      6.46        24.69   
     15      0.262      6.46        24.69   
  done · converged · 15 iters · reduced χ² 24.69 · Rwp 6.46 % · 0.28 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/10.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/11.html"></iframe>
</div>

### Displacements

Every site's displacement in both phases.

```python
for structure in (yalo3, alumina):
    for site in structure.atom_sites:
        site.adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-cwl_yalo3-al2o3-spodi, 2959 pts fitted / 2959 loaded, 56 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        6.46        24.74
      1      0.045      4.13        10.13   59.0% ↓
      2      0.060      4.06         9.79   3.4% ↓
      3      0.075      4.06         9.77   0.1% ↓
      4      0.089      4.06         9.77   
      5      0.103      4.06         9.77   
      6      0.118      4.06         9.77   
      7      0.132      4.06         9.76   
      8      0.146      4.06         9.76   0.1% ↓
      9      0.159      4.05         9.74   0.1% ↓
     10      0.171      4.05         9.73   0.1% ↓
     11      0.185      4.05         9.73   
     12      0.198      4.05         9.73   
     13      0.211      4.05         9.73   
     14      0.223      4.05         9.73   
     15      0.266      4.05         9.73   
  done · converged · 15 iters · reduced χ² 9.73 · Rwp 4.05 % · 0.28 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/12.html"></iframe>
</div>

```python
project.display.pattern('spodi')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/13.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/14.html"></iframe>
</div>

```python
project.display.structure('YAlO3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/15.html"></iframe>
</div>

```python
project.display.structure('Al2O3')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_yalo3-al2o3-spodi/16.html"></iframe>
</div>

## Save the project

```python
project.save_as('pd-neut-cwl_yalo3-al2o3-spodi')
project.report.save_html('pd-neut-cwl_yalo3-al2o3-spodi.html')
```

```text
Saving project to 'pd-neut-cwl_yalo3-al2o3-spodi'
Saving report to 'pd-neut-cwl_yalo3-al2o3-spodi.html'
```
