---
name: human-design
description: Design distinctive, coherent product interfaces with considered typography, color, layout, and interaction. Use when creating or redesigning websites, dashboards, apps, landing pages, or component systems, especially when the visual result feels generic or AI-generated.
---

# HumanDesign

Design the product, not a collection of trendy components. Make deliberate visual decisions that fit the product, its audience, and the content it needs to present.

## Working principles

- Understand the product and its users before choosing a visual style.
- Prefer a clear point of view over decoration. Every prominent visual choice should have a reason.
- Do not default to purple gradients, glass cards, oversized rounded panels, floating blobs, or the familiar centered-hero-plus-three-cards layout.
- These patterns are not forbidden. Use them only when they support the product's identity and improve the interface.
- Do not imitate a reference site. Extract the relevant principles and make an original composition.
- Keep the design coherent across pages, states, and screen sizes.
- Respect the existing stack, accessibility requirements, content, and project conventions.
- Do not claim a visual review happened unless you inspected a rendered page or screenshot.

## Workflow

### 1. Inspect the project

Before changing files, inspect the application structure, framework, routing, existing components, styling approach, assets, and available run or test commands. Identify what already works and what should be preserved.

If the task is limited to a single component and the context is already clear, keep this inspection proportionate.

### 2. Understand the product

Establish:

- What the product does and what the user needs to accomplish
- Who the primary audience is
- The most important content and actions on the page
- The product's personality and level of formality
- Any brand assets, existing design decisions, or technical constraints

Ask a short, focused set of questions when missing information would materially change the design. Ask one question at a time when practical. Do not make the user complete a long questionnaire.

If the user is unsure, offer two or three distinct visual directions with a concise explanation. Use the product context to recommend one. Do not ask questions whose answers can be found in the repository.

### 3. Establish or load the Design DNA

Before designing a new page, look for an existing project Design DNA document. The default location is `design/DESIGN-DNA.md`; if the project already has an established design-system document, use that instead of creating a competing source of truth.

Follow `references/design-dna.md`:

- If a Design DNA exists, read it and inspect the implementation to confirm it is still accurate. Treat confirmed decisions as constraints across pages.
- If it does not exist, gather enough product context, define the visual direction and core rules, then create it from `examples/DESIGN-DNA.md`.
- Mark unknown or unverified details as unresolved. Do not invent brand decisions, tokens, or behavior to make the document look complete.
- Keep the document concise and actionable. Record decisions that affect future screens, not every one-off implementation detail.
- Ask for confirmation only when a decision materially changes the product identity or conflicts with existing evidence.

A Design DNA document is the project's persistent design contract. Read it before each substantial design task and update it when an approved decision changes. Do not silently rewrite the identity to justify a one-page variation.

### 4. Choose a visual direction

Use `references/styles.md` to select a direction or combine compatible principles. Explain the choice briefly before implementation when the task is substantial.

A style name is not a design system. Define the actual decisions: composition, density, typography, color roles, surfaces, borders, imagery, spacing, and interaction behavior.

### 5. Define the design system

Use `references/color-and-type.md` and create project-appropriate tokens for:

- Background, surface, elevated surface, text, muted text, border, and accent roles
- Semantic states such as success, warning, danger, and information
- Display, heading, body, label, and data typography
- Spacing, content width, grid, radius, border, and elevation
- Focus, hover, active, disabled, and selected states

Choose colors by role and contrast, not by filling the interface with accents. Keep the palette restrained unless the product calls for a more expressive system. Check text and interactive contrast.

Prefer fonts already available in the project or reliable system stacks. Do not add a remote font dependency without a reason. Use a type scale with clear hierarchy and sensible line lengths.

### 6. Plan the page

Decide the information hierarchy and page composition before building components. Consider the actual content, empty states, loading states, errors, and responsive behavior. Avoid repeating the same layout on every page when their jobs differ.

### 7. Implement

Build with the project's existing framework and conventions. Use semantic HTML and accessible controls. Reuse components when they represent the same pattern, not merely because they look similar.

Use real content or realistic content shaped like the product's domain. Avoid filler copy, meaningless metrics, and decorative elements that compete with the task.

Do not silently remove existing functionality. Keep interactions functional and include keyboard focus states. Make responsive decisions intentionally rather than shrinking a desktop layout until it fits.

### 8. Review the rendered result

Use the available browser, preview, or screenshot workflow when one exists. Inspect at least the primary desktop view and a narrow mobile view for substantial page work. If visual inspection is unavailable, say so and perform a code-level review without presenting it as a visual review.

Use `references/review-checklist.md`. Look for hierarchy, alignment, rhythm, density, contrast, responsive behavior, content fit, and consistency. Check the page against the project's Design DNA, not just generic design principles. Fix the most visible issues, then inspect again when practical.

### 9. Update the Design DNA and report

After implementation:

- Update the Design DNA only if a durable design decision was added, corrected, or explicitly approved.
- Keep page-specific exceptions local unless they should become a product-wide rule.
- Record meaningful changes in the decision log, including the reason and affected areas.
- Do not change the document just because implementation temporarily deviated from it; fix the deviation or explain why an exception is needed.
- Summarize what changed, the chosen direction, checks performed, and any remaining visual limitations.

Never say a page is polished or verified if it was not inspected.

## Delegation

Use the optional Claude Code subagents when their separate context will improve the work:

- `design-researcher` for a read-only project and product audit before a substantial redesign
- `design-system-architect` for a focused visual system proposal or token review
- `visual-reviewer` after implementation when a rendered page or screenshot is available

Do not invoke all three automatically for a small change. Delegate only well-scoped tasks, pass the relevant product context, and reconcile their findings yourself. Subagents are optional; the main workflow must remain usable without them.

## Reference material

- `references/styles.md` — visual directions and when to use them
- `references/color-and-type.md` — palette and typography decisions
- `references/design-dna.md` — how to create and maintain a persistent project design contract
- `references/review-checklist.md` — implementation and visual review criteria
- `examples/design-brief.md` — a compact design brief format
- `examples/DESIGN-DNA.md` — a starting template for the project's Design DNA
