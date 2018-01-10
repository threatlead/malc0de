import feedparser
from collections import namedtuple
import re


class Malcode:
    """
    Malc0de : Ingest malware data
    """
    data = namedtuple('Malcode', ['domain', 'url', 'ipaddress', 'country', 'asn', 'md5sum'])
    rss_url = 'http://malc0de.com/rss/'
    re_parser = re.compile('URL:\s+(.*?),\s+IP\s+Address:\s+([\d.]+),'
                           '\s+Country:\s+([A-Z]{2}),\s+ASN:\s+(\d+),'
                           '\s+MD5:\s+([a-f0-9]{32})')

    @classmethod
    def get_rss_items(cls, rss=rss_url):
        """Get www.malc0de.com RSS Feed Elements"""
        feed = feedparser.parse(rss)
        (domain, url, ipaddress, country, asn, md5sum) = (None, None, None, None, None, None)
        malcode_item_list = []
        for item in feed.entries:
            match = cls.re_parser.match(item.summary_detail.value)
            if not match:
                print('Error while parsing: {0}'.format(item.summary_detail.value))
                continue
            else:
                url, ipaddress, country, asn, md5sum = match.groups()
            if item.title_detail.value:
                domain = item.title_detail.value
            malcode_item_list.append(cls.data(domain=domain, url=url, ipaddress=ipaddress, country=country, asn=asn, md5sum=md5sum))
        return malcode_item_list
