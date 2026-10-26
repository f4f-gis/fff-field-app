# FfF branding

This folder and the files listed below turn QField into the **FfF** field app
(Foundations for Farming). Base: QField v4.3.7.

| What | Where | How to change |
|---|---|---|
| App name shown under the icon | `APP_NAME` in `.github/workflows/fff-android.yml` (and the default in `CMakeLists.txt`) | Edit the name, push, rebuild. Safe to change at any time. |
| App ID `org.foundationsforfarming.field` | Set by `scripts/rebrand.sh`; suffix is `APP_PACKAGE_NAME` | **Never change after the app is first published** (stores treat it as a different app). |
| In-app logo | `branding/fff/fff_logo.svg` | Replace the file (square SVG, 512x512 recommended). |
| Launcher icon + splash | `platform/android/res/drawable/launcher_fff_logo*.xml`, `fff_logo_vector.xml` | Android vector drawables. Regenerate with `make_icons.py`, or convert the official logo (e.g. Android Studio > New > Vector Asset). |
| Default server | `src/core/qfieldcloud/qfcloudconnection.cpp` (`defaultUrl`) | Users can also type another server on the login screen. |
| Colours | `resources/theme/theme.json` (or set `APP_THEME_PATH` to a copy) | Optional. |

The current icons are **placeholders** (white "FfF" on green). Replace them with the official
Foundations for Farming logo before any public release.

Building: `.github/workflows/fff-android.yml` (GitHub Actions, Android arm64).
Updating to a newer QField release: merge the new upstream release tag into the `fff` branch,
resolve any conflicts in the files listed in `NOTICE.md`, rebuild and test.
Licence: GPL-2.0-or-later, same as QField. See `NOTICE.md`.
