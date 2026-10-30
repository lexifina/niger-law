import json, re, hashlib, subprocess, pathlib
here = pathlib.Path(__file__).parent
pdf = here / '.cache' / 'constitution.pdf'
sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
txt = subprocess.run(['pdftotext', '-enc', 'UTF-8', '-layout', str(pdf), '-'], capture_output=True, check=True).stdout.decode('utf8')


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace('\xa0', ' ').replace('\f', '')
    return re.sub(r'\s+', ' ', s).strip()


raw = txt.split('\n')
# drop page numbers; mark them so a paragraph broken by a page can be rejoined
lines = []
for l in raw:
    s = l.replace('\f', '').strip()
    if re.fullmatch(r'\d{1,3}', s):
        lines.append('\x00PB')
    else:
        lines.append(s)
i0 = next(i for i, l in enumerate(lines) if l.startswith('PR') and 'AMBULE' in l)
body = lines[i0:]
ROM = {'PREMIER': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9, 'X': 10, 'XI': 11, 'XII': 12, 'XIII': 13, 'XIV': 14}
units = {}
cur = None
ART = re.compile(r'^Art(?:icle|\.)?\s*(premier|\d+)\s*(.*)$', re.I)
paras = None


def start(key, label, kind, head, first=None):
    global cur
    assert key not in units, key
    cur = {'label': label, 'kind': kind, 'head': head, 'raw': []}
    units[key] = cur
    if first:
        cur['raw'].append(first)


pending_title = False
for l in body:
    if pending_title:
        pending_title = False
        if l and l == l.upper() and not ART.match(l) and not l.startswith('\x00'):
            cur['head'] += ' ' + norm(l)
            continue
    if l.startswith('PR') and 'AMBULE' in l and 'preamble' not in units:
        start('preamble', 'Préambule', 'preamble', '# Préambule')
        continue
    m = re.match(r'^TITRE (\S+)\s*:', l)
    if m:
        start('titre-%02d' % ROM[m.group(1)], 'Titre ' + m.group(1).capitalize(), 'chapter', '# ' + norm(l))
        pending_title = True
        continue
    m = ART.match(l)
    if m:
        n = 1 if m.group(1).lower() == 'premier' else int(m.group(1))
        rest = m.group(2)
        suf = ''
        mb = re.match(r'^\s*\(?\s*bis\s*\)?', rest, re.I)
        if mb:
            suf = '-bis'
        rest = re.sub(r'^\s*(\(?\s*(nouveau|bis)\s*\)?\s*)*[:.\-–]*\s*', '', rest, flags=re.I)
        if re.match(r'^\(?\s*[Ll]oi\b[^)]*\)?\.?\s*(JORN.*)?$', rest):
            rest = ''
        start(f'art-{n:03d}{suf}', f'Art. {n}' + (' bis' if suf else ''), 'art', f'# Article {n}' + (' bis' if suf else ''), rest or None)
        continue
    if cur is not None:
        cur['raw'].append(l)

out = {}
for k, u in units.items():
    paras = []
    brk = False
    prev = ''
    for l in u['raw']:
        if l == '\x00PB':
            brk = True
            continue
        if not l:
            if not brk:
                paras.append(None)  # paragraph break
            continue
        bullet = re.match(r'^[-•]\s+', l)
        if bullet:
            paras.append(norm(l)); brk = False; continue
        short_end = bool(paras) and paras[-1] is not None and len(prev) < 80 and prev[-1:] in '.;:' and not brk
        if short_end:
            paras.append(norm(l))
        elif paras and paras[-1] is not None and not bullet and (not brk and True):
            # continuation line of the current paragraph
            paras[-1] = paras[-1] + ' ' + norm(l)
        elif brk and paras and paras[-1] is not None and l[:1].islower():
            paras[-1] = paras[-1] + ' ' + norm(l)
        else:
            paras.append(norm(l))
        brk = False
        prev = l
    final = [p for p in paras if p]
    out[k] = {'label': u['label'], 'kind': u['kind'], 'text': '\n'.join([u['head']] + final) + '\n'}

