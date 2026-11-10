Canonical page: https://easydiffraction.org/python/structures/

# :fa5-layer-group: Structures and parameters

A structure describes the crystal: its symmetry, unit-cell geometry and atom sites. Experiments link the structures that contribute to their calculated data.

The shared [Structure](https://easydiffraction.org/user-guide/analysis-workflow/structure/) chapter explains the scientific model; the steps below describe this interface.

## Inspect a loaded structure

```python
import edi

project = edi.Project.load('path/to/project')

for structure in project.structures:
    print(structure.name)
    print(structure.space_group.name_h_m)
    print(structure.cell.length_a.value)
```

[Cell lengths and angles](https://easydiffraction.org/physics/crystallography/#eq-cell-metric) are parameters with values. A space-group name selects symmetry; it is not a floating-point fit parameter.

## Read and change a parameter

For a project with at least one structure:

```python
structure = project.structures[0]
length_a = structure.cell.length_a

print(length_a.value)
print(length_a.free)
length_a.free = True
```

The [`free` flag](https://easydiffraction.org/physics/minimization/#eq-jacobian) allows a parameter to vary during a fit. Set it only when that parameter belongs in the scientific model you intend to fit. Setting `free = True` on a value a fit cannot vary raises an error that gives the reason. On a value set by symmetry or a constraint, it is ignored with a warning and the value stays dependent. Shared [parameter concepts](https://easydiffraction.org/user-guide/parameters/) explain values, uncertainties and constraints.

## Inspect the free set

```python
for parameter in project.free_parameters:
    print(parameter.name, parameter.value, parameter.units)
```

This project-level list includes structural and experimental parameters. It helps you review the analysis before running a fit.

## Read a structure file

The factory reads a structure from a CIF or `.edi` file, and the project's collection reads one and adds it:

```python
structure = edi.StructureFactory.from_cif_path('structure.cif')
project.structures.add_from_cif_path('structure.cif')
```

`from_cif_str` and `add_from_cif_str` take the text instead of a path.

This creates a structure object; it does not by itself create a complete measurement and analysis project. Imported values start fixed. Items in the file that EasyDiffraction does not read come back as Python warnings starting with `crysta.schema.cif_items_not_read`, and a file EasyDiffraction cannot read raises an error that names the item. See [CIF files](https://easydiffraction.org/user-guide/data-formats/#cif-files).

For a complete runnable analysis, start from a project or a checked example. These pages intentionally document a demonstrated subset rather than claiming that all constructors and file variants are covered.



[Compare Python paths with GUI labels, Edi keys and CIF names](https://easydiffraction.org/user-guide/parameters/#parameter-names).
