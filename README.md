
# ![Malcode](logo.png) Malc0de RSS Feed Parser

## Usage
### Import library


```python
import malc0de
```

### Get latest entries


```python
entries = Malcode.get_rss_items()
```

### Access entry data


```python
for entry in entries[0:5]:
    print('Domain:{0} \t MD5:{1} \t URL={2}'.format(entry.domain, entry.md5sum, entry.url))
```

    Domain:gcleaner.info 	 MD5:b0305d1ad459a94506d7b857af0a80bb 	 URL=gcleaner.info/setup.exe
    Domain:gcleaner.info 	 MD5:9c896e35007cc63ba400ef1e964cd571 	 URL=gcleaner.info/success.reg
    Domain:gcleaner.info 	 MD5:751675a571dd42a5f2f879a3612b885c 	 URL=gcleaner.info/koseu.exe
    Domain:faqshub.xyz 	 MD5:dd9866000a55f0794a551603d90c83d9 	 URL=faqshub.xyz/wp/mexzy/mexzy.exe
    Domain:faqshub.xyz 	 MD5:c623c38a0f89211ff438d3249bddab97 	 URL=faqshub.xyz/wp/clunny/clunny.exe


# Misc

- [MIT License](LICENSE)
