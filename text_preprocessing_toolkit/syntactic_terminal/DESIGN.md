---
name: Syntactic Terminal
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#bcc9cd'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#869397'
  outline-variant: '#3d494c'
  surface-tint: '#4cd7f6'
  primary: '#4cd7f6'
  on-primary: '#003640'
  primary-container: '#06b6d4'
  on-primary-container: '#00424f'
  inverse-primary: '#00687a'
  secondary: '#c0c1ff'
  on-secondary: '#1000a9'
  secondary-container: '#3131c0'
  on-secondary-container: '#b0b2ff'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#1bbd85'
  on-tertiary-container: '#00452e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#acedff'
  primary-fixed-dim: '#4cd7f6'
  on-primary-fixed: '#001f26'
  on-primary-fixed-variant: '#004e5c'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
typography:
  headline-xl:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '600'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-code:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: -0.01em
  label-metric:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: 24px
    letterSpacing: -0.02em
  label-badge:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  gutter-desktop: 1.25rem
  margin: 1rem
  margin-desktop: 2rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1rem
  space-xl: 1.5rem
---

## Brand & Style

This design system targets machine learning engineers, data scientists, and computational linguists interacting with complex NLP pipelines on mobile web clients. The aesthetic bridges technical precision and high-density legibility, blending an engineered developer terminal ethos with modern, polished utility. 

The emotional response should evoke calculated confidence, operational clarity, and razor-sharp data insight. Visual patterns reject ornamental fluff in favor of structural grid discipline, high-information-density metrics, disciplined monospace readouts, and glowing luminescent state indicators. The direction balances Dark High-Tech with Precision Minimalism—dark slate canvas foundations overlaid with crisp visual dividers, neon-accented telemetry indicators, and tactile micro-surfaces.

## Colors

The palette operates in default dark mode to provide contrast for telemetry metrics, tokenized text, and dense model performance logs:

- **Primary (`#06B6D4` - Electric Cyan):** Reserved for primary interactive elements, active syntax highlights, latency benchmarks, and current execution states.
- **Secondary (`#6366F1` - Electric Indigo):** Applied to vector embeddings, semantic groupings, model architecture metadata, and secondary action paths.
- **Tertiary (`#10B981` - Emerald Telemetry):** Anchors validation indicators, optimal inference scores, accuracy metrics, and healthy deployment health statuses.
- **Neutral (`#0F172A` - Deep Slate):** Forms the base application canvas. Surface layers build upward using tonal variations: `#1E293B` (Surface Raised), `#334155` (Surface Highlight / Subtle Borders), and `#94A3B8` / `#F8FAFC` for high-contrast typography hierarchy.

Never use pure black (`#000000`) for surfaces; depth is achieved strictly via slate transitions to prevent visual fatigue under dense code inspection.

## Typography

The type system pairs **Geist** for structural layout and narrative reading with **JetBrains Mono** for developer data, metrics, tokens, and technical telemetry:

- **Headlines & Interface Text (Geist):** Clean, geometric, neutral Grotesque rendering ensures dense tables, multi-column metrics, and parameter forms remain legible on constrained mobile viewports.
- **Data, Tokens, & Code (JetBrains Mono):** Monospaced numbers ensure tabular lining alignment across live-updating charts, loss counters, and inference latency readouts without layout shifting.
- **Hierarchical Scale:** Headers use tight negative tracking (`-0.02em` to `-0.01em`) to maintain editorial polish, while small badge labels use loose positive letter-spacing (`0.04em`) to optimize uppercase legibility on handheld devices.

## Layout & Spacing

The layout philosophy follows a high-density mobile-first fluid grid structured for technical monitoring:

- **Grid Architecture:** 4 columns on mobile viewports (<640px) expanding to a fluid 12-column grid on tablet and desktop monitors.
- **Rhythm & Compaction:** Strict 4px base increments prioritize information density without visual collision. Mobile outer gutters are bounded at `1rem` (16px), maximizing horizontal real estate for parsed token streams, embeddings, and log monitors.
- **Adaptive Reflow:** Complex telemetry cards reflow from vertical stacked streams on mobile into side-by-side metric dashboards on wider viewports. Scrollable horizontal token trays handle extended model payloads on touch screens.

## Elevation & Depth

Visual hierarchy uses **tonal layer stacking** combined with **subtle micro-luminescent ambient glows** and **low-contrast precision borders**:

- **Layer 0 (Canvas):** Base background tone `#0F172A`.
- **Layer 1 (Card / Container):** Elevated surface tone `#1E293B` bounded by a 1px solid low-contrast hairline border (`rgba(148, 163, 184, 0.12)`).
- **Layer 2 (Overlays / Modals / Active Token Hover):** High-level surface `#334155` with an ambient cyan-tinted drop glow: `0px 8px 24px -4px rgba(6, 182, 212, 0.15)`.
- **Data Callouts:** Metric nodes employ a subtle inner hairline highlight (`inset 0 1px 0 0 rgba(255, 255, 255, 0.06)`) rather than diffuse drop shadows, retaining a clean, physical instrument aesthetic.

## Shapes

The design system adopts a **Soft (Level 1)** corner geometry (`0.25rem` / 4px base):

- **Data Cards & Panels:** Styled with 4px to 8px radii, preserving the structured, monolithic silhouette of server racks and hardware diagnostic tools.
- **Badges & Token Chips:** Use 4px corner rounding to evoke postage-stamp syntax tags rather than rounded consumer pills.
- **Interactive Triggers:** Retain intentional 4px geometric corners to reinforce industrial utility and technical precision.

## Components

- **Buttons:**
  - *Primary:* Solid Electric Cyan background (`#06B6D4`), dark slate text (`#0F172A`), semi-bold weight. Active state features a 1px inset border with a cyan drop flare.
  - *Secondary:* Background `#1E293B`, subtle slate hairline border (`#334155`), text in `#F8FAFC`.
  - *Terminal/Ghost:* Borderless with JetBrains Mono typography and cyan underline transitions on press.

- **Chips & Token Tags:**
  - Specialized for NLP tokenization (POS tags, NER entities, attention weights).
  - Background: Alpha-tinted containers (e.g., `rgba(6, 182, 212, 0.12)` for Entities, `rgba(99, 102, 241, 0.12)` for Dependencies).
  - Typography: `label-badge` in JetBrains Mono with 1px hairline border matching the accent color at 30% opacity.

- **Metric Counters & Telemetry Displays:**
  - Dedicated cards featuring small uppercase labels, a large numeric readout (`label-metric`), and an inline delta trend in Emerald (`#10B981`) or Rose.
  - Optional mini inline sparkline chart with glowing terminal vector paths.

- **Cards & Data Containers:**
  - `#1E293B` background with structural 1px border (`#334155`). Top border can take an optional 2px status accent line (Cyan for active running state, Emerald for converged, Indigo for eval mode).

- **Input Fields & Code Prompts:**
  - Dark inputs (`#0F172A`) inset within surface cards, displaying a persistent monospace prompt symbol (`>_`). Active focus displays an Electric Cyan hairline ring with zero exterior spread blur.

- **Checkboxes & Segmented Controls:**
  - Sharp, compact rectangular hit areas with cyan filled-state indicators and high-contrast checked states.