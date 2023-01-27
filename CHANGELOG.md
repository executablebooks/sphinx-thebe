# Changelog

## v0.2.1 - 2023-01-27

- FIX: Add name to the kernelOptions [#60](https://github.com/executablebooks/sphinx-thebe/pull/60) (@joergbrech)
 
## v0.2.0 - 2023-01-05

Minor improvements to support up to Sphinx 6. See https://github.com/executablebooks/sphinx-thebe/pull/57 for more details.

## v0.1.2 - 2022-04-29

This is a minor patch release to fix a JSON metadata bug with myst-nb notebooks.

## v0.1.1 - 2022-02-06

A minor feature addition release to add default CSS selectors for MyST-NB cells.

([full changelog](https://github.com/executablebooks/sphinx-thebe/compare/v0.1.0...ff1fd4b40615c32e6c9d0a60b98434cc1fe2f084))

- ENH: Add defaults for MyST-NB [#48](https://github.com/executablebooks/sphinx-thebe/pull/48) ([@choldgraf](https://github.com/choldgraf))


## v0.1.0 - 2022-02-05

([full changelog](https://github.com/executablebooks/sphinx-thebe/compare/v0.0.10...4d1a60c5126ce633b1a36de43b4990b2f4d08730))

**Lazy load thebe javascript** [#41](https://github.com/executablebooks/sphinx-thebe/pull/41) ([@choldgraf](https://github.com/choldgraf))

`thebe` will now "lazily load" its javascript only when a bootstrap button is pressed, rather than loading the Javascript on each page.
This saves on bandwidth and pageload speed, since Thebe is generally _not_ used on a page even if it _could_ be used.

## v0.0.10 - 2021-08-24

([full changelog](https://github.com/executablebooks/sphinx-thebe/compare/v0.0.9...e18d1bf94a8fa79476f035a349bd63d03bba83e7))

This is a minor release to conditionally load the JS on pages that have a "launch button".
This will save some load time on non-interactive pages.

### Enhancements made

- Option to conditionally load on pages, see [documentation for details](https://sphinx-thebe.readthedocs.io/en/latest/configure.html#only-load-js-on-certain-pages) [#30](https://github.com/executablebooks/sphinx-thebe/pull/30) ([@choldgraf](https://github.com/choldgraf))

### Other merged PRs

- PIN: thebe v0.5.1 [#31](https://github.com/executablebooks/sphinx-thebe/pull/31) ([@choldgraf](https://github.com/choldgraf))

## v0.0.9 - 2021-08-21

### Updates

- `sphinx-thebe` now uses the correct and latest version of thebe, since it has been renamed from `thebelab` to `thebe`.
