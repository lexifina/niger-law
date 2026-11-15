# Niger: law history in git


The law of Niger as a git history: one file per article, one commit per version on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to an article; picking a date gives the text in force that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Niger's national law, which global-law reads at `niger/national/acts/`.

**What is in it now:** six texts, each in one version and none with a change history yet: the Constitution of 25 November 2010 as amended to 2018 (the preamble, 185 articles and Article 99 bis); the Code pénal in the Ministry of Justice's edition of January 2018; the Code de procédure pénale as amended to 2004 (749 articles); the Code du travail as enacted in 2012 (365 articles); and the Charte des partis politiques and the Code électoral, each as amended to 2019. Each act's `README.md` lists its provisions.

**Not the law in force today.** The Constitution was suspended after the military takeover of 26 July 2023, the Code pénal is reported to have been replaced in 2026, and later amendments to the other texts are not applied (see [What it does not show](#what-it-does-not-show)).

Each act has its own folder with one file per article (`code-du-travail/art-116.md` is Article 116 of the Code du travail, on paid leave; `constitution/art-099-bis.md` is Article 99 bis). The Constitution's preamble and title headings are `preamble.md` and `titre-01.md` to `titre-14.md`; the Code pénal's headings are `part-*.md`; the Code électoral and the Charte des partis politiques are each one file, `texte-integral.md`.

The text is in French, as its sources print it. An English translation is not part of this record.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every change to Article 116 of the Code du travail (paid leave) | `git log -p --word-diff -- code-du-travail/art-116.md` |
| Which law wrote each line of Article 116? | `git blame code-du-travail/art-116.md` |
| Every version of Article 116, with the day each took effect | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- code-du-travail/art-116.md` |
| Article 116 on 1 January 2015, as this record holds it | `python tools/on.py 2015-01-01 code-du-travail art-116` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about the law of Niger](https://global-law.lexifina.com/v1/try_claude?country=niger)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=niger)**: the same question in ChatGPT.
- **[Call the API in your browser](https://global-law.lexifina.com/v1/search_law?query=cong%C3%A9+pay%C3%A9&jurisdictions=niger)**: a search of the law of Niger for "congé payé" (paid leave), returned as JSON. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in French or in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add niger/national/acts
python3 tools/law.py show 2026-01-01 niger/national/acts/code-du-travail/art-116.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, Africa/Niamey, on the day the version took effect, and carries it in its `In-force:` trailer. No source gives a commencement date for its version, so:

- the Constitution is dated 22 June 2018, the date of loi n°2018-44, the last amending law it names; the Code de procédure pénale 16 May 2004, the date of loi n° 2004-21, likewise;
- the Code du travail is dated 25 September 2012, the date of loi n° 2012-45 (its Article 365 only orders publication in the Journal officiel);
- the Code électoral and the Charte des partis politiques are dated by the latest amendment their PDFs print (18 July 2019 and 17 June 2019);
- the Code pénal is dated 1 January 2018: its edition gives only the month.

Each version is the "oldest version available", credited to the publisher the repository records, the Gouvernement du Niger (gouv.ne), Textes fondamentaux, including the three texts taken from UNODC SHERLOC and Droit-Afrique; its commit message names the laws the source says produced the text (the Constitution's names the 2010 promulgation décret and five amending laws). The committer is always Lexifina.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before, and both must match the corpus the history was built from; it also checks that every commit's trailers parse, that there are no merge commits and that no commit date goes backwards or lies in the future.
- `tools/build.py` writes the history from that corpus in one pass; a second build into an empty folder gave identical hashes. The results are in [`REPRODUCE.md`](REPRODUCE.md), and [`data/corpus.sha256`](data/corpus.sha256) gives the corpus's hash.
- The text is the PDFs' own text layer, not a transcription. [`LICENSE`](LICENSE) lists what was changed (layout, page numbers, spacing, quotes and dashes; amendment notes in article headings left out), and `REPRODUCE.md` each act's decisions by hand.

## What it does not show

- **The law in force today.** The Constitution of the VIIth Republic was suspended after 26 July 2023 and replaced by the transition's own texts. The ordonnance n°2026-09 du 16 février 2026 portant institution du Code pénal is reported to have replaced the Code pénal; its text is not here.
- **Later amendments.** The Code de procédure pénale lacks those after 2004 (among them loi n° 2019-55 du 22 novembre 2019); the Code du travail those after 2012, and its regulatory part (décret n° 2017-682/PRN/MET/PS).
- **Earlier wording.** The Constitution comes with the changes of 2011, 2017 and 2018 already in place; the portal gives no earlier wording of the changed articles.
- **Articles the editions do not print.** The Code de procédure pénale skips articles 310 to 317, 736, 737 and 739 to 741; two misprinted numbers are filed as `art-717` and `art-679-01`.
- **Other law.** No civil or commercial code was found online as an official text (commercial law is largely the OHADA Uniform Acts), and there is no case law.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [gouv.ne](https://www.gouv.ne), Textes fondamentaux (Gouvernement du Niger) | Government portal: official PDFs | no, one consolidated text each | The Constitution (to 2018), the Code électoral and the Charte des partis politiques (to 2019) |
| [UNODC SHERLOC](https://sherloc.unodc.org) | Copies of national PDFs | no, one edition each | The Code pénal (Ministry of Justice edition, January 2018) and the Code de procédure pénale (to 2004) |
| [Droit-Afrique](http://web.archive.org/web/20160615103820/http://www.droit-afrique.com:80/upload/doc/niger/Niger-Code-2012-du-travail.pdf) (Internet Archive copy of 15 June 2016) | Publisher of African law texts | no, the Code as enacted | The Code du travail of 2012 |

## Licence

See [`LICENSE`](LICENSE). The legal texts are the public law of the Republic of Niger, reproduced with attribution to each source; no source states a licence, and Article 6(i) of Annex VII of the Bangui Agreement, which applies in Niger as an OAPI member, excludes official legislative texts from copyright. The history, commit messages, tables and tools are CC0 1.0.

No AI model wrote, translated or corrected legal text, and none runs when the history is built; the scripts were written by an AI model (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
