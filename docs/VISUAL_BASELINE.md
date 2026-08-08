# ERA SOFT visual baseline

This baseline brands the local Frappe/ERPNext site as ERA SOFT without changing
Frappe or ERPNext source. It adds only custom-app hooks, static assets, standard
Workspace configuration, a standard Workspace Sidebar, and local helper scripts.
It introduces no business DocTypes, workflows, reports, or accounting logic.

## Start and open

The normal macOS entry point is the `ERA SOFT.app` application bundle. Install
its desktop shortcut once:

```bash
scripts/install_macos_app.sh
```

After installation, double-click **ERA SOFT** on the Desktop. The application
starts only the missing local services and opens the site in a dedicated Chrome
application window. If Chrome is unavailable, it uses the default browser. The
launcher then exits quietly. Diagnostics are written to:

```text
~/Library/Logs/ERA SOFT Launcher.log
```

The application icon is generated from the versioned ERA SOFT brand mark. The
Desktop entry is a symbolic link, so reviewed launcher and icon updates take
effect without reinstalling it.

After changing the native launcher source or its shell entry point, rebuild the
local application bundle with:

```bash
scripts/build_macos_app.sh
```

### Terminal fallback

On macOS, double-click `macos/ERA SOFT.command`. The launcher resolves its real
location even when it is installed as a Desktop symlink, starts missing local
services through `scripts/local_stack.sh`, waits for the web server, and opens:

```text
http://era.localhost:8003
```

Install the legacy Terminal-style launcher on the current user's Desktop once:

```bash
scripts/install_macos_launcher.sh
```

The same operation can be run in Terminal:

```bash
scripts/local_stack.sh start
open http://era.localhost:8003
```

After a fresh app install, or after adding/changing files under `public`, run the
normal Frappe synchronization and asset build once:

```bash
cd ../frappe-bench
../toolchain/bin/bench --site era.localhost migrate
../toolchain/bin/bench build --app era_soft
```

The launcher uses the default HTTP browser and falls back to Google Chrome when
macOS has no default HTTP handler.

## Status and stop

From the ERA SOFT repository:

```bash
scripts/local_stack.sh status
scripts/local_stack.sh stop
```

Stopping is clean: the local web process, both Redis processes, and the
workspace-local MariaDB process are stopped. No site data is deleted.

## Branding and navigation

The visual layer uses supported Frappe extension points in `era_soft/hooks.py`:

- `app_title`, `app_logo_url`, `app_home`, and `add_to_apps_screen` identify the
  application and make ERA SOFT Platform its landing workspace;
- `app_include_css` loads a small ERA palette and component polish from the
  custom app's public assets;
- `after_migrate` applies the ERA name, logo, favicon, splash image, and default
  application through normal singleton settings;
- ERA Workspaces and separate Platform and Construction sidebars provide the
  two-level navigation;
- the existing ERPNext Projects workspace and standard Supplier and Employee
  DocTypes are reused rather than copied.

The landing page is an application portfolio: ERA Construction is active;
Concrete is marked as coming soon; Education, HR, Documents and AI are planned;
Finance and the Executive Dashboard expose only their existing foundations.
Selecting Construction changes the navigation to Overview, Projects, Budgets,
Procurement, Materials, Contractors, Payments and Reports. Other ERPNext modules
are not deleted. They remain available to permitted users through the standard
ERPNext app tile and global search. The restore helper returns that tile to its
upstream hidden default.

### Replace the temporary logo

The shipped SVG assets are temporary:

```text
era_soft/public/images/era-soft-mark.svg
era_soft/public/images/era-soft-logo.svg
```

An administrator can upload a future approved logo in **Website Settings > App
Logo**. A non-ERA custom path is intentionally preserved on later migrations.
The hook logo remains the fallback for the application switcher. Replace the two
versioned SVG files in a reviewed branding change if the fallback and launcher
identity must also change.

## Restore the architecture baseline

First remove only site settings owned by this visual baseline:

```bash
cd ../frappe-bench
../toolchain/bin/bench --site era.localhost execute \
  era_soft.setup.visual_baseline.restore_visual_baseline
../toolchain/bin/bench --site era.localhost clear-cache
```

The restore helper does not overwrite a logo or name that an administrator has
customized after this baseline.

To inspect the approved pre-visual code without changing the current branch:

```bash
git worktree add ../era-soft-architecture v0.1-architecture-approved
```

To roll back the visual commit on the current branch, run the site restore above,
revert the tagged commit, and migrate so Frappe removes the standard records that
are no longer supplied by the app:

```bash
git revert v0.2-visual-baseline
cd ../frappe-bench
../toolchain/bin/bench --site era.localhost migrate
```

Use `git revert`, not a destructive reset, on a shared branch.
