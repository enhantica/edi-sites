Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-xray-cwl_pbso4-lab/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/e9334c7713570499c3a02e4010c0832ce46d44fd/docs/user/tutorials/pd-xray-cwl_pbso4-lab.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-xray-cwl_pbso4-lab.ipynb){ .md-button .ed-tutorial-button download }
</div>

# PbSO₄ on a laboratory diffractometer

Fit PbSO₄ to the Rietveld round robin's laboratory X-ray pattern, with the Cu K&alpha; doublet
and Bérar-Baldinozzi asymmetry.

The project is the catalogue case `pd-xray-cwl_pbso4-lab`, the one the command line and the
app's Examples open.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Single</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">xray</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span>

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('pd-xray-cwl_pbso4-lab', destination='data')
project = edi.Project.load(project_path)
structure = project.structures['pbso4']
lab = project.experiments['lab']
```

```text
Data 'pd-xray-cwl_pbso4-lab' is at data/pd-xray-cwl_pbso4-lab-a5c4b3ad01e7/pd-xray-cwl_pbso4-lab
```

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/1.html"></iframe>
</div>

## Perform the analysis

The fit goes in stages, freeing one group of parameters at a time.

### Scale and 2θ zero

The 2θ zero first: freed together with the cell from the start, the two pull against each
other and the fit cannot take a step.

```python
lab.linked_structures['pbso4'].scale.free = True
lab.instrument.calib_twotheta_offset.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 152px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/2.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 2 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                      114.69       551.55
      1      0.024     58.28       142.41   74.2% ↓
      2      0.044     56.65       134.57   5.5% ↓
      3      0.064     54.94       126.54   6.0% ↓
      4      0.083     53.17       118.53   6.3% ↓
      5      0.103     51.27       110.21   7.0% ↓
      6      0.123     49.26       101.76   7.7% ↓
      7      0.142     47.28        93.73   7.9% ↓
      8      0.162     45.50        86.81   7.4% ↓
      9      0.182     44.08        81.48   6.1% ↓
     10      0.202     43.08        77.81   4.5% ↓
     11      0.222     42.43        75.49   3.0% ↓
     12      0.241     42.04        74.09   1.9% ↓
     13      0.261     41.80        73.27   1.1% ↓
     14      0.281     41.67        72.80   0.6% ↓
     15      0.300     41.59        72.54   0.4% ↓
     16      0.320     41.55        72.39   0.2% ↓
     17      0.340     41.53        72.31   0.1% ↓
     18      0.360     41.52        72.27   0.1% ↓
     19      0.379     41.51        72.25   
     20      0.399     41.51        72.23   
     21      0.419     41.50        72.23   
     22      0.438     41.50        72.22   
     23      0.458     41.50        72.22   
     24      0.478     41.50        72.22   
     25      0.497     41.50        72.22   
     26      0.517     41.50        72.22   
     27      0.551     41.50        72.22   
  done · converged · 27 iters · reduced χ² 72.22 · Rwp 41.50 % · 0.58 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/3.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/4.html"></iframe>
</div>

### Cell

```python
structure.cell.length_a.free = True
structure.cell.length_b.free = True
structure.cell.length_c.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 5 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       41.50        72.26
      1      0.029     39.32        64.85   10.3% ↓
      2      0.054     36.89        57.10   11.9% ↓
      3      0.079     34.51        49.96   12.5% ↓
      4      0.103     32.61        44.61   10.7% ↓
      5      0.128     31.42        41.42   7.1% ↓
      6      0.153     30.72        39.60   4.4% ↓
      7      0.228     30.68        39.48   0.3% ↓
      8      0.253     30.48        38.97   1.3% ↓
      9      0.278     30.45        38.90   0.2% ↓
     10      0.302     30.42        38.81   0.2% ↓
     11      0.327     30.38        38.72   0.2% ↓
     12      0.355     30.35        38.64   0.2% ↓
     13      0.382     30.32        38.57   0.2% ↓
     14      0.408     30.30        38.51   0.2% ↓
     15      0.435     30.27        38.45   0.2% ↓
     16      0.462     30.25        38.38   0.2% ↓
     17      0.489     30.22        38.32   0.2% ↓
     18      0.516     30.21        38.28   0.1% ↓
     19      0.543     30.20        38.25   0.1% ↓
     20      0.570     30.19        38.23   0.1% ↓
     21      0.597     30.18        38.20   0.1% ↓
     22      0.622     30.16        38.16   0.1% ↓
     23      0.646     30.14        38.11   0.1% ↓
     24      0.671     30.12        38.05   0.1% ↓
     25      0.696     30.10        38.01   0.1% ↓
     26      0.720     30.09        37.98   0.1% ↓
     27      0.745     30.08        37.97   
     28      0.769     30.08        37.96   
     29      0.794     30.08        37.96   
     30      0.819     30.08        37.96   
     31      0.843     30.08        37.95   
     32      0.868     30.08        37.95   
     33      0.908     30.08        37.95   
  done · converged · 33 iters · reduced χ² 37.95 · Rwp 30.08 % · 0.94 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/5.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/6.html"></iframe>
</div>

### Background

The six Chebyshev terms.

```python
for term in lab.background_terms:
    term.coef.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 11 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       30.08        37.99
      1      0.043     29.27        35.97   5.3% ↓
      2      0.070     29.27        35.97   
      3      0.097     29.27        35.97   
      4      0.132     29.26        35.97   
      5      0.164     29.26        35.97   
      6      0.197     29.26        35.97   
      7      0.224     29.26        35.96   
      8      0.259     29.26        35.96   
      9      0.289     29.26        35.96   
     10      0.314     29.26        35.96   
     11      0.344     29.26        35.95   
     12      0.369     29.25        35.93   0.1% ↓
     13      0.394     29.21        35.82   0.3% ↓
     14      0.419     29.16        35.71   0.3% ↓
     15      0.445     29.15        35.69   0.1% ↓
     16      0.470     29.15        35.68   
     17      0.495     29.15        35.68   
     18      0.520     29.15        35.68   
     19      0.545     29.15        35.68   
     20      0.585     29.15        35.68   
  done · converged · 20 iters · reduced χ² 35.68 · Rwp 29.15 % · 0.61 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/7.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/8.html"></iframe>
