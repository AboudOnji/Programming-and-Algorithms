# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Course materials for **Algoritmos y Programación** (Facultad de Ingeniería, Universidad Anáhuac México). It contains LaTeX Beamer presentations, Python example scripts, and utility scripts for managing compiled PDFs. See `PLAN_MAGISTERIAL.md` for the full 14-conference syllabus.

## Students profil
- Students in Fac. of Engineering (mecatronic, industrial, ... etc.) with basic information about computers, algoritms and programming.

## Identity
- Prof. Dr. Aboud Barsekh-Onji, Professor at the Faculty of Engineering, Universidad Anáhuac México
- Researche Topics:Evolutionary computation, Many Objectives Optimization, Fuzzy Substractive Clustering, hybrid models (Fuzzy Logic, PSO/MOPSO, LSTM, Deep and Machine learning algorithms)

## Technical environment
- OS: Ubuntu 24.04, ThinkPad T14
- Python: conda env `research` (Python 3.11)
  - NEVER use venv/virtualenv, always conda
  - Interpreter: /home/aboudonji/miniforge3/envs/research/bin/python
- MATLAB: R2025b (main language)
- LaTeX: pdflatex by default, xelatex as fallback

## Delivery rules
- Academic documents: Markdown or LaTeX/Beamer (Berlin theme, 16:9)
- Presentations: Beamer, NOT PowerPoint
- Skills available in: ~/.config/claude/skills/

## Language
- Respond in the language in which the question is asked (ES/EN/AR)

## Compiling presentations

Each conference lives in its own `conf (N) Topic/` folder. To compile a single presentation:

```bash
cd "conf (10) Subrutinas"
pdflatex -interaction=nonstopmode subrutinas1.tex
```

Run twice if cross-references or overlays are stale. The utility script compiles all folders missing PDFs:

```bash
python compile_missing_pdfs.py
```

To copy all PDFs into `Evidencias/`:

```bash
python copy_evidence_prog.py
```

> **Note:** Both utility scripts hardcode a macOS Google Drive path. Update `source_root` to the local Linux path before running.

## Beamer theme and preamble

All presentations use the **SimpleDarkBlue** theme (`aspectratio=169`). The four `.sty` files for this theme must exist in the same folder as the `.tex` file (each `conf */` folder contains its own copy).

Standard preamble pattern:

```latex
\documentclass[aspectratio=169,xcolor=dvipsnames]{beamer}
\usetheme{SimpleDarkBlue}
\usepackage[spanish]{babel}
\usepackage{listings}   % code blocks
\usepackage{algorithm,algorithmicx,algpseudocode}
```

Python `lstlisting` style (colors: `codegreen`, `codegray`, `codepurple`, `backcolour`) is defined in each file — copy from any existing `.tex` when creating new slides.

## Folder conventions

| Folder | Contents |
|---|---|
| `conf (N) Topic/` | `.tex` source + compiled `.pdf` + theme `.sty` files |
| `Graphics conferences/` | Slides for Phase 6 (OOP/tkinter) + Python GUI examples |
| `Listas/` | Slides for the Lists module |
| `example/` | Blank template (`free.tex`) to start a new presentation |
| `Evidencias/` | Copies of all compiled PDFs (managed by `copy_evidence_prog.py`) |

## Python examples

Scripts inside conference folders and `Graphics conferences/` are live demos shown in class. They target **Python 3.11** (`conda env research`). No test suite exists — run scripts directly with the conda interpreter:

```bash
/home/aboudonji/miniforge3/envs/research/bin/python script.py
```
