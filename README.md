# Niger: law history in git

The law of Niger as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change to a section; `tools/on.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ne/`.

Language: the official language, French. This README is English first.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution de la VIIème République (décret n°2010-754/PCSRD du 25 novembre 2010), with the modifications to the loi n°2018-44 du 22 juin 2018 | 1 | One "oldest version available": the consolidated text the Government's portal prints, dated 22 June 2018 |
| `code-penal/` | Code pénal (loi n°61-27 du 15 juillet 1961), with all modifications consolidated to January 2018 | 1 | One "oldest version available": the Ministry of Justice edition of January 2018, dated 1 January 2018 (the source gives only the month) |
| `code-procedure-penale/` | Code de procédure pénale (loi n° 61-33 du 14 août 1961), as amended by loi n° 2003-026 du 13 juin 2003 and loi n° 2004-21 du 16 mai 2004 | 1 | One "oldest version available", dated 16 May 2004 (the last amending law the edition names); later amendments not applied |
| `code-du-travail/` | Code du travail (loi n° 2012-45 du 25 septembre 2012) | 1 | One "oldest version available": the Code as enacted, dated 25 September 2012; later amendments not applied |

This is a first build. It holds four texts (the Constitution, the Code pénal, the Code de procédure pénale and the Code du travail) and no change history.

## What it does not show

- **It is a historical text.** The Constitution of the VIIth Republic was suspended after the military takeover of 26 July 2023 and has been replaced by the transition's own texts. Nothing after 2018 is here, and **this repository is not the law in force today.**
- **Earlier wording is not shown.** The portal's PDF prints the 2010 Constitution with the changes of 2011 (loi n°2011-17 and loi n°2011-43), 2017 (loi n°2017-50 and loi n°2017-56) and 2018 (loi n°2018-44) already in place, and gives no earlier wording of the changed articles. These laws are named as the earlier laws in the first commit.
- **The Code pénal is superseded.** It is the Ministry of Justice's consolidated edition of January 2018 (the PDF is hosted by UNODC SHERLOC). The ordonnance n°2026-09 du 16 février 2026 portant institution du Code pénal is reported to have replaced it; that text is not in this record, so the Code pénal here is also not the law in force today. Its amendment notes (for example "(Loi n° 2016-22 du 16 juin 2016)") stay in the paragraphs they introduce. Articles 322 et 323 and 326 à 331 are printed as repealed and each range is one file (`art-322`, `art-326`).
- **The Code de procédure pénale is an older text.** It is the 1961 Code as amended in 2003 and 2004, from a born-digital PDF hosted by UNODC SHERLOC. Later amendments, including loi n° 2019-55 du 22 novembre 2019, are not applied, so it is not the law in force today. Amendment notes such as "(Loi n° 2003-26 du 13 juin 2003)" stay in the text as printed. The edition does not print articles 310 to 317, 736, 737 and 739 to 741; three orphan lines that close Article 317 are left out. Two misprinted numbers ("Art. 7I7", "Art. 679- l") are filed as `art-717` and `art-679-01`.
- **The Code du travail is the text as enacted.** It is loi n° 2012-45 of 25 September 2012, from a born-digital copy published by Droit-Afrique (read from an Internet Archive copy of 15 June 2016). Later amendments are not applied, and the regulatory part (décret n° 2017-682/PRN/MET/PS) is not included.
- **Other law.** Only these four acts. No civil or commercial code was found as an official text online (commercial law is largely the OHADA Uniform Acts). The portal's other pages link to compilations that are scans.
- The notes in article headings naming the amending law are left out of the text. Article 99 appears twice in the source (as amended, and "bis"); the second is `art-099-bis`.
- This is not legal advice, and it is not an official text.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| Article 47 as printed | `python tools/on.py 2018-06-22 constitution art-047` |
| Who wrote each line of Article 47? | `git blame constitution/art-047.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |

Files are named by the printed number: `art-047` is Article 47, `art-099-bis` is Article 99 bis, `titre-03` is Titre III, and `preamble` is the Préambule.

## Dates

Each commit is dated at noon, Africa/Niamey, on the day the version took effect. The single version is dated 22 June 2018, the date of the latest amending law the document names (loi n°2018-44, Article 91). The document gives no entry-into-force dates for the amendments. The original Constitution entered into force on promulgation (Article 183), by décret n°2010-754/PCSRD of 25 November 2010, published in the JORN special issue 19 of 29 November 2010.

## What "author" means

The author of a commit is the law that made the change, at an address that cannot exist. Here the single commit is by the publisher, the Government of Niger's portal, as the **oldest version available**, naming the 2010 décret and the five amending laws.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

The text comes from the Government of Niger's portal, Textes fondamentaux (https://www.gouv.ne/index.php/textes-fondamentaux/constitution-de-la-7eme-republique), PDF https://www.gouv.ne/images/textes-fondamentaux/constitution.pdf, retrieved 29 October 2026. Only the PDF's own text layer was read; nothing was OCRed. The portal publishes no licence; the law of the Republic is public law, reproduced with this attribution.

Changes made by Lexifina: the PDF text was converted to one Markdown file per provision, one paragraph or item per line; page numbers were dropped; spacing, quotes and dashes were normalised; the amendment notes in the article headings were left out. The wording of the law was not changed. The Government of Niger does not endorse this repository.

Lexifina's own contributions (the arrangement of the history, the commit messages, the tables and the tools) are dedicated to the public domain under CC0 1.0 Universal: https://creativecommons.org/publicdomain/zero/1.0/legalcode
