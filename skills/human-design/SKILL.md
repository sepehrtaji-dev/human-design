---
name: human-design
description: Design distinctive, coherent product interfaces with considered typography, color, layout, and interaction. Use when creating or redesigning websites, dashboards, apps, or component systems, and when auditing or improving an existing interface.
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

### 2. Choose the task path

Determine what the user is asking for:

- **Create:** build a new interface or page. Continue with the product understanding and design workflow below.
- **Redesign:** intentionally change the visual direction or structure of an existing interface. Understand what should change and what must remain.
- **Audit and improve:** the user provides an existing design, asks to fix it, says it looks wrong, or expects the agent to find and resolve design problems. Follow **Audit and improve an existing design** before making implementation changes.
- **Review only:** the user asks for feedback or critique without authorizing changes. Report findings and recommendations; do not edit files.

Do not treat every existing-design task as a request for a full redesign. When the user asks to fix problems, preserve the current product identity and improve the implementation with the smallest coherent set of changes. If the requested outcome is ambiguous between critique and implementation, ask one short question.

These paths are mutually exclusive starting points, not a sequence of workflows to run one after another:

- **Create** continues to product understanding, Design DNA, visual direction, system definition, planning, implementation, and review.
- **Redesign** continues through product understanding and Design DNA, then establishes an intentionally revised direction before implementation.
- **Audit and improve** follows the complete audit path below and then goes directly to the final report. Do not continue into the new-page visual-direction, design-system-definition, or page-planning steps unless a diagnosed issue actually requires that work.
- **Review only** ends with findings and recommendations. Do not edit files.

Shared review and reporting guidance may still be used by every path.

### 3. Audit and improve an existing design

Use this path when the user hands over an existing interface and expects the agent to identify what makes it feel weak, inconsistent, unfinished, confusing, or visually poor, then fix those issues.

#### Establish the baseline

- Inspect the relevant routes, components, styles, assets, and existing design-system rules before editing.
- If possible, run the project and capture the current rendered state at representative desktop and mobile sizes. Inspect the full page, not only the first viewport.
- Understand the product, audience, primary tasks, content, and existing visual identity. Load the project's Design DNA or established design-system documentation when available.
- Separate intentional design choices from defects. Do not label a style as wrong merely because it differs from your personal preference.
- Preserve working behavior, meaningful content, brand assets, and established patterns unless they are part of the problem or the user asks to change them.

#### Find design problems

Evaluate the interface as a complete experience. Look for issues such as:

- **Visual hierarchy:** no clear focal point, weak distinction between headings and body content, competing calls to action, or important information buried.
- **Composition and layout:** unbalanced sections, awkward proportions, inconsistent alignment, poor content width, repetitive layouts, or elements that feel randomly placed.
- **Spacing and rhythm:** cramped groups, excessive empty space, inconsistent gaps, uneven padding, or a lack of visual grouping.
- **Typography:** unsuitable type choices, too many competing styles, weak scale or weight hierarchy, poor line length, awkward wrapping, or hard-to-scan text.
- **Color and contrast:** unclear color roles, excessive accents, muddy surfaces, insufficient text or control contrast, and semantic colors used inconsistently.
- **Density and content:** overcrowded screens, oversized low-value elements, sparse areas without purpose, weak information grouping, placeholder content, or poor content fit.
- **Components and consistency:** mismatched buttons, inputs, cards, radii, borders, shadows, icon styles, navigation patterns, or inconsistent states.
- **Imagery and decoration:** irrelevant imagery, poor crops, arbitrary icons, excessive effects, visual noise, or decoration that competes with the task.
- **Responsive quality:** broken reflow, overflow, clipped content, awkward mobile hierarchy, unusable tables or navigation, and controls that become difficult to use.
- **Usability and accessibility:** unclear affordances, confusing actions, poor focus visibility, inaccessible contrast, missing labels, or interaction states that are difficult to understand.
- **Finish and coherence:** a generic template feel, disconnected sections, inconsistent visual language, unfinished states, or details that make the product feel unreliable.

