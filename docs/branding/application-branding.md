# ERA SOFT application branding

Status: Approved baseline

## Branding hierarchy

ERA SOFT uses three distinct identity levels:

1. **Platform** — ERA SOFT provides the shared visual system, navigation, surfaces, spacing, typography, and interaction language.
2. **Applications** — official product logos identify ERA Construction, ERA Concrete, and SRIS Bishkek inside the platform.
3. **Projects and objects** — operational entities such as EcoCity Ayni or Silk Road Campus use standard project cards and do not receive independent logos by default.

Application logos identify products; they do not replace the ERA SOFT design system.

## Asset locations

| Application | Runtime asset | Official source supplied by the product owner |
| --- | --- | --- |
| ERA Construction | `era_soft/public/branding/construction.png` | `Logos/ERA LOGO/ERA.pdf`, official Latin ERA reproduction |
| ERA Concrete | `era_soft/public/branding/concrete.png` | `Logos/Era concrete logo.jpg`, official Latin ERA Concrete reproduction |
| SRIS Bishkek | `era_soft/public/branding/education.png` | `Logos/SRIS original logo 2023.pdf`, official Knowledge & Experience shield |

The runtime files are crops of the supplied official artwork. Cropping removes surrounding brand-guide content only. Colors, proportions, lettering, and internal composition are unchanged. The source material did not contain transparent standalone exports, so the current PNG files retain a white background and are always displayed on a white logo holder in both light and dark themes.

## Usage rules

- Never stretch, skew, rotate, recolor, redraw, or typeset any part of an official logo.
- Always render with `object-fit: contain` and preserve the intrinsic aspect ratio.
- Keep the logo inside the standard 92 × 92 px desktop holder or 72 × 72 px mobile holder.
- Keep a white holder around supplied raster artwork so its appearance remains consistent in light and dark themes.
- Do not use application brand colors to recolor platform controls, navigation, or status indicators.
- Use the official application name next to the logo; do not make the logo carry navigation meaning by itself.
- Provide meaningful alternative text for every official logo.
- Neutral emoji placeholders remain acceptable only for applications without approved artwork.

## Supported formats

- **Preferred master:** SVG or another approved vector export with the official clear space preserved.
- **Accepted runtime format:** transparent PNG at 2× display resolution or higher.
- **Temporary source format:** high-resolution JPEG only when no vector or transparent master is available.

When a new official vector master is supplied, replace the corresponding runtime asset without changing its predictable application filename. This allows branding to improve without rewriting Platform Shell markup.

## Future applications

New applications must provide an approved logo, application name, status, short description, and release stage before the placeholder is removed. A logo addition is a branding change, not authorization to create business functionality or a new data model.
