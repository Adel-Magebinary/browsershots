Please write to [johann@browsershots.org](mailto:johann@browsershots.org) if you find a privacy violation, or if you have ideas for improvement.

## For anonymous users ##

Everybody can see your screenshots, so there's no privacy at all.

If your website is NSFW, it may not show up on the public /screenshots/ page (automatic keyword filtering).

## For authenticated users ##

Starting with milestone:0.4-beta3, your screenshot requests will be private if you log in before you submit them.

Private screenshots will not show up on the public /screenshots/ page and /factories/ detail pages, and your URL will not appear on the /websites/ search page. The result is that nobody can see your screenshots except yourself, or somebody who already knows your URL.

## For search engines ##

Browsershots uses a [robots.txt](http://browsershots.org/robots.txt) file to keep search engines away from the screenshot result pages, so that Browsershots should not appear in search results for your website. Please write to [johann@browsershots.org](mailto:johann@browsershots.org) if it does anyway.

## For webmasters ##

Browsershots respects the [robots.txt standard](http://www.robotstxt.org/orig.html). You can disallow automatic screenshots of your website by adding a section like this to the **robots.txt** file on your server:
```
User-agent: Browsershots
Disallow: /
```

Or if you have disallowed robots, but you want to make screenshots with Browsershots, you can explicitly allow it by adding a section like this to the **robots.txt** file on your server:
```
User-agent: Browsershots
Disallow:
```