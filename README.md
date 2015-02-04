# Potato Fork of the Google App Engine Pipeline API

## Why?

The original had the following issues:

 - Bundles Java and Python code together, we're only interested in Python
 - Duplicated the library twice in the repo (once in src, once in demo)
 - Had shebangs pointing at python2.5
 - Imported and required simplejson instead of json
 - Had its own copy of simplejson packaged
 - Died if there was no PYTHONPATH environment variable
 - etc.

So I've forked it, and cleaned it up

The original README follows...


## Google App Engine Pipeline API

Official site: https://github.com/GoogleCloudPlatform/appengine-pipelines

The Google App Engine Pipeline API connects together complex,
workflows (including human tasks). The goals are flexibility,
workflow reuse, and testability.

A primary use-case of the API is connecting together various
App Engine MapReduces into a computational pipeline.