These are diagnostic categories, not a checklist to force every interface into the same style. Only report issues that are actually present and matter in context.

#### Prioritize findings

For each real finding, record the affected page or component, what is wrong, why it harms the experience, and the intended correction. Prioritize by impact:

- **Critical:** blocks a core task, makes essential content or controls inaccessible, or breaks a primary flow.
- **Major:** strongly damages hierarchy, readability, consistency, responsive behavior, or the usability of an important interaction.
- **Minor:** local polish issue such as a small alignment, spacing, icon, or visual-detail inconsistency.

Fix critical and major findings first. Address minor findings when they are low-risk and within scope. Do not invent problems to make the audit look thorough.

#### Repair without unnecessary redesign

- Make the smallest coherent set of changes that resolves the diagnosed problems.
- Improve the underlying layout, tokens, shared components, and responsive rules where appropriate; avoid accumulating one-off overrides.
- Follow the existing Design DNA. If it is missing, infer only what is supported by the current product and implementation, and mark uncertain decisions as unresolved rather than inventing a new identity.
- Do not replace the entire visual direction, rewrite content, remove features, or introduce new dependencies unless the findings justify it or the user approves it.
- Preserve functional behavior and verify that controls, navigation, and important flows still work.
- If a correction requires a product or brand decision, ask before making an irreversible or identity-changing choice. Otherwise, use a conservative, reversible improvement.

#### Verify the repairs

- Re-render and inspect the affected pages and states after changes. Compare them with the baseline when available.
- Recheck desktop and narrow mobile layouts, visual hierarchy, spacing, typography, color contrast, content fit, and consistency.
- Run relevant interaction, accessibility, and project checks. Fix regressions introduced by the repair.
- If browser rendering is unavailable, perform a code-level audit and clearly state that the visual result could not be verified.
- Report the most important findings, what was changed, what was retested, and any remaining limitations. Never claim a problem was fixed without checking the relevant result.

For a user-provided screenshot or mockup without source access, inspect and explain the visible issues. Do not claim to have implemented fixes in the product. Ask for the relevant project files or repository when implementation is expected.

**This is the end of the Audit and improve execution path.** After verification, go directly to the final report. Do not run the Create or Redesign workflow as a follow-up. Revisit a shared component, token, or Design DNA only when a specific finding requires it.

### 4. Understand the product

Establish:

- What the product does and what the user needs to accomplish
- Who the primary audience is
- The most important content and actions on the page
- The product's personality and level of formality
- Any brand assets, existing design decisions, or technical constraints

Ask a short, focused set of questions when missing information would materially change the design. Ask one question at a time when practical. Do not make the user complete a long questionnaire.

If the user is unsure, offer two or three distinct visual directions with a concise explanation. Use the product context to recommend one. Do not ask questions whose answers can be found in the repository.

### 5. Establish or load the Design DNA

Before designing a new page, look for an existing project Design DNA document. The default location is `design/DESIGN-DNA.md`; if the project already has an established design-system document, use that instead of creating a competing source of truth.

Follow `references/design-dna.md`:

- If a Design DNA exists, read it and inspect the implementation to confirm it is still accurate. Treat confirmed decisions as constraints across pages.
- If it does not exist, gather enough product context, define the visual direction and core rules, then create it from `examples/DESIGN-DNA.md`.
- Mark unknown or unverified details as unresolved. Do not invent brand decisions, tokens, or behavior to make the document look complete.
- Keep the document concise and actionable. Record decisions that affect future screens, not every one-off implementation detail.
- Ask for confirmation only when a decision materially changes the product identity or conflicts with existing evidence.

A Design DNA document is the project's persistent design contract. Read it before each substantial design task and update it when an approved decision changes. Do not silently rewrite the identity to justify a one-page variation.

### 6. Choose a visual direction

