const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const root = path.resolve(__dirname, '..');
const template = fs.readFileSync(
  path.join(root, 'themes/cfm/layouts/_default/baseof.html'), 'utf8'
);
const guide = fs.readFileSync(
  path.join(root, 'static/content/week40/study-guide.html'), 'utf8'
);

function extract(start, end) {
  const from = template.indexOf(start);
  const to = template.indexOf(end, from);
  assert(from >= 0 && to > from, `Missing template section: ${start}`);
  return template.slice(from, to);
}

const context = { URL, window: { location: { origin: 'http://localhost' } } };
vm.createContext(context);
vm.runInContext(
  extract('function parseSefariaQuery(href)', 'function parseBLBSearchCriteria(href)') +
  extract('function getTargetAnchor(target)', '// Desktop hover'),
  context
);

const target = href => ({ closest: () => ({ href }) });
const references = [...guide.matchAll(/href="(https:\/\/www\.sefaria\.org[^"]+)"/g)]
  .map(match => match[1]);
assert.equal(references.length, 12, 'Unexpected Week 40 Sefaria citation count');
for (const href of references) {
  assert.equal(context.getTargetAnchor(target(href)), null, href);
}
assert.equal(
  context.getTargetAnchor(target('https://www.sefaria.org/')), null,
  'Sefaria navigation should remain a normal link'
);
assert.notEqual(
  context.getTargetAnchor(target('https://www.sefaria.org/search?q=dagesh')), null,
  'Grammar searches should retain their popup'
);
assert.notEqual(
  context.getTargetAnchor(target('https://www.blueletterbible.org/kjv/isa/40/1/')), null,
  'BLB links should retain their popup'
);

process.stdout.write('Sefaria popup dispatch: 12 citations bypass; search and BLB retained\n');
