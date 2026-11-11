# EasyDiffraction data

The example projects, structures and measured data that EasyDiffraction (edi) loads from the web:
the app's Examples list and its Load ▸ From web… popup, the `edi collection` command and
`edi.load_collection()` in Python all read this folder through its index.

## Layout

```
index.json          the generated index, schema edi-data-index/1
structures/         crystal structures (.cif, .edi)
experiments/        full experiment descriptions (.edi)
data/               measured patterns (.xye and other plain formats)
projects/           zipped example projects, opened as a whole
```

Every file may have a sidecar `<file>.meta.json` holding what the file does not say about itself:
a name, a description, the instrument and facility, the radiation and technique. The index folds
the sidecars together with each file's size and SHA-256 digest into one entry per file, with a
stable id, a kind (structure, experiment, data or project), the chemical formula in Hill notation,
the elements, the space group and the cell when the file states them.

An experiment entry lists the structures it links (`structures`, their entry ids), so loading it from
the web brings them along. `journal-abbreviations.json` holds the ISO 4 journal abbreviations the
app shows in a structure's reference, generated from JabRef's lists (CC0 1.0) with
`python tools/data/build_journal_abbreviations.py <this folder>` in the edi repository.

## Generating the index

The index is generated, never edited by hand, with the script in the edi repository:

```
python tools/data/build_collection.py index  <this folder>   # rewrite index.json
python tools/data/build_collection.py check  <this folder>   # every file present, every digest current
```

`populate` in the same script writes this folder's content from edi's bundled examples and tutorial
files. To add an entry, put the file in its folder, write its sidecar and run `index`.

## Mirrors

The same files are served unchanged from `https://raw.githubusercontent.com/enhantica/edi-data/main/`
and `https://data.easydiffraction.org/`. Any static web server that serves the folder as it is
works as a source; add its URL in the app's Preferences, under Projects, Online sources.
