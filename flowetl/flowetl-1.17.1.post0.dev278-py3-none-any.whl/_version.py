
# This file was generated by 'versioneer.py' (0.23) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2022-10-20T08:07:51+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "b88744cec720439fc99ae9145708ad465e63622b",
 "version": "1.17.1.post0.dev278"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
