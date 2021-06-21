# Strangler pattern

## Intro

The [strangler pattern](https://martinfowler.com/bliki/StranglerFigApplication.html) is a pattern that gives you the
opportunity to fix / evolve a legacy application that is hard to maintain / evolve by strangling it with a new
application.

The main ideas are:

- do not rewrite the legacy application from a blank page, the legacy app is still working
- new functionalities are implemented in a new application
- both app, legacy and new one, work fine together. A proxy helps to redirect the flow between the new application and
  the legacy one
- step by step, we move the old functionality from the legacy to the new app

For this dojo, we chose the [gilded rose](https://github.com/emilybache/GildedRose-Refactoring-Kata) kata and started to
implement the new functionalities in the new app while we still call the legacy part for existing functionalities.
