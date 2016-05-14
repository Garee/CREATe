# CREATe
Data visualisations for academic copyright studies.

#### Wiki Website
http://www.copyrightevidence.org/evidence-wiki/index.php/Copyright_Evidence

#### Wiki Website Api Docs Link
http://www.copyrightevidence.org/evidence-wiki/api.php

## Quick Start

```sh
$ sudo apt-get install python3 pip3
$ git clone https://github.com/Garee/CREATe.git create
$ cd create
$ pip3 install -r requirements.txt
$ export CREATE_CFG=/absolute/path/to/cfg/development.cfg
$ python3 create/server.py
```

Navigate to http://localhost:3000.


#### Query for retrieving pages, their titles and their text content
```sql
SELECT
    `p`.`page_id` AS "page_id",
    CAST(`p`.`page_title` AS CHAR(10000) CHARACTER SET utf8) AS "page_title",
    `r`.`rev_text_id` AS "revision_id",
    `t`.`old_id` AS "text_id",
    `t`.`old_text`
    FROM
    page p
        INNER JOIN `revision` r
            ON `p`.`page_id` = `r`.`rev_page`    
        INNER JOIN `text` t
            ON `r`.`rev_text_id` = `t`.`old_id`
where p.page_title = 'De_Beer_and_Bouchard,_2010'
```
