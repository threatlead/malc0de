# ![Malcode](https://s13.postimg.org/mex3nuox3/debug.png) Malc0de RSS Feed

## Usage

### Feed Parser

```python
import malc0de
print(malc0de.Malcode.get_rss_items()[:5])
```

```javascript
[
    Malcode(domain='www.motoclubfojeteiros.com', url='www.motoclubfojeteiros.com/wp-content/aeHwbX/index.html', ipaddress='82.165.134.81', country='DE', asn='8560', md5sum='c1e58deff777f2fdb48a50a42618f599'),
    Malcode(domain='www.kickassgrowth.com', url='www.kickassgrowth.com/LjzmE/index.html', ipaddress='46.4.90.232', country='DE', asn='24940', md5sum='8ea76c5c4f2c268eecf02e3604a4f7a6'),
    Malcode(domain='umunna.info', url='umunna.info/bestfile/builder.exe', ipaddress='37.72.171.98', country='PL', asn='35017', md5sum='71169e2bb6e19b3c3edcd7d8f3d6d3f1'),
    Malcode(domain='umunna.info', url='umunna.info/bestfile/Loki_original.exe', ipaddress='37.72.171.98', country='PL', asn='35017', md5sum='5455364b437d431400267a9092d65442'),
    Malcode(domain='ow.ly', url='ow.ly/32nP30h187Z', ipaddress='54.183.130.144', country='US', asn='16509', md5sum='6c29b80a61ff5ca7f5d8db8b002e9631')]
>>>
```
