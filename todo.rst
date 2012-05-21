export todos
============

(0): Re-write
-------------
* get rid of funkiness in odk_logger/xform_instance_parser (line 68, looking at you)

* choose an intermediate data structure to receive data from mongo -- pandas? 

  * the current "default" is jsonlist, which seems inferior because most operations are column-wise

* encode all xpath transformations as optional / configurable transformations on that datastructure

  * [default:on]  for type select_all: expand column into boolean columns per option
  * [default:on]  for type gps: expand column into column per _latitute, _longitute, _altitude, and _precision
  * [default:on]  for type note: delete column 

* filters

  * time-filtration, as implemented currently, should be kept

* re-write the csv/xls/kml export to work off of this intermediate data structure (NOTE: the kml export has a different default for the "replace header names" option above)

QUESTIONS:
* post-parse, in the intermediate data structure, which is built from pre-flattened json: how do we realize that child[0]/name child[1]/name child[2]/name etc. are all fileds that are related to the 'child' attribute, which is a repeat element

(1): Enhancement
----------------
* xpath transformations
  
  * [default:on] for type image/video/audio: add a _url column that is that s3 permalink for that piece of media
  * [default:off] for type select_one: replace names within column as labels
  * [default:off] for type repeat: flatten repeats using the JOIN method (see #173 for detail)

* add new global transformations
  
  * [default: off] replace header names with labels (NOTE: have to deal with languages, pick default to begin) 

* filters
  
  * [default: off] allow ability to download *all* elements, including deleted

* UI: expose these options to users

(2): Level 2 Enhancement:
-------------------------
* global transformations

  * [default: /] choice of delimeter (stata doesn't deal with / -- has been a consistent complaint from stata users)
  * [default: off] "unique by"; request data that is unique by a certain column, such as "uuid", and perhaps, something like, "facility_id" --> dependency for updates?

QUESTIONS:

* how to let people specify the options in terms of what to do when two values are detected. default is probably submit_time, do we let users get more complex?

