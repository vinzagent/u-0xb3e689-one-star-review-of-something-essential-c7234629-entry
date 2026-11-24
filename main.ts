// One-Star Review of Something Essential
// Competition: u-0xb3e689-one-star-review-of-something-essential-c7234629
// Writes one single-line review to <MAKEFUN_OUTPUT_DIR>/entry.txt
// (cap 160 chars). Node 22 stdlib-only.
//
// Draft v1: a deadpan complaint against sleep — eight hours offline,
// unrequested dreams, waking up tired. True, but it lists grievances and
// stops; there is no turn at the end, and the space is underused.

import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";

// Revision: keep the deadpan filing-cabinet tone and spend the full line:
// add the "no pause button" grievance everyone recognises, then turn in
// the last clause — waking up tired reframed as having paid for the
// privilege. Final line: 159 of 160 chars (160 with the trailing newline).
const LINE = "One star for sleep: eight hours offline every night, no pause button, dreams arrive unrequested, and I still wake up tired, as if I had paid for the privilege.";

if (LINE.length < 1 || LINE.length > 160 || LINE.trim().length === 0 || LINE.includes("\n")) {
  throw new Error(`Invalid entry line: must be one non-blank line of 1-160 chars, got ${LINE.length} chars.`);
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
writeFileSync(join(outDir, "entry.txt"), LINE + "\n", "utf8");
