"""
Set remote target URL for communication with phpsploit

This setting should contain at least 1 URL, previously
backdoored with the backdoor code generated by
`exploit --get-backdoor`.

When running `exploit`, phpsploit uses this URL to try
to open a remote shell.
"""
import linebuf
import datatypes


linebuf_type = linebuf.RandLineBuffer


def validator(value):
    if str(value).lower() in ["", "none"]:
        return default_value()
    else:
        return datatypes.Url(value)


def default_value():
    return None