// One-Line Roast: The Gadget You Use Every Day
// u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610
//
// The entry is a single roast line, chosen by an independent three-model
// CrowLLM panel (see candidates.md): the panel unanimously overruled the
// internal winner C15 (a washing machine fails the on-subject gate — it is
// not a gadget people use every day) and picked C3, combined 236 vs C6 197
// vs C15 152, laugh test 3/3.
//
// This program writes exactly that line to /output/entry.txt.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

// Panel winner C3 (83 chars): the smartwatch cheers when you stand up, as
// if a trip to the snack cupboard were a mountaineering feat.
const LINE =
  "My smartwatch applauds me for standing up, as if reaching for snacks were a summit.";

// The gate requires UTF-8 text of 1-200 characters, not only whitespace,
// and the brief requires a single line.
const charCount = [...LINE].length;
if (charCount < 1 || charCount > 200) {
  throw new Error(`entry must be 1-200 characters, got ${charCount}`);
}
if (LINE.trim().length === 0) {
  throw new Error("entry must not be only whitespace");
}
if (LINE.includes("\n") || LINE.includes("\r")) {
  throw new Error("entry must be a single line");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
// Write the line exactly — no trailing newline — so the file is
// byte-identical to the winning line.
const outPath = join(outDir, "entry.txt");
writeFileSync(outPath, LINE, "utf8");
// Read back and confirm the file is byte-identical to the winning line.
const written = readFileSync(outPath, "utf8");
if (written !== LINE) {
  throw new Error("entry.txt does not match the winning line");
}
console.log(`wrote ${charCount} chars to ${outPath}`);
