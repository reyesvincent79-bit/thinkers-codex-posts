# @_thethinkerscodex carousel system

Brand: "THINK For Yourself" / The Thinker's Codex, author pen name VincenT YeS. Store: thinkerscodex.store.
Books: (1) The Science of Learning Your Inner Speech, (2) Learn To Think For Yourself, (3) The 14-Day Clarity Reset.

## Carousel = exactly 10 slides
1. cover: quote from a real authority figure (philosopher/author), with attribution. NEVER quote the user's books on slide 1. Only well-attested quotes; avoid disputed or modern misattributions.
2-7. six short essay slides (2-3 short paragraphs each, italics with *...*, plain, concrete, no statistics unless verified).
8. closing question (type "question").
9. bridge slide: "This is the thread behind the book *<Title>*." + one line.
10. CTA slide: two short lines + button "LINK IN BIO".

## Caption
Hook line, blank line, one engagement line (save/send/try), blank line, `From "<Book title>." Link in bio.`, blank line, at most 5 hashtags (Instagram limit). Do NOT include any #thinkerscodex hashtag.

## Cadence
4 per day, 8:00 AM / 12:00 PM / 5:00 PM / 9:00 PM America/New_York. Rotate books and topics; do not repeat a quote already used (check every */posts.json in this repo).

## Files
Each day folder `YYYY-MM-DD/` has `posts.json` and PNGs named `<id>_NN.png` (id like d3_1700). posts.json entries: {id, time, header, caption, slides:[{type, text:[...], attr?, button?}]}.
Render: `python3 tools/render.py <posts.json> <outdir>` (1080x1350, cream paper, black serif TeX Gyre Pagella). See tools/example_posts_builder.py for the JSON shape.
