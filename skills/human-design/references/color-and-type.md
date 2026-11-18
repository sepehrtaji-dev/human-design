# Color and typography

## Build a palette by role

Start with functional roles rather than choosing a favorite color:

- `canvas`: the page background
- `surface`: cards, panels, and controls
- `surface-raised`: overlays or elements that need a clear layer distinction
- `text`: primary content
- `text-muted`: supporting content that remains readable
- `border`: separators and component boundaries
- `accent`: the main action or selected state
- `accent-subtle`: quiet accent backgrounds
- `success`, `warning`, `danger`, `info`: semantic feedback

Use one dominant neutral family and a limited accent palette. The accent should identify important actions and states, not decorate every section. Semantic colors should retain their meaning across the product.

## Palette directions

These are starting points, not fixed presets. Adjust them for contrast, brand fit, and display conditions.

### Paper and ink

- Canvas: `#F4F1EA`
- Surface: `#FBFAF6`
- Text: `#242521`
- Muted: `#6E7069`
- Border: `#DCD8CE`
- Accent: `#315B50`

### Clay and olive

- Canvas: `#F1EEE7`
- Surface: `#FAF8F2`
- Text: `#292A25`
- Muted: `#77766B`
- Border: `#D8D3C7`
- Accent: `#777A4B`

### Ink and mineral

- Canvas: `#171A1B`
- Surface: `#202526`
- Surface raised: `#292F30`
- Text: `#ECEDE7`
- Muted: `#A5ADA8`
- Border: `#3A4241`
- Accent: `#8BA99A`

### Oxblood and parchment

- Canvas: `#F3EEE8`
- Surface: `#FCF9F4`
- Text: `#302724`
- Muted: `#7D706A`
- Border: `#DDD1C9`
- Accent: `#783F43`

### Cobalt and warm grey

- Canvas: `#F0F1EF`
- Surface: `#FAFBF9`
- Text: `#202428`
- Muted: `#687078`
- Border: `#D8DDE0`
- Accent: `#315E9E`

Do not apply a palette mechanically. Check text, icons, borders, disabled states, and focus indicators against their actual backgrounds. Aim for WCAG AA contrast for normal text where applicable.

## Typography

Choose typefaces for the product's language, tone, and available assets. Check that the chosen family includes the required glyphs, especially for multilingual interfaces. Do not use a fashionable display face for every text role.

Define a small, consistent type system:

- Display: reserved for one or two high-impact moments
- Heading: clear section and page hierarchy
- Body: comfortable reading size and line height
- Label: compact UI labels, never too small to read
- Data: aligned numerals where tables or metrics need scanning

Use weight, size, line length, and spacing together to establish hierarchy. Avoid relying on color alone. Keep body copy at a readable measure and avoid long paragraphs across very wide screens.

## Spacing and shape

Choose a spacing scale and apply it consistently. Use larger gaps to separate groups and smaller gaps within related controls. Radius should reflect the product's character: it does not need to be large on every component. Use shadows sparingly; borders and surface contrast are often clearer.
