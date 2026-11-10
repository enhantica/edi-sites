Canonical page: https://easydiffraction.org/python/tutorials/cases/pd-neut-cwl_cosio-d20/

<div class="ed-tutorial-buttons" markdown>
[:simple-googlecolab: Open in Google Colab](https://colab.research.google.com/github/enhantica/edi/blob/e9334c7713570499c3a02e4010c0832ce46d44fd/docs/user/tutorials/pd-neut-cwl_cosio-d20.ipynb){ .md-button .ed-tutorial-button target="_blank" rel="noopener" }
[:fa5-download: Download Notebook](https://easydiffraction.org/assets/tutorials/notebooks/pd-neut-cwl_cosio-d20.ipynb){ .md-button .ed-tutorial-button download }
</div>

# Co₂SiO₄ on D20

This tutorial fits the olivine Co₂SiO₄ to constant-wavelength neutron powder data measured on
D20 at the ILL. Its structure and its measured pattern come from EasyDiffraction's collection;
the tutorial describes the experiment, links the two and fits the coordinates, the
displacements and the oxygen occupancies.

<span style="color:#398648;background:#39864821;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMzk4NjQ4IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA0OTYgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI0OCA4QzExMS4wMzAyNzM0Mzc1IDguMCAwLjAgMTE5LjAzMDI3MzQzNzUgMC4wIDI1Ni4wQzAuMCAzOTIuOTY5NzI2NTYyNSAxMTEuMDMwMjczNDM3NSA1MDQuMCAyNDguMCA1MDQuMEMzODQuOTY5NzI2NTYyNSA1MDQuMCA0OTYuMCAzOTIuOTY5NzI2NTYyNSA0OTYuMCAyNTYuMEM0OTYuMCAxMTkuMDMwMjczNDM3NSAzODQuOTY5NzI2NTYyNSA4LjAgMjQ4LjAgOC4wWk0yNDguMCA0NDAuMEMxNDYuMzA5NTcwMzEyNSA0NDAuMCA2NC4wIDM1Ny43MDk5NjA5Mzc1IDY0LjAgMjU2LjBDNjQuMCAxNTQuMzA5NTcwMzEyNSAxNDYuMjkwMDM5MDYyNSA3Mi4wIDI0OC4wIDcyLjBDMzQ5LjY5MDQyOTY4NzUgNzIuMCA0MzIuMCAxNTQuMjkwMDM5MDYyNSA0MzIuMCAyNTYuMEM0MzIuMCAzNTcuNjkwNDI5Njg3NSAzNDkuNzA5OTYwOTM3NSA0NDAuMCAyNDguMCA0NDAuMFpNMjQ4LjAgMTI4LjBDMTc3LjMwOTU3MDMxMjUgMTI4LjAgMTIwLjAgMTg1LjMwOTU3MDMxMjUgMTIwLjAgMjU2LjBDMTIwLjAgMzI2LjY5MDQyOTY4NzUgMTc3LjMwOTU3MDMxMjUgMzg0LjAgMjQ4LjAgMzg0LjBDMzE4LjY5MDQyOTY4NzUgMzg0LjAgMzc2LjAgMzI2LjY5MDQyOTY4NzUgMzc2LjAgMjU2LjBDMzc2LjAgMTg1LjMwOTU3MDMxMjUgMzE4LjY5MDQyOTY4NzUgMTI4LjAgMjQ4LjAgMTI4LjBaTTI0OC4wIDMyMC4wQzIxMi43MDk5NjA5Mzc1IDMyMC4wIDE4NC4wIDI5MS4yOTAwMzkwNjI1IDE4NC4wIDI1Ni4wQzE4NC4wIDIyMC43MDk5NjA5Mzc1IDIxMi43MDk5NjA5Mzc1IDE5Mi4wIDI0OC4wIDE5Mi4wQzI4My4yOTAwMzkwNjI1IDE5Mi4wIDMxMi4wIDIyMC43MDk5NjA5Mzc1IDMxMi4wIDI1Ni4wQzMxMi4wIDI5MS4yOTAwMzkwNjI1IDI4My4yOTAwMzkwNjI1IDMyMC4wIDI0OC4wIDMyMC4wWiIvPjwvc3ZnPgo=" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Fitting</span> <span style="color:#96601d;background:#96601d21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjOTY2MDFkIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTI1NiA4QzExOS4wMzMyMDMxMjUgOC4wIDguMCAxMTkuMDMzMjAzMTI1IDguMCAyNTYuMEM4LjAgMzkyLjk2Njc5Njg3NSAxMTkuMDMzMjAzMTI1IDUwNC4wIDI1Ni4wIDUwNC4wQzM5Mi45NjY3OTY4NzUgNTA0LjAgNTA0LjAgMzkyLjk2Njc5Njg3NSA1MDQuMCAyNTYuMEM1MDQuMCAxMTkuMDMzMjAzMTI1IDM5Mi45NjY3OTY4NzUgOC4wIDI1Ni4wIDguMFpNMzM2LjAgMjU2LjBDMzM2LjAgMzAwLjExMjMwNDY4NzUgMzAwLjExMjMwNDY4NzUgMzM2LjAgMjU2LjAgMzM2LjBDMjExLjg4NzY5NTMxMjUgMzM2LjAgMTc2LjAgMzAwLjExMjMwNDY4NzUgMTc2LjAgMjU2LjBDMTc2LjAgMjExLjg4NzY5NTMxMjUgMjExLjg4NzY5NTMxMjUgMTc2LjAgMjU2LjAgMTc2LjBDMzAwLjExMjMwNDY4NzUgMTc2LjAgMzM2LjAgMjExLjg4NzY5NTMxMjUgMzM2LjAgMjU2LjBaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Single</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">pd</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">neut</span> <span style="color:#424242;background:#42424221;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">cwl</span> <span style="color:#0084c7;background:#0084c721;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em">Bragg</span> <span style="color:#00796b;background:#00796b21;border-radius:3px;padding:0.1em 0.4em;font-size:0.85em"><img src="data:image/svg+xml;base64,PHN2ZyBmaWxsPSIjMDA3OTZiIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48IS0tIEZvbnQgQXdlc29tZSBGcmVlIDUuMTUuNCBieSBAZm9udGF3ZXNvbWUsIGh0dHBzOi8vZm9udGF3ZXNvbWUuY29tLCBDQyBCWSA0LjAgLS0+PHBhdGggZD0iTTEyLjQxMDE1NjI1IDE0OC4wMTk1MzEyNSAyNDUuMzQ5NjA5Mzc1IDI1My42OTA0Mjk2ODc1QzI1Mi4xNTAzOTA2MjUgMjU2Ljc4MDI3MzQzNzUgMjU5LjgzOTg0Mzc1IDI1Ni43ODAyNzM0Mzc1IDI2Ni42Mzk2NDg0Mzc1IDI1My42OTA0Mjk2ODc1TDQ5OS41ODAwNzgxMjUgMTQ4LjAxOTUzMTI1QzUxNi4xMjk4ODI4MTI1IDE0MC41MDk3NjU2MjUgNTE2LjEyOTg4MjgxMjUgMTE1LjUgNDk5LjU4MDA3ODEyNSAxMDcuOTkwMjM0Mzc1TDI2Ni42NTAzOTA2MjUgMi4zMDk1NzAzMTI1QzI2My40MTMwODU5Mzc1IDAuODMwMDc4MTI1IDI1OS44MTU0Mjk2ODc1IDAuMDA1ODU5Mzc1IDI1Ni4wMjYzNjcxODc1IDAuMDA1ODU5Mzc1QzI1Mi4yMzczMDQ2ODc1IDAuMDA1ODU5Mzc1IDI0OC41OTY2Nzk2ODc1IDAuODMwMDc4MTI1IDI0NS4zNjAzNTE1NjI1IDIuMzA5NTcwMzEyNUwxMi40MTAxNTYyNSAxMDcuOTgwNDY4NzVDLTQuMTM5NjQ4NDM3NSAxMTUuNDkwMjM0Mzc1IC00LjEzOTY0ODQzNzUgMTQwLjUwOTc2NTYyNSAxMi40MTAxNTYyNSAxNDguMDE5NTMxMjVaTTQ5OS41ODk4NDM3NSAyMzYuMjk5ODA0Njg3NSA0NDEuNSAyMDkuOTY5NzI2NTYyNSAyNzkuODYwMzUxNTYyNSAyODMuMjQwMjM0Mzc1QzI3Mi4yOTk4MDQ2ODc1IDI4Ni42Njk5MjE4NzUgMjY0LjI2OTUzMTI1IDI4OC40MTAxNTYyNSAyNTYuMCAyODguNDEwMTU2MjVDMjQ3LjczMDQ2ODc1IDI4OC40MTAxNTYyNSAyMzkuNzA5OTYwOTM3NSAyODYuNjY5OTIxODc1IDIzMi4xMzk2NDg0Mzc1IDI4My4yNDAyMzQzNzVMNzAuNTA5NzY1NjI1IDIwOS45Njk3MjY1NjI1TDEyLjQxMDE1NjI1IDIzNi4yOTk4MDQ2ODc1Qy00LjEzOTY0ODQzNzUgMjQzLjc5OTgwNDY4NzUgLTQuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSAxMi40MTAxNTYyNSAyNzYuMjk5ODA0Njg3NUwyNDUuMzQ5NjA5Mzc1IDM4MS44ODk2NDg0Mzc1QzI1Mi4xNTAzOTA2MjUgMzg0Ljk2OTcyNjU2MjUgMjU5LjgzOTg0Mzc1IDM4NC45Njk3MjY1NjI1IDI2Ni42Mzk2NDg0Mzc1IDM4MS44ODk2NDg0Mzc1TDQ5OS41ODk4NDM3NSAyNzYuMjk5ODA0Njg3NUM1MTYuMTM5NjQ4NDM3NSAyNjguNzk5ODA0Njg3NSA1MTYuMTM5NjQ4NDM3NSAyNDMuNzk5ODA0Njg3NSA0OTkuNTg5ODQzNzUgMjM2LjI5OTgwNDY4NzVaTTQ5OS41ODk4NDM3NSAzNjQuMDk5NjA5Mzc1IDQ0MS43MTk3MjY1NjI1IDMzNy44NzAxMTcxODc1IDI3OS44NjAzNTE1NjI1IDQxMS4yNDAyMzQzNzVDMjcyLjI5OTgwNDY4NzUgNDE0LjY2OTkyMTg3NSAyNjQuMjY5NTMxMjUgNDE2LjQxMDE1NjI1IDI1Ni4wIDQxNi40MTAxNTYyNUMyNDcuNzMwNDY4NzUgNDE2LjQxMDE1NjI1IDIzOS43MDk5NjA5Mzc1IDQxNC42Njk5MjE4NzUgMjMyLjEzOTY0ODQzNzUgNDExLjI0MDIzNDM3NUw3MC4yOTAwMzkwNjI1IDMzNy44NzAxMTcxODc1TDEyLjQxMDE1NjI1IDM2NC4wOTk2MDkzNzVDLTQuMTM5NjQ4NDM3NSAzNzEuNTk5NjA5Mzc1IC00LjEzOTY0ODQzNzUgMzk2LjU5OTYwOTM3NSAxMi40MTAxNTYyNSA0MDQuMDk5NjA5Mzc1TDI0NS4zNDk2MDkzNzUgNTA5LjY5MDQyOTY4NzVDMjUyLjE1MDM5MDYyNSA1MTIuNzY5NTMxMjUgMjU5LjgzOTg0Mzc1IDUxMi43Njk1MzEyNSAyNjYuNjM5NjQ4NDM3NSA1MDkuNjkwNDI5Njg3NUw0OTkuNTg5ODQzNzUgNDA0LjA5OTYwOTM3NUM1MTYuMTM5NjQ4NDM3NSAzOTYuNTk5NjA5Mzc1IDUxNi4xMzk2NDg0Mzc1IDM3MS41OTk2MDkzNzUgNDk5LjU4OTg0Mzc1IDM2NC4wOTk2MDkzNzVaIi8+PC9zdmc+Cg==" alt="" style="height:0.85em;vertical-align:-0.1em;margin-right:0.3em">Crystal structure</span>

## Import the library

```python
import easydiffraction as edi
```

## Define the project

```python
project = edi.Project(name='cosio_d20')
```

## Define the structure

Load the structure from the collection. The CIF gives the space group P n m a, the cell and the
six sites, and marks the cell, coordinates, displacements and oxygen occupancies to fit. The fit
below frees them in stages, so start with all of them fixed.

```python
structure_path = edi.download_data('pd-neut-cwl_cosio-d20-cosio', destination='data')
project.structures.add_from_cif_path(structure_path)
structure = project.structures['cosio']
for parameter in project.free_parameters:
    parameter.free = False
```

```text
Data 'pd-neut-cwl_cosio-d20-cosio' is at data/pd-neut-cwl_cosio-d20-cosio.edi
```

```python
project.display.structure('cosio')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/1.html"></iframe>
</div>

## Define the experiment

The measured pattern also comes from the collection.

```python
data_path = edi.download_data('pd-neut-cwl_cosio-d20-d20-data', destination='data')
project.experiments.add_from_data_path(
    name='d20',
    data_path=data_path,
    sample_form='powder',
    beam_mode='constant wavelength',
    radiation_probe='neutron',
    scattering_type='bragg',
)
experiment = project.experiments['d20']
```

```text
Data 'pd-neut-cwl_cosio-d20-d20-data' is at data/pd-neut-cwl_cosio-d20-d20.xye
```

D20's wavelength is 1.87 Å. The profile is the Thompson-Cox-Hastings pseudo-Voigt, and a flat
background runs through fourteen points.

```python
experiment.instrument.setup_wavelength = 1.87
experiment.instrument.calib_twotheta_offset = 0
experiment.peak.broad_gauss_u = 0.2
experiment.peak.broad_gauss_v = -0.5
experiment.peak.broad_gauss_w = 0.4
experiment.peak.broad_lorentz_y = 0.01
for position in (8, 9, 10, 11, 12, 15, 25, 30, 50, 70, 90, 110, 130, 150):
    experiment.background.create(position=position, intensity=340)
experiment.linked_structures.create(structure_id='cosio', scale=1)
```

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/2.html"></iframe>
</div>

## Perform the analysis

The fit goes in stages, freeing one group of parameters at a time.

### Scale, 2θ zero and cell

The scale sets the overall height of the pattern, and the zero shift and the three cell lengths
put the peaks where they are measured.

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
<iframe style="width: 100%; height: 236px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/3.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 5 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       40.51       452.01
      1      0.003     32.67       293.90   35.0% ↓
      2      0.005     28.52       224.01   23.8% ↓
      3      0.007     24.07       159.57   28.8% ↓
      4      0.009     20.61       117.03   26.7% ↓
      5      0.012     20.10       111.27   4.9% ↓
      6      0.014     20.09       111.14   0.1% ↓
      7      0.016     20.09       111.14   
      8      0.019     20.09       111.14   
  done · converged · 8 iters · reduced χ² 111.14 · Rwp 20.09 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/4.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/5.html"></iframe>
</div>

### Background

With the peaks in place, the fourteen background points follow the level between them.

```python
for point in experiment.background:
    point.intensity.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 19 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                       20.09       112.25
      1      0.004      5.51         8.45   92.5% ↓
      2      0.007      5.51         8.45   
      3      0.011      5.51         8.45   
  done · converged · 3 iters · reduced χ² 8.45 · Rwp 5.51 % · 0.01 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/6.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/7.html"></iframe>
</div>

### Peak widths

The profile terms now fit the widths and shapes of the peaks. diffraction-lib's tutorial also
fits a peak asymmetry; this case's profile has none.

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
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 23 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        5.51         8.47
      1      0.004      4.84         6.54   22.8% ↓
      2      0.007      4.80         6.43   1.7% ↓
      3      0.010      4.80         6.42   0.1% ↓
      4      0.013      4.80         6.42   
      5      0.017      4.80         6.42   
  done · converged · 5 iters · reduced χ² 6.42 · Rwp 4.80 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/8.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/9.html"></iframe>
</div>

### Atom positions

The peak intensities now depend mostly on where the atoms are. Co1 sits on a centre of
symmetry and the other sites on the mirror plane, so only their free coordinates are fitted.

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
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 34 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.80         6.47
      1      0.006      4.15         4.84   25.2% ↓
      2      0.010      4.14         4.82   0.4% ↓
      3      0.015      4.14         4.82   
      4      0.021      4.14         4.82   
  done · converged · 4 iters · reduced χ² 4.82 · Rwp 4.14 % · 0.03 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/10.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/11.html"></iframe>
</div>

### Displacements

The displacements change the intensities more at high angle.

```python
for site in structure.atom_sites:
    site.adp_iso.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 40 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.14         4.84
      1      0.006      3.99         4.50   7.0% ↓
      2      0.010      3.99         4.49   0.1% ↓
      3      0.017      3.99         4.49   
  done · converged · 3 iters · reduced χ² 4.49 · Rwp 3.99 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/12.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/13.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/14.html"></iframe>
</div>

### Constrain the two Co sites

The correlations show no strong pair for the two Co sites, yet the fit gives them very different
displacements, Co1's even negative, which no atom can have: both are Co and scatter alike, so
the pattern cannot tell their thermal motions apart. Give each an alias and constrain Co2's to
follow Co1's, starting again from 0.5 Å², then fit again; the shared displacement is positive and
its s.u. smaller than either had alone.

```python
structure.atom_sites['Co2'].adp_iso.free = False
structure.atom_sites['Co1'].adp_iso = 0.5
project.analysis.aliases.create(id='biso_Co1', param=structure.atom_sites['Co1'].adp_iso)
project.analysis.aliases.create(id='biso_Co2', param=structure.atom_sites['Co2'].adp_iso)
project.analysis.constraints.create(id='biso_Co2', expression='biso_Co2 = biso_Co1')
project.display.constraints()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 180px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/15.html"></iframe>
</div>

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 39 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.05         4.64
      1      0.006      4.02         4.57   1.6% ↓
      2      0.010      4.02         4.57   
      3      0.016      4.02         4.57   
  done · converged · 3 iters · reduced χ² 4.57 · Rwp 4.02 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/16.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/17.html"></iframe>
</div>

### Oxygen occupancies

Last, the oxygen occupancies, which change the intensities as the displacements do.

```python
structure.atom_sites['O1'].occupancy.free = True
structure.atom_sites['O2'].occupancy.free = True
structure.atom_sites['O3'].occupancy.free = True
```

```python
project.analysis.fit()
project.display.fit.results()
```

```text
edi fit: project cosio_d20, 1418 pts fitted / 1418 loaded, 42 free
   iter   time (s)   Rwp (%)  reduced χ²   change
                        4.02         4.58
      1      0.005      3.98         4.48   2.2% ↓
      2      0.009      3.97         4.45   0.5% ↓
      3      0.014      3.97         4.45   
  done · converged · 3 iters · reduced χ² 4.45 · Rwp 3.97 % · 0.02 s
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 376px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/18.html"></iframe>
</div>

```python
project.display.pattern('d20')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/19.html"></iframe>
</div>

```python
project.display.pattern('d20', x_min=40, x_max=60)
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 480px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/20.html"></iframe>
</div>

```python
project.display.fit.correlations()
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 560px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/21.html"></iframe>
</div>

```python
project.display.structure('cosio')
```

<div class="ed-notebook-output" markdown="0">
<iframe style="width: 100%; height: 660px; border: none" onload="(f=&gt;{const d=f.contentDocument;if(!d)return;const r=()=&gt;{f.style.height=Math.ceil(d.body.getBoundingClientRect().height)+'px'};r();new ResizeObserver(r).observe(d.body)})(this)" loading="lazy" src="../../../assets/tutorials/views/pd-neut-cwl_cosio-d20/22.html"></iframe>
</div>

## Save the project

```python
project.save_as('cosio_d20')
```

```text
Saving project to 'cosio_d20'
```
