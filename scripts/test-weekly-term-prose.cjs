const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../themes/cfm/layouts/weeks/single.html'), 'utf8');
function block(start, end) {
  const from = source.indexOf(start);
  const to = source.indexOf(end, from);
  assert(from >= 0 && to > from, `Missing source boundary: ${start}`);
  return source.slice(from, to);
}

// Exercise the template's actual pure helpers without a browser or a copied matcher.
const more = {strongs: 'H4175'};
const day = {strongs: 'H1767'};
const sophia = {strongs: 'G4678'};
const helpers = vm.runInNewContext([
  block('const normalizeLatin =', 'const translitIndex ='),
  block('const prefixes =', 'const COMMON_ENGLISH ='),
  block('const COMMON_ENGLISH =', '// HEBREW LETTER NAMES'),
  block('const resolveTargetFromText =', 'const buildLexiconHref ='),
  '({isEnglishProseSpan, resolveTargetFromText})'
].join('\n'), {
  translitIndex: {more, day, sophia},
  originalIndex: {'די': day},
  ambiguousTranslitKeys: new Set(),
  overriddenTranslitKeys: new Set(),
  LETTER_NAMES: new Set()
});

for (const text of [
  '"the path of the just is as the shining light, that shineth more and more unto the perfect day"',
  'more and more unto the perfect day',
  'a time to weep',
  'Our hearts are open.'
]) assert.equal(helpers.isEnglishProseSpan(text, ''), true, text);

for (const text of ['sophia', 'môrê', 'heḇel', 'qol demamah daqqah', 'qōl demāmâ daqqâ', 'kol heḇel']) {
  assert.equal(helpers.isEnglishProseSpan(text, ''), false, text);
}
assert.equal(helpers.isEnglishProseSpan('be midbar', 'במדבר'), false);
for (const text of ['more', 'More', 'day', 'day"', '“more”']) {
  assert.equal(helpers.resolveTargetFromText(text, ''), null, text);
}
assert.equal(helpers.resolveTargetFromText('môrê', '').strongs, 'H4175');
assert.equal(helpers.resolveTargetFromText('sophia', '').strongs, 'G4678');
assert.equal(helpers.resolveTargetFromText('day', 'די').strongs, 'H1767');
assert.match(source, /if \(isEnglishProseSpan\(termText, hebrewHint\)\) return;/);
console.log('Weekly term English-prose and real-transliteration controls passed.');

// Run the actual browser enhancer with an authored <em><a> node. Any attempt
// to replace that node would discard the explicitly chosen H639 identity.
const authored = {
  textContent: 'ʾaph',
  closest: () => null,
  querySelector: () => ({dataset: {strongs: 'H639'}}),
  replaceWith: () => { throw new Error('Authored link overwritten'); }
};
vm.runInNewContext(
  block('async function enhanceWeeklyTerms()', '\nfunction enhanceWeeklyShorthandScriptures()') + '\nenhanceWeeklyTerms();',
  {
    window: {},
    fetch: async () => ({ok: true, json: async () => ({
      H637: {translit: 'aph', original: 'אַף', definition: 'also'},
      H639: {translit: 'aph', original: 'אַף', definition: 'nose, anger'}
    })}),
    document: {querySelectorAll: () => [{querySelectorAll: () => [authored]}]}
  }
).then(() => console.log('Authored link identity survives the browser enhancer.'))
 .catch(error => { console.error(error); process.exitCode = 1; });
