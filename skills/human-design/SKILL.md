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

### 3. Choose a visual direction

Use `references/styles.md` to select a direction or combine compatible principles. Explain the choice briefly before implementation when the task is substantial.

A style name is not a design system. Define the actual decisions: composition, density, typography, color roles, surfaces, borders, imagery, spacing, and interaction behavior.

### 4. Define the design system

Use `references/color-and-type.md` and create project-appropriate tokens for:

- Background, surface, elevated surface, text, muted text, border, and accent roles
- Semantic states such as success, warning, danger, and information
- Display, heading, body, label, and data typography
- Spacing, content width, grid, radius, border, and elevation
- Focus, hover, active, disabled, and selected states

Choose colors by role and contrast, not by filling the interface with accents. Keep the palette restrained unless the product calls for a more expressive system. Check text and interactive contrast.

Prefer fonts already available in the project or reliable system stacks. Do not add a remote font dependency without a reason. Use a type scale with clear hierarchy and sensible line lengths.

### 5. Plan the page

Decide the information hierarchy and page composition before building components. Consider the actual content, empty states, loading states, errors, and responsive behavior. Avoid repeating the same layout on every page when their jobs differ.

### 6. Implement

Build with the project's existing framework and conventions. Use semantic HTML and accessible controls. Reuse components when they represent the same pattern, not merely because they look similar.

Use real content or realistic content shaped like the product's domain. Avoid filler copy, meaningless metrics, and decorative elements that compete with the task.

Do not silently remove existing functionality. Keep interactions functional and include keyboard focus states. Make responsive decisions intentionally rather than shrinking a desktop layout until it fits.

### 7. Review the rendered result

Use the available browser, preview, or screenshot workflow when one exists. Inspect at least the primary desktop view and a narrow mobile view for substantial page work. If visual inspection is unavailable, say so and perform a code-level review without presenting it as a visual review.

Use `references/review-checklist.md`. Look for hierarchy, alignment, rhythm, density, contrast, responsive behavior, content fit, and consistency. Fix the most visible issues, then inspect again when practical.

### 8. Report

Summarize what changed, the chosen direction, checks performed, and any remaining visual limitations. Be specific. Never say a page is polished or verified if it was not inspected.

## Delegation

Use the optional Claude Code subagents when their separate context will improve the work:

- `design-researcher` for a read-only project and product audit before a substantial redesign
- `design-system-architect` for a focused visual system proposal or token review
- `visual-reviewer` after implementation when a rendered page or screenshot is available

Do not invoke all three automatically for a small change. Delegate only well-scoped tasks, pass the relevant product context, and reconcile their findings yourself. Subagents are optional; the main workflow must remain usable without them.

## Reference material

- `references/styles.md` — visual directions and when to use them
- `references/color-and-type.md` — palette and typography decisions
- `references/review-checklist.md` — implementation and visual review criteria
- `examples/design-brief.md` — a compact design brief format
