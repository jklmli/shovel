# shovel

Shovel is a set of tools for scrapers.  That means defaults for modern user-agent override, retry 
logic with timeout, compression.

## How is this different from Beautiful Soup?

shovel and Beautiful Soup aren't targeting the same niche.  Beautiful Soup is a scraping framework -
 it abstracts a lot of the low-level regex matching you would do.  shovel provides general-purpose
 tools you'll probably use - unrelated to parsing.  You can easily use them together!
