# How this repository was made (Niger)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Gouvernement du Niger, Textes fondamentaux: Constitution de la 7ème République (PDF) | <https://www.gouv.ne/index.php/textes-fondamentaux/constitution-de-la-7eme-republique> | 2026-10-29 | none published; legislation is public law |
| Ministère de la Justice du Niger, Code pénal et Code de procédure pénale, édition de janvier 2018 (PDF hosted by UNODC SHERLOC) | <https://sherloc.unodc.org/cld/uploads/res/document/code-pnal_html/CODE_PENAL_DU_NIGER_2018.pdf> | 2026-10-30 | none stated; Nigerien legislation is public law |
| UNODC SHERLOC: Niger, Code de procédure pénale (loi n° 61-33, modifiée en 2003 et 2004) | <https://sherloc.unodc.org/cld/uploads/res/document/ner/1961/code_de_procedure_penale_html/Niger_CODE_DE_PROCEDURE_PENALE.pdf> | 2026-10-30 | text of law; the PDF states no licence |
| Droit-Afrique: Niger, Loi n° 2012-45 du 25 septembre 2012 portant Code du travail (Internet Archive capture of 15 June 2016) | <http://www.droit-afrique.com/upload/doc/niger/Niger-Code-2012-du-travail.pdf> | 2026-10-30 | text of law, not protected by copyright (Bangui Agreement, Annex VII, art. 6(i), which applies in Niger as an OAPI member) |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la VIIème République du Niger (décret n°2010-754/PCSRD du 25 novembre 2010), avec les modifications jusqu'à la loi n°2018-44 du 22 juin 2018 | 1 | 2018-06-22 to 2018-06-22 |
| `code-penal` | Code pénal (loi n°61-27 du 15 juillet 1961), avec la refonte de toutes les modifications jusqu'en janvier 2018 | 1 | 2018-01-01 to 2018-01-01 |
| `code-procedure-penale` | Code de procédure pénale (loi n° 61-33 du 14 août 1961), modifié par la loi n° 2003-026 du 13 juin 2003 et la loi n° 2004-21 du 16 mai 2004 | 1 | 2004-05-16 to 2004-05-16 |
| `code-du-travail` | Loi n° 2012-45 du 25 septembre 2012 portant Code du travail de la République du Niger | 1 | 2012-09-25 to 2012-09-25 |

The build made 4 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 6 laws in the record.
- 4 tags.

## Dates

Each commit is dated at noon (Africa/Niamey) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution of 25 November 2010, art. 183: it enters into force on its promulgation. No general commencement rule for amending laws was read; the one version here is dated by the latest amending law the document names. https://www.gouv.ne/images/textes-fondamentaux/constitution.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `bd83ea8d985cdb9f233445c10cb87bcaf17eb1d58fed51a276a67e860d43fd70` (1143375 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

4 versions of 4 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 4 history commits and 4 tags (history tip `8d857a6c953564ced48b3057541878012754fced`).

## Decisions made by hand

- The only official text found online is the consolidated PDF on gouv.ne; it is one 'oldest version available' dated 2018-06-22, the date of the last amending law it names (loi n°2018-44, art. 91).
- Amendment notes in article headings (for example '(nouveau) : (loi n°2017-50 du 06 juin 2017)') are left out of the text; the amending laws are listed as earlier laws, not credited per article.
- Art. 99 appears twice in the source (99 nouveau and 99 bis); the second is stored as art-099-bis.
- Text-layer PDF only, read with pdftotext; page numbers dropped; lines rejoined into paragraphs.
- Code pénal: the Ministry of Justice edition of January 2018 is the only official consolidated text found online; recorded as one 'oldest version available' dated 2018-01-01 (the source gives only the month). It does not include the 2026 ordonnance that is reported to replace it.
- Code pénal: Livre, Titre, Chapitre and Section headings are separate files; the amendment history list, table of contents and page numbers are omitted; wrapped lines are rejoined into paragraphs.
- Code de procédure pénale: one version (first_law null, oldest version available) dated 2004-05-16, the date of loi n° 2004-21, the last amending law the edition names; its publication date in the Journal officiel was not found, so the law date is used. Later amendments, including loi n° 2019-55 du 22 novembre 2019, are not applied.
- Code de procédure pénale units: one per article, keyed by number and sub-number (art-131-01-bis is Article 131-1 bis); amendment notes such as "(Loi n° 2003-26 du 13 juin 2003)" stay in the text as printed; Livre, Titre, Chapitre, Section and § headings and the table of contents are left out; words split at a line end are rejoined and paragraph breaks are rebuilt from the line layout.
- Code de procédure pénale: two article numbers are misprinted in the source ("Art. 7I7", "Art. 679- l"); they are read as 717 and 679-1 for the unit key, and the text is kept as printed. Article numbers missing from the edition (310, 311, 312, 313, 314, 315, 316, 317, 736, 737) have no unit; articles 739 to 741, listed in its table of contents, are not printed. The edition jumps from Article 309 to Article 318 in mid-text: three lines that close Article 317 ("La cour statue sur cette opposition. ...") follow Article 309 without a heading and are left out, because they cannot be placed under a printed article.
- Code du travail: one version, the Code as enacted (first_law null, oldest version available), dated 2012-09-25, the date of loi n° 2012-45; its article 365 only orders publication in the Journal officiel, so the law date is used. Later amendments are not applied; the regulatory part (décret n° 2017-682/PRN/MET/PS) is not included.
- Code du travail units: one per article (art-001 to art-365); Titre, Chapitre and Section headings, page numbers, the promulgation formula and the signatures are left out; words split at a line end are rejoined and paragraph breaks are rebuilt from the line layout.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
- Claude Code wrote the code and chose the source; it did not write or alter any legal text. The code is deterministic and runs no model.
