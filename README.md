# Lizard Magic · Big Cartel theme

Custom code for the Lizard Magic Big Cartel store, based on the
"Crested Gecko Store Mockups" design.

## Files

These map one-to-one to Big Cartel's **Customize Design > Code** editor:
`layout.html`, `home.html`, `products.html`, `product.html`, `cart.html`,
`contact.html`, `maintenance.html`, `care-guide.html` and `theme.css`.
`settings.json` is a snapshot of the current Customize settings.

## Big Cartel's size limit

Big Cartel silently refuses to save `theme.css` above roughly **150,000
characters** (no error, the save just doesn't happen). It's ~125,000 now.
Check before pasting:

```
python3 -c "print(len(open('theme.css', encoding='utf-8').read()))"
```

Big inline data (the NCL Enigmatic `@font-face`) lives in Customize Design's
Custom CSS box instead.

## Home page

- `home.html` holds the markup; the styles are at the end of `theme.css`
  under `LIZARD MAGIC · HOME`.
- `layout.html` loads Almendra, Recursive and Unbounded from Google Fonts. Recursive's Casual and Mono settings are `--lm-body-casual` / `--lm-body-mono` at the top of the Lizard Magic styles in `theme.css`.
- **Hero seal:** upload `assets/lizard-magic-seal.png` as the Welcome image
  (Customize Design > Home). It sits inside the magic circle.
- **Categories:** "Chosen this cycle" pulls the first 4 available products
  from the `live-geckos` category; "Merch" shows the first 3 from `merch`.
  Change the permalinks at the top of `home.html` if yours differ.
- **Morph / sex line:** the first line of each gecko's product description,
  e.g. `Extreme Harlequin · Female`.
- **Newsletter:** set `lm_newsletter_action` at the top of `home.html` to a
  mailing-list form URL to show the email field. Otherwise the button links
  to Instagram (if set) or the contact page.

## Merch page

`products.html` gives the Merch category the same head and cards as Live
Geckos, without the sidebar, with the spinning drop badge in the header and
the "Two vessels" tee panel below the products. The tee names, prices, descriptions and sizes are `lm_tee1_*` /
`lm_tee2_*` at the top of `products.html` (typed in, so update them if the
product prices change). The spinning drop badge's text is `lm_drop_label` /
`lm_drop_month` / `lm_drop_day` (plus an optional `lm_drop_note`) in the same
spot; set `lm_drop_month` to `''` to hide the badge between drops. The day is
sized automatically to match the month's width. Starburst size is
`--lm-drop-burst` in `theme.css`.

## Merch product page

`product.html` gives products in the Merch category their own layout: photo
gallery, an Age toggle, vessel (Style) cards, size pills, an add-to-cart that
stays on the page, the size chart, and related products. Everything else
(geckos) still uses the theme's product layout.

- Ages, styles, sizes, prices and sold-out sizes come straight from the
  product's Big Cartel variants (option groups named **Age**, **Style**,
  **Sizes**).
- What Big Cartel can't store lives in the `lm-tee-config` JSON block in
  `product.html`: each style's subtitle, spec rows, fit notes, and size-chart
  measurements in inches `[chest, length]`, keyed by the exact option names.
  The size chart only shows when there's chart data for the chosen style + age.
- `lm_eyebrow` and `lm_note` at the top set the small line above the title and
  the note under the button.

## Type scale

All Lizard Magic text sizes live as variables at the top of the Lizard Magic
section in `theme.css`. Tablet (≤1100px) and mobile (≤900px) only change
those variables, so a new page just uses the same names:

| Variable | Desktop | Tablet | Mobile | Used for |
| --- | --- | --- | --- | --- |
| `--lm-text` | 16px | 16px | 15px | paragraphs |
| `--lm-text-sm` | 14px | 14px | 13px | paragraphs in tight spots |
| `--lm-leading` | 1.6 | | | paragraph line height |
| `--lm-heading-lg` (`.lm-display--lg`) | 72px | 60px | 44px | page titles |
| `--lm-heading-md` (`.lm-display--md`) | 52px | 44px | 34px | section titles |
| `--lm-heading-sm` (`.lm-display--sm`) | 32px | 32px | 24px | small headings |
| `--lm-card-title` | 28px | 26px | 24px | gecko names |
| `--lm-heading-leading` | 1.05 | | | heading line height |

Paragraphs inside `.lm-home` inherit `--lm-text` / `--lm-leading`
automatically; only small text needs `font-size: var(--lm-text-sm)`.

## Header + footer (layout.html)

- **Announcement bar:** today's affirmation, followed by the Announcement
  text from Customize Design. If that's empty it shows "Live arrival
  guaranteed · Free shipping over $500".
- **Header:** Live Geckos / Merch / Care Guide on the left, the store name as
  the wordmark in the middle, Search and Cart on the right. On phones it's
  MENU · wordmark · CART.
- **Footer:** @lizardmagic777 (links to Instagram when that's set in
  Customize), your custom pages except the Care Guide, Big Cartel's required
  pages and Contact, then "Made & raised with love in Texas".
- The affirmation list lives in the script near the end of `layout.html`.

## NCL Enigmatic

The headline font is a commercial font, so it is not committed to this public
repo. Until it's added, headings fall back to Almendra. If your license
covers web embedding, paste its `@font-face` rule at the very end of
`theme.css` in Big Cartel.

## Up next

- **Trait filters from categories:** a gecko can have several traits (e.g. Tricolor + Lily White + Red Base).
  Plan: create a Big Cartel category per trait, tick every one that applies on each gecko (alongside
  Live Geckos), and build the listing's filter chips from `product.categories`. Picking several chips
  shows geckos that have all of them. Sex stays in the description's first line. Still to decide: one
  "Traits" group or separate groups (Morph, Base color…). Waiting on the categories being set up.
