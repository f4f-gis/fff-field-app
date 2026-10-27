# FfF branding

This folder and the files listed below turn QField into the **FfF** field app
(Foundations for Farming). Base: QField v4.3.7.

| What | Where | How to change |
|---|---|---|
| App name shown under the icon | `APP_NAME` in `.github/workflows/fff-android.yml` (and the default in `CMakeLists.txt`) | Edit the name, push, rebuild. Safe to change at any time. |
| App ID `org.foundationsforfarming.field` | Set by `scripts/rebrand.sh`; suffix is `APP_PACKAGE_NAME` | **Never change after the app is first published** (stores treat it as a different app). |
| Logo (in-app, cloud sign-in screen, default avatar, launcher icon, splash) | Source: `branding/fff/fff_logo_source.png` | Replace the source image and run `python3 branding/fff/make_logo_assets.py branding/fff/fff_logo_source.png`, then commit. |
| "QField" / "QFieldCloud" in the app's texts | Renamed to "FfF" / "FfF Cloud" by `branding/fff/rename_texts.py` (all languages) | To use other names, run it again on a fresh QField checkout: `python3 branding/fff/rename_texts.py "FfF" "FfF Cloud"`. Credits and links to QField itself are deliberately kept. |
| Default server | `src/core/qfieldcloud/qfcloudconnection.cpp` (`defaultUrl`) | Users can also type another server on the login screen. |
| Colours | `resources/theme/theme.json` (or set `APP_THEME_PATH` to a copy) | Optional. |

The logo is the Foundations for Farming logo (raster, from FfF). If FfF can supply it as a
vector (SVG/PDF/AI), the in-app SVGs can be replaced with it for sharper rendering.

Building: `.github/workflows/fff-android.yml` (GitHub Actions, Android arm64).
Updating to a newer QField release: merge the new upstream release tag into the `fff` branch,
resolve any conflicts in the files listed in `NOTICE.md` (for texts and translations it is often
easiest to take QField's version and re-run `rename_texts.py`), rebuild and test.
Licence: GPL-2.0-or-later, same as QField. See `NOTICE.md`. The FfF logo belongs to Foundations for Farming.
