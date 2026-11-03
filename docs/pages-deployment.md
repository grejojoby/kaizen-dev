# GitHub Pages landing page

The marketing site lives in [`site/`](../site/). It is plain HTML, CSS, and a small progressive-enhancement script. There is no framework, package installation, backend, analytics, or build step. The deploy workflow uploads only this directory, so repository docs and evaluation files are not published.

The project site URL is [https://grejojoby.github.io/kaizen-dev/](https://grejojoby.github.io/kaizen-dev/). GitHub project sites use the owner's `github.io` domain followed by the repository name [1].

## Preview locally

From the repository root, run:

```bash
python3 -m http.server 8000 --directory site
```

Then open `http://localhost:8000/`. The site itself has no runtime dependencies. `scripts/social-card.html` is the editable source for the Open Graph card; run `scripts/render-social-card.sh` to regenerate `site/assets/og-card.png` on a machine with Chromium installed.

## Publish

[`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml) runs on pushes to `main` when site files or the workflow change. It can also be run manually. It uploads `site/` as the Pages artifact and deploys it with GitHub's Pages actions. The job grants only the required repository-content, Pages-write, and OIDC-token permissions [2].

For the first deployment, set the repository's **Settings → Pages → Build and deployment → Source** to **GitHub Actions** [3]. The GitHub REST API can also configure the site with `build_type: "workflow"`; creating or updating the Pages site requires repository-administrator permission [4]. Once configured, an approved push to `main` triggers the deployment workflow. The website is public; do not put secrets, private project data, or customer information in `site/` [3]. GitHub also logs visitors' IP addresses for security. This project adds no analytics or third-party tracking [1].

After a deploy, check the home page, mobile layout, `robots.txt`, `sitemap.xml`, and a missing route. If the repository name or public domain changes, update the canonical URL, Open Graph URLs, sitemap, robots file, and 404-page link together.

## References

[1]: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages "What is GitHub Pages?"
[2]: https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages "Using custom workflows with GitHub Pages"
[3]: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site "Configuring a publishing source for your GitHub Pages site"
[4]: https://docs.github.com/en/rest/pages/pages?apiVersion=2026-03-10 "REST API endpoints for GitHub Pages"
