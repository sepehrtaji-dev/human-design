# Design DNA

Design DNA is a compact, project-level record of the visual decisions that should remain consistent as an interface grows. It is not a moodboard, a component inventory, or a replacement for the codebase.

## Location

Use `design/DESIGN-DNA.md` at the project root by default. If the project already has a clear, maintained design-system document, extend or reference that document instead of creating a second source of truth. Do not create duplicate copies.

## When to create it

Create a Design DNA when:

- The project has multiple pages or will grow beyond a one-off screen.
- A redesign establishes a new visual identity.
- Existing design decisions are scattered, inconsistent, or difficult for future work to discover.

For a small, isolated component change, do not create a document just for ceremony.

## What belongs in it

Record only decisions that should influence future work:

- Product context and audience, as relevant to design
- Visual character and principles
- Color roles and actual token values, when known
- Typography roles and chosen families
- Layout, spacing, density, and responsive rules
- Surface, border, radius, and elevation behavior
- Shared component and interaction conventions
- Accessibility requirements that affect visual decisions
- Known exceptions and unresolved decisions
- A short decision log for durable changes

Do not copy every CSS declaration, list every component, or record temporary implementation details. Link to the actual token or component files when that is the better source.

## How to establish it

1. Inspect the existing interface, assets, styles, and project documentation.
2. Separate observed implementation from inferred intent.
3. Ask about decisions that cannot be established from the project and would materially affect its identity.
4. Propose a concise set of durable rules.
5. Create the document from the example template after the direction is sufficiently clear.
6. Keep unresolved choices visibly marked; do not fill gaps with invented facts.

## How to use it

Before substantial UI work:

1. Read the Design DNA.
2. Check whether the current implementation still matches it.
3. Reuse its tokens and conventions rather than inventing new ones.
4. Treat a page-specific variation as an exception, not a new global rule.
5. Review the rendered result against both the document and the task's requirements.

The document is guidance, not permission to preserve a bad decision forever. If a rule is inaccessible, technically unsuitable, or no longer fits the product, explain the conflict and propose a deliberate revision.

## Update rules

Update the document when a durable decision changes, not after every component edit.

- Do not silently change established brand or identity decisions.
- For a material identity change, explain the impact and get the user's agreement before treating it as the new direction.
- For a small correction that clearly implements an existing decision, update the relevant token or reference without adding noise to the decision log.
- Record the date, decision, reason, and affected areas for meaningful changes.
- Keep page-specific exceptions near the relevant page unless they become a repeated product-wide pattern.
- Remove stale rules when they are replaced; do not leave contradictory guidance.

## Quality check

A useful Design DNA should let another agent answer these questions without guessing:

- What should this product feel like, and what should it avoid?
- Which colors, type roles, spacing rules, and surfaces are shared?
- Which patterns must remain consistent across pages?
- Which decisions are confirmed, unresolved, or intentionally exceptional?
- Where is the source implementation of the tokens and components?
