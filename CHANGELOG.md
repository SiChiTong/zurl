Zurl Changelog
==============

v. 1.4.5 (2015-06-26)

  * Fix regression with GET requests.
  * Ensure responses with no content (HEAD, 204, 304) are handled properly.

v. 1.4.4 (2015-06-26)

  * Fix HEAD requests.

v. 1.4.3 (2015-06-25)

  * Allow request body with GET and DELETE.

v. 1.4.2 (2015-06-18)

  * Support redirects when there is a request body.
  * Fix bool types when using JSON as the message format.

v. 1.4.1 (2015-06-12)

  * Fix type conversions when using JSON as the message format.

v. 1.4.0 (2015-06-11)

  * follow-redirects option.
  * timeout option.
  * id is now optional.
  * Ack stream requests immediately so they become referenceable.
  * Respond with headers even before initial body received.

v. 1.3.1 (2014-09-16)

v. 1.3.0 (2014-02-13)

v. 1.1.0 (2013-11-24)

v. 1.0.0 (2013-08-10)

  * Stable version.