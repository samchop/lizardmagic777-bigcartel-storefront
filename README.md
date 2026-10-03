# Lizard Magic · Big Cartel theme

Custom code for the Lizard Magic Big Cartel store, based on the
"Crested Gecko Store Mockups" design.

## Files

These map one-to-one to Big Cartel's **Customize Design > Code** editor:
`layout.html`, `home.html`, `products.html`, `product.html`, `cart.html`,
`contact.html`, `maintenance.html`, `care-guide.html` and `theme.css`.
`settings.json` is a snapshot of the current Customize settings.

## Home page

- `home.html` holds the markup; the styles are at the end of `theme.css`
  under `LIZARD MAGIC · HOME`.
- `layout.html` loads Grenze Gotisch, Space Mono and Syncopate from Google Fonts.
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
repo. Until it's added, headings fall back to Grenze Gotisch. If your license
covers web embedding, paste its `@font-face` rule at the very end of
`theme.css` in Big Cartel.
