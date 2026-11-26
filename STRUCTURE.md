# Structure du dépôt / Repository layout

Un dossier par texte, rangé par type puis par année ; un fichier par article.
One folder per text, filed by type and then by year; one file per article.

```
charte-de-la-refondation/             Charte de la Refondation du 26 mars 2025 (valeur constitutionnelle, en vigueur)
constitution/                         Constitution du 25 novembre 2010 (modifiée jusqu'en 2018 ; suspendue en 2023)
codes/<code>/                         codes : code-penal, code-procedure-penale, code-du-travail, code-electoral
lois/<année>/<numéro>-<objet>/        lois et lois organiques
ordonnances/<année>/<numéro>-<objet>/ ordonnances
decrets/<année>/<numéro>-<objet>/     décrets
arretes/<année>/<numéro>-<objet>/     arrêtés (ministériels, interministériels)
corpus.json                           liste des textes (corpus ne/national/acts)
```

Dans chaque dossier de texte / in each text folder:

- `README.md` : intitulé, source, date, nature de la couche texte, nombre d'articles ;
- `visas.md` : en-tête et visas (tout ce qui précède l'article premier) ;
- `art-001.md`, `art-002.md`, `art-012-bis.md` … : un article par fichier ;
- `signatures.md` : la formule finale (« Fait à Niamey, le … ») et les signatures ;
- `texte-integral.md` au lieu des articles quand aucun intitulé d'article n'a pu être repéré.

`<numéro>` est le numéro officiel en minuscules ASCII (`2014-11`, `2016-303-prn-mag-el`) ;
`<objet>` reprend les premiers mots de l'intitulé (`portant-code-de-l-electricite`). Aucun dossier ne dépasse
1 000 entrées.

## Commits

- Un commit par version d'un texte. Pour les lois, ordonnances, décrets et arrêtés, la version est celle que publie la
  source (la plus ancienne disponible), sans les modifications ultérieures.
- Date : midi, heure Africa/Niamey (UTC+1), du jour d'entrée en vigueur quand il est connu ; sinon du jour du texte
  donné par son intitulé (signature ou promulgation), ce que dit le trailer `In-force-evidence`. Jamais le jour de
  la collecte. Avant 1970 : commit au 1er janvier 1970 UTC, la vraie date dans le sujet et dans `In-force`.
- Auteur : le texte lui-même (« Loi n° 2014-11 du 16 avril 2014 ») ; committer : Lexifina.
- Trailers : `In-force`, `In-force-evidence`, `Source` (le PDF), `Text-layer` (`born-digital` : PDF natif ;
  `publisher-ocr` : couche texte fournie par l'éditeur sur un document numérisé, non relue), `Version`.

Aucune reconnaissance optique (OCR) n'est faite par Lexifina : un PDF sans couche texte, ou dont la couche texte est
illisible, n'est pas repris.

`ohada/actes-uniformes/<acte>/`: OHADA Uniform Acts, which apply directly in Niger as an OHADA State Party; one file
per article, `visas.md` and a `README.md` giving the Journal officiel de l'OHADA issue and the date of application.