# merge: lines are joined only when no blank line separates them; a blank-line break set paras to None
amend = [('loi-2011-17', 'Loi n°2011-17', '2011-08-08'), ('loi-2011-43', 'Loi n°2011-43', '2011-12-14'),
         ('loi-2017-50', 'Loi n°2017-50', '2017-06-06'), ('loi-2017-56', 'Loi n°2017-56', '2017-06-08'),
         ('loi-2018-44', 'Loi n°2018-44', '2018-06-22')]
U = 'https://www.gouv.ne/index.php/textes-fondamentaux/constitution-de-la-7eme-republique'
P = 'https://www.gouv.ne/images/textes-fondamentaux/constitution.pdf'
laws = {'decret-2010-754': {'label': 'Décret n°2010-754/PCSRD', 'title': 'Décret promulguant la Constitution de la VIIème République (25 novembre 2010; JORN spécial n°19 du 29 novembre 2010)', 'kind': 'decree', 'enacted': '2010-11-25', 'published': '2010-11-29', 'url': P, 'temporary_until': None, 'restores': None, 'note': None}}
for k, l, d in amend:
    laws[k] = {'label': l, 'title': f'Loi portant modification de la Constitution, {l} du {d}', 'kind': 'law', 'enacted': d, 'published': None, 'url': P, 'temporary_until': None, 'restores': None, 'note': None}
corpus = {
    'country': {'code': 'NE', 'name': 'Niger', 'slug': 'niger', 'lang': 'fr', 'tz': 'Africa/Niamey', 'future_branch': 'futur',
                'publisher': {'name': 'Gouvernement du Niger (gouv.ne), Textes fondamentaux', 'email': 'gouv@gouv-ne.invalid'},
                'default_in_force_rule': {'text': "Constitution of 25 November 2010, art. 183: it enters into force on its promulgation. No general commencement rule for amending laws was read; the one version here is dated by the latest amending law the document names.", 'source': P},
                'licence_note': "Text from the Government of Niger's portal (www.gouv.ne), Textes fondamentaux. No licence is published; Nigerien legislation is public law."},
    'sources': [{'name': 'Gouvernement du Niger, Textes fondamentaux: Constitution de la 7ème République (PDF)', 'url': U, 'retrieved': '2026-10-29', 'requests': 3,
                 'licence': 'none published; legislation is public law', 'notes': f'constitution.pdf sha256 {sha[:16]}; text layer read with pdftotext, no OCR. robots.txt on gouv.ne is the standard Joomla file.'}],
    'laws': laws,
    'acts': [{'slug': 'constitution', 'short': 'Const.',
              'title': 'Constitution de la VIIème République du Niger (décret n°2010-754/PCSRD du 25 novembre 2010), avec les modifications jusqu\'à la loi n°2018-44 du 22 juin 2018', 'url': U,
              'first_law': None, 'earlier_laws': ['decret-2010-754'] + [a[0] for a in amend],
              'versions': [{'from': '2018-06-22', 'source_url': P, 'sha256': sha, 'units': out, 'credits': {},
                            'note': "The text the Government of Niger's portal prints: the Constitution of 25 November 2010 with the modifications of 2011, 2017 and 2018 already in place, and no earlier version. The Constitution was suspended after the military takeover of 26 July 2023 and has been replaced; the portal's text is therefore historical."}]}],
    'applies': [],
    'decisions': ["The only official text found online is the consolidated PDF on gouv.ne; it is one 'oldest version available' dated 2018-06-22, the date of the last amending law it names (loi n°2018-44, art. 91).",
                  "Amendment notes in article headings (for example '(nouveau) : (loi n°2017-50 du 06 juin 2017)') are left out of the text; the amending laws are listed as earlier laws, not credited per article.",
                  "Art. 99 appears twice in the source (99 nouveau and 99 bis); the second is stored as art-099-bis.",
                  "Text-layer PDF only, read with pdftotext; page numbers dropped; lines rejoined into paragraphs."],
    'ai_use': ['none']}
(here / 'corpus.json').write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf8')
print(len(out), 'units')
