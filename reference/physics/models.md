Canonical page: https://easydiffraction.org/physics/models/

# Model catalogue

<span id="planned-scientific-models"></span>

Use the exact model identifier to select its explanation. Planned and proposed capabilities appear beside related models with their status; they have no selectable type token in this reference snapshot. The [parameter index](https://easydiffraction.org/physics/parameters/) defines individual scientific fields. [Features](https://easydiffraction.org/user-guide/features/) distinguishes editing, execution and planned work in the four interfaces.

## <span class="ed-reference-icon" aria-hidden="true">&#63228;</span> Peak profiles {#peak-profiles}

### Constant-wavelength peak profiles

| Type | Scope | Explanation |
| --- | --- | --- |
| `cwl-gaussian` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/profiles/cw/#eq-cwl-pseudovoigt) |
| `cwl-lorentzian` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/profiles/cw/#eq-cwl-pseudovoigt) |
| `cwl-pseudo-voigt` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/profiles/cw/#eq-caglioti) |
| `cwl-pseudo-voigt-berar-baldinozzi` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/profiles/cw/#eq-berar-baldinozzi) |
| `cwl-tch-pseudo-voigt` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/profiles/cw/#eq-tch) |
| `cwl-tch-pseudo-voigt-fcj` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/profiles/cw/#eq-fcj) |

### Time-of-flight peak profiles

| Type or model | Scope | Explanation |
| --- | --- | --- |
| `tof-jorgensen` | <a class="ed-tag ed-tag--technique" data-ed-tag="beamMode" data-ed-token="time-of-flight" href="../user-guide/glossary/#time-of-flight" title="Time of flight">tof</a> neutron powder | [Physics](https://easydiffraction.org/physics/profiles/tof/#eq-jorgensen) |
| `tof-jorgensen-von-dreele` | <a class="ed-tag ed-tag--technique" data-ed-tag="beamMode" data-ed-token="time-of-flight" href="../user-guide/glossary/#time-of-flight" title="Time of flight">tof</a> neutron powder | [Physics](https://easydiffraction.org/physics/profiles/tof/#eq-jorgensen-von-dreele) |
| `tof-pseudo-voigt` | <a class="ed-tag ed-tag--technique" data-ed-tag="beamMode" data-ed-token="time-of-flight" href="../user-guide/glossary/#time-of-flight" title="Time of flight">tof</a> neutron powder | [Physics](https://easydiffraction.org/physics/profiles/tof/#tof-pseudo-voigt) |
| Ikeda–Carpenter · **Planned** | <a class="ed-tag ed-tag--technique" data-ed-tag="beamMode" data-ed-token="time-of-flight" href="../user-guide/glossary/#time-of-flight" title="Time of flight">tof</a> pulse profile | [Planned model](https://easydiffraction.org/physics/profiles/tof/#ikeda-carpenter) |

## <span class="ed-reference-icon" data-reference-category="absorption" aria-hidden="true">&#61507;</span> Absorption {#absorption}

| Type | Scope | Explanation |
| --- | --- | --- |
| `none` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a>/<a class="ed-tag ed-tag--technique" data-ed-tag="beamMode" data-ed-token="time-of-flight" href="../user-guide/glossary/#time-of-flight" title="Time of flight">tof</a> | [Physics](https://easydiffraction.org/physics/corrections/absorption/#absorption-types) |
| `cylinder-hewat` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a>; <a class="ed-tag ed-tag--technique" data-ed-tag="beamMode" data-ed-token="time-of-flight" href="../user-guide/glossary/#time-of-flight" title="Time of flight">tof</a> input spelling cylinder | [Physics](https://easydiffraction.org/physics/corrections/absorption/#eq-hewat) |
| `cylinder-lobanov` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> | [Physics](https://easydiffraction.org/physics/corrections/absorption/#eq-lobanov) |

## <span class="ed-reference-icon" data-reference-category="extinction" aria-hidden="true">&#62373;</span> Extinction {#extinction}

| Type | Scope | Explanation |
| --- | --- | --- |
| `none` | single-crystal Bragg | [Physics](https://easydiffraction.org/physics/corrections/extinction/#extinction-types) |
| `becker-coppens-type-1` | single-crystal Bragg | [Physics](https://easydiffraction.org/physics/corrections/extinction/#extinction-types) |
| `becker-coppens-type-2` | single-crystal Bragg | [Physics](https://easydiffraction.org/physics/corrections/extinction/#extinction-types) |
| `becker-coppens-mixed` | single-crystal Bragg | [Physics](https://easydiffraction.org/physics/corrections/extinction/#extinction-types) |
| `larson-isotropic` | single-crystal Bragg | [Physics](https://easydiffraction.org/physics/corrections/extinction/#eq-larson) |
| `larson-anisotropic` | single-crystal Bragg | [Physics](https://easydiffraction.org/physics/corrections/extinction/#eq-larson) |

## <span class="ed-reference-icon" data-reference-category="background" aria-hidden="true">&#63550;</span> Background {#background}

| Type | Scope | Explanation |
| --- | --- | --- |
| `line-segment` | powder | [Physics](https://easydiffraction.org/physics/background/#eq-line-segment-background) |
| `polynomial` | powder | [Physics](https://easydiffraction.org/physics/background/#eq-polynomial-background) |
| `chebyshev` | powder | [Physics](https://easydiffraction.org/physics/background/#eq-chebyshev-background) |

## <span class="ed-reference-icon" data-reference-category="atom-site-aniso" aria-hidden="true">&#61618;</span> Atomic displacement {#adp}

| Type | Scope | Explanation |
| --- | --- | --- |
| `Biso` | structure | [Physics](https://easydiffraction.org/physics/displacement/#eq-isotropic-adp) |
| `Uiso` | structure | [Physics](https://easydiffraction.org/physics/displacement/#eq-isotropic-adp) |
| `Bani` | structure | [Physics](https://easydiffraction.org/physics/displacement/#eq-anisotropic-adp) |
| `Uani` | structure | [Physics](https://easydiffraction.org/physics/displacement/#eq-anisotropic-adp) |
| `beta` | structure | [Physics](https://easydiffraction.org/physics/displacement/#eq-anisotropic-adp) |

## <span class="ed-reference-icon" data-reference-category="background-estimate" aria-hidden="true">&#61648;</span> Background estimation {#background-estimation}

| Type | Scope | Explanation |
| --- | --- | --- |
| `auto` | powder baseline proposal | [Physics](https://easydiffraction.org/physics/background/#background-estimation) |
| `arpls` | powder baseline proposal | [Physics](https://easydiffraction.org/physics/background/#eq-arpls) |
| `snip` | powder baseline proposal | [Physics](https://easydiffraction.org/physics/background/#eq-snip) |
| `fabc` | powder baseline proposal | [Physics](https://easydiffraction.org/physics/background/#fabc) |

## <span class="ed-reference-icon" aria-hidden="true">&#62930;</span> Scattering models {#scattering-models}

The current [nuclear neutron](https://easydiffraction.org/physics/diffraction/#eq-nuclear-structure-factor) and [X-ray](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) models use the source selections listed above.

| Model | Status | Explanation |
| --- | --- | --- |
| Nuclear neutron Bragg | Current | [Structure factor](https://easydiffraction.org/physics/diffraction/#eq-nuclear-structure-factor) |
| X-ray Bragg | Current | [Structure factor](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |
| Magnetic neutron powder Bragg, commensurate | Current | [Magnetic structures](https://easydiffraction.org/physics/magnetic/) |
| Polarised diffraction | Planned | [Scattering](https://easydiffraction.org/physics/diffraction/#polarised-diffraction) |
| Total scattering and PDF | Planned | [Scattering](https://easydiffraction.org/physics/diffraction/#total-scattering-and-pdf) |

## <span class="ed-reference-icon" aria-hidden="true">&#62615;</span> X-ray form factor {#xray-form-factor}

| Type | Scope | Explanation |
| --- | --- | --- |
| `wk1995` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> X-ray | [Physics](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |
| `it1992` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> X-ray | [Physics](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |

## <span class="ed-reference-icon" aria-hidden="true">&#61953;</span> X-ray dispersion {#xray-dispersion}

| Type | Scope | Explanation |
| --- | --- | --- |
| `cromer-liberman` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> X-ray | [Physics](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |
| `sasaki1989` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> X-ray | [Physics](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |
| `it1992` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> X-ray | [Physics](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |
| `none` | <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> X-ray | [Physics](https://easydiffraction.org/physics/diffraction/#eq-xray-structure-factor) |

## <span class="ed-reference-icon" aria-hidden="true">&#62791;</span> Neutron scattering length {#neutron-scattering-length}

| Type | Scope | Explanation |
| --- | --- | --- |
| `rauch2003ext` | neutron | [Physics](https://easydiffraction.org/physics/diffraction/#eq-nuclear-structure-factor) |
| `sears1992` | neutron | [Physics](https://easydiffraction.org/physics/diffraction/#eq-nuclear-structure-factor) |

## <span class="ed-reference-icon" data-reference-category="fitting-mode" aria-hidden="true">&#61918;</span> Fitting mode {#fitting-mode}

| Type | Scope | Explanation |
| --- | --- | --- |
| `single` | project analysis | [Physics](https://easydiffraction.org/physics/rietveld/#joint-fitting) |
| `joint` | project analysis | [Physics](https://easydiffraction.org/physics/rietveld/#joint-fitting) |
| `sequential` | project analysis | [Physics](https://easydiffraction.org/physics/rietveld/#sequential-scans) |
| `independent` | project analysis | [Physics](https://easydiffraction.org/physics/rietveld/#independent-scans) |

## <span class="ed-reference-icon" aria-hidden="true">&#61568;</span> Intensity extraction {#intensity-extraction}

| Model | Status | Explanation |
| --- | --- | --- |
| Le Bail | Proposed | [Analysis](https://easydiffraction.org/physics/rietveld/#le-bail-intensity-extraction) |
| Pawley | Proposed | [Analysis](https://easydiffraction.org/physics/rietveld/#pawley-intensity-extraction) |

## <span class="ed-reference-icon" aria-hidden="true">&#62398;</span> Descent {#descent}

| Type | Scope | Explanation |
| --- | --- | --- |
| `ladder` | least-squares; selected strategies have bound restrictions | [Physics](https://easydiffraction.org/physics/minimization/#eq-lm) |
| `fast_descent` | least-squares; selected strategies have bound restrictions | [Physics](https://easydiffraction.org/physics/minimization/#eq-lm) |
| `multistart_prune` | least-squares; selected strategies have bound restrictions | [Physics](https://easydiffraction.org/physics/minimization/#eq-lm) |

## <span class="ed-reference-icon" data-reference-category="preferred-orientation" aria-hidden="true">&#61774;</span> Preferred orientation {#preferred-orientation}

| Type | Scope | Explanation |
| --- | --- | --- |
| `march-dollase` | linked phase in <a class="ed-tag ed-tag--neutral" data-ed-tag="beamMode" data-ed-token="constant wavelength" href="../user-guide/glossary/#constant-wavelength" title="Constant wavelength">cwl</a> powder | [Physics](https://easydiffraction.org/physics/corrections/orientation/#eq-march-dollase) |

## <span class="ed-reference-icon" aria-hidden="true">&#61486;</span> Reference snapshot {#reference-snapshot}

The [machine-readable catalogue](https://easydiffraction.org/physics/catalogue.json) records the inspected edi source and its declared crysta SDK, along with the model/parameter identifiers used for this reference. Availability is scoped to that source snapshot; a development build or installed release can differ. Use its declared model list and version when answering a build-specific question.
