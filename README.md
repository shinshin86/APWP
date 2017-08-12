# APWP
Automatic Post for WordPress

## Requirement

##### Use Python3 and 

this library to pip install

	pip install python-wordpress-xmlrpc

## Usage

setup **post** directory.



```
post
├── content => wordpress content text
│   ├── content_1.txt
│   └── content_2.txt
├── image => post image file
│   └── sample_image_1.png
│   └── sample_image_2.png
├── postdata.csv => post data(csv)
└── postdata.json => post data(json)
```



postdata.csv

* For csv files, you can specify only one tag


* post/content/{content_file}.txt => content

```
id,title,content_file,tags,category,date,image
00000001,title is here 1,content_1.txt,cat,mylife,2017-08-31 14:59:59,sample_image_1.png
00000002,title 2,content_2.txt,vacance,summer,2017-08-31 15:00:00,sample_image_2.png
```

postdata.json

```
[
  {
    "id":"00000001",
    "title":"Title is here 1",
    "content_file":"content_1.txt",
    "tag":"cat, vegetable",
    "category":"mylife",
    "date":"2017-8-31 14:59:59",
    "image": "sample_image_1.png"
  },
  {
    "id":"00000002",
    "title":"title 2",
    "content_file":"content_2.txt",
    "tag":"vacance, music",
    "category":"summer",
    "date":"2017-08-31 23:59:59",
    "image": "sample_image_2.png"
  }
]
```



## Setting

Clone this repository then make "post" directory and content.

next, set info of wordpress connection and postdata config.

execute "main.py"

```
git clone https://github.com/shinshin86/APWP.git

cd APWP
mkdir post # and make content(look "Usage")

# copy and edit cfg file.
cp config/connect_wp.cfg.example config/connect_wp.cfg
cp config/postdata_dir.cfg.example config/postdata_dir.cfg

# execute
python app/main.py
```



## Make a roadmap to Version 1.0

Function of Implementation plan.

* Create a multi post function.
* Create some "apwp" command.
* Create web base ui.
* Change application architecture



## Design drawing of application

>  APWP(web ui)
>
>  ​         │
>
>  ​         │Store post schedule and Check post schedule
>
>  ​         │
>
>  APWP(cli) <— fetch post data— json, csv, and DB
>
>  ​         │
>
>  ​         │send post to wordpress
>
>  ​         │
>
>   WordPress

## Test

Use unittest

```
python -m unittest discover
```



## Licence

[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](./LICENSE)
