Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-tof_lbco-si-mcstas/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/e9334c7713570499c3a02e4010c0832ce46d44fd/docs/user/tutorials/pd-neut-tof_lbco-si-mcstas.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-tof_lbco-si-mcstas.ipynb){ .md-button .ed-tutorial-button download }
</div>

# La₀.₅Ba₀.₅CoO₃ and Si on a McStas instrument

Fit two phases, La₀.₅Ba₀.₅CoO₃ and silicon, to a time-of-flight pattern simulated with McStas.

The project is the catalogue case `pd-neut-tof_lbco-si-mcstas`, the one the command line and the
app's Examples open.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Single</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">tof</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span>

```python
import easydiffraction as edi
```

## Load the project

```python
project_path = edi.download_data('pd-neut-tof_lbco-si-mcstas', destination='data')
project = edi.Project.load(project_path)
lbco = project.structures['lbco']
si = project.structures['si']
experiment = project.experiments['mcstas']
```

```text
Data 'pd-neut-tof_lbco-si-mcstas' is at data/pd-neut-tof_lbco-si-mcstas-301812138a70/pd-neut-tof_lbco-si-mcstas
```

The project marks what its fit frees. The fit below frees it in stages, so start with all of it
fixed.

```python
for parameter in project.free_parameters:
    parameter.free = False
```

```python
project.display.pattern('mcstas')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/1.html"></iframe>
</div>

## Perform the analysis

The fit goes in stages, freeing one group of parameters at a time.

### Scales and cells

Both phases' scales and cells put the peaks in place and at the right height; the DIFC stays
fixed, as in diffraction-lib's tutorial.

```python
experiment.linked_structures['lbco'].scale.free = True
experiment.linked_structures['si'].scale.free = True
lbco.cell.length_a.free = True
si.cell.length_a.free = True
```

```python
project.display.parameters.free()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 208px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/2.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-tof_lbco-si-mcstas, 633 pts fitted / 1000 loaded, 4 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       50.18       398.16
      1      0.061     26.80       113.57   71.5% ↓
      2      0.121     23.13        84.56   25.5% ↓
      3      0.180     23.12        84.52   
      4      0.243     23.12        84.52   
  done · converged · 4 iters · reduced χ² 84.52 · Rwp 23.12 % · 0.28 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/3.html"></iframe>
</div>

```python
project.display.pattern('mcstas')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/4.html"></iframe>
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
edi fit: project pd-neut-tof_lbco-si-mcstas, 633 pts fitted / 1000 loaded, 17 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       23.12        86.31
      1      0.076     21.09        71.82   16.8% ↓
      2      0.136     21.09        71.82   
      3      0.219     21.09        71.82   
  done · converged · 3 iters · reduced χ² 71.82 · Rwp 21.09 % · 0.25 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/5.html"></iframe>
</div>

```python
project.display.pattern('mcstas')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/6.html"></iframe>
</div>

### Peak widths

```python
experiment.peak.broad_gauss_sigma_0.free = True
experiment.peak.broad_gauss_sigma_1.free = True
experiment.peak.broad_gauss_sigma_2.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-tof_lbco-si-mcstas, 633 pts fitted / 1000 loaded, 20 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       21.09        72.17
      1      0.081     21.05        71.92   0.4% ↓
      2      0.140     21.05        71.87   0.1% ↓
      3      0.200     21.04        71.81   0.1% ↓
      4      0.259     21.03        71.75   0.1% ↓
      5      0.318     21.02        71.69   0.1% ↓
      6      0.378     21.01        71.62   0.1% ↓
      7      0.437     20.99        71.51   0.2% ↓
      8      0.504     20.97        71.33   0.3% ↓
      9      0.566     20.93        71.09   0.3% ↓
     10      0.625     20.90        70.86   0.3% ↓
     11      0.685     20.88        70.75   0.2% ↓
     12      0.744     20.88        70.73   
     13      0.818     20.88        70.73   
  done · converged · 13 iters · reduced χ² 70.73 · Rwp 20.88 % · 0.85 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/7.html"></iframe>
</div>

```python
project.display.pattern('mcstas')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/8.html"></iframe>
</div>

### Rise and decay

```python
experiment.peak.rise_alpha_1.free = True
experiment.peak.decay_beta_0.free = True
experiment.peak.decay_beta_1.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-tof_lbco-si-mcstas, 633 pts fitted / 1000 loaded, 23 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       20.88        71.07
      1      0.020     20.86        70.93   0.2% ↓
      2      0.030     20.86        70.93   
      3      0.040     20.86        70.92   
      4      0.050     20.86        70.92   
      5      0.071     20.86        70.92   
  done · converged · 5 iters · reduced χ² 70.92 · Rwp 20.86 % · 0.08 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/9.html"></iframe>
</div>

```python
project.display.pattern('mcstas')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/10.html"></iframe>
</div>

### Displacements

Co's and O's; La's, Ba's and Si's stay fixed, as the case's project keeps them.

```python
lbco.atom_sites['Co'].adp_iso.free = True
lbco.atom_sites['O'].adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project pd-neut-tof_lbco-si-mcstas, 633 pts fitted / 1000 loaded, 25 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       20.86        71.15
      1      0.021      7.47         9.13   87.2% ↓
      2      0.031      6.22         6.33   30.7% ↓
      3      0.041      5.98         5.85   7.7% ↓
      4      0.051      5.73         5.36   8.3% ↓
      5      0.061      5.53         5.00   6.8% ↓
      6      0.071      5.43         4.83   3.4% ↓
      7      0.080      5.38         4.73   2.0% ↓
      8      0.090      5.31         4.61   2.6% ↓
      9      0.100      5.22         4.45   3.4% ↓
     10      0.110      5.13         4.30   3.4% ↓
     11      0.121      5.07         4.20   2.2% ↓
     12      0.131      5.05         4.17   0.9% ↓
     13      0.141      5.04         4.16   0.2% ↓
     14      0.152      5.04         4.16   
     15      0.175      5.04         4.16   
  done · converged · 15 iters · reduced χ² 4.16 · Rwp 5.04 % · 0.18 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/11.html"></iframe>
</div>

```python
project.display.pattern('mcstas')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/12.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/13.html"></iframe>
</div>

```python
project.display.structure('lbco')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/14.html"></iframe>
</div>

```python
project.display.structure('si')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-tof_lbco-si-mcstas/15.html"></iframe>
</div>

## Save the project

```python
project.save_as('pd-neut-tof_lbco-si-mcstas')
project.report.save_html('pd-neut-tof_lbco-si-mcstas.html')
```

```text
Saving project to 'pd-neut-tof_lbco-si-mcstas'
Saving report to 'pd-neut-tof_lbco-si-mcstas.html'
```
