"""
Used for parsing [[ versionadded X.X.X ]] and [[ versionchanged X.X.X ]]
into rendered HTML.
"""

from markdown.inlinepatterns import Pattern
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

VERSION_RE = r"\[{2}\s*version(added|changed)(.*)\]{2}"

class VersionPattern(Pattern):
    def handleMatch(self, m):
        el = etree.Element("em")
        # Could link version to changelog?
        el.text = f"{m.group(2).capitalize()} in version {m.group(3).strip()}"
        return el

class VersionExtension(Extension):
    def extendMarkdown(self, md):
        pattern = VersionPattern(VERSION_RE)
        md.inlinePatterns.register(pattern, "version", 20)  # 20 is priority, not sure what it should be

def makeExtension(**kwargs):
    return VersionExtension(**kwargs)

