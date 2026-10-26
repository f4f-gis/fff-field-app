# FfF

FfF is a modified version of **QField** (https://github.com/opengisch/QField),
copyright (C) OPENGIS.ch and the QField contributors, licensed under the
GNU General Public License version 2 or (at your option) any later version.
FfF is distributed under the same licence; see LICENSE.

FfF is an independent project and is not endorsed by OPENGIS.ch.
"QField" and the QField logo belong to their owners.

## Modifications

On 2026-10-26, starting from upstream commit `3fb12810b42654c6c45b39d669227d82a25f1fc8`, the following files were
modified to change the application name, package identifier (org.foundationsforfarming.field) and default
server (https://fff-summer202627.southafricanorth.cloudapp.azure.com). Later changes are recorded in this repository's git history.

- .github/workflows/android.yml
- CMakeLists.txt
- cmake/Package.cmake
- platform/android/AndroidManifest.xml.in
- platform/android/build.gradle.in
- platform/android/src/org/foundationsforfarming/qfield/QFieldActivity.java
- platform/android/src/org/foundationsforfarming/qfield/QFieldCloudService.java
- platform/android/src/org/foundationsforfarming/qfield/QFieldPositioningService.java
- platform/android/src/org/foundationsforfarming/qfield/QFieldUtils.java
- scripts/build-vcpkg.sh
- scripts/ci/env_gh.sh
- scripts/ci/generate-version-details.sh
- src/app/qml/QfWelcomeScreen.qml
- src/app/qml/QgisMobileapp.qml
- src/core/platforms/android/qfandroidplatformutilities.cpp
- src/core/positioning/qfinternalgnssreceiver.cpp
- src/core/qfieldcloud/qfcloudconnection.cpp
- src/core/utils/qfcloudutils.cpp
- src/service/qfieldcloudservice.cpp
- src/service/qfieldpositioningservice.cpp
