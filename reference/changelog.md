Canonical page: https://easydiffraction.org/changelog/

# What's new

Changes in published EasyDiffraction releases, newest first. The labels show which part of EasyDiffraction a change affects:

- **:fa5-desktop: desktop**{ .ed-release-interface } Affects the EasyDiffraction desktop app
- **:fa5-globe: web**{ .ed-release-interface } Affects the EasyDiffraction web app
- **:simple-python: py**{ .ed-release-interface } Affects the Python API in scripts or notebooks
- **:simple-python: cli-py**{ .ed-release-interface } Affects the CLI installed from the Python package
- **:fa5-terminal: cli**{ .ed-release-interface } Affects the standalone CLI executable

## [v2026.11.22 (17 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.22)

**Added**

- Sign the installers and command-line tools on macOS and Windows ([#82](https://github.com/enhantica/edi/pull/82)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface } **:fa5-terminal: cli**{ .ed-release-interface }

**Fixed**

- Point the Pages check's fake web app at its multithread kit ([#80](https://github.com/enhantica/edi/pull/80)) **:fa5-globe: web**{ .ed-release-interface }
- Ship a separately signed maintenance tool on macOS ([#83](https://github.com/enhantica/edi/pull/83)) **:fa5-desktop: desktop**{ .ed-release-interface }

<!-- edi release date 2026-11-17 -->

---

## [v2026.11.20 (16 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.20)

**Added**

- Faster fits, selectable stop rules, ABSCOR2 removed ([#24](https://github.com/enhantica/edi/pull/24)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface } **:simple-python: py**{ .ed-release-interface } **:simple-python: cli-py**{ .ed-release-interface } **:fa5-terminal: cli**{ .ed-release-interface }
- Survey, intro animation, merged title bar and Auto fits ([#73](https://github.com/enhantica/edi/pull/73)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface } **:simple-python: py**{ .ed-release-interface } **:simple-python: cli-py**{ .ed-release-interface } **:fa5-terminal: cli**{ .ed-release-interface }

**Fixed**

- Install the smoke-test wheel with its declared dependencies ([#75](https://github.com/enhantica/edi/pull/75)) **:simple-python: py**{ .ed-release-interface }
- Keep the environment lib directory on the macOS CLI link path ([#76](https://github.com/enhantica/edi/pull/76)) **:fa5-terminal: cli**{ .ed-release-interface }
- Link only the SDK's sleef into the macOS CLI ([#77](https://github.com/enhantica/edi/pull/77)) **:fa5-terminal: cli**{ .ed-release-interface }
- Admit the system libc++abi in the macOS CLI runtime check ([#78](https://github.com/enhantica/edi/pull/78)) **:fa5-terminal: cli**{ .ed-release-interface }
- Skip a macOS library's own install name in the dependency checks ([#79](https://github.com/enhantica/edi/pull/79)) **:fa5-terminal: cli**{ .ed-release-interface }

<!-- edi release date 2026-11-16 -->

---

## [v2026.11.14 (13 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.14)

**Fixed**

- Improve scan responsiveness and fit progress reporting ([#64](https://github.com/enhantica/edi/pull/64)) **:fa5-desktop: desktop**{ .ed-release-interface }

<!-- edi release date 2026-11-13 -->

---

## [v2026.11.13 (12 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.13)

**Fixed**

- Fix the assistant on Windows; install EasyDiffraction with shortcuts ([#60](https://github.com/enhantica/edi/pull/60)) **:fa5-desktop: desktop**{ .ed-release-interface }

**Changed**

- New tutorial screenshots in the docs ([#57](https://github.com/enhantica/edi/pull/57)) **:fa5-desktop: desktop**{ .ed-release-interface }
- Start the Windows installer from Command Prompt when Run anyway is missing ([#58](https://github.com/enhantica/edi/pull/58)) **:fa5-desktop: desktop**{ .ed-release-interface }

<!-- edi release date 2026-11-12 -->

---

## [v2026.11.12 (12 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.12)

**Added**

- Tutorials in fewer clear steps, consistent numbers and GUI fixes ([#55](https://github.com/enhantica/edi/pull/55)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface }

**Fixed**

- Export ENV so the web app can show its release version ([#53](https://github.com/enhantica/edi/pull/53)) **:fa5-globe: web**{ .ed-release-interface }

<!-- edi release date 2026-11-12 -->

---

## [v2026.11.11 (11 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.11)

**Fixed**

- Find Qt from the macOS assistant guard ([#49](https://github.com/enhantica/edi/pull/49)) **:fa5-desktop: desktop**{ .ed-release-interface }

<!-- edi release date 2026-11-11 -->

---

## [v2026.11.10 (11 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.10)

**Added**

- Survey notice, download buttons, assistant start errors and tags ([#48](https://github.com/enhantica/edi/pull/48)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface }

<!-- edi release date 2026-11-11 -->

---

## [v2026.11.9 (11 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.9)

**Added**

- Docs screenshots, tutorial fixes and edi's DOI ([#45](https://github.com/enhantica/edi/pull/45)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface } **:simple-python: py**{ .ed-release-interface }

<!-- edi release date 2026-11-11 -->

---

## [v2026.11.8 (11 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.8)

**Added**

- Survey, GUI and docs updates for the next release ([#34](https://github.com/enhantica/edi/pull/34)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface } **:simple-python: py**{ .ed-release-interface }

<!-- edi release date 2026-11-11 -->

---

## [v2026.11.0 (10 Nov)](https://github.com/enhantica/edi/releases/tag/v2026.11.0)

**Added**

- This is the first release of the new EasyDiffraction, based on crysta ([#3](https://github.com/enhantica/edi/pull/3)) **:fa5-desktop: desktop**{ .ed-release-interface } **:fa5-globe: web**{ .ed-release-interface } **:simple-python: py**{ .ed-release-interface } **:simple-python: cli-py**{ .ed-release-interface } **:fa5-terminal: cli**{ .ed-release-interface }

<!-- edi release date 2026-11-10 -->