Use `references/styles.md` to select a direction or combine compatible principles. Explain the choice briefly before implementation when the task is substantial.

A style name is not a design system. Define the actual decisions: composition, density, typography, color roles, surfaces, borders, imagery, spacing, and interaction behavior.

### 7. Define the design system

Use `references/color-and-type.md` and create project-appropriate tokens for:

- Background, surface, elevated surface, text, muted text, border, and accent roles
- Semantic states such as success, warning, danger, and information
- Display, heading, body, label, and data typography
- Spacing, content width, grid, radius, border, and elevation
- Focus, hover, active, disabled, and selected states

Choose colors by role and contrast, not by filling the interface with accents. Keep the palette restrained unless the product calls for a more expressive system. Check text and interactive contrast.

Prefer fonts already available in the project or reliable system stacks. Do not add a remote font dependency without a reason. Use a type scale with clear hierarchy and sensible line lengths.

### 8. Plan the page

Decide the information hierarchy and page composition before building components. Consider the actual content, empty states, loading states, errors, and responsive behavior. Avoid repeating the same layout on every page when their jobs differ.

### 9. Implement

Build with the project's existing framework and conventions. Use semantic HTML and accessible controls. Reuse components when they represent the same pattern, not merely because they look similar.

Use real content or realistic content shaped like the product's domain. Avoid filler copy, meaningless metrics, and decorative elements that compete with the task.

Do not silently remove existing functionality. Keep interactions functional and include keyboard focus states. Make responsive decisions intentionally rather than shrinking a desktop layout until it fits.

### 10. Review the rendered result

Use the available browser, preview, or screenshot workflow when one exists. Inspect at least the primary desktop view and a narrow mobile view for substantial page work. If visual inspection is unavailable, say so and perform a code-level review without presenting it as a visual review.

Use `references/review-checklist.md`. Look for hierarchy, alignment, rhythm, density, contrast, responsive behavior, content fit, and consistency. Check the page against the project's Design DNA, not just generic design principles. Fix the most visible issues, then inspect again when practical.

### 11. Run a final design audit and repair loop

Do not stop after checking the page you just implemented. Before calling substantial UI work complete, perform one coherent pass over the affected experience as a user would encounter it.

1. Identify the scope: list the changed pages, shared components, and important user flows. For a broad redesign, include the main routes rather than reviewing only the landing page.
2. Inspect the rendered experience at representative desktop and mobile widths. Check the initial viewport and the full page; scroll through long pages. Inspect important interactive states, not only the default state.
3. Compare related pages side by side against the Design DNA. Look for drift in typography, color roles, spacing, content width, navigation, controls, and surface treatment. Preserve intentional page-specific differences.
4. Check functional and structural quality alongside appearance: broken or dead links, clipped or overflowing content, console/runtime errors, missing assets, unusable controls, keyboard access, focus visibility, and relevant empty, loading, and error states.
5. Classify findings by impact:
   - **Critical:** blocks a core task, breaks navigation, causes data loss, or makes content/control inaccessible.
   - **Major:** clear visual inconsistency, broken responsive layout, unreadable content, or a key interaction that does not work.
   - **Minor:** small spacing, alignment, icon, or polish issue that does not obstruct use.
6. Fix critical and major issues before finishing. Fix minor issues when they are local and low-risk; do not expand scope into an unrequested redesign.
7. Re-run the relevant checks and inspect the affected rendered areas again. A fix is not verified merely because the source code changed.
8. If a finding cannot be fixed safely or needs a product decision, explain it clearly and leave it as an explicit limitation rather than silently ignoring it.

For a small isolated change, keep the audit proportional: review the changed component and the surrounding page instead of traversing the whole application. If a browser or screenshot workflow is unavailable, perform a code-level audit and state that rendered verification could not be completed.

Use the final-audit section in `references/review-checklist.md` as the completion gate. Report the scope inspected, findings fixed, checks rerun, and any remaining issues.

### 12. Update the Design DNA and report

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
