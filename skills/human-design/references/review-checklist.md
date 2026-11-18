# Design review checklist

## Existing design diagnosis

- Was the current implementation inspected before edits?
- Is the product's purpose, audience, and primary task understood?
- Were actual design defects distinguished from subjective style preferences?
- Were hierarchy, composition, alignment, spacing, typography, color, contrast, density, content fit, components, imagery, responsive behavior, and usability considered?
- Does each finding describe the affected area, its impact, and a concrete correction?
- Were findings prioritized instead of treating every visual difference as equally important?
- Were existing brand decisions, useful patterns, content, and working behavior preserved?
- Were fixes made at the right level (shared token/component when appropriate) rather than through scattered overrides?
- Was the full redesign avoided unless the user requested it or the findings justified it?
- Were changed pages rendered and inspected again after repairs?
- Were desktop/mobile behavior and important interactions rechecked?
- Are limitations clearly stated when implementation or visual verification was not possible?

## Product fit

- Is the primary task obvious without explanation?
- Does the visual direction suit the product and its audience?
- Is the content specific to the product rather than generic placeholder material?

## Design DNA

- Was the existing Design DNA read before substantial design work?
- Do the page's tokens, typography, surfaces, and interaction patterns follow it?
- Are deviations intentional and limited to the page where they are needed?
- Were durable decisions recorded without turning the document into a component inventory?
- Are unresolved decisions clearly distinguished from confirmed rules?

## Hierarchy and composition

- Is there a clear first, second, and third level of attention?
- Are alignment, spacing, and content widths consistent?
- Does the page have a deliberate composition rather than a stack of identical cards?
- Are important actions visually distinct without competing with one another?

## Color and type

- Are color roles consistent across the page?
- Is the accent used with restraint?
- Is text readable on every surface, including muted and disabled states?
- Do type sizes, weights, and line lengths create a useful hierarchy?

## Components and interaction

- Do controls look and behave like controls?
- Are hover, focus, active, selected, disabled, loading, empty, and error states considered where relevant?
- Can the main flow be completed with a keyboard?
- Are semantic elements and accessible names used appropriately?

## Responsive behavior

- Does the layout reflow intentionally at narrow widths?
- Are navigation, tables, dialogs, and dense controls usable on mobile?
- Do headings wrap cleanly without collisions or awkward orphaned words?
- Are touch targets large enough for comfortable use?

## Visual finish

- Are icon sizes and stroke weights consistent?
- Are borders, shadows, and radii used consistently?
- Are images cropped intentionally and relevant to the content?
- Is there any decoration that does not help comprehension or identity?
- Does the page still feel coherent when viewed without animation?

## Evidence

Record which pages and viewport sizes were actually inspected. Separate observed issues from assumptions. Do not mark a visual check as complete if only source code was reviewed.

## Final design audit

- Were all affected pages and shared components identified, rather than reviewing only the most recently edited component?
- Were representative desktop and mobile layouts inspected in a rendered browser or screenshots?
- Were long pages reviewed beyond the initial viewport?
- Were key interaction states and core user flows exercised?
- Were related pages compared for visual drift against the Design DNA?
- Were navigation targets, links, assets, and controls checked for broken or dead behavior?
- Were console/runtime errors and layout overflow checked where tools allow?
- Were findings classified by severity, with critical and major issues fixed before completion?
- Were the relevant tests rerun and the changed rendered areas inspected after fixes?
- Are unresolved issues and unavailable verification stated explicitly?
