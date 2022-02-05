# Changelog

## v0.1.0

([full changelog](https://github.com/executablebooks/sphinx-thebe/compare/v0.0.10...4d1a60c5126ce633b1a36de43b4990b2f4d08730))

**Lazy load thebe javascript** [#41](https://github.com/executablebooks/sphinx-thebe/pull/41) ([@choldgraf](https://github.com/choldgraf))

`thebe` will now "lazily load" its javascript only when a bootstrap button is pressed, rather than loading the Javascript on each page.
This saves on bandwidth and pageload speed, since Thebe is generally _not_ used on a page even if it _could_ be used.