</div>

### Peak widths

```python
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
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 15 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       29.15        35.71
      1      0.042     17.53        12.92   63.8% ↓
      2      0.074     14.02         8.26   36.1% ↓
      3      0.113     13.51         7.67   7.2% ↓
      4      0.158     13.46         7.62   0.6% ↓
      5      0.201     13.46         7.62   
      6      0.245     13.46         7.62   
      7      0.288     13.46         7.62   
      8      0.356     13.46         7.62   
  done · converged · 8 iters · reduced χ² 7.62 · Rwp 13.46 % · 0.41 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/9.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/10.html"></iframe>
</div>

### Peak asymmetry

```python
lab.peak.asym_beba_a0.free = True
lab.peak.asym_beba_b0.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 17 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       13.46         7.62
      1      0.070     12.84         6.93   9.0% ↓
      2      0.115     12.76         6.85   1.3% ↓
      3      0.162     12.76         6.84   0.1% ↓
      4      0.208     12.76         6.84   
      5      0.255     12.76         6.84   
      6      0.301     12.76         6.84   
      7      0.348     12.76         6.84   
      8      0.394     12.76         6.84   
      9      0.466     12.76         6.84   
  done · converged · 9 iters · reduced χ² 6.84 · Rwp 12.76 % · 0.53 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/11.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/12.html"></iframe>
</div>

### Lead and sulphur positions

X-rays see the heavy atoms first, so their coordinates come before the oxygens'.

```python
for site in structure.atom_sites:
    if site.type_symbol != 'O':
        for coordinate in (site.fract_x, site.fract_y, site.fract_z):
            coordinate.free = not coordinate.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 21 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       12.76         6.85
      1      0.093     11.94         6.00   12.3% ↓
      2      0.161     11.93         5.99   0.2% ↓
      3      0.230     11.93         5.99   
      4      0.323     11.93         5.99   
  done · converged · 4 iters · reduced χ² 5.99 · Rwp 11.93 % · 0.40 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/13.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/14.html"></iframe>
</div>

### Oxygen positions

```python
for site in structure.atom_sites:
    if site.type_symbol == 'O':
        for coordinate in (site.fract_x, site.fract_y, site.fract_z):
            coordinate.free = not coordinate.symmetry_constrained
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 28 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.93         6.00
      1      0.095     11.83         5.90   1.7% ↓
      2      0.164     11.83         5.90   0.1% ↓
      3      0.233     11.83         5.90   
      4      0.302     11.83         5.90   
      5      0.396     11.83         5.90   
  done · converged · 5 iters · reduced χ² 5.90 · Rwp 11.83 % · 0.48 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/15.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/16.html"></iframe>
</div>

### Displacements

The correlations after this stage show how far the oxygen displacements can be told apart; the
case keeps them separate.

```python
for site in structure.atom_sites:
    site.adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-xray-cwl_pbso4-lab, 5799 pts fitted / 6001 loaded, 33 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       11.83         5.90
      1      0.076      8.96         3.38   42.6% ↓
      2      0.115      8.41         2.98   12.0% ↓
      3      0.153      8.40         2.98   0.1% ↓
      4      0.190      8.40         2.98   
      5      0.246      8.40         2.98   
  done · converged · 5 iters · reduced χ² 2.98 · Rwp 8.40 % · 0.30 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/17.html"></iframe>
</div>

```python
project.display.pattern('lab')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/18.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/19.html"></iframe>
</div>

```python
project.display.structure('pbso4')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-xray-cwl_pbso4-lab/20.html"></iframe>
</div>

## Save the project

```python
project.save_as('pd-xray-cwl_pbso4-lab')
project.report.save_html('pd-xray-cwl_pbso4-lab.html')
```

```text
Saving project to 'pd-xray-cwl_pbso4-lab'
Saving report to 'pd-xray-cwl_pbso4-lab.html'
```
