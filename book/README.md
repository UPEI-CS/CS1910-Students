# CS1910 — The Interactive Book

One chapter per lecture topic, in teaching order. Every chapter is a **standalone
notebook**: open it anywhere — JupyterLab, a fresh clone, or a bare upload to
Google Colab — run the setup cell, and everything works. No installs, no
downloads, no other files needed.

## Reading order

| # | Topic | Chapter |
|---|---|---|
| 1 | Course Orientation | *(no chapter — orientation is lecture-only)* |
| 2 | Computational Thinking | [02-Computational-Thinking](02-Computational-Thinking/CS1910_Computational-Thinking_Chapter.ipynb) |
| 3 | Variables, Literals and Types | [03-Variables-Literals-Types](03-Variables-Literals-Types/CS1910_Variables-Literals-Types_Chapter.ipynb) |
| 4 | Expressions | [04-Expressions](04-Expressions/CS1910_Expressions_Chapter.ipynb) |
| 5 | Input and Output | [05-Input-Output](05-Input-Output/CS1910_Input-Output_Chapter.ipynb) |
| 6 | Decisions | [06-Decisions](06-Decisions/CS1910_Decisions_Chapter.ipynb) |
| 7 | Repetitions | [07-Repetitions](07-Repetitions/CS1910_Repetitions_Chapter.ipynb) |
| 8 | Functions | [08-Functions](08-Functions/CS1910_Functions_Chapter.ipynb) |
| 9 | Sequences | [09-Sequences](09-Sequences/CS1910_Sequences_Chapter.ipynb) |
| 10 | Problem Solving and Debugging | [10-Problem-Solving-Debugging](10-Problem-Solving-Debugging/CS1910_Problem-Solving-Debugging_Chapter.ipynb) |
| 11 | Lists | [11-Lists](11-Lists/CS1910_Lists_Chapter.ipynb) |
| 12 | Tuples and Comprehensions | [12-Tuples-Comprehensions](12-Tuples-Comprehensions/CS1910_Tuples-Comprehensions_Chapter.ipynb) |
| 13 | Dictionaries | [13-Dictionaries](13-Dictionaries/CS1910_Dictionaries_Chapter.ipynb) |
| 14 | File Input/Output | [14-File-IO](14-File-IO/CS1910_File-IO_Chapter.ipynb) |
| — | Appendix: Debugging Tips | [appendix](appendix/CS1910_Debugging-Tips_Chapter.ipynb) |

Chapter learning objectives are taken from `course-info/LECTURE_LOS.md`, so the
book and the lecture deck state the same objectives for each topic.

## For students

**Run the setup cell first.** It is the first code cell in every chapter. It
draws that chapter's figures and switches the notebook into "show me every
result" mode, so a cell containing several expressions prints all of them —
the way the Python prompt does. The examples in this book rely on that.

Some cells are marked **▶ Interactive** — they wait for you to type something.
Run those yourself; *Run All* skips them so the rest of the chapter still works.

Cells that show a mistake on purpose are either fenced as text (⚠️ "deliberately
incorrect") or run and display the error they are meant to raise.

## For maintainers

Figures are Python, not images — nothing binary is committed. They are authored
once in `cs1910book/figures.py` and **inlined** into each chapter's setup cell,
which is what makes a lone `.ipynb` work in Colab.

```
cs1910book/figures.py    one draw_<name>(ax) per figure + the FIGURES registry
cs1910book/data.py       sample data files the File-IO chapter writes for itself
cs1910book/build.py      inlines the right code into each chapter's setup cell
cs1910book/verify.py     structural checks over the built chapters
```

To change a figure: edit `figures.py`, then

```
python cs1910book/build.py           # rewrite every chapter's setup cell
python cs1910book/build.py --check   # CI-style: fail if a chapter is out of date
python cs1910book/verify.py          # no dead LaTeX, no >>> transcripts, etc.
```

To check that every chapter still runs standalone (the real test — it copies each
notebook **alone** into an empty directory first):

```
python - <<'PY'
import pathlib, shutil, tempfile, nbformat
from nbclient import NotebookClient
for p in sorted(pathlib.Path(".").glob("*/CS1910_*_Chapter.ipynb")):
    with tempfile.TemporaryDirectory() as td:
        w = pathlib.Path(td); shutil.copy(p, w / p.name)
        nb = nbformat.read(w / p.name, as_version=4)
        NotebookClient(nb, timeout=180, kernel_name="python3",
                       resources={"metadata": {"path": str(w)}}).execute()
    print("ok", p)
PY
```

`FIGURES.md` records what each generated figure replaces. `GAP_REPORT.md` lists
learning objectives the book does not yet cover.

## Provenance

The original LaTeX sources are in `private/book_source/` and the first (lossy)
notebook conversion is in `legacy/book/Notebooks/`. Both are kept as the reference
for everything above; neither is part of the student-facing book, and neither is
published. Retired end-of-chapter exercises and the un-taught Arrays and Recursion
chapters live in `legacy/book/`.

`FIGURES.md`, `GAP_REPORT.md`, and `cs1910book/` are excluded by
`tools/publish_students.py` — students get the chapters and this page, not the workshop.
