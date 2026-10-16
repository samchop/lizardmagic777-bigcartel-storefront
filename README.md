# Lizard Magic · Big Cartel theme

Custom code for the Lizard Magic Big Cartel store, built from the "Elevated Explorations"
redesign (geckos, merch, care guide, contact, plus search and cart).

## Files

These map one-to-one to Big Cartel's **Customize Design > Code** editor:
`layout.html`, `home.html`, `products.html`, `product.html`, `cart.html`, `contact.html`,
`maintenance.html` and `theme.css`. Paste them **all at once**. The pages share classes, so a
half-pasted theme looks broken. `settings.json` is a snapshot of the Customize settings.

The theme no longer loads the stock `theme.js` or jQuery. It only needs Big Cartel's `api.js`.

## Where things live

| Page | Template | Notes |
| --- | --- | --- |
| Home | `home.html` | Hero photo is Customize > **Welcome image**. If it's blank, the first gecko's photo is used. Copy (vows, rites, Elixir, reviews) is set at the top of the file. |
| All wares `/products` | `products.html` | Two doors (Entities / Artifacts) with live counts and starting prices. |
| Geckos `/category/live-geckos` | `products.html` | Filters are built from each gecko's categories and first description line. `#Lilly+White` style links preselect a filter. |
| Merch `/category/merch` | `products.html` | Drop badge, the two vessels (Relic / Familiar), copy at the top of the file. |
| Search `/products?search=…` | `products.html` | Result grid. The instant search overlay lives in `layout.html`. |
| Gecko page | `product.html` | Used when the product is in **Live Geckos**. Deposit, pickup and shipping text are at the top of the gecko branch. |
| Tee page | `product.html` | Everything else. Size charts and fit notes are in the `#lm-tee-config` JSON block. |
| Cart `/cart` | `cart.html` | Works without JavaScript. Geckos show "One of a kind" and no quantity stepper. |
| Cart drawer ("Satchel") | `layout.html` | Opens from the header cart link and after add-to-cart. |
| Contact | `contact.html` | Uses Big Cartel's own fields and reCAPTCHA. Customize > Contact text overrides the lede. |
| Care guide | `layout.html` | Rendered whenever the custom page's permalink is `care-guide`. **The page body typed into Big Cartel is ignored.** Edit the guide in `layout.html`. `care-guide.html` is the old version, kept for reference only. |

## Gecko listings

- **Categories:** tick **Live Geckos**, one category per trait (Lilly White, Tricolor, Quadstripe,
  Extreme Harlequin…) and one base category ending in "Base" (Dark Base, Red Base).
- **Description, first line:** `Morph · Sex · RTB`, separated by `·`.
- **Following lines** (each one is optional):

```
Hatched: 05/05/2024
Weight: 42g
Age: Adult
Breeder: Miami Art Gecko
Sire: Dr Whoo · Yellow Harlequin
Dam: Nirvana · Lilly White
```

  `Hatched` accepts `2025`, `09/2023` or `05/05/2024`. The sky chart (sun sign) only shows for a full
  date. When `Age` is missing it's estimated from the weight.
- **Photos:** when Sire or Dam is listed, the **last** photo is used as the parents' photo.
- Everything after those lines is the catalogue note.

## Big Cartel's size limit

Big Cartel silently refuses to save `theme.css` above roughly **150,000 characters** (no error,
the save just doesn't happen). It's about 95,000 now. Check before pasting:

```
python3 -c "print(len(open('theme.css', encoding='utf-8').read()))"
```

## NCL Enigmatic

The headline font is a commercial font, so it is not committed to this public repo. Paste its
`@font-face` rule into Customize Design's **Custom CSS** box. Without it, headings fall back to
Instrument Serif.

## Hosted assets (Cloudflare Pages)

The `assets/` folder is published to Cloudflare Pages, so the store loads files from it, e.g.
`https://lizardmagic-assets.pages.dev/art/pentacle.svg` (no `assets/` in the URL). Every push to
`claude/big-cartel-home-page-7vwp4t` redeploys. Pages settings: framework preset None, no build
command, build output directory `assets`. `assets/_headers` allows cross-origin loading.

- `art/`: pentacle, barbed wire, flower and flames ornaments
- `icons/`: gecko hand, Astroicons and moon phases
- `photos/elixir.jpg`: the Elixir photo on the home page. **Not uploaded yet.** Until it is, that
  section shows without a photo.

## Astro icons

`assets/icons/astro/` holds the [Astroicons](https://github.com/marcmarine/astroicons) set, copied from
commit `75bdad0`. MIT licensed: keep `assets/icons/astro/LICENSE` with them. `assets/icons/moon/` has
the 8 moon phases, drawn to match. The icons the theme uses are inlined as an SVG sprite at the top of
`layout.html` (`<use href="#lm-i-mars"/>`), so they don't count toward the theme.css limit.
